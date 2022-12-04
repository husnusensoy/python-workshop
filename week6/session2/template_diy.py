from itertools import product
from typing import Tuple

import typer

COLUMN = ["temp","Humadity","prEssure","jitter"]
FN=["avg","max","min","count","Stddev","median"]

SCHEMA = "iot"
TABLE = "metric"

app = typer.Typer()

def fn_column_sort(tup:Tuple[str,str]):
    return tup[1].lower()

def fn_fn_sort(tup:Tuple[str,str]):
    return tup[0].lower()


def aggr_expr(fn:str, col:str) -> str:
    return f"{fn.upper()}({col.lower()}) AS {fn.lower()}_{col.lower()}"

@app.command()
def print_sql(metric:bool=True):
    """"select avg(temp) as mean_temp
        ...
        .
        from table
        """
    if not metric:
        p = sorted(product(FN, COLUMN), key=fn_column_sort)
    else:
        p = sorted(product(FN, COLUMN), key=fn_fn_sort)

    exprs = [aggr_expr(fn, col) for fn,col in p]

    typer.echo(f'SELECT {",".join(exprs)} FROM {SCHEMA}.{TABLE}')




if __name__ == "__main__":
    app()


