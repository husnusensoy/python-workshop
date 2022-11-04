from dataclasses import dataclass
from typing import Dict, List, Tuple

l = [1, 2, 3]


@dataclass
class SomeObject:
    order_id: int
    shipment_id: int
    vendor_id: int


print(l[0])

so = SomeObject(order_id=1, shipment_id=2, vendor_id=3)

so.order_id
so.shipment_id
so.vendor_id

l = []
l = list()
l = [1, 2, 3]

d = {}
d = dict()
d = {"order_id": 1, "shipment_id": 2, "vendor_id": 3}

print(d)

d["cargo_on_us"] = True

print(d["order_id"])


print(f"Do you carry 'warehouse_id': {'warehouse' in d}")
print(f"Do you carry 'order_id': {'order_id' in d}")


m = [[1, 2, 0], [0, 1, 1], [0, 0, 1]]  # ~36 byte storage capacity Sparsity 20 byte


def show_matrix(m: List[List[int]]) -> None:
    """Pretty printing of dense matrix"""

    for i, _ in enumerate(m):
        for v in m[i]:
            print(v, end=" ")

        print()


show_matrix(m)


m[0][1]
print(f"Elements in row 0 and col 2 is {m[0][2]}")


def to_sparse(m: List[List[int]]) -> Dict[Tuple[int, int], int]:
    sparse = {}
    for i, _ in enumerate(m):
        for j, v in enumerate(m[i]):
            if v != 0:
                sparse[i, j] = v

    return sparse


s = to_sparse(m)


def get_value(s: Dict[Tuple[int, int], int], index: Tuple[int, int]) -> int:
    if index in s:
        return s[index]
    else:
        return 0


print(s)

print(s[0, 1])

print(f"Elements in row 0 and col 2 is {get_value(s, (0,2))}")
print(f"Elements in row 0 and col 2 is {s.get((0,2),0)}")


numbers = {"one": 1, "two": 2, "three": 3}  # {1:"one",2:"two",3:"three"}

print(numbers.keys())
print(numbers.values())

kv: List[Tuple[str,int]] = list(numbers.items())
vk: List[Tuple[int,str]] = [(v,k) for k,v in kv]

numbers_r = dict(vk)
numbers_r = {(v,k) for k,v in kv}
numbers_r = {v:k for k,v in kv}

print(numbers_r)

v= numbers.pop("one")

#_= numbers.pop("one")

numbers.pop("one")

print(numbers)

#print(kv)


"""
void *l = malloc(sizeof(void*) * N)

void *elemen = malloc(sizeof(char))
&element = 'c'
l[0] = element


void *elemen = malloc(sizeof(int))
&element = 4
l[1] = element


int *l = (int*) malloc(sizeof(int) * 10195149)

"""

import array  # import numpy
