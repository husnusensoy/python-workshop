from typing import List, Tuple

from tqdm import tqdm


def generate_data(n=1_000_000) -> List[Tuple]:
    l = []
    for i in range(n):
        l.append((i, f"Husnu{i}",f"Sensoy{i}"))

    return l

def dump_csv(l:List[Tuple], filename="local_data/output.csv"):
    with open(filename, "w") as wp:
        for i, name, surname in l:
            print(f"{i},{name},{surname}",file=wp)
     


def dump_jsonlines():
    ...

import vertica_python as v
#dump_csv(generate_data())
from vert_connection import get_connection_info

with v.connect(
    **get_connection_info()
) as conn:
    with conn.cursor() as cur:
        cur.execute("create table if not exists output(i int, name varchar, surname varchar) order by i segmented by hash(i) all nodes")

        if bool(input("\nDo you want me to truncate table?> ")):
            cur.execute("truncate table output")

        with open("local_data/output.csv") as fp:
            cur.copy("COPY output FROM STDIN DELIMITER ',' REJECTMAX 1", fp)


        #with open("local_data/output.csv") as fp:
        #    for line in tqdm(fp):
        #        t = tuple(line.split(','))

        #        cur.execute("insert into output values(?,?,?)", t)

        #cur.commit()
