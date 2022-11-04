tup = 1,2,3,4,5 # Homogenious tuple
tup = (1,2,3,4,5) # Homogenious tuple

print(tup)
print(type(tup))


print(tup[0])
print(tup[0:2])

print(type(tup[0:2]))

# Tuples does not allow modification aka Immutable: tup[0] = 5

# Unpacking
a,b, *rest = tup

print("Unpacking")
print(a)
print(b)
print(rest)
print(type(rest))

print("Using _ (special variable)")
a,b, *_ = tup

print(a)
print(b)
#print(rest)

print("Heterogenous Tuple")
tup_het = 1, "Monkey", None, True, 3.14

print(type(tup_het))
print(tup_het[0:2])

print(tup[0] + 1 )
print(tup[1] + 1 )
print(tup[2] + 1 )


# if type(tup_het[0] ) == int or type(tup_het[0] ) == float or type(tup_het[0] ) == bool:
#     print(tup_het[0] + 1 )

# if type(tup_het[1] ) == int or type(tup_het[1] ) == float or type(tup_het[1] ) == bool:
#     print(tup_het[1] + 1 )

# if type(tup_het[2] ) == int or type(tup_het[2] ) == float or type(tup_het[2] ) == bool:
#     print(tup_het[2] + 1 )

# if type(tup_het[4] ) == int or type(tup_het[4] ) == float or type(tup_het[4] ) == bool:
#     print(tup_het[4] + 1 )    





