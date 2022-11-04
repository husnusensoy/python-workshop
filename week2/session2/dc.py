from dataclasses import dataclass
from typing import List

husnu = "Husnu", "Sensoy", 39, 12, 97.5, 189


@dataclass
class Person:
    name: str
    surname: str
    age: int
    years_of_retention_at_employee: int
    weight: float
    height_in_cm: int


@dataclass
class Team:
    members: List[Person]





husnu = Person(
    name="Husnu",
    surname="Sensoy",
    age=39,
    years_of_retention_at_employee=12,
    weight=97.5,
    height_in_cm=189,
)

husnubad = Person(
    name="Husnu",
    surname="Sensoy",
    age=39,
    years_of_retention_at_employee=12,
    weight=97.5,
    height_in_cm=189,
)

print(husnubad)
