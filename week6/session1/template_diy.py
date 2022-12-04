from typing import List, Tuple

COLUMN = ["temp", "pressure", "humadity"]
METRIC = ["avg", "stddev", "min", "max"]

""""
select avg(temp) as mean_temp
from table
"""

def expr_gen(column:str, metric:str) ->str:
    return f"{metric}({column}) as {metric}_{column}"

def all_combinations(order_by_column:bool=True) ->List[Tuple[str,str]]:
    comb = []

    if order_by_column:
        for col in COLUMN:
            for met in METRIC:
                comb.append((col,met))

    else:
        for met in METRIC:
            for col in COLUMN:
                comb.append((col,met))

    return  comb



def entry():
    exprs = [expr_gen(col,met) for col,met in all_combinations()]
    exptr_str= ',\n'.join(exprs)

    print(f"""select 
    {exptr_str} 
    from table""")


if __name__ == "__main__":
    entry()
