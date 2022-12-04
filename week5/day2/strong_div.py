from cmath import exp
from multiprocessing.sharedctypes import Value
from typing import Tuple, Union

BAD_INPUT, DIV_ZERO,OTHER = 0,1,2

class MyDivisorIssues(Exception):
    def __init__(self, a,b:str,reason:int):
        self.a = a
        self.b = b
        self.reason = reason

    def __str__(self):
        if self.reason == BAD_INPUT:
            return f"Either of '{a}' or '{b}' is not an integer"
        else:
            return f"'b' is zero"


def div(a, b: str) -> Tuple[float, Union[str, None]]:
    try:
        ia, ib = int(a), int(b)

        return ia / ib, None
    except ZeroDivisionError:
        raise MyDivisorIssues(a,b, DIV_ZERO)     
    except ValueError:
        raise MyDivisorIssues(a,b, BAD_INPUT)   
    except Exception:
        raise MyDivisorIssues(a,b, OTHER) 


def bad(a, b: str) -> Tuple[float, Union[str, None]]:
    try:
        ia, ib = int(a), int(b)

        return ia / ib, None
    except Exception:
        return 0.0, f"Somthing happend event it doesnt"


a = input("Divident\n> ")
b = input("Divisor\n> ")

try:
    d, msg = div(a, b)
    print(f"{a}/{b} = {d}")
except MyDivisorIssues as mdi:
    print(mdi)
    print(mdi.a)
    print(mdi.b)


