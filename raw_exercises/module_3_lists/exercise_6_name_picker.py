# Exercise 6: Tribute Reaping! (Hunger Games Style)

import random


def pick_tribute(names):
    # ✏️ YOUR CODE HERE ✏️
    # Return a random tribute from the list
    # Hint: use random.choice(list)
    pass


def main():
    print("=" * 45)
    print("   THE REAPING - District 12")
    print("=" * 45)
    print("May the odds be ever in your favor!\n")

    # You can pre-fill this with Hunger Games characters:
    # names = ["Katniss", "Peeta", "Gale", "Prim", "Madge"]
    # Or let the user enter names:
    names = []

    # Collect names
    while True:
        name = input("Enter a name for the reaping (or 'done' to draw): ")
        if name.lower() == "done":
            break
        names.append(name)

    # Make sure we have names
    if len(names) == 0:
        print("No names in the reaping ball!")
    else:
        # Pick a random tribute
        tribute = pick_tribute(names)
        print("\n✨ The tribute selected is:", tribute, "✨")
        print("I volunteer as tribute!...?")


main()
