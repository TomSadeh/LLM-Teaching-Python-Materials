# Exercise 1: Guess the Number Game

import random


def play_game():
    secret = random.randint(1, 20)
    attempts = 0

    print("I'm thinking of a number between 1 and 20...")
    print("You have 5 tries to guess it!")
    print()

    # ✏️ YOUR CODE HERE ✏️
    # Create a game loop that:
    # 1. Asks the player for a guess (use int(input(...)))
    # 2. Add 1 to attempts
    # 3. Check if guess equals secret - if yes, print "You won!" and break
    # 4. If guess is too high, print "Too high!"
    # 5. If guess is too low, print "Too low!"
    # 6. If attempts reaches 5, print "Game over!" and break
    #
    # Hint: use while True: and break to exit
    pass


def main():
    print("🎯 Guess the Number 🎯")
    print("======================")
    play_game()


main()
