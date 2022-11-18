from dataclasses import dataclass


class Car:
    def __init__(self, hp: int, top_speed: int, is_electric: bool = False) -> None:
        self.hp = hp
        self.top_speed = top_speed
        self.is_electric = is_electric

    def __str__(self) -> str:
        return f"a {self.hp} HP {'electric' if self.is_electric else 'fuel'} car with a top speed of {self.top_speed} km/s"
        # return f"{self.__class__.__name__}"


@dataclass
class Excavator:
    hp: float
    max_weight: float
    manufacture_year: int
