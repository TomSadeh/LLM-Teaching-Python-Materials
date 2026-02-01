# Exercise 3: Number Guessing Game


def check_guess(secret, guess):
    # ✏️ YOUR CODE HERE ✏️
    # Compare the guess to the secret number:
    # - If guess equals secret: print "Correct!"
    # - If guess is too high: print "Too high!"
    # - If guess is too low: print "Too low!"
    pass


def main():
    secret_number = 7  # The number to guess

    guess = int(input("Guess a number between 1-10: "))
    check_guess(secret_number, guess)


main()
