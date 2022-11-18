import pandas as pd
import vertica_python as v
from vert_connection import get_connection_info

with v.connect(
    **get_connection_info()
) as conn:
    df = pd.read_sql_query("select * from output limit 100000", conn)

print(df.head())