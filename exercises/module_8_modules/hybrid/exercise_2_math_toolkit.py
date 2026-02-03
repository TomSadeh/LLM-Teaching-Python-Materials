"""
{{CONTEXT_PROJECT_INTRO}}

This is a multi-part exercise where you build a complete math utilities
module for {{school}}. You'll implement helper functions, extend them
with more features, and add error handling.

Programming concepts: math module, function design, error handling
Difficulty: 2-3
"""

import math


# ============================================================
# PART 1: Growth - Basic Math Helper Functions
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Build foundational math utility functions.


def calculate_circle_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius: The radius of the circle (positive number)

    Returns:
        float: The area (pi * r^2)

    Example:
        >>> calculate_circle_area(5)
        78.53981633974483
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Use math.pi and the formula: area = pi * radius^2
    # Step 2: Return the calculated area
    #
    # Hint: radius**2 or math.pow(radius, 2)
    pass


def calculate_hypotenuse(a, b):
    """
    Calculate the hypotenuse of a right triangle.

    Args:
        a: Length of first side
        b: Length of second side

    Returns:
        float: Length of hypotenuse (sqrt(a^2 + b^2))

    Example:
        >>> calculate_hypotenuse(3, 4)
        5.0
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Use the Pythagorean theorem: c = sqrt(a^2 + b^2)
    # Step 2: Return the result
    #
    # Hint: math.sqrt(a**2 + b**2)
    pass


def round_to_precision(value, direction="nearest"):
    """
    Round a value in the specified direction.

    Args:
        value: The number to round
        direction: "up", "down", or "nearest"

    Returns:
        int: The rounded value

    Examples:
        >>> round_to_precision(3.7, "up")
        4
        >>> round_to_precision(3.7, "down")
        3
        >>> round_to_precision(3.7, "nearest")
        4
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Check the direction parameter
    # Step 2: If "up", use math.ceil()
    # Step 3: If "down", use math.floor()
    # Step 4: If "nearest", use round() (built-in)
    # Step 5: Return the result
    pass


# ============================================================
# PART 2: Growth - Advanced Calculations
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Add more sophisticated math operations.


def calculate_distance(x1, y1, x2, y2):
    """
    Calculate distance between two points in 2D space.

    Args:
        x1, y1: Coordinates of first point
        x2, y2: Coordinates of second point

    Returns:
        float: The Euclidean distance

    Example:
        >>> calculate_distance(0, 0, 3, 4)
        5.0
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Calculate differences: dx = x2 - x1, dy = y2 - y1
    # Step 2: Apply distance formula: sqrt(dx^2 + dy^2)
    # Step 3: Return the result
    pass


def calculate_rectangle_diagonal(width, height):
    """
    Calculate the diagonal of a rectangle.

    Args:
        width: Width of the rectangle
        height: Height of the rectangle

    Returns:
        float: Length of the diagonal

    Example:
        >>> calculate_rectangle_diagonal(3, 4)
        5.0
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Hint: The diagonal IS the hypotenuse of width and height!
    # You can reuse calculate_hypotenuse() or calculate directly
    pass


def power_with_modulo(base, exponent, modulo=None):
    """
    Calculate base^exponent, optionally with modulo.

    Args:
        base: The base number
        exponent: The power to raise to
        modulo: Optional modulo value

    Returns:
        Result of base^exponent (mod modulo if provided)

    Examples:
        >>> power_with_modulo(2, 10)
        1024
        >>> power_with_modulo(2, 10, 100)
        24
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Calculate math.pow(base, exponent) and convert to int
    # Step 2: If modulo is provided, return result % modulo
    # Step 3: Otherwise, return result
    pass


# ============================================================
# PART 3: Improvement - Error Handling
# ============================================================
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Add error handling for invalid inputs.


def safe_circle_area(radius):
    """
    Calculate circle area with input validation.

    Args:
        radius: The radius (must be non-negative)

    Returns:
        float: The area, or None if invalid input

    Should handle:
    - Negative radius -> return None and print error
    - Non-numeric input -> return None and print error
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Check if radius is a number (int or float)
    #         Use: isinstance(radius, (int, float))
    # Step 2: If not a number, print "Error: radius must be a number"
    #         and return None
    # Step 3: Check if radius is negative
    # Step 4: If negative, print "Error: radius cannot be negative"
    #         and return None
    # Step 5: Calculate and return the area
    pass


def safe_square_root(value):
    """
    Calculate square root with error handling.

    Args:
        value: The number to find the square root of

    Returns:
        float: The square root, or None if invalid

    Should handle:
    - Negative numbers -> return None and print error
    - Non-numeric input -> return None and print error
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Check if value is a number
    # Step 2: Check if value is negative (can't take sqrt of negative)
    # Step 3: If valid, return math.sqrt(value)
    # Step 4: If invalid, print appropriate error and return None
    pass


def safe_divide(a, b):
    """
    Divide two numbers safely.

    Args:
        a: Numerator
        b: Denominator

    Returns:
        float: Result of a/b, or None if invalid

    Should handle:
    - Division by zero -> return None and print error
    - Non-numeric inputs -> return None and print error
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Check if both a and b are numbers
    # Step 2: Check if b is zero
    # Step 3: If valid, return a / b
    # Step 4: Handle errors appropriately
    pass


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("Math Toolkit for {{school}}")
    print("=" * 60)
    print()

    print(">>> PART 1: Basic Math Helpers")
    print("-" * 40)
    # Uncomment to test after implementing:
    # print(f"Circle area (r=5): {calculate_circle_area(5)}")
    # print(f"Hypotenuse (3,4): {calculate_hypotenuse(3, 4)}")
    # print(f"Round 3.7 up: {round_to_precision(3.7, 'up')}")
    # print(f"Round 3.7 down: {round_to_precision(3.7, 'down')}")
    # print(f"Round 3.7 nearest: {round_to_precision(3.7, 'nearest')}")
    print()

    print(">>> PART 2: Advanced Calculations")
    print("-" * 40)
    # Uncomment to test:
    # print(f"Distance (0,0) to (3,4): {calculate_distance(0, 0, 3, 4)}")
    # print(f"Rectangle diagonal 3x4: {calculate_rectangle_diagonal(3, 4)}")
    # print(f"2^10: {power_with_modulo(2, 10)}")
    # print(f"2^10 mod 100: {power_with_modulo(2, 10, 100)}")
    print()

    print(">>> PART 3: Safe Functions with Error Handling")
    print("-" * 40)
    # Uncomment to test:
    # print(f"Safe circle area (5): {safe_circle_area(5)}")
    # print(f"Safe circle area (-5): {safe_circle_area(-5)}")
    # print(f"Safe sqrt (16): {safe_square_root(16)}")
    # print(f"Safe sqrt (-16): {safe_square_root(-16)}")
    # print(f"Safe divide (10, 2): {safe_divide(10, 2)}")
    # print(f"Safe divide (10, 0): {safe_divide(10, 0)}")
    print()

    print("=" * 60)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")
    print("=" * 60)


if __name__ == "__main__":
    main()
