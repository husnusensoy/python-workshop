import json
import os
from pathlib import Path

import pandas as pd
from prefect import flow, get_run_logger, task

URL = {
    "may": "https://data.ibb.gov.tr/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/00d72836-d035-462d-a66e-408883216195/download/traffic_density_202105.csv",
    "apr": "https://data.ibb.gov.tr/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/1eb158e8-8da7-4572-9825-108714a8856e/download/traffic_density_202104.csv",
    "mar": "https://data.ibb.gov.tr/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/fdbc8e2f-0cf1-4952-b50f-df8f40d5a649/download/traffic_density_202103.csv",
    "feb": "https://data.ibb.gov.tr/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/395811ac-4152-4e04-88ef-8d4e30e6ac17/download/traffic_density_202102.csv",
    "jan": "https://data.ibb.gov.tr/dataset/3ee6d744-5da2-40c8-9cd6-0e3e41f1928f/resource/fb7094a3-cf2f-46a6-996a-f6a9c5f3b9be/download/traffic_density_202101.csv",
}

BASE_DIRECTORY = "data/staging/traffic"

CREDENTIAL_FILE = "credentials/python-workshop-369005-7b43562c51c7.json"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIAL_FILE


@task
def prerequisite():
    Path(BASE_DIRECTORY).mkdir(parents=True, exist_ok=True)


@task
def download_url(month: str, url: str) -> str:
    """Download relevant month traffic data from IBB data portal.

    :return Intermediate parquet file name
    """
    logger = get_run_logger()
    file_name = f"{BASE_DIRECTORY}/{month}.parquet"

    if not Path(file_name).exists():

        logger.info(f"Downloading {month} data into {file_name}")

        df = pd.read_csv(url)
        df.to_parquet(file_name)
    else:
        logger.info(f"{month} data is already downloaded in {file_name}")

    return file_name


def get_project_id() -> str:
    """

    :return project_id in Google crdentials file.
    """
    with open(CREDENTIAL_FILE) as fp:
        j = json.load(fp)

    return j["project_id"]


@task
def upload_to_bq(file):
    df = pd.read_parquet(file)

    month = Path(file).stem
    table_name = f"traffic.{month}"
    project_id = get_project_id()

    df.to_gbq(table_name, project_id=project_id, if_exists="replace")

    logger = get_run_logger()

    logger.info(f"{len(df)} rows loaded into {table_name} in your project `{project_id}`")

@flow
def traffic_flow():
    file_names = []

    prerequisite()

    for month, url in URL.items():
        file_name = download_url.submit(month, url)
        file_names.append(file_name)

    for file_name in file_names:
        upload_to_bq(file_name)


if __name__ == "__main__":
    traffic_flow()
