from typing import Union

import pandas as pd
import vertica_python as v
from jinja2 import Environment, FileSystemLoader, Template
from pyparsing import col

from dynsql import run_sql
from vconn import vconn_info

envi = Environment(loader=FileSystemLoader("sqls/"))


sqlt = envi.get_template("auto.sql.j2")

df = run_sql(
    sqlt,
    True,
    schema="store",
    table="store_sales_fact",
    metrics=["avg", "min", "max", "count","approximate_median"],
    cols=["sales_quantity","sales_dollar_amount"],order_by_metric=True
).drop(["dummy"],axis=1)

df.to_csv("agg.csv",index=False)

