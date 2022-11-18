from dataclasses import dataclass
from typing import Any, Dict, List

CONTENT = """Name,Age,Company,City
Mehmet Fahri Sensoy,39,Global Maksimum,İstanbul
Kerem Kargin,25,Global Maksimum,İstanbul
İnanç Dokurel,28,Global Maksimum,İzmir"""


@dataclass
class Employee:
    name: str
    surname: str
    age: int
    company: str
    city: str
    is_admin: bool 
    flex: Dict[str,Any]


def get_employee(d: Dict[str,Any])-> Employee:
    name = d['name']
    surname = d['surname']
    age = int(d['age'])
    company = d.get('company',"Global Maksimum")
    city = d['city']
    is_admin = bool(d.get('is_admin', False))

    flex = d.copy()
    flex.pop("name")
    flex.pop("surname")
    flex.pop("age")

    if "company" in flex:
        flex.pop("company")

    flex.pop("city")
    if "is_admin" in flex:
        flex.pop("is_admin")

    return Employee(name,surname,age,company,city,is_admin,flex)





@dataclass
class EmployeeGroup:
    name: List[str]
    surname: List[str]
    age: List[int]
    company: List[str]
    city: List[str]
    is_admin: List[bool]

    

    def add(self, e: Employee):
        self.name.append(e.name)
        self.surname.append(e.surname)
        self.age.append(e.age)
        self.company.append(e.company)
        self.city.append(e.city)
        self.is_admin.append(e.is_admin)


def get_employee_by_content(
    name_surname: str, age_str: str, company: str, city: str, is_admin: bool = False
) -> Employee:
    age = int(age_str)

    # Another was to get names and surname
    # *names, surname = name_surname.split()
    # name = "".join(names)

    name, surname = name_surname.rsplit(maxsplit=1)

    # print(name)
    # print(surname)

    e = Employee(name, surname, age, company, city,is_admin)

    return e


def read_file(path=None, sep: str = ","):
    if path is None:
        header, *body = CONTENT.split("\n")
    else:
        header, *body = fp.read().split("\n")

        # fp = open(path)
        # fp.close()

    fields = header.split(sep)

    print(fields)

    ll: List[List[str]] = [line.split(sep) for line in body]

    emps = [get_employee_by_content(*_ll) for _ll in ll]



    return emps


if __name__ == "__main__":

    e = get_employee_by_content(
        *["Mehmet Fahri Sensoy", "39", "Global Maksimum", "İstanbul"]
    )

    with open("data/sample.csv") as fp:
        list_of_employees = read_file(fp)

    print(list_of_employees)

    list_of_employees = read_file()
    print(list_of_employees)


    # c = -1
    # try:
    #     c = int("10")
    # except ValueError:
    #     print(f"Problem in string to int conversion asgb")

    # print(c)
