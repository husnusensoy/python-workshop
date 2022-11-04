from typing import List

d = {"one": 1}

d["one"] = 2


d = {"one": [1]}

d["one"].append(2)

d["two"] = []
d["two"].append(1)
d["two"].append(1)

print(d)


def add(d: dict, key: str, v: int):
    if key not in d:
        d[key] = []

    if v not in d[key]:
        d[key].append(v)


def get_history(d, key: str) -> List[int]:
    all_values = d[key]

    return all_values


def get_value(d, key: str) -> int:
    return get_history(d, key)[-1]


d = {}

add(d, "one", 1)
add(d, "one", 1)
add(d, "one", 2)

print(d)
