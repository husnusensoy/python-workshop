from pprint import pprint as pp
from typing import List, Union

import pandas as pd
import requests


def serv01() -> Union[pd.DataFrame, None]:
    r = requests.get("http://127.0.0.1:8000/trip", params=dict(order=True))

    if r.status_code == 200:
        pp(r.json())

        d = {
            "month": [rec["month"] for rec in r.json()],
            "trip_count": [rec["trip_count"] for rec in r.json()],
        }

        return pd.DataFrame(d)


def serv02(months: List[str]) -> Union[pd.DataFrame, None]:
    r = requests.post(
        "http://127.0.0.1:8000/trip", params=dict(order=True, expire=10), json=months
    )

    if r.status_code == 200:
        d = {
            "month": [rec["month"] for rec in r.json()],
            "trip_count": [rec["trip_count"] for rec in r.json()],
        }

        return pd.DataFrame(d)


d = serv01()
d = serv02(["JanUARY", "June"])

print(d)
