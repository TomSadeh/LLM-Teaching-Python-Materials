# Exercise 3: The Sorting Hat!

import random


def get_house():
    # ✏️ YOUR CODE HERE ✏️
    # 1. Create a list with the 4 Hogwarts houses:
    #    "Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"
    # 2. Use random.choice() to pick one
    # 3. Return the chosen house
    pass


def get_house_message(house):
    # ✏️ BONUS: Add this function! ✏️
    # Return a message based on the house:
    # Gryffindor -> "Where dwell the brave at heart!"
    # Hufflepuff -> "Where they are just and loyal!"
    # Ravenclaw -> "Where those of wit and learning will always find their kind!"
    # Slytherin -> "Where you'll make your real friends!"
    pass


def main():
    print("🎩 The Sorting Hat 🎩")
    print("=" * 25)

    name = input("What is your name, young wizard? ")
    print(f"\nHmm, let me see, {name}...")
    print("Difficult... very difficult...")

    house = get_house()
    print(f"\nBetter be... {house}!")


main()
