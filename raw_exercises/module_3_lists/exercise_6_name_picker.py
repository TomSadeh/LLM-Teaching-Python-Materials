# Exercise 6: Random Name Picker! (Adventure style)

import random


def pick_name(names):
    # ✏️ YOUR CODE HERE ✏️
    # Return a random name from the list
    # Hint: use random.choice(list)
    pass


def main():
    print("=" * 45)
    print("   THE MAGICAL SELECTION - {{school}}")
    print("=" * 45)
    print("{{exclamation}}!\n")

    # You can pre-fill this with characters:
    # names = ["{{heroine}}", "{{hero}}", "{{friend}}", "{{mentor}}"]
    # Or let the user enter names:
    names = []

    # Collect names
    while True:
        name = input("Enter a name (or 'done' to draw): ")
        if name.lower() == "done":
            break
        names.append(name)

    # Make sure we have names
    if len(names) == 0:
        print("No names entered!")
    else:
        # Pick a random name
        chosen = pick_name(names)
        print("\n✨ The chosen one is:", chosen, "✨")
        print("{{exclamation}}")


main()
