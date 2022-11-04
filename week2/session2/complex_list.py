# print(int("346346346335"))
# print(int("a849595",16))
# This will raise an error print(int("a849595"))

husnu = []
husnu = list()
tup = "Husnu", "Sensoy", 39
husnu = list(tup)  # To list
tup = tuple(husnu)  # To tuple
husnu = ["Husnu", "Sensoy"]

print(len(husnu))

husnu.append(39)
print(husnu)

husnu = ["Sensoy", 39]

husnu.insert(0, "Husnu")

print(husnu)

surname = husnu.pop(1)
print(f"I have popped up surname '{surname}' from the list.")


l1 = ["a", "b"]
l2 = ["c", "d"]


l3 = l1 + l2

print(l3)


t1 = 1, 3, 2, 4, 6, 5, 8, 7 # tuple
l1 = [1, 3, 2, 4, 6, 5, 8, 7] # list

print(f"l1 before calling .sorted {l1}")
#l1 = l1.sort()

l1s = sorted(l1)

print(f"l1 after calling .sorted {l1}")
print(f"l1 (sorted) {l1s}")

print(f"l1 before calling .reversed {l1}")
# l1.reverse()

il1r = reversed(l1)

print(next(il1r))
print(next(il1r))
print(next(il1r))
print(next(il1r))
print(next(il1r))

l1 = [1, 3, 2, 4, 6, 5, 8, 7] # list


print(f"l1 after calling .reversed {l1}")
#print(f"l1 (reversed) {l1r}")

l1c = l1
l1.sort()



