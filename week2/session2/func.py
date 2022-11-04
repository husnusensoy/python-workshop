from ast import Call
from curses.ascii import isdigit
from typing import Callable, Tuple, Union


def add2i(a: int, b: int) -> int:
    return a + b


def min2i(a: int, b: int) -> int:
    return a - b


def mul2i(a: int, b: int) -> int:
    return a * b


def div2i(a: int, b: int) -> int:
    return a // b


def int_reader_with_retry(prompt: str, max_retry_count: int) -> Union[int, None]:

    for _ in range(max_retry_count):
        inp = input(prompt)

        if inp.isdigit():
            return int(inp)

    print(f"Max retry count of {max_retry_count} is exceeded. Do calculate your self")
    return None


def operator_builder_with_retry(
    prompt: str, max_retry_count: int
) -> Union[Callable[[int, int], int], None]:
    for _ in range(max_retry_count):
        inp = input(prompt)

        if inp in ["+", "-", "/", "*"]:
            if inp == "+":
                return add2i
            elif inp == "-":
                return min2i
            elif inp == "*":
                return mul2i
            else:
                return div2i

    print(f"Max retry count of {max_retry_count} is exceeded. Do calculate your self")
    return None


OPERAND_READ_FAILED, OPERATOR_READ_FAILED, SUCCESS = 0, 1, 2  # enum
message = ["Operand read failed", "Operator read failed"]


def tui() -> Tuple[int, Union[int, None]]:
    a = int_reader_with_retry("Provide the first operand\n> ", 3)

    if a is None:
        return OPERAND_READ_FAILED, 1

    b = int_reader_with_retry("Provide the second operand\n> ", 3)

    if b is None:
        return OPERAND_READ_FAILED, 2

    op = operator_builder_with_retry("Provide the operator\n> ", 3)

    if op is None:
        return OPERATOR_READ_FAILED, None

    print(op(a, b))

    return SUCCESS, None


print(add2i(1, 2))
print(min2i(1, 2))
print(mul2i(1, 2))
print(div2i(1, 2))

while True:
    retcode, *detail = tui()

    if retcode != SUCCESS:
        print("Something has failed with parameter reading.")
        print(f"Detail: {message[retcode]} {detail}")
