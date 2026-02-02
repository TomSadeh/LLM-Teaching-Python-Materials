# Exercise 3: The {{item}}!

import random


def get_house():
    # ✏️ YOUR CODE HERE ✏️
    # 1. Create a list with the 4 {{school}} houses:
    #    "{{house}}", "{{house}}", "{{house}}", "{{house}}"
    # 2. Use random.choice() to pick one
    # 3. Return the chosen house
    pass


def get_house_message(house):
    # ✏️ BONUS: Add this function! ✏️
    # Return a message based on the house:
    # {{house}} -> "Where dwell the brave at heart!"
    # {{house}} -> "Where they are just and loyal!"
    # {{house}} -> "Where those of wit and learning will always find their kind!"
    # {{house}} -> "Where you'll make your real friends!"
    pass


def main():
    print("🎩 The {{item}} 🎩")
    print("=" * 25)

    name = input("What is your name, young student? ")
    print(f"\nHmm, let me see, {name}...")
    print("Difficult... very difficult...")

    house = get_house()
    print(f"\nBetter be... {house}!")


main()
