from vert_conn import vconn_info

import vertica_python as v
import pandas as pd

with v.connect(**vconn_info()) as conn:
    people = pd.read_sql_query("select * from person", conn)

print(people)
