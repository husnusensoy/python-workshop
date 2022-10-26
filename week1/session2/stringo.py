name = "HüsnÜ"
surname = "ŞeNsoY"


full_name = name + " " + surname
# full_name = name  " "  surname

first_string = "My name is 'husnu sensoy'"
second_string = 'My name is "husnu sensoy"'


dynamic_string = "My name is %s %s" % (name, surname)
print(dynamic_string)

dynamic_string = "My name is {} {}".format(name, surname)
print(dynamic_string)

dynamic_string = f"My name is {name} {surname}"
dynamic_string = f"My name is {name.title()} {surname.title()} with a total of {len(name) + len(surname)} characters"

print(dynamic_string)


# Indexing & Slicing
i = 3
print(f"{i}. character of string '{name}' is {name[i]}")

b, e = 2, 4

print(f"Substring between {b}:{e} of string '{name}' is {name[b:e]}")

print(f"Substring between :{e} of string '{name}' is {name[:e]}")
print(f"Substring between {b}: of string '{name}' is {name[b:]}")

b = len(name) -3 
b = -3
print(f"Substring between {b}: of string '{name}' is {name[b:]}")

# print(full_name)
