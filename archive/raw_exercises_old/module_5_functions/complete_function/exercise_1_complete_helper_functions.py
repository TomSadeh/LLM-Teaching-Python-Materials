# Exercise 1: Complete the Function - Helper Functions
#
# Each function is partially written. Read the docstring and
# the starter code, then complete the implementation.
#
# Theme: Building utilities for {{school}}


def validate_score(score):
    """
    Check if a score is valid (between 0 and 100 inclusive).

    Args:
        score: The score to validate

    Returns:
        True if valid, False otherwise

    Examples:
        >>> validate_score(85)
        True
        >>> validate_score(-5)
        False
        >>> validate_score(101)
        False
        >>> validate_score(0)
        True
        >>> validate_score(100)
        True
    """
    # ✏️ COMPLETE THIS FUNCTION ✏️
    # Hint: Return True if 0 <= score <= 100

    pass  # Replace with implementation


def format_greeting(name, title="Student"):
    """
    Create a formal greeting with optional title.

    Args:
        name: The person's name
        title: Optional title (default: "Student")

    Returns:
        A formatted greeting string

    Examples:
        >>> format_greeting("{{hero}}")
        "Welcome, Student {{hero}}!"
        >>> format_greeting("{{mentor}}", "Professor")
        "Welcome, Professor {{mentor}}!"
    """
    # ✏️ COMPLETE THIS FUNCTION ✏️
    # Hint: Use an f-string to combine title and name

    pass  # Replace with implementation


def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers: A list of numbers

    Returns:
        The average (mean) of the numbers, or 0 if list is empty

    Examples:
        >>> calculate_average([10, 20, 30])
        20.0
        >>> calculate_average([5])
        5.0
        >>> calculate_average([])
        0
    """
    # Started for you:
    if not numbers:
        return 0

    # ✏️ COMPLETE THIS FUNCTION ✏️
    # Hint: Average = sum of all numbers / count of numbers

    pass  # Replace with implementation


def clamp(value, minimum, maximum):
    """
    Clamp a value to be within a range.

    If value is below minimum, return minimum.
    If value is above maximum, return maximum.
    Otherwise, return value unchanged.

    Args:
        value: The value to clamp
        minimum: The minimum allowed value
        maximum: The maximum allowed value

    Returns:
        The clamped value

    Examples:
        >>> clamp(5, 0, 10)
        5
        >>> clamp(-3, 0, 10)
        0
        >>> clamp(15, 0, 10)
        10
    """
    # ✏️ COMPLETE THIS FUNCTION ✏️
    # Hint: Use if/elif/else to check the three cases

    pass  # Replace with implementation


def repeat_string(text, times, separator=" "):
    """
    Repeat a string multiple times with a separator.

    Args:
        text: The string to repeat
        times: How many times to repeat
        separator: What to put between repetitions (default: space)

    Returns:
        The repeated string

    Examples:
        >>> repeat_string("{{spell1}}", 3)
        "{{spell1}} {{spell1}} {{spell1}}"
        >>> repeat_string("ha", 4, "")
        "hahahaha"
        >>> repeat_string("{{exclamation}}", 2, "! ")
        "{{exclamation}}! {{exclamation}}"
    """
    # Started for you:
    parts = []

    # ✏️ COMPLETE THIS FUNCTION ✏️
    # Hint: Build a list of the text repeated, then join with separator

    for i in range(times):
        pass  # Add text to parts

    return separator.join(parts)


def is_palindrome(text):
    """
    Check if a string is a palindrome (same forwards and backwards).

    Ignores case and spaces.

    Args:
        text: The string to check

    Returns:
        True if palindrome, False otherwise

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("A man a plan a canal Panama")
        True
    """
    # Started for you:
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()

    # ✏️ COMPLETE THIS FUNCTION ✏️
    # Hint: Compare cleaned with its reverse
    # Reverse a string with: text[::-1]

    pass  # Replace with implementation


def main():
    print("=== Complete the Function: Helper Functions ===")
    print()

    # Test validate_score
    print("Test validate_score:")
    print(f"  validate_score(85) = {validate_score(85)}")
    print(f"  Expected: True")
    print(f"  validate_score(-5) = {validate_score(-5)}")
    print(f"  Expected: False")
    print()

    # Test format_greeting
    print("Test format_greeting:")
    print(f"  format_greeting('Alice') = {format_greeting('Alice')}")
    print(f"  Expected: Welcome, Student Alice!")
    print(f"  format_greeting('Bob', 'Professor') = {format_greeting('Bob', 'Professor')}")
    print(f"  Expected: Welcome, Professor Bob!")
    print()

    # Test calculate_average
    print("Test calculate_average:")
    print(f"  calculate_average([10, 20, 30]) = {calculate_average([10, 20, 30])}")
    print(f"  Expected: 20.0")
    print()

    # Test clamp
    print("Test clamp:")
    print(f"  clamp(5, 0, 10) = {clamp(5, 0, 10)}")
    print(f"  Expected: 5")
    print(f"  clamp(-3, 0, 10) = {clamp(-3, 0, 10)}")
    print(f"  Expected: 0")
    print(f"  clamp(15, 0, 10) = {clamp(15, 0, 10)}")
    print(f"  Expected: 10")
    print()

    # Test repeat_string
    print("Test repeat_string:")
    print(f"  repeat_string('ha', 4, '') = {repeat_string('ha', 4, '')}")
    print(f"  Expected: hahahaha")
    print()

    # Test is_palindrome
    print("Test is_palindrome:")
    print(f"  is_palindrome('racecar') = {is_palindrome('racecar')}")
    print(f"  Expected: True")
    print(f"  is_palindrome('hello') = {is_palindrome('hello')}")
    print(f"  Expected: False")


main()
