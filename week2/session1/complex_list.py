from multiprocessing import pool

lst = [1,2,3,4,5]

print(lst)
print(type(lst))

lst.append(6)
print(lst)

lst.append("Husnu Sensoy")
print(lst)

lst.insert(0, -1)
print(lst)

print(lst[2:4])

print(len(lst))

popped = lst.pop(2)

print(f"You have popped {popped} at index 2")
print(lst)


new_list = [1,2,3,4,5,6]

print(f"New List: {new_list}")
new_list.reverse()
print(f"New List  (after reverse): {new_list}")


new_list.sort()
print(f"New List  (after sort): {new_list}")

new_list = [2,1,4,3,6,5]

print(f"New List: {new_list}")

new_list_reversed = list(reversed(new_list))
print(f"New List  (after reverse): {new_list}")
print(f"New List  (after reverse): {new_list_reversed}")

new_list_sorted = list(sorted(new_list))
print(f"New List  (after sort): {new_list_sorted}")
print(f"New List  (after sort): {new_list}")

# TODO: To Tuple or To List

tup = 1,2
lst = [1,2]

lst_from_tuple = list(tup)
tup_from_list = tuple(lst)

print(f"I a list {lst} to be a tuple {tup_from_list}")
print(f"I a tup {tup} to be a list {lst_from_tuple}")