import getpass
import os
from typing import Any, Dict

import sec as s
import vertica_python as v

"""Hiding Password

    1. Seperate configuration configuration
    2. (Interactive) Ask user
    3. Environment variable

"""
if "VERTICA_AUTH" not in os.environ:
    user = input("\nUsername> ")
    passw = getpass.getpass(f"\nPassword for '{user}'>")
else:
    auth = os.environ["VERTICA_AUTH"]
    user, passw = auth.split(":")

def get_connection_info() -> Dict[str, Any]:
    return dict(host="127.0.0.1",
    port=5433,
    user=user,
    password=passw,
    session_label="My first python application",
    autocommit=False,
    connection_timout=300,
    connection_load_balance=True,
    use_prepared_statements= True,
    backup_server_node=["127.0.0.1", "127.0.0.1", "127.0.0.1"])

with v.connect(
    **get_connection_info()
) as conn:
    with conn.cursor() as cur:
        cur.execute("create table if not exists t(i int, v varchar, k varchar)")

        data = [("a", "b"), ("c", "d")]

        #for i, kv in enumerate(data):
            #cur.execute(f"insert into t values({i},'{kv[0]}','{kv[1]}')")
            #cur.execute("insert into t values(?,?,?)", (i, kv[0], kv[1]))

        cur.executemany("insert into t values(?,?,?)", [(i, kv[0], kv[1]) for i, kv in enumerate(data)])

        conn.rollback()

    with conn.cursor() as cur:
        cur.execute("select * from t order by i")
        rows = cur.fetchall()
        print(rows[0][1])

        print(rows)

    with conn.cursor('dict') as cur:
        cur.execute("select * from t order by i")
        rows = cur.fetchall()

        print(rows)

        print(rows[0]['v'])

    with conn.cursor('dict') as cur:
        cur.execute("select * from t where i = ?", (1,))
        row = dict(cur.fetchone())

        print(row)

    #with conn.cursor() as cur:
    #    predicate = {"propI":1}
    #    cur.execute("select * from t where i = :propI", predicate)
    #    row = dict(cur.fetchone())

    #    print(row)


