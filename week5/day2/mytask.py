import json
import time
from pathlib import Path

import requests
from prefect import flow, task
from pyspark.sql import SparkSession
from pyspark.sql import functions as f


@task
def create_data_directory(dirname: Path):
    dirname.mkdir(parents=True, exist_ok=True)


@task
def download(
    url: str, file: Path, force: bool = False, cache_invalid_sec: int = 15 * 60
):

    s = file.stat()

    if (time.time() - s.st_mtime > cache_invalid_sec) or force:

        with open(file, "w") as fp:
            js = requests.get(url).json()

            json.dump(js, fp)


@task
def get_tokens(spark, json_files: Path):
    j = spark.read.json(str(json_files))

    return j.select(f.explode(f.split(j.body, r"\W")).alias("word"))


@task
def most_least(spark, df, k: int = 10):
    df.cache().registerTempTable("tokens")

    topk = spark.sql(
        "select word, count(1) n from tokens group by 1 order by 2 desc"
    ).limit(k)
    
    bottomk = spark.sql(
        "select word, count(1) n from tokens group by 1 order by 2"
    ).limit(k)

    return topk, bottomk


@task
def save_to_parquet(spark, topk, bottomk, proc_data_dir: Path):
    topk.coalesce(1).write.mode("overwrite").parquet(
        str(proc_data_dir / "topk.parquet")
    )
    bottomk.coalesce(1).write.mode("overwrite").parquet(
        str(proc_data_dir / "bottomk.parquet")
    )


@flow
def word_count_analysis(data_dir: str, num_post: int = 3):

    raw_data_dir = Path(data_dir) / Path("raw")
    proc_data_dir = Path(data_dir) / Path("processed")

    create_data_directory(raw_data_dir)
    create_data_directory(proc_data_dir)

    for id in range(1, num_post + 1):
        download(
            f"https://jsonplaceholder.typicode.com/posts/{id}",
            raw_data_dir / f"{id}.json",
        )

    spark = (
        SparkSession.builder.master("local[*]")
        .appName("PySpark Workshop")
        .getOrCreate()
    )

    df = get_tokens(spark, raw_data_dir / "*.json")

    topk, bottomk = most_least(spark, df)

    save_to_parquet(spark, topk, bottomk, proc_data_dir)


word_count_analysis(data_dir="data", num_post=100)

