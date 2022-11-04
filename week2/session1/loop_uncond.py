lst = [0, 1, 2, 3, 4, 5]
lst2 = [None, True, False, "Husnu", 3.14, 9]


proper_way_of_listing = list(range(6))
print(proper_way_of_listing)

print(0)
print(1)
print(2)
print(3)

for i in proper_way_of_listing:
    print(i)

for i in list(range(6)):
    print(i)

for i in range(6):
    print(i)

for e in lst2:
    print(e)

print(f"0the elementh of {lst2} is {lst2[0]}")

n = len(lst2)
print(f"{list(range(n))}")


for i in range(len(lst2)):
    e = lst2[i]
    print(f"{i}. element of {lst2} is {e}")

for i, e in enumerate(lst2):
    print(f"{i}. element of {lst2} is {e}")

enum_output = list(enumerate(lst2))

i, e = enum_output[0]
i, e = enum_output[1]
i, e = enum_output[2]
i, e = enum_output[3]
