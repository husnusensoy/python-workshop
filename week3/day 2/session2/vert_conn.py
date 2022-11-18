# pip install vertica_python
import time
from dataclasses import dataclass

import vertica_python as v
from pkg_resources import ensure_directory

DEFAULT_PORT = 5433

user = "power"
passw = "1234"


def sleep_with_prompt(prompt: str, sec: int) -> None:
    print(prompt)
    time.sleep(sec)

    print("Proceeding...")


@dataclass
class Person:
    id: int
    name: str
    surname: str
    age: int


from typing import Any, Dict


def get_person_by_id(conn, id: int) -> Person:
    """Query the conn and return the person by id"""
    with conn.cursor("dict") as cur:
        cur.execute("select * from person where id = ?", (1,))

        d = cur.fetchone()

        return Person(id=d["id"], name=d["name"], surname=d["surname"], age=d["age"])


def vconn_info() -> Dict[str, Any]:
    return dict(
        host="127.0.0.1",
        port=DEFAULT_PORT,
        user=user,
        password=passw,
        session_label="Will start using python with vertica",
        autocommit=False,
        connection_load_balance=True,
        backup_server_node=["127.0.0.1", "127.0.0.1", "127.0.0.1"],
        connection_timeout=300,
        use_prepared_statements=True,
    )


def entrypoint():
    with v.connect(**vconn_info()) as conn:
        people = [Person(1, "Husnu", "Sensoy", 39), Person(2, "Kerem", "Kargin", 25)]
        with conn.cursor("dict") as cur:
            cur.execute("select * from dual")

            singular_duality = cur.fetchone()
            # print(singular_duality['dummy'])

            cur.execute(
                "create table if not exists person(id int, name varchar, surname varchar, age int)"
            )

            cur.execute("truncate table person")

            for p in people:
                cur.execute(
                    "insert into person values(?,?,?,?)",
                    (p.id, p.name, p.surname, p.age),
                )

            conn.rollback()

            cur.executemany(
                "insert into person values(?,?,?,?)",
                [(p.id, p.name, p.surname, p.age) for p in people],
            )

            p = get_person_by_id(conn, 1)

            print(f"I can see my own session inserted data {p}")

            sleep_with_prompt(
                "I will sleep before commit", 30
            )  # to do the simulation set 1 to 30 seconds

            conn.commit()


if __name__ == "__main__":
    entrypoint()
