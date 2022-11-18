import math


def is_euc(a, b, c: float) -> bool:
    e1, e2, e3 = sorted((a, b, c))

    return e1**2 + e2**2 == e3**2


def area(r: float) -> float:
    return math.pi * r**2