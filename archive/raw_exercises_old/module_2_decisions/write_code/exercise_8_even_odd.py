# Exercise 8: Even or Odd?

def is_even(number):
    # ✏️ YOUR CODE HERE ✏️
    # Return True if the number is even, False if it's odd
    #
    # Hint: Use the modulo operator %
    # The modulo gives you the remainder after division
    # Example: 7 % 2 = 1 (7 divided by 2 is 3 remainder 1)
    # Example: 8 % 2 = 0 (8 divided by 2 is 4 remainder 0)
    #
    # If a number % 2 equals 0, it's even!
    pass


def main():
    number = int(input("Enter a number: "))

    if is_even(number):
        print(number, "is even!")
    else:
        print(number, "is odd!")


main()
