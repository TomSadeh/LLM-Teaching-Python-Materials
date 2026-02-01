# Exercise 3: Useful Helper Functions

import random


def is_even(number):
    # ✏️ YOUR CODE HERE ✏️
    # Return True if number is even, False if odd
    # Hint: use % (modulo) - if number % 2 == 0, it's even
    pass


def get_max(a, b):
    # ✏️ YOUR CODE HERE ✏️
    # Return the bigger number
    pass


def get_random_item(items):
    # ✏️ YOUR CODE HERE ✏️
    # Return a random item from the list
    pass


def count_letter(text, letter):
    # ✏️ YOUR CODE HERE ✏️
    # Count how many times 'letter' appears in 'text'
    # Hint: loop through each character in text
    pass


def reverse_string(text):
    # ✏️ YOUR CODE HERE ✏️
    # Return the text backwards
    # Hint: text[::-1] reverses a string!
    pass


def main():
    # Test your functions!
    print("Testing is_even:")
    print("4 is even:", is_even(4))   # Should be True
    print("7 is even:", is_even(7))   # Should be False

    print("\nTesting get_max:")
    print("Max of 5 and 9:", get_max(5, 9))  # Should be 9

    print("\nTesting get_random_item:")
    fruits = ["apple", "banana", "orange"]
    print("Random fruit:", get_random_item(fruits))

    print("\nTesting count_letter:")
    print("'l' in 'hello':", count_letter("hello", "l"))  # Should be 2

    print("\nTesting reverse_string:")
    print("Reverse 'hello':", reverse_string("hello"))  # Should be 'olleh'


main()
