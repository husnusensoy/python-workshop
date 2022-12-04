TODO_URL = "https://jsonplaceholder.typicode.com/todos"

import json
from pathlib import Path
from typing import List

import pandas as pd
import requests as r
from prefect import flow, task
from pyspark.sql import SparkSession

from my_first_flow import create_directory


@task
def save_content(url: str, path: Path) -> List[dict]:
    respo = r.get(url)

    if respo.status_code == 200:
        list_of_dict = respo.json()

    with path.open("w") as wp:
        for d in list_of_dict:
            print(json.dumps(d), file=wp)

    return list_of_dict


@task
def calculate_status_count(spark, path: str):
    df = spark.read.json(path)

    df.registerTempTable("todo")

    return spark.sql("select completed,count(1) as n from todo group by 1").coalesce(1)


def freq_fn(tup):
    return tup[1]


@task
def calculate_wf_pure_python(content: List[dict]) -> pd.DataFrame:
    token_count = {}
    for d in content:
        text = d["title"]

        for token in text.lower().split():
            token_count[token] = token_count.get(token, 0) + 1

    tokens = list(token_count.keys())

    counts = [token_count[tok] for tok in tokens]

    # most_popular_word, count_of_most_popular_word = max(token_count.items(),key=freq_fn)

    return pd.DataFrame(dict(token=tokens, count=counts))


@flow
def todo_flow(base_dir: str = "data"):
    basedir = Path(base_dir)

    create_directory(basedir / "parquet")

    content = save_content(TODO_URL, basedir / "json/todo.jsonl")

    spark = (
        SparkSession.builder.master("local[*]")
        .appName("PySpark Workshop 2 ")
        .getOrCreate()
    )

    df = calculate_status_count(spark, str(basedir / "json/todo.jsonl"))
    df.write.mode("overwrite").parquet(str(basedir / "parquet/todo_status.parquet"))

    word_freq = calculate_wf_pure_python(content)

    word_freq.to_csv(basedir / "csv/word_freq.csv", index=False)


todo_flow()
