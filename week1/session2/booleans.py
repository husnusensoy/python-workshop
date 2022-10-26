b10 = True
b11 = bool(4)
b12 = bool(-6)

b20 = False
b21 = bool(0)
b22 = bool("")

print(b10 == b11)

print("See that all True")
print(b10 == b11 == b12)

print("See that all False")
print(b20 == b21 == b22)

b_and = b10 and b20
b_or = b10 or b20
b_x = b10 or (not b20)

# EQ and NEQ
b_arithm = 1 == 1  # eq
print(b_arithm)

b_arithm = 1 != 1  # neq
b_arithm = 1 < 2  # lt
b_arithm = 1 > 2  # gt
b_arithm = 1 <= 2  # lte
b_arithm = 1 >= 2  # gte


print(1 < 2 <= 3)