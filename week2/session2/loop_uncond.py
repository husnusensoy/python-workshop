r = list(range(100))
same = ["Dalton"] * 100

list_r = list(r)

print(list_r)

for i in list_r:
    print(f"Excuse me!!! {i}")
    print(f"Excuse me!!! {same[i]}")

for e in same:
    print(f"Excuse me!!! {e}")

for i in range(len(same)):
    print(f"Excuse me!!! {same[i]} for the {r[i] + 1} times")

for (i, e) in enumerate(same):
    print(f"{i}. {e}")

enum = list(enumerate(same))

for j in range(len(same)):
    i, e = enum[j]
    print(f"{i}. {e}")

list_enum = list(enum)

name = ["Joe", "Jack", "William", "Avarel"]
surname = ["Dalton"] * 4
height = [1, 1.5, 2, 3]

for (i, (n,s,h)) in enumerate(zip(name,surname,height)):
    print(f"{i+1}. member of the ganster. My name is {n} {s} with an heigth of {h * 150}")

zlist = list(zip(name,surname,height))

print(type(zlist[0]))
print(zlist[0])

# print(list_enum)

print(type(list_enum[11]))



