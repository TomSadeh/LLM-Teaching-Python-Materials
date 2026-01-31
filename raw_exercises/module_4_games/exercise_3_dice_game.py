# Exercise 3: Dice Game (Pig)

import random


def roll_dice():
    return random.randint(1, 6)


def play_turn():
    turn_total = 0

    # ✏️ YOUR CODE HERE ✏️
    # One turn of the dice game:
    #
    # Loop until player chooses to stop:
    # 1. Ask "Roll or hold? (r/h): "
    # 2. If "h" (hold): break and return turn_total
    # 3. If "r" (roll):
    #    - Roll the dice using roll_dice()
    #    - Print what was rolled
    #    - If rolled 1: print "Oops! You lose this turn's points!"
    #                   return 0
    #    - Otherwise: add the roll to turn_total
    #    - Print current turn total
    #
    # Hint: while True with break works well here

    return turn_total


def main():
    print("🎲 Dice Game 🎲")
    print("===============")
    print("Roll dice to get points.")
    print("Roll a 1 and you lose all points from this turn!")
    print("Choose 'hold' to keep your points safely.")
    print()

    score = 0
    points = play_turn()
    score = score + points
    print("You scored:", points, "points this turn!")
    print("Total score:", score)


main()
