import json
import os

import pandas as pd
from fastapi import FastAPI, HTTPException
from jinja2 import Environment, FileSystemLoader

app = FastAPI()

envi = Environment(loader=FileSystemLoader("templates/bq"))

MONTHS = ["jan", "feb", "mar"]

CREDENTIAL_FILE = "credentials/python-workshop-369005-24786d080402.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIAL_FILE


def get_project_id() -> str:
    with open(CREDENTIAL_FILE) as fp:
        credentials = json.load(fp)

    return credentials["project_id"]


@app.get("/v1/metadata/time_range")
def get_time_range():
    tr = envi.get_template("time_range.sql.j2")

    sql = tr.render(months=MONTHS)

    result = pd.read_gbq(
        sql, project_id=get_project_id(), dialect="standard", use_bqstorage_api=True
    )

    return result.to_dict(orient="records")[0]


def get_prefix(resolution_km:float) -> int:
    """
    ```
Geohash length Cell width Cell height
1 ≤ 5,000km × 5,000km
2 ≤ 1,250km × 625km
3 ≤ 156km × 156km
4 ≤ 39.1km × 19.5km
5 ≤ 4.89km × 4.89km
6 ≤ 1.22km × 0.61km
7 ≤ 153m × 153m
8 ≤ 38.2m × 19.1m
9 ≤ 4.77m × 4.77m
10 ≤ 1.19m × 0.596m
11 ≤ 149mm × 149mm
12 ≤ 37.2mm × 18.6mm
```
    """

    if resolution_km < 0.153:
        raise HTTPException(500, detail=f"Resolution less than 0.153 km ({resolution_km} km requested) is not available")
    elif resolution_km < 1.22:
        return 6
    elif resolution_km < 4.89:
        return 5
    elif resolution_km < 39.1:
        return 4
    elif resolution_km < 156:
        return 3
    elif resolution_km < 1250:
        return 2
    else:
        return 1        

@app.get("/v1/metadata/statistics/vehicle/")
def get_vehicle_stats(hour:int, resolution_km:float):
    tr = envi.get_template("total_vehicle.sql.j2")

    sql = tr.render(months=MONTHS, prefix=get_prefix(resolution_km))

    print(sql)

    result = pd.read_gbq(
        sql, project_id=get_project_id(), dialect="standard", use_bqstorage_api=True
    )

    return result[result.hour == hour].to_dict(orient="records")[0]