from dataclasses import dataclass
from typing import List


@dataclass
class Employee:
    name:str
    surname:str
    age:int
    company: str
    city:str
    is_admin: bool


def read_file(path: str) ->None:
    fp = open(path)

    for line in fp:
        print(line.strip())

    #fp.close()

    fp.seek(0)

    print([line.strip() for line in fp.readlines()])
    fp.close()

def read_file_better(path: str) ->List[Employee]:

    employees:List[Employee] = []
    with open(path) as fp:
        for line in fp:
            fields = line.strip().split(',')

            if len(fields) == 4:
                name,surname = fields[0].rsplit(' ',maxsplit=1)
                age = int(fields[1])
                company, city = fields[2:]

                employees.append(Employee(name=name,surname=surname,age=age, company=company,city=city))


            else:
                print(f"BAD RECORD: {line.strip()}")

    return employees



        
    

def entrypoint():
    read_file("data/sample.csv")
    emps = read_file_better("data/sample.csv")

    print(emps)


if __name__ == "__main__":
    entrypoint()
