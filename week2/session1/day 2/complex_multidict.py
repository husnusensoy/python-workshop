from typing import Dict, List

d: Dict[bool, str] = {True: "Go to cinema", False: "Stay at home"}

print(d)

d[True] = "Go to sea shore"

print(d)


md: Dict[bool, List[str]] = {True: ["Go to cinema"], False: ["Stay at home"]}

n:int = 10
for _ in range(10_000):
    if len(md[True]) == n:
        md[True].pop(0)

    md[True].append("Go to sea shore")

print(f"Size of the history {len(md[True])}")

print(md[False][-1])
print(md[False])

print(md[True][-1])
print(md[True])

print(md)
