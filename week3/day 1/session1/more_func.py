from typing import Union

from dunder import Person
from mymath import polynomial as p
from mymath.polynomial import Polynomial


def inc(a: int, step: int = 1) -> int:
    return a + step


def total_price(
    unit_price: float,
    amount: int = 1,
    kdv: float = 0.08,
    tevk: float = 0.0,
    discount: float = 0.0,
) -> Union[float, None]:

    if kdv not in (0.00, 0.01, 0.08, 0.18):
        print(f"Invalid KDV ratio {kdv}")
        return None

    if not (0 <= discount < 1 and 0 <= tevk < 1):
        print(f"Invalid discount or tevk ratio {kdv}")
        return None

    subtotal = unit_price * amount
    discounted = subtotal * (1 - discount)
    total = discounted * (1 + kdv) * (1 - tevk)

    return total


def infinite_sum(*nums) -> int:
    return sum(nums)


def zoo(*animals, **animal_count):
    print(animals)
    print(animal_count)

    for an in animals:
        # print(f"We have {animal_count[an] if an in animal_count else 0} {an} in our zoo")
        print(f"We have {animal_count.get(an,0)} {an} in our zoo")


if __name__ == "__main__":
    print(inc(5, 2))
    print(inc(5))

    print(inc(5, step=2))

    print(total_price(5, 10, kdv=0.18, tevk=0.0, discount=0.05))
    print(total_price(5, 10, kdv=0.18, discount=0.05))
    print(total_price(5, 10, discount=0.05, kdv=0.18))
    # FIXME: print(total_price(5, discount=0.05 ,10,  kdv=0.18))

    print(infinite_sum(1, 2))
    print(infinite_sum(1, 2, 3))
    print(infinite_sum(1, 2, 3, 4))
    print(infinite_sum(1, 2, 3, 5))

    zoo("lion", "monkey", "elephant", lion=3, monkey=4, elephant=2)

    print(Person("Hüsnü Şensoy",39))

    poly1 = Polynomial(1,2,3)
    poly2 = p.Polynomial(1,2,3)

    
    
