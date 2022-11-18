MAX_CAGE_CAPACITY = 4


def total_price(
    unit_price: float,
    amount: int = 1,
    kdv: float = 0.08,
    tevk: float = 0.0,
    discount: float = 0.0,
) -> float:

    subtotal = unit_price * amount
    discounted = subtotal * (1 - discount)
    total = discounted * (1 + kdv * (1 - tevk))

    return total


def zoo_display(*animals, **animal_count):
    # print(type(animal_count))
    # print(animal_count)
    print("\n__List of our Animals__")

    for an in animals:
        print(f"{animal_count.get(an,'?')}x {an}")

    print(set(animal_count.keys()) - set(animals))


def accouting():
    food = total_price(50, 2, 0.01, discount=0.01)

    hw_support = total_price(10_000, 1, 0.18, tevk=0.3, discount=0.1)
    hw_support = total_price(10_000, 1, 0.18, 0.3, 0.1)
    hw_support = total_price(
        amount=1, tevk=0.3, unit_price=10_000, kdv=0.18, discount=0.1
    )

    print(f"Food costs {food}")
    print(f"HW Support {hw_support}")


def zoo_fill_the_cage(*cages, **animal_count):
    i = 0
    for an in animal_count:
        total_count = animal_count[an]

        for _ in range(total_count):
            cages[i].append(an)

        i += 1

        if i == len(cages):
            break


if __name__ == "__main__":
    total_price(1000)
    
    # acxcouting()
    zoo_display("elephant")
    zoo_display("elephant", "zebra", "monkey")
    zoo_display("elephant", "zebra", "monkey", "lion")
    zoo_display("elephant", "zebra", "monkey", "lion", "crocodile")
    zoo_display("elephant", "zebra", "monkey", "lion", "crocodile", "parrot")

    zoo_display(
        "elephant",
        "zebra",
        "monkey",
        "lion",
        "crocodile",
        elephant=2,
        zebra=3,
        monkey=5,
        lion=4,
        penguin=3,
    )

    cage1, cage2, cage3,cage4 = [], [], [],[]

    zoo_fill_the_cage(
        cage1, cage2, cage3,cage4,elephant=2, zebra=3, monkey=5, lion=4, penguin=3
    )

    print(cage1)

    print(cage2)
    print(cage3)
    print(cage4)
