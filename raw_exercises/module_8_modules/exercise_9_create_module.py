# Exercise 9: Create Your Own Module!
#
# This exercise teaches you how to create and use your own Python modules.
# You'll create a separate file with helper functions, then import it here!


# =====================
# STEP 1: Create a module file
# =====================
# Create a new file called "game_helpers.py" in the same folder
# with these functions:

# --- game_helpers.py content: ---
"""
# game_helpers.py - Your custom game utilities!

import random

def roll_dice(sides=6):
    '''Roll a die with the given number of sides'''
    return random.randint(1, sides)


def calculate_damage(base_damage, multiplier=1.0):
    '''Calculate damage with optional multiplier'''
    return int(base_damage * multiplier)


def random_enemy():
    '''Return a random enemy name'''
    enemies = ["goblin", "{{creature}}", "dark wizard", "troll"]
    return random.choice(enemies)


def format_health_bar(current, maximum, length=20):
    '''Create a visual health bar'''
    filled = int((current / maximum) * length)
    bar = "█" * filled + "░" * (length - filled)
    return f"[{bar}] {current}/{maximum}"


GAME_VERSION = "1.0.0"
STARTING_HEALTH = 100
"""


# =====================
# STEP 2: Import and use your module
# =====================

# ✏️ Uncomment this after creating game_helpers.py:
# import game_helpers

def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # After creating game_helpers.py, import it and use roll_dice()
    # Roll a 20-sided die (like in D&D!) 5 times
    # Print each roll
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Use format_health_bar to show a character's health
    # Show health at 100/100, then 75/100, then 30/100
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Access constants from your module!
    # Print the GAME_VERSION and STARTING_HEALTH
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # Use random_enemy() and calculate_damage() together
    # Generate 3 random encounters with random damage
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # Add a new function to game_helpers.py called generate_loot()
    # It should return a random item from a list
    # Then use it here!
    pass


def mini_battle():
    # ✏️ YOUR CODE HERE ✏️
    # Create a mini battle using all the helper functions!
    # 1. Player starts with STARTING_HEALTH
    # 2. Encounter a random_enemy()
    # 3. Roll dice to determine who hits
    # 4. Use calculate_damage() and format_health_bar()
    # 5. Continue until someone's health reaches 0
    pass


def main():
    print("=" * 40)
    print("   CUSTOM MODULE EXERCISES")
    print("=" * 40)
    print()
    print("First, create 'game_helpers.py' with the code above!")
    print()

    print("=== Exercise A: Roll Dice ===")
    exercise_a()

    print("\n=== Exercise B: Health Bars ===")
    exercise_b()

    print("\n=== Exercise C: Module Constants ===")
    exercise_c()

    print("\n=== Exercise D: Combat Encounters ===")
    exercise_d()

    print("\n=== Exercise E: Custom Function ===")
    exercise_e()

    print("\n=== Mini Battle ===")
    mini_battle()


main()
