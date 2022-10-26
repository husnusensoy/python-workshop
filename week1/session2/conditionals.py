"""A chapter on if/else/elif"""

temp = int(input("What is the temprature for today : "))

if 15 < temp <= 20:
    print("A good day for walking...")
elif 28 < temp < 35:
    print("A good day for swimming...")
else:
    print("Stay at home")

msg = "A good day for walking..." if 15 < temp <= 20 else "Stay at home"

print(msg)