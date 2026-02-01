# Exercise 8: Word Scramble Game

import random


def scramble_word(word):
    # ✏️ YOUR CODE HERE ✏️
    # Scramble the letters in the word and return the scrambled version
    #
    # Hint: Convert word to a list of letters: letters = list(word)
    # Hint: Use random.shuffle(letters) to mix them up
    # Hint: Join them back: "".join(letters)
    pass


def play_round(word):
    # ✏️ YOUR CODE HERE ✏️
    # 1. Scramble the word
    # 2. Show the scrambled word to the player
    # 3. Let them guess (give them 3 tries!)
    # 4. Return True if they got it, False if they used all tries
    #
    # Hint: Use a for loop for the 3 tries
    # Hint: Compare their guess (lowercase) to word (lowercase)
    pass


def main():
    print("=== Word Scramble ===")
    print("Unscramble the letters to find the word!\n")

    # Words to scramble
    words = ["python", "turtle", "coding", "games", "learn"]

    score = 0

    for word in words:
        if play_round(word):
            score += 1
            print("✓ Correct!\n")
        else:
            print("✗ The word was:", word, "\n")

    print("=== Game Over ===")
    print("Score:", score, "/", len(words))


main()
