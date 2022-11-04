import json as js
import string
from collections import Counter
from itertools import product, zip_longest
from pprint import pprint as pp
from typing import Dict, List, Tuple

print(string.ascii_letters)
print(string.punctuation)
print(string.digits)

c_of_char = Counter('gallahad')
c_of_words1 = Counter("The quick brown fox jumps over the lazy dog .".lower().split())
c_of_words2 = Counter("I saw the man on the hill with the telescope .".lower().split())

c_of_words = c_of_words1 + c_of_words2

print(c_of_char)
print(c_of_words)

d = {"name": "Husnu","surname":"Sensoy","age":39,"has_pet":False}

print(d)
print(js.dumps(d))

pp(c_of_words)



d_loaded = js.loads('{"name": "Husnu", "surname": "Sensoy", "age": 39, "has_pet": false}')

print(type(d_loaded))

print(list(product([1,2,3],['a','b','c'],[True,False],[1.3,1.2,.19])))


for a,b in zip_longest([1,2],[1,2,3]):
    print(f"{a}, {b}")