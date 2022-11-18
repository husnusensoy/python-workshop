import vertica_python as v
from vert_connection import get_connection_info

with v.connect(
    **get_connection_info()
) as conn:
    with conn.cursor() as cur:
        with open("sql/q1.sql") as fp:
            q1 = fp.read()

        cur.execute(q1)

        print(cur.fetchall())

    