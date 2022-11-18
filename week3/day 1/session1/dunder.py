"""This might be a documentation for my dunder module"""
from dataclasses import dataclass
from typing import Any


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        #return f"{self.name} at age {self.age}"
        return f"Person(name='{self.name}', age={self.age})"

    def speak(self):
        print(f"Hello!!! This is {self.name}")

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.speak()

@dataclass
class PersonDC:
    name:str
    age:int


def entrypoint():
    print(__doc__)
    p = Person("Hüsnü", 39)
    p.speak()

    p()
    p_dc = PersonDC("Hüsnü", 39)

    print(p)
    print(p_dc)


if __name__ == "__main__":
    entrypoint()