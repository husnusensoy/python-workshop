import pandas as pd
import vertica_python as v
from tqdm import tqdm

from vert_conn import vconn_info

with v.connect(**vconn_info()) as conn:
    with conn.cursor() as cur:
        cur.execute(
            "create table if not exists private_data(name varchar, color varchar, cc varchar)"
        )
        cur.execute("truncate table private_data")

        with open("data/sample.csv") as fp:
            cur.copy(
                "copy private_data from stdin delimiter ',' REJECTMAX 1 NO COMMIT", fp
            )

        conn.commit()
