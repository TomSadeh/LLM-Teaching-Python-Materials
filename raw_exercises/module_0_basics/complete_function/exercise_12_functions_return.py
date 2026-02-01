# Exercise 12: Functions that Return Values


# ✏️ Exercise A
# Write a function double(n) that returns n * 2

def double(n):
    pass


# ✏️ Exercise B
# Write a function add(a, b) that returns a + b

def add(a, b):
    pass


# ✏️ Exercise C
# Write a function square(n) that returns n * n

def square(n):
    pass


# ✏️ Exercise D
# Write a function is_even(n) that returns True if n is even, False otherwise

def is_even(n):
    pass


# ✏️ Exercise E
# Write a function max_of_two(a, b) that returns the bigger number

def max_of_two(a, b):
    pass


# ✏️ Exercise F
# Write a function sum_to(n) that returns the sum of 1 to n

def sum_to(n):
    pass


# ✏️ Exercise G
# Write a function make_greeting(name) that returns "Hello, [name]!"
# (returns it, doesn't print it!)

def make_greeting(name):
    pass


# ✏️ Exercise H
# Write a function calculate_area(width, height) that returns width * height

def calculate_area(width, height):
    pass


def main():
    print("=== Exercise A: double ===")
    print("double(5) =", double(5))  # Should be 10
    print("double(12) =", double(12))  # Should be 24

    print("\n=== Exercise B: add ===")
    print("add(3, 4) =", add(3, 4))  # Should be 7

    print("\n=== Exercise C: square ===")
    print("square(5) =", square(5))  # Should be 25
    print("square(9) =", square(9))  # Should be 81

    print("\n=== Exercise D: is_even ===")
    print("is_even(4) =", is_even(4))  # Should be True
    print("is_even(7) =", is_even(7))  # Should be False

    print("\n=== Exercise E: max_of_two ===")
    print("max_of_two(5, 9) =", max_of_two(5, 9))  # Should be 9
    print("max_of_two(12, 3) =", max_of_two(12, 3))  # Should be 12

    print("\n=== Exercise F: sum_to ===")
    print("sum_to(5) =", sum_to(5))  # Should be 15
    print("sum_to(10) =", sum_to(10))  # Should be 55

    print("\n=== Exercise G: make_greeting ===")
    message = make_greeting("Maya")
    print(message)  # Should be "Hello, Maya!"

    print("\n=== Exercise H: calculate_area ===")
    print("Area of 5x3 =", calculate_area(5, 3))  # Should be 15


main()
