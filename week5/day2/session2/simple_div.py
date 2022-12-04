from dataclasses import dataclass
from typing import Any, Tuple, Union

# GoLang


@dataclass
class MathResult:
    value: float
    success: bool
    description: str


def div01(a, b: int) -> MathResult:
    if b == 0:
        return MathResult(value=0, success=False, description="Divison by zero")
    else:
        return MathResult(value=a / b, success=True, description="Success")


def div02(a, b: int) -> Tuple[float, Union[str, None]]:
    if b == 0:
        return 0, "Divison by zero"
    else:
        return a / b, None


div = div01


def do_math():
    res = div(13, 0)

    if res.success:
        print(f"Division= {res.value}")
    else:
        print(f"Houston we have a problem: {res.description}")

    res = div(12, 4)

    if res.success:
        print(f"Division= {res.value}")
    else:
        print(f"Houston we have a problem: {res.description}")

    v, err = div02(13, 0)

    if err is None:
        print(f"Division= {v}")
    else:
        print(f"Houston we have a problem: {err}")

    v, err = div02(12, 4)

    if err is None:
        print(f"Division= {v}")
    else:
        print(f"Houston we have a problem: {err}")


class BoundList:
    def __init__(self, n: int = 10):
        self.l = []
        self.max_length = n

    def append(self, e: Any) -> bool:
        """List is bound so maximium number of elements is limited with n"""

        if len(self.l) == self.max_length:
            return False
        else:
            self.l.append(e)
            return True

    def at(self, i: int) -> Tuple[Any, bool]:
        """i can only take non-negative values. we are not allowed to ask for negative numbers"""
        if 0 <= i < self.max_length:
            return self.l[i], True
        else:
            return None, False


class MaxCapacityReached(Exception):
    def __init__(self, max_capacity: int) -> None:
        super().__init__()

        self.max_capacity = max_capacity

    def __str__(self) -> str:
        return f"Max capacity of {self.max_capacity} is exceeded"


class NegativeIndexError(Exception):
    def __init__(self, index: int) -> None:
        super().__init__()

        self.index = index

    def __str__(self) -> str:
        return f"Negative index {self.index} is not allowed for Bounded List"


class HighBoundExceeded(Exception):
    def __init__(self, index: int, max_capacity: int) -> None:
        super().__init__()

        self.index = index
        self.max_capacity = max_capacity

    def __str__(self) -> str:
        return f"{self.index} is not allowed for a Bounded List of max capacity {self.max_capacity}"


class BoundListPP:
    def __init__(self, n: int = 10):
        self.l = []
        self.max_length = n

    def append(self, e: Any):
        """List is bound so maximium number of elements is limited with n"""

        if len(self.l) == self.max_length:
            raise MaxCapacityReached(self.max_length)
        else:
            self.l.append(e)

    def at(self, i: int) -> Any:
        """i can only take non-negative values. we are not allowed to ask for negative numbers"""

        if i < 0:
            raise NegativeIndexError(i)

        if i >= self.max_length:
            raise HighBoundExceeded(i, self.max_length)

        return self.l[i]


def bounded_list_driver():
    bl = BoundList(3)

    items = ["first", "second", "third", "fifth"]

    for i in items:
        status = bl.append(i)

        if status:
            print(f"I succeed to append element '{i}'")
        else:
            print(
                f"Bounded list with a maximum capacity of {bl.max_length}. Failed to append '{i}'"
            )

    for i in [-1, 0, 1, 2, 3, 4]:
        v, status = bl.at(i)

        if status:
            print(f"Element at {i}= {v}")
        else:
            print(
                f"Bounded list of size {bl.max_length} does not allow you to access index {i}"
            )


def bounded_list_driver2():
    bl = BoundListPP(3)

    items = ["first", "second", "third", "fifth"]

    for i in items:
        try:
            bl.append(i)
            print(f"{i} is added")
        except MaxCapacityReached as err:  # MaxCapacityReached
            print(err)
            print(err.max_capacity)

    print("Adding elements is over.")
    for i in [-1, 0, 1, 2, 3, 4]:
        try:
            v = bl.at(i)
            print(f"Value at {i}={v}")
        except NegativeIndexError as err:  # NegativeIndexError | HighBoundExceeded
            print(err)
            print(err.index)
        except HighBoundExceeded as err:
            print(err)
            print(err.index)
            print(err.max_capacity)


if __name__ == "__main__":
    bounded_list_driver2()

    # s = bl.at(0)
    # s = bl.at(1)
    # s = bl.at(-1)  # this is also an issue


# resposnse = requests.get("https://google.com")
