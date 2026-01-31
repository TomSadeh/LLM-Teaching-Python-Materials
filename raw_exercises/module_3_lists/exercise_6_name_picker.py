# Exercise 6: challenger Selection! (Adventure style)

import random


def pick_challenger(names):
    # ✏️ YOUR CODE HERE ✏️
    # Return a random challenger from the list
    # Hint: use random.choice(list)
    pass


def main():
    print("=" * 45)
    print("   THE Selection - {{school}}")
    print("=" * 45)
    print("{{exclamation}}!\n")

    # You can pre-fill this with Hunger Games characters:
    # names = ["{{heroine}}", "{{hero}}", "{{friend}}", "{{friend}}", "Madge"]
    # Or let the user enter names:
    names = []

    # Collect names
    while True:
        name = input("Enter a name for the Selection (or 'done' to draw): ")
        if name.lower() == "done":
            break
        names.append(name)

    # Make sure we have names
    if len(names) == 0:
        print("No names in the Selection ball!")
    else:
        # Pick a random challenger
        challenger = pick_challenger(names)
        print("\n✨ The challenger selected is:", challenger, "✨")
        print("I volunteer as challenger!...?")


main()
