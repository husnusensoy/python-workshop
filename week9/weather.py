import json
from lib2to3.pytree import Base
from pathlib import Path

import requests
from arrow.arrow import Arrow
from prefect import flow, get_run_logger, task

LAT, LONG = 41.057497, 28.877886


MONTH = {5: "may", 4: "apr", 3: "mar", 2: "feb", 1: "jan"}

BASE_DIR = "data/staging/weather"

JSON_BASE_DIR = Path(BASE_DIR) / "json"
JSONL_BASE_DIR = Path(BASE_DIR) / "jsonl"


def get_stormglass_apikey() -> str:
    """Returns the api key for stormglass.io"""
    with open("credentials/stormglass.key") as fp:
        return fp.read()


class StormApiException(Exception):
    def __init__(self, respo: requests.Response) -> None:
        self.status_code = respo.status_code
        self.json_data = respo.json()
        # super().__init__(*args)

    def __str__(self):
        return f"Unknown Storm Api Exception with code {self.status_code}. Detail: {self.json_data}"


class BadRequest(StormApiException):
    def __str__(self) -> str:
        return "Bad Request – Your request is invalid."


class UnAuthorized(StormApiException):
    def __str__(self) -> str:
        return "Unauthorized – Your API key is invalid."


class QuotaExceeded(StormApiException):
    def __str__(self) -> str:
        return "Too Many Requests – You’ve reached your daily limit."


def handle_error(respo: requests.Response):
    if respo.status_code == 400:
        raise BadRequest(respo)
    elif respo.status_code == 401:
        raise UnAuthorized(respo)
    elif respo.status_code in [429, 402]:
        raise QuotaExceeded(respo)
    else:
        raise StormApiException(respo)


@task
def download_weather_data(month: int) -> str:
    logger = get_run_logger()
    start = Arrow(year=2021, month=month, day=1, tzinfo="Europe/Istanbul")
    end = start.ceil("month")

    file_path = Path(JSON_BASE_DIR) / f"{MONTH[month]}.json"

    if not file_path.exists():
        response = requests.get(
            "https://api.stormglass.io/v2/weather/point",
            params={
                "lat": LAT,
                "lng": LONG,
                "params": ",".join(["airTemperature", "visibility"]),
                "start": start.to("UTC").timestamp(),  # Convert to UTC timestamp
                "end": end.to("UTC").timestamp(),  # Convert to UTC timestamp
            },
            headers={"Authorization": get_stormglass_apikey()},
            timeout=30,
        )

        if response.status_code == 200:
            json_data = response.json()

            with file_path.open("w") as wp:
                json.dump(json_data, wp)
        else:
            handle_error(response)
    else:
        logger.info(f"{MONTH[month]} weather data is already stored in {file_path}")

    return str(file_path)


@task
def to_jsonl(json_file_name) -> str:
    """Returns the name of json line file name after flattening json in json_file_name

    Example input
    {
            "airTemperature": {
                "noaa": 17.24,
                "sg": 17.24
            },
            "time": "2021-04-30T21:00:00+00:00",
            "visibility": {
                "noaa": 24.14,
                "sg": 24.14
            }
        }
    """
    logger = get_run_logger()

    month = Path(json_file_name).stem

    with open(json_file_name) as fp:
        j = json.load(fp)

    jsonl_file = Path(JSONL_BASE_DIR) / f"{month}.jsonl"

    with jsonl_file.open("w") as wp:
        for measure in j["hours"]:
            x_measure = {
                "airTemperature": sum(measure["airTemperature"].values()) / 2,
                "visibility": sum(measure["visibility"].values()) / 2,
                "time": measure["time"],
            }

            print(json.dumps(x_measure), file=wp)

    logger.info(f'Total of {len(j["hours"])} measurements dumped into {jsonl_file}')

    return str(jsonl_file)


@task
def prerequisites():
    Path(JSON_BASE_DIR).mkdir(parents=True, exist_ok=True)
    Path(JSONL_BASE_DIR).mkdir(parents=True, exist_ok=True)


@flow
def weather_flow():
    prerequisites()

    for month in MONTH:
        json_file_name = download_weather_data.submit(month)
        jsonl_file_name = to_jsonl.submit(json_file_name)


if __name__ == "__main__":
    weather_flow()
