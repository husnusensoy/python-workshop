from typing import Callable, List

lst = ["Jack", "Joe", "William", "Avarel"]

def diy_reverse(orginal:List[str]) -> List[str]:

    rev: List[str] = []

    n = len(orginal)
    for i in range(n):
        rev.append(orginal[n - i -1])

    return rev




def test_func(expectation:List[str], orginal:List[str], your_fn: Callable[[List[str]], List[str]]) -> None:
    res = your_fn(orginal)

    if res  == expectation:
        print("OK")
    else:
        print(f"FAIL: Expected {expectation} Found {res}")


test_func( list(reversed(lst)), lst, diy_reverse)
test_func( [], [], diy_reverse)
test_func( ["Jack"], ["Jack"], diy_reverse)
