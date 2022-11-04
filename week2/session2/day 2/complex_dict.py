from typing import Callable, Dict, List, Tuple

l = []
l = list()
l = [1, 2, 3, 4]

d = {}
d = dict()
d = {"one": 1, "two": 2, "three": 3}
d2 = {(1, 2): 1, (2, 3): 3, (0, 0): 4}
d = dict(one=1, two=2, three=3)
d = {"one": 1, "two": 2, "three": 3}

print(d)
print(d2)
print(type(d))

l[0]
d["one"]
print(f"(1,2) element of d2 is {d2[(1,2)]}")
d2[1, 2]


key_of_d2_ordered = list(sorted(d2.keys()))

print(key_of_d2_ordered)
print(key_of_d2_ordered[0])

values_of_d2_ordered = list(sorted(d2.values()))

print(values_of_d2_ordered)

kv = list(sorted(d.items()))
kv2 = list(sorted(d2.items()))

print(kv)
print(kv2)


d["zero"] = 0
print(d)

d2["zero"] = 0
d2[(1, 1)] = "Husnu Sensoy"

print(d2)

print(d)

kv = list(d.items())
print(kv)


def tuple_sorter(t: Tuple[str, int]) -> int:
    return t[1]


tuple_sorter(("one", 1))
tuple_sorter(t=("one", 1))


kv_sorted_custom = sorted(kv)

print(kv_sorted_custom)

kv_sorted_custom = sorted(kv, key=tuple_sorter)

print(kv_sorted_custom)


def xform(
    l: List[Tuple[str, int]], key: Callable[[Tuple[str, int]], Tuple[int, str]]
) -> List[Tuple[int, str]]:
    return [key(e) for e in l]


def mutate(t: Tuple[str, int]) -> Tuple[int, str]:
    s, i = t

    return i * 2, s.title()


def mutate2(t: Tuple[str, int]) -> Tuple[int, str]:
    s, i = t

    return i**2, s.upper()


kv_xformed = xform(kv, key=mutate2)

print(kv_xformed)


d2 = {(1, 2): 1, (2, 3): 3, (0, 0): 4}
d = {"one": 1, "two": 2, "three": 3}


def swap(d: Dict[Tuple[int, int], int]) -> Dict[int, Tuple[int, int]]:
    d_r = {}

    for k, v in d.items():
        d_r[v] = k

    return d_r


def swap2(d: Dict[Tuple[int, int], int]) -> Dict[int, Tuple[int, int]]:
    return {(v, k) for k, v in d.items()}
    # return {v:k for k, v in d.items()}
    # return dict((v,k) for k, v in d.items())


print(swap(d2))
print(swap(d))
print(swap2(d))


d_backup = {(k, v) for k, v in d.items() if k != "one"}

print(d_backup)
v = d.pop("one")


print(v)
print(d)
