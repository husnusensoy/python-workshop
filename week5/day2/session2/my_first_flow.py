import json
from pathlib import Path
from pprint import pprint as pp
from typing import List, Tuple

import pandas as pd
import requests as r
from prefect import flow, task

"""
- Collect 20 random cat facts from service
- Create a directory to store data
- Store facts in a single json file data/json
- convert json into csv data/csv
"""


class BatchStatusIssue(Exception):
    def __init__(self, problem_indexes: List[int]) -> None:
        super().__init__()

        self.problem_indexes = problem_indexes

    def __str__(self) -> str:
        return f"We have status code issue with {self.problem_indexes}"

@task
def get_facts(n: int) -> List[dict]:
    responses = [r.get("https://catfact.ninja/fact") for _ in range(n)]

    status_codes = [r.status_code == 200 for r in responses]

    if all(status_codes):
        return [r.json() for r in responses]
    else:
        raise BatchStatusIssue([i for i, r in enumerate(status_codes) if not r])

@task
def create_directory(*paths: Tuple[Path]):
    for p in paths:
        p.mkdir(parents=True, exist_ok=True)

@task
def store_json(facts: List[dict], path: Path):
    with path.open("w") as wp:
        json.dump(facts, wp)


@task
def json_to_pandas(path: Path) -> pd.DataFrame:
    with path.open() as fp:
        facts = json.load(fp)

    fact = [f["fact"] for f in facts]
    length = [f["length"] for f in facts]

    return pd.DataFrame(dict(fact=fact, length=length))


@flow
def do_flow():
    facts: List[dict] = get_facts(n=20)

    create_directory(Path("data/json"), Path("data/csv"))

    store_json(facts, Path("data/json/facts.json"))

    df = json_to_pandas(Path("data/json/facts.json"))
    df.to_csv(Path("data/csv/facts.csv"), index=False)


do_flow()
