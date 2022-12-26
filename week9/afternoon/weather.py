import json
import os
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd
import requests
import vertica_python as v
from arrow.arrow import Arrow
from jinja2 import Environment, FileSystemLoader
from prefect import flow, get_run_logger, task

BASE_DIR = Path("data/weather")
JSON_BASE_DIR = BASE_DIR / "json"
JSONLINE_BASE_DIR = BASE_DIR / "jsonl"

METRICS = ["humidity", "airTemperature", "visibility"]


MONTHS = {"jan": 1, "feb": 2, "mar": 3}

LAT, LONG = 41.05322091807502, 28.894204641792093

SCHEMA = "weather"
TABLE = "istanbul"


@task
def prereq():
    Path(JSON_BASE_DIR).mkdir(parents=True, exist_ok=True)
    Path(JSONLINE_BASE_DIR).mkdir(parents=True, exist_ok=True)


def get_stormglass_apikey() -> str:
    with open("credentials/stormglass.key") as fp:
        return fp.read()


@task
def fetch_stormglass(month: str, overwrite: bool = False) -> Path:
    """Download the url csv and store it in parquet format"""

    logger = get_run_logger()

    start = Arrow(year=2020, month=MONTHS[month], day=1, tzinfo="Europe/Istanbul")
    end = start.ceil("month")

    target_path = JSON_BASE_DIR / f"{month}.json"

    if (not target_path.exists()) or overwrite:

        response = requests.get(
            "https://api.stormglass.io/v2/weather/point",
            params={
                "lat": LAT,
                "lng": LONG,
                "params": ",".join(METRICS),
                "start": start.to("UTC").timestamp(),  # Convert to UTC timestamp
                "end": end.to("UTC").timestamp(),  # Convert to UTC timestamp
            },
            timeout=30,
            headers={"Authorization": get_stormglass_apikey()},
        )

        if response.status_code == 200:
            with target_path.open("w") as wp:
                json.dump(response.json(), wp)
    else:
        logger.info(f"{target_path} already exists")

    return target_path


@task
def to_jsonline(json_path: Path) -> Path:
    """Process json file and return a json-line path


    Sample Input
    {
            "airTemperature": {
                "dwd": 7.64,
                "noaa": 8.96,
                "sg": 7.64
            },
            "humidity": {
                "dwd": 72.99,
                "noaa": 59.5,
                "sg": 72.99
            },
            "time": "2020-01-31T21:00:00+00:00",
            "visibility": {
                "noaa": 24.14,
                "sg": 24.14
            }
    }
    """

    logger = get_run_logger()

    target_path = JSONLINE_BASE_DIR / f"{json_path.stem}.jsonl"

    with json_path.open() as fp:
        weather = json.load(fp)

    with target_path.open("w") as wp:

        for sample in weather["hours"]:
            x_d = {"time": sample["time"]}

            for metric in METRICS:
                x_d[metric] = sum(sample[metric].values()) / len(
                    sample[metric].values()
                )

            print(json.dumps(x_d), file=wp)

    return target_path


def get_connection_info() -> Dict[str, Any]:
    with open("credentials/vertica.json") as fp:
        return json.load(fp)


def get_table_ddl(logger):
    envi = Environment(loader=FileSystemLoader("templates/"))

    template = envi.get_template("create.sql.j2")

    sql = template.render(schema=SCHEMA, table=TABLE, metrics=METRICS)

    logger.info(f"[CREATE TABLE STATEMENT]: {sql}")

    return sql


@task
def vertica_ddl():
    cinfo = get_connection_info()
    cinfo["session_label"] = "Metadata operation for weather data"

    with v.connect(**cinfo) as conn:
        with conn.cursor() as cur:
            cur.execute(f"create schema if not exists {SCHEMA}")
            cur.execute(get_table_ddl(get_run_logger()))


def get_copy_dml(logger):
    envi = Environment(loader=FileSystemLoader("templates/"))

    template = envi.get_template("copy.sql.j2")

    sql = template.render(schema=SCHEMA, table=TABLE, metrics=METRICS)

    logger.info(f"[COPY STATEMENT]: {sql}")

    return sql


@task
def vertica_copy(json_line_paths: List[Path]):
    cinfo = get_connection_info()
    cinfo["session_label"] = "Loading data"

    with v.connect(**cinfo) as conn:
        with conn.cursor() as cur:
            cur.execute(f"truncate table {SCHEMA}.{TABLE}")
            for json_line_path in json_line_paths:
                with json_line_path.open() as fp:
                    cur.copy(get_copy_dml(get_run_logger()), fp)

        conn.commit()


@flow
def upload_to_vertica(json_line_paths: List[Path]) -> int:
    """Load Json Line files into Vertica"""

    logger = get_run_logger()

    logger.info(f"[PATHS to LOAD]: {json_line_paths}")

    vertica_ddl()
    vertica_copy(json_line_paths)


@flow
def weather_flow():
    logger = get_run_logger()

    prereq()

    json_line_paths: List = []

    for month in MONTHS:
        json_path = fetch_stormglass.submit(month)
        json_line_path = to_jsonline.submit(json_path)

        json_line_paths.append(json_line_path)

    total_rows = upload_to_vertica(json_line_paths)

    logger.info(f"Total number of weather data loaded into vertica: {total_rows}")


if __name__ == "__main__":
    weather_flow()
