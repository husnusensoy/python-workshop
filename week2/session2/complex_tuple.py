# Entity of a Person
name = "Husnu"
surname = "Sensoy"
age = 39

husnu = "Husnu" , "Sensoy", 39


print(husnu)

print(husnu[0])
print(husnu[0:2])

age # ? what is the type of age ? 

print(type(age))
print(type(husnu))

# Mutable vs Immutable
# husnu[2] = husnu[2] + 1

a = 1
b = 2

# Other languages
# c = a
# a = b
# b = c


# Python for swap
a,b = b,a

name, *rest = husnu

print(name)
print(rest)

print(type(rest)) # TODO: Then, whas is list type ?


name, *_, age = husnu
print(_)

print(f"{name} ? is at age of {age}")





# TODO: Why we can not use attributes with tuple ? 