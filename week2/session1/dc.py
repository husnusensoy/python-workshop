from dataclasses import dataclass

tup = ("Husnu", "Sensoy", 39, 12, 97.4)


@dataclass
class Human:
    """Class represents a human entity for our program.

    last_emplyee_retention is set in years
    weight in kg
    """

    name: str
    surname: str
    age: int
    last_emplyee_retention: int
    weight: float


hs = Human(
    name="Husnu", surname="Sensoy", age=39, last_emplyee_retention=12, weight=97.4
)

ns = Human(
    name="Nuri", surname="Sensoy", age=35, last_emplyee_retention=4, weight=95
)

print(hs == ns)



print(hs)
print(hs.name)
