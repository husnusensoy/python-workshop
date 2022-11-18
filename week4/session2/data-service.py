import json
from typing import List, Union

import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

from data import get_list_summary, get_summary

app = FastAPI()


@app.get("/trip/{month}")
def get_summary_srv(month: str, expire: int = 15 * 60):
    df = get_summary(month, expr=expire)

    return dict(
        month=df["trip_month"].iloc[0], trip_count=int(df["trip_count"].iloc[0])
    )


@app.get("/trip")
def get_all_summary_srv(expire: int = 15 * 60, order: bool = False):
    df: pd.DataFrame = get_list_summary(None, expr=expire)

    if order:
        return [
            dict(month=rec.trip_month, trip_count=int(rec.trip_count))
            for rec in df.sort_values(by=["trip_count"]).itertuples()
        ]
    else:
        return [
            dict(month=rec.trip_month, trip_count=int(rec.trip_count))
            for rec in df.itertuples()
        ]


@app.post("/trip")
def get_all_summary_srv(mons: List[str], expire: int = 15 * 60):
    df = get_list_summary(mons, expr=expire)

    return [
        dict(month=rec.trip_month, trip_count=int(rec.trip_count))
        for rec in df.itertuples()
    ]
