# Exercise 2: Advanced Random (Beyond Basic Random!)

import random


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # You already know random.randint() - now try random.choice()!
    # Create a list of spells: ["{{spell1}}", "{{spell2}}", "{{spell3}}", "{{spell4}}"]
    # Pick a random spell and print it
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Use random.shuffle() to shuffle a list IN PLACE
    # Create a list of characters
    # Shuffle them and print the new order
    # (Great for randomizing game order!)
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Use random.sample() to pick multiple items WITHOUT duplicates
    # Create a list of 10 possible items
    # Pick 3 random items for a starter kit
    # Hint: random.sample(items, 3)
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # Use random.random() to get a float between 0 and 1
    # Create a spell that has a 70% chance to succeed
    # If random.random() < 0.7: success, else: fail
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # Create a loot drop system with different rarities!
    # Use random.random() for probability:
    # - Common (60% chance): "health potion"
    # - Uncommon (25% chance): "{{item}}"
    # - Rare (10% chance): "{{pet}}"
    # - Legendary (5% chance): "{{transport}}"
    pass


def exercise_f():
    # ✏️ YOUR CODE HERE ✏️
    # Use random.choices() for WEIGHTED random selection
    # Each item has a different probability
    # Hint: random.choices(items, weights=[50, 30, 15, 5], k=1)
    pass


def exercise_g():
    # ✏️ YOUR CODE HERE ✏️
    # Gacha/Card pack opener!
    # Create a list of characters with rarities
    # Open a "pack" of 5 cards using weighted random
    # Print what you got!
    pass


def dice_game():
    # ✏️ YOUR CODE HERE ✏️
    # Create a dice game where player and computer each roll 2 dice
    # Compare totals to see who wins
    # Best of 3 rounds!
    pass


def main():
    print("=== Exercise A: random.choice() ===")
    exercise_a()

    print("\n=== Exercise B: random.shuffle() ===")
    exercise_b()

    print("\n=== Exercise C: random.sample() ===")
    exercise_c()

    print("\n=== Exercise D: Spell Success Rate ===")
    exercise_d()

    print("\n=== Exercise E: Loot Drops ===")
    exercise_e()

    print("\n=== Exercise F: Weighted Choice ===")
    exercise_f()

    print("\n=== Exercise G: Card Pack ===")
    exercise_g()

    print("\n=== Dice Game ===")
    dice_game()


main()
