# Exercise 5: The Math Module (Advanced Calculations!)

import math


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Use math.sqrt() to find square roots
    # Find the square root of 144
    # Print: "The square root of 144 is [result]"
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Use math.floor() and math.ceil()
    # floor() rounds DOWN, ceil() rounds UP
    # Try with 4.7: print both floor and ceil
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Use math.pi and math.pow()
    # Calculate the area of a circle with radius 5
    # Formula: pi * r^2
    # Hint: math.pi * math.pow(radius, 2)
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # Distance calculator!
    # Use math.sqrt() to calculate distance between two points
    # Distance = sqrt((x2-x1)^2 + (y2-y1)^2)
    # How far is {{hero}} at (3, 4) from {{villain}} at (0, 0)?
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # Damage calculator with randomness!
    # Base damage = 50
    # Critical hit = 1.5x damage
    # Use math.floor() to round down the final damage
    pass


def exercise_f():
    # ✏️ YOUR CODE HERE ✏️
    # Experience points needed for next level
    # Many games use: XP_needed = floor(100 * (level ^ 1.5))
    # Create a table showing XP needed for levels 1-10
    pass


def exercise_g():
    # ✏️ YOUR CODE HERE ✏️
    # Spell range checker!
    # {{hero}} is at position (0, 0)
    # {{villain}} is at a position the user enters
    # Spell has a maximum range of 10 units
    # Calculate distance and say if spell can reach!
    pass


def game_stats():
    # ✏️ YOUR CODE HERE ✏️
    # RPG Stats Calculator!
    # Ask for base stats: strength, intelligence, agility
    # Calculate derived stats:
    # - Attack Power = floor(strength * 1.5)
    # - Magic Power = floor(intelligence * 2)
    # - Speed = floor(sqrt(agility) * 10)
    # - Health = floor(100 + (strength * 5))
    pass


def main():
    print("=== Exercise A: Square Root ===")
    exercise_a()

    print("\n=== Exercise B: Floor and Ceil ===")
    exercise_b()

    print("\n=== Exercise C: Circle Area ===")
    exercise_c()

    print("\n=== Exercise D: Distance ===")
    exercise_d()

    print("\n=== Exercise E: Critical Damage ===")
    exercise_e()

    print("\n=== Exercise F: XP Table ===")
    exercise_f()

    print("\n=== Exercise G: Spell Range ===")
    exercise_g()

    print("\n=== Game Stats Calculator ===")
    game_stats()


main()
