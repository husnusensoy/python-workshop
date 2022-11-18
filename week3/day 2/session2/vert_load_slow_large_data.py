import pandas as pd
import vertica_python as v
from tqdm import tqdm

from vert_conn import vconn_info

with v.connect(**vconn_info()) as conn:
    with conn.cursor() as cur:
        cur.execute("create table if not exists private_data(name varchar, color varchar, cc varchar)")

        with open("data/sample.csv") as fp:
            for line in tqdm(fp):
                tup = tuple(line.split(','))

                cur.execute("insert into private_data values(?,?,?)", tup)

        conn.commit()

print(people)
