from dataclasses import dataclass
from typing import Any, Callable, Tuple, Union


def get_input() -> Tuple[int, int]:
    a = int(input("Divident\n> "))
    b = int(input("Divisor\n> "))

    return a, b


@dataclass
class Result:
    d: float
    status_code: bool
    reason: str


def div01(a, b: int) -> Result:
    if b == 0:
        return Result(0.0, status_code=False, reason="Divisor is given to be 0")
    else:
        return Result(a / b, status_code=True, reason="")


def div02(a, b: int) -> Tuple[float, Union[None, str]]:
    if b == 0:
        return 0.0, "Divisor is given to be 0"
    else:
        return a / b, None


def div03(a, b: int) -> Tuple[float, Union[None, str]]:
    try:
        res, msg = a / b, None
    except ZeroDivisionError:
        res, msg = 0.0, "Divisor is given to be 0"

    return res, msg


def driver(divisor_implementaion: Callable[[int, int], Any]):
    a, b = get_input()

    d, msg = divisor_implementaion(a, b)

    if not msg:
        print(f"{a}/{b} = {d}")
    else:
        print(msg)


if __name__ == "__main__":
    driver(div03)
