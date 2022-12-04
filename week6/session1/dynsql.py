from typing import Union

import pandas as pd
import typer
import vertica_python as v
from jinja2 import Environment, FileSystemLoader, Template
from pyparsing import col

from vconn import vconn_info

envi = Environment(loader=FileSystemLoader("sqls/"))


app = typer.Typer()


def run_sql(template: Template, verbose: bool, **targs) -> pd.DataFrame:
    with v.connect(**vconn_info()) as conn:
        with conn.cursor("dict") as cur:
            sqlr = template.render(**targs)

            if verbose:
                typer.echo(f"\nSQL: {sqlr}\n")

            df = pd.DataFrame(cur.execute(sqlr).fetchall())

            return df


@app.command()
def topk(table: str, schema: str = "public", n: int = 10, verbose: bool = False):
    """Get first k rows of a given table"""
    sqlt = envi.get_template("topk.sql.j2")

    df = run_sql(sqlt, verbose, schema=schema, table=table, n=n)
    typer.echo(df)


@app.command()
def agg(
    table: str,
    column: str,
    schema: str = "public",
    keycol: Union[str, None] = None,
    verbose: bool = False,
):
    """Calcualte an aggregate column values"""
    sqlt = envi.get_template("agg.sql.j2")

    df = run_sql(sqlt, verbose, column=column, table=table, schema=schema,keycol=keycol)
    typer.echo(df)


if __name__ == "__main__":
    app()
