import json
import time
from dataclasses import dataclass
from typing import Dict, List, Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from api import get_list_monthly_summary, get_monthly_summary

app = FastAPI()


@app.get("/summary/")
def summary(expire: int = 15 * 60):
    s = get_list_monthly_summary(None, expire=expire)

    return dict(summary={rec.mon: rec.num_trips for rec in s})


@app.get("/summary/{month}")
def summary_mon(month: str, expire: int = 15 * 60):
    try:
        s = get_monthly_summary(month, expire=expire)
    except Exception as e:
        raise HTTPException(500, detail=str(e))

    return dict(summary={s.mon: s.num_trips})


@app.post("/summary/")
def summary_list_mon(months: List[str], expire: int = 15 * 60):
    try:
        s = get_list_monthly_summary(months, expire=expire)
    except Exception as e:
        raise HTTPException(500, detail=str(e))

    return dict(summary={rec.mon: rec.num_trips for rec in s})


#

# if __name__ == "__main__":
#     s = get_monthly_summary("Jan", expire=15*60)

#     print(s)

#     s = get_list_monthly_summary(["Jan","Mar"], expire=15*60)

#     print(s)

#     s = get_list_monthly_summary(None, expire=15*60)

#     print(s)
