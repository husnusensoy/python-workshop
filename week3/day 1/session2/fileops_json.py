import json as j
from pprint import pprint as pp
from typing import List

from fileops import Employee, get_employee, get_employee_by_content


# def get_employee_by_content(
#     name_surname: str, age_str: str, company: str, city: str, is_admin: bool = False
# )
def read_json(fp) -> List[Employee]:

    header = ["name", "age", "company", "city", "is_admin"]

    l = j.load(fp)

    # return [get_employee_by_content(*[rec.get(field,"Global Maksimum") for field in header]) for rec in l]

    return [get_employee(d) for d in l]


def read_json_line(fp) -> List[dict]:

    # l = j.load(fp)

    return [j.loads(rec) for rec in fp.read().split("\n")]


if __name__ == "__main__":
    with open("data/sample.json") as fp:
        list_of_employees = read_json(fp)

    pp(list_of_employees)

    with open("data/sample.jsonline") as fp:
        emps = read_json_line(fp)

    pp(emps)
