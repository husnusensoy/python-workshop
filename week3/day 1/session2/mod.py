from gadget.engine import Car, Excavator
from mymath.arit import Add
from mymath.func import Polynomial
from mymath.geom import is_euc


def entrypoint():
    p = Polynomial(coeff=[1, 2, 3])

    print(p.eval(3))

    print(is_euc(3, 4, 5))

    #c0 = Car(160)
    #print(f"My car is {c0}")
    c = Car(160, 220)
    print(f"My car is {c}")

    tesla = Car(160, 220, True)
    e = Excavator(500, 40_000, 2020)

    print(f"My car is {tesla}")
    print(f"Their machine is {e}")

    a = Add(3,4)

    print(a.calculate())
    print(a())

    






if __name__ == "__main__":
    entrypoint()
