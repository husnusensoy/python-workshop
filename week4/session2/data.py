import os
import time
from pathlib import Path
from typing import List, Union

import pandas as pd

CREDENTIAL_FILE = "/Users/husnusensoy/Documents/code/python-training-2910/week4/session2/python-workshop-369005-a89d082a12b6.json"
PROJECT_ID = "python-workshop-369005"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIAL_FILE


def run_bq(sql: str) -> pd.DataFrame:
    return pd.read_gbq(
        sql, project_id=PROJECT_ID, dialect="standard", use_bqstorage_api=True
    )


def norm(orginal: str) -> str:
    if len(orginal) == 3:
        return orginal.title()
    else:
        return orginal[:3].title()


def get_list_summary(mon: Union[List[str], None], expr: int = 30) -> pd.DataFrame:

    if Path("database/trip_cache.csv").exists():
        summary = pd.read_csv("database/trip_cache.csv")

        last_update = float(summary["last_update"].max())

        if time.time() - last_update > expr:
            summary = run_bq(
                'select FORMAT_DATE("%h",pickup_datetime) trip_month,count(1) trip_count from `nyc-tlc.green.trips_2014` group by 1'
            )
            summary["last_update"] = time.time()

            summary.to_csv("database/trip_cache.csv", index=False)
    else:
        summary = run_bq(
            'select FORMAT_DATE("%h",pickup_datetime) trip_month,count(1) trip_count from `nyc-tlc.green.trips_2014` group by 1'
        )

        summary["last_update"] = time.time()

        summary.to_csv("database/trip_cache.csv", index=False)

    if mon is None:
        return summary.drop("last_update", axis=1)
    else:
        months: List[str] = [norm(m) for m in mon]

        return summary[summary["trip_month"].isin(months)].drop("last_update", axis=1)


def get_summary(mon: str, expr: int = 30) -> pd.DataFrame:
    return get_list_summary([mon], expr)


if __name__ == "__main__":
    # print(get_list_summary(None))

    print(get_summary("March"))
