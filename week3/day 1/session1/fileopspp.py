import json as j
from json import dump as json_dunmp
from json import load as json_load
from typing import Any, Dict, List, Union

from fileops import Employee


def get_employee_by_dict(d: Dict[str, Any]) -> Employee:
    name, surname = d["name"].rsplit(" ", maxsplit=1)
    age = d["age"]
    city = d["city"]
    is_admin = d.get("is_admin", False)

    return Employee(
        name=name,
        surname=surname,
        age=age,
        company="Global Maksimum",
        is_admin=is_admin,
        city=city,
    )


def get_dict_by_emplyee(e: Employee) -> Dict[str, Any]:
    return {
        "name": f"{e.name} {e.surname}",
        "age": e.age,
        "city": e.city,
        "is_admin": e.is_admin,
        "company": e.company,
    }


def read_json(path: str) -> List[Employee]:
    with open(path) as fp:
        js = j.load(fp)

    emps = [get_employee_by_dict(d) for d in js]

    return emps


def read_jsonlines(path: str) -> List[Employee]:

    with open(path) as fp:
        emps = [get_employee_by_dict(j.loads(line)) for line in fp]

    return emps


def write_json(emps: List[Employee], path: str) -> None:
    lod = [get_dict_by_emplyee(e) for e in emps]

    with open(path, "w") as wp:
        j.dump(lod, wp)


def write_jsonline(emps: List[Employee], path: str) -> None:
    lod: List[Dict[str, Any]] = [get_dict_by_emplyee(e) for e in emps]
    loj: List[str] = [j.dumps(d) for d in lod]

    # content = "\n".join(loj)

    with open(path, "w") as wp:
        for line in loj:
            print(line, file=wp)


def write_jsonline(emps: List[Employee], path: str) -> None:
    lod: List[Dict[str, Any]] = [get_dict_by_emplyee(e) for e in emps]
    loj: List[str] = [j.dumps(d) for d in lod]

    # content = "\n".join(loj)

    with open(path, "w") as wp:
        for line in loj:
            print(line, file=wp)


def write_delimited(
    emps: List[Employee], path: str, sep: str = ",", header: bool = True
) -> None:
    header: List[str] = ["name", "age", "city", "company", "is_admin"]
    lod: List[Dict[str, Any]] = [get_dict_by_emplyee(e) for e in emps]

    lolany: List[List[Any]] = [[str(d[h]) for h in header] for d in lod]
    lostr: List[str] = [sep.join(l) for l in lolany]

    print(lostr)
    # loj:List[str] = [j.dumps(d) for d in lod]

    # #content = "\n".join(loj)

    with open(path, "w") as wp:
        if header:
            print(sep.join(header), file=wp)
        for line in lostr:
            print(line, file=wp)


def entrypoint():
    emps = read_json("data/sample.json")

    print(emps)
    print(type(emps[0]))

    emps = read_jsonlines("data/sample.jsonline")

    write_json(emps, "data/sample.recreate.json")
    write_jsonline(emps, "data/sample.recreate.jsonline")
    write_delimited(emps, "data/sample.recreate.csv", sep="|")
    write_delimited(emps, "data/sample.recreate2.csv", sep=",",header=False)

    # print(emps)


if __name__ == "__main__":
    entrypoint()
