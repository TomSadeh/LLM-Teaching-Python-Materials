# Exercise 15: Mini Project - Combine Everything!
#
# Create a simple "Number Analyzer" program that:
# 1. Asks the user for a number
# 2. Tells them interesting facts about that number!
#
# Use functions for each analysis!


def is_even(n):
    # ✏️ Return True if even, False if odd
    pass


def is_positive(n):
    # ✏️ Return True if positive, False if zero or negative
    pass


def get_factors(n):
    # ✏️ Print all factors of n (numbers that divide evenly into n)
    # Example: factors of 12 are 1, 2, 3, 4, 6, 12
    pass


def sum_of_digits(n):
    # ✏️ Return the sum of all digits in n
    # Example: sum_of_digits(123) = 1 + 2 + 3 = 6
    # Hint: convert to string, loop through characters, convert back to int
    pass


def is_prime(n):
    # ✏️ Return True if n is prime (only divisible by 1 and itself)
    # Hint: check if any number from 2 to n-1 divides evenly
    pass


def analyze_number(n):
    print("Analyzing:", n)
    print("-" * 20)

    # ✏️ Call your functions and print results!
    # - Is it even or odd?
    # - Is it positive, negative, or zero?
    # - What are its factors?
    # - What's the sum of its digits?
    # - Is it prime?

    pass


def main():
    print("=== Number Analyzer ===")
    print()

    number = int(input("Enter a number to analyze: "))
    print()

    analyze_number(number)


main()
