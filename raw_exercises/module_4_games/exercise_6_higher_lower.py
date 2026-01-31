# Exercise 6: Higher or Lower

import random


def get_random_number():
    """Returns a random number between 1 and 10"""
    return random.randint(1, 10)


def play_round(current_number):
    # ✏️ YOUR CODE HERE ✏️
    # 1. Generate a new random number
    # 2. Ask the player to guess if it will be "higher" or "lower"
    # 3. Compare the new number to current_number
    # 4. Return True if they guessed right, False if wrong
    #
    # Hint: Use input() to get their guess
    # Hint: Compare the new number to current_number
    #
    # Don't forget to show them what the new number was!
    pass


def main():
    print("=== Higher or Lower ===")
    print("Guess if the next number will be higher or lower!")
    print("Numbers are between 1 and 10\n")

    score = 0
    current = get_random_number()

    while True:
        print("Current number:", current)
        won_round = play_round(current)

        if won_round:
            score += 1
            print("✓ Correct! Score:", score)
            current = get_random_number()
            play_again = input("Keep playing? (y/n): ")
            if play_again.lower() != "y":
                break
        else:
            print("✗ Wrong! Game over!")
            break

    print("\nFinal score:", score)


main()
