from typing import Dict, Set

d: Dict[bool, str] = {True: "Go to cinema", False: "Stay at home"}

s: Set[bool] = {True, False}


s1: Set[int] = {i * 2 for i in range(1000)}
s2: Set[int] = {i * 3 for i in range(667)}
s3: Set[int] = {i * 5 for i in range(200)}

print(len(s1))
s1.add(2)
print(len(s1))
s1.add(3)
print(len(s1))

print(30 in s1)
print(30 in s2)
print(30 in s3)

s30 = s1 & s2 & s3

# print(s1 - s2)
# print(s1 | s2)
# print(sorted(s30))
