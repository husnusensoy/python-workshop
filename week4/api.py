import json
import os
import time
from dataclasses import dataclass
from typing import Dict, List, Union

import pandas as pd

MONTHS = (
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
)

CREDENTIAL_FILE = "/Users/husnusensoy/Documents/code/python-training-2910/week4/python-workshop-369005-da7a8c3e4340.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIAL_FILE
PROJECT_ID = "python-workshop-369005"


@dataclass
class Summary:
    """Monthly trip summary"""

    mon: str
    num_trips: int


@dataclass
class Cache:
    last_update: float

    summary: List[Summary]

    def is_expired(self, expire) -> bool:
        return time.time() - self.last_update > expire


def cache_load() -> Cache:
    with open("cache/trips.json") as fp:
        js = json.load(fp)

    return Cache(
        last_update=js["last_update"],
        summary=[
            Summary(mon=month, num_trips=trip_count)
            for month, trip_count in js["summary"].items()
        ],
    )


def cache_save(cache: Cache):
    with open("cache/trips.json", "w") as wp:
        json.dump(
            dict(
                last_update=cache.last_update,
                summary={rec.mon: rec.num_trips for rec in cache.summary},
            ),
            wp,
        )


def fetch_from_cache(expire: int) -> Dict[str, int]:
    cache = cache_load()

    if cache.is_expired(expire):
        summ = pd.read_gbq(
            'select FORMAT_DATE("%h",pickup_datetime) trip_month,count(1) trip_count from `nyc-tlc.green.trips_2014` group by 1',
            project_id=PROJECT_ID,
            dialect="standard",
            use_bqstorage_api=True,
        )

        cache.summary = []
        for rec in summ.itertuples():
            cache.summary.append(
                Summary(mon=rec.trip_month, num_trips=int(rec.trip_count))
            )

        cache.last_update = time.time()

        cache_save(cache)
    else:
        print(
            f"WARNING: Data found in cache that is not exipred yet. Time to expiration {expire  - (time.time() - cache.last_update) } sec"
        )

    return {rec.mon: rec.num_trips for rec in cache.summary}


def normalize(mon: str) -> str:
    if len(mon) == 3:
        m = mon.title()

    else:
        m = mon[:3].title()

    if m not in MONTHS:
        raise Exception(f"{mon} can not be formated into a valid 3 letter month")

    return m


def get_monthly_summary(mon: str, expire: int = 15 * 60) -> Summary:
    """Fetch monthly trip summary from Google Big query with an expiration period of 15 min
    - months
        str: Month to be returned -> Summary
    """

    m = normalize(mon)

    trip_summary = fetch_from_cache(expire)

    return Summary(mon=mon, num_trips=trip_summary[m])


def get_list_monthly_summary(
    months: Union[List[str], None], expire: int = 15 * 60
) -> List[Summary]:
    """Fetch monthly trip summary from Google Big query with an expiration period of 15 min
    - months
        List[str]: List of months to be retuned -> List[Summary]
        None: All months summary
    """

    if months is None:
        return [get_monthly_summary(mon, expire) for mon in MONTHS]
    else:
        return [get_monthly_summary(mon, expire) for mon in months]
