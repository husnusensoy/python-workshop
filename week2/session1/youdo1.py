from curses.ascii import isdigit
from math import expm1
from pickle import FALSE

bot_name = "Aid"  # You can change bot's name
birth_year = 2020

# Write your code here

print(f"Hello! My name is {bot_name}.")
print(f"I was created in {birth_year}.")


user_name = input("Please, remind me your name.\n> ")

print(f"What a great name you have, {user_name.title()}!")

print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")


input_success = False

while not input_success:
    all_rem = input("Remainder division by 3,5,7\n> ")
    elements = all_rem.split()

    if len(elements) < 3:
        print("RETRY: Ensure that you provide 3 inputs")
        continue

    e1, e2, e3 = elements

    if not (e1.isdigit() and e2.isdigit() and e3.isdigit()):
        print("RETRY: Non integer input")
        continue

    rem3, rem5, rem7 = [int(e) for e in all_rem.split()]

    if not (0 <= rem3 < 3 and 0 <= rem5 < 5 and 0 <= rem7 < 7):
        print("RETRY: Ensure that remainder ranges are proper.")
        continue

    your_age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print(f"Your age is {your_age}; that's a good time to start programming!")

    input_success = True


# rem3 = int(input("Remainder division by 3\n> "))
# rem5 = int(input("Remainder division by 5\n> "))
# rem7 = int(input("Remainder division by 7\n> "))
