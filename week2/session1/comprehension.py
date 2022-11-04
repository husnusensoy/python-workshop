lst = ["Jack", "Joe", "William", "Avarel"]
surname = ["Dalton"] * 4

indexes = list(range(len(lst)))

tuple_list = []

for i in indexes:
    tuple_list.append((i, lst[i]))

print(tuple_list)
print(list(enumerate(lst)))


tuple_list = [(i, lst[i]) for i in range(len(lst))]

# Comprehension
# List Comprehension
tuple_list_with_even_index = [(i, e) for i, e in enumerate(lst) if i % 2 == 0]
tuple_list_with_odd_index = [(i, e) for i, e in enumerate(lst) if i % 2 == 1]

print(tuple_list_with_even_index)


tuple_list_with_even_index = []
tuple_list_with_odd_index = []

for i in indexes:
    if i % 2 == 0:
        tuple_list_with_even_index.append((i, lst[i]))
    else:
        tuple_list_with_odd_index.append((i, lst[i]))

print(tuple_list_with_even_index)


tuple_list_with_odd_index = [
    (e, rest) for e, *rest in zip(lst, surname, indexes) if rest[1] % 2 == 1
]

print(tuple_list_with_odd_index)
