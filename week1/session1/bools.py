# Boolean operation
bool_v1 = True
bool_v2 = False
bool_v3 = None

print(bool_v1 == bool_v2)  # False
print(bool_v1 == (not bool_v2))  # True
print((not bool_v1) == bool_v2)  # True
print(not bool_v1)  # False
print(bool_v3)  # ?
print(not bool_v3)  # ?
print(bool_v3 is None)  # ?

# Boolean arithemetics
print()
print("## Boolean arithemetics")
print()
print (bool_v1 and bool_v2) # False
print (bool_v1 or bool_v2) # True
print(1 == 1)
print(1 != 2)
print(1 < 2)
print(1 <= 2)
print(2 > 1)
print(2 >= 1)


print(1 < 2 <= 3)
print(1 < 2 and 2<= 3)
