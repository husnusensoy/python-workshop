s = {"one"}
l = ["one"]

print(type(s))

for _ in range(100):
    s.add("one")

print(s)
print(l)

mul2 = {e*2 for e in range(1000)}
mul3 = {e*3 for e in range(600)}
mul4 = {e*4 for e in range(500)}

print(mul2 | mul3)
print(mul4 - mul2)
print(f"Multiplier of 6: {mul3 & mul2}")

l_from_s = list(s)
s_from_l = set(l)
