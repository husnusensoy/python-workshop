"""In this chapter we talk about if/elif/else"""

temp = 25

if temp < 23:
    print("Good for a walk")
elif temp < 30:
    print("Good for a swim")
else:
    print("Find a climate control...")

print("Good for a walk" if temp < 23 else "Good for a swim")