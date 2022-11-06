import json
from collections import Counter
from itertools import permutations
from itertools import zip_longest as zipl
from json import dumps as jdumps
from json import loads

complex = dict(
    names=["Jack", "Joe", "William"],
    weapons=dict(knifes=[1, 2, 3, 4], guns=[1, 2, 3, 3], is_lethal=True),
)

print(jdumps(complex))

print(json.dumps(complex))


s1 = "The quick fox jumps over the lazy dog ."
s2 = "I saw the girl on the hill with the telescope ."

c1 = Counter(s1.lower().split())
c2 = Counter(s2.lower().split())

print(c1)
print(c2)

c = c1 + c2

print(c)

l1 = ["a", "b"]
l2 = [1, 2, 3, 4]

for a, b in zipl(l1, l2):
    print(f"{a}, {b}")


for perm in permutations(l2, 3):
    print(perm)
