evens = []
odds = []

for i in range(10_000):
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)


evens = [i for i in range(10_000) if i % 2 == 0]
odds = [i for i in range(10_000) if i % 2 == 1]

print(evens)

string_of_ints = [str(i) for i in range(1000)]
strings_of_ints_with_badguys = string_of_ints + ["a", "b", "c", "d"]
print(string_of_ints)

ints = [int(e) if e.isdigit() else None for e in strings_of_ints_with_badguys]
tints = tuple((int(e) if e.isdigit() else None for e in strings_of_ints_with_badguys))
tints_with_exclusion = tuple(
    (int(e) for e in strings_of_ints_with_badguys if e.isdigit())
)

print(ints)
print(tints)
print(tints_with_exclusion)




