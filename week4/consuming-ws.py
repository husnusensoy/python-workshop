from typing import List

import pandas as pd
import requests as r


def get_all_months_from_ws() -> pd.DataFrame:
    all_summaries = r.get("http://127.0.0.1:8000/summary")

    js = all_summaries.json()

    print(js)

    months = [k for k, _ in js["summary"].items()]
    trip_count = [v for _, v in js["summary"].items()]

    df = pd.DataFrame(dict(mon=months, trip_count=trip_count))
    return df


def get_from_ws(mon: str) -> pd.DataFrame:

    all_summaries = r.get(f"http://127.0.0.1:8000/summary/{mon}")

    rc = all_summaries.status_code
    if rc == 200:
        js = all_summaries.json()

        print(js)

        months = [k for k, _ in js["summary"].items()]
        trip_count = [v for _, v in js["summary"].items()]

        df = pd.DataFrame(dict(mon=months, trip_count=trip_count))

        return df
    else:
        print(f"ERROR: An issue occurred with service call {all_summaries.json()}")


def get_some_months_from_ws(months: List[str], expire_sec: int) -> pd.DataFrame:
    all_summaries = r.post(
        "http://127.0.0.1:8000/summary", json=months, params={"expire": expire_sec}
    )

    rc = all_summaries.status_code

    if rc == 200:
        js = all_summaries.json()

        print(js)

        months = [k for k, _ in js["summary"].items()]
        trip_count = [v for _, v in js["summary"].items()]

        df = pd.DataFrame(dict(mon=months, trip_count=trip_count))
        return df


if __name__ == "__main__":
    df = get_all_months_from_ws()
    print(df)

    df = get_from_ws("Şub")
    print(df)

    df = get_some_months_from_ws(["Jan", "Sep"], 24 * 60 * 60)
    print(df)
