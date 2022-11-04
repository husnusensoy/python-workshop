from typing import Callable, Union


def addi(a: int, b: int) -> int:
    return a + b

def mult(a: int, b: int) -> int:
    return a * b    

def divi(a: int, b: int) -> int:
    return a // b        

def subs(a: int, b: int) -> int:
    return a - b            


def prompt(text: str, value: int) -> None:
    print(f"{text}... Value: {value}")


def do_operation(op: Callable[[int, int], int], a: int, b: int) -> Union[int,None]:
    
    if type(a) == int and type(b) == int:
        print("I will be doing the operation for you now")

        c = op(a, b)
        prompt("Result", c)
    else:
        print(f"Expecting integer for a,b {type(a)},{type(b)} found")


        c = None

    return c


c = addi(1, 2)

prompt("Result of 1 + 2", c)

do_operation(addi, 1, 2)
do_operation(subs, 1, 2)
do_operation(mult, 1, 2)
do_operation(divi, 1, 2)

res = do_operation(divi, 1, 2.)
print(res)
