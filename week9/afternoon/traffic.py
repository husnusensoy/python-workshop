import json
import os
from pathlib import Path
from typing import List

import pandas as pd
from prefect import flow, get_run_logger, task

URLS = {
    "jan": "https://data.ibb.gov.tr/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/db9c7fb3-e7f9-435a-92f4-1b917e357821/download/traffic_density_202001.csv",
    "feb": "https://data.ibb.gov.tr/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/5fb30ee1-e079-4865-a8cd-16efe2be8352/download/traffic_density_202002.csv",
    "mar": "https://data.ibb.gov.tr/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/efff9df8-4f40-4a46-8c99-2b3b4c5e2b8c/download/traffic_density_202003.csv",
}

BASE_DIR = "data/traffic"

CREDENTIAL_FILE = "credentials/python-workshop-369005-24786d080402.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIAL_FILE


@task
def prereq():
    Path(BASE_DIR).mkdir(parents=True, exist_ok=True)


@task
def download_csv(month: str, url: str, overwrite: bool = False) -> Path:
    """Download the url csv and store it in parquet format"""

    logger = get_run_logger()

    target_path = Path(BASE_DIR) / f"{month}.parquet"
    logger.info(f"Checking for target path {target_path}")

    if (not target_path.exists()) or overwrite:
        traffic = pd.read_csv(url)
        traffic.to_parquet(target_path)
        logger.info(f"Download Complete: {month} ({target_path})")
    else:
        logger.info(f"{month} data is already downloaded in {target_path}")

    return target_path


def get_project_id() -> str:
    with open(CREDENTIAL_FILE) as fp:
        credentials = json.load(fp)

    return credentials["project_id"]


@task
def upload_to_bq(path: Path) -> int:
    logger = get_run_logger()

    logger.info(f"Start uploading {path} to BQ")

    traffic = pd.read_parquet(path)

    table_name = f"traffic.{path.stem}"
    project_id = get_project_id()

    traffic.to_gbq(table_name, project_id=project_id, if_exists="replace")

    logger.info(
        f"{len(traffic)} rows are loaded (maybe overwritten) into {table_name} @ project {project_id}"
    )

    return len(traffic)


@flow
def traffic_flow():
    logger = get_run_logger()

    prereq()

    paths: List = []

    for month, url in URLS.items():
        parquet_path = download_csv.submit(month, url)

        paths.append(parquet_path)

    total_rows = 0
    for path in paths:
        total_rows += upload_to_bq(path)

    logger.info(f"Total number of traffic data loaded into bq: {total_rows}")


if __name__ == "__main__":
    traffic_flow()
