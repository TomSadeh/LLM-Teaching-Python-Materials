# Exercise 5: Coin Flip Streak

import random


def flip_coin():
    # ✏️ YOUR CODE HERE ✏️
    # Return either "heads" or "tails" randomly
    # Hint: use random.choice(["heads", "tails"])
    pass


def play_game():
    # ✏️ YOUR CODE HERE ✏️
    # The game: How many heads can you flip in a row?
    #
    # 1. Flip a coin
    # 2. If it's heads, add to the streak and ask to flip again
    # 3. If it's tails, the game is over!
    #
    # Return the final streak count
    #
    # Hint: Use a while loop
    # Hint: Use input() to ask "Flip again? (y/n)"
    pass


def main():
    print("=== Coin Flip Streak ===")
    print("How many HEADS can you flip in a row?")
    print("The streak ends when you get TAILS!\n")

    streak = play_game()

    print("\n🪙 Your streak:", streak, "heads in a row!")

    if streak >= 5:
        print("🎉 Amazing luck!")
    elif streak >= 3:
        print("👍 Nice streak!")
    else:
        print("Better luck next time!")


main()
