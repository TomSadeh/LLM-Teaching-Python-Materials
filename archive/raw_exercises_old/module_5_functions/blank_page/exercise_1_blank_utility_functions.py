# Exercise 1: Write From Scratch - Utility Functions
#
# These exercises give you minimal guidance. Read the docstring,
# understand what's needed, and implement it yourself.
#
# This is how real programming works!
#
# Theme: Creating utility spells for {{school}}


# ============================================================
# CHALLENGE A: EASY - Double a Value
# ============================================================

def double_it(value):
    """
    Return the value multiplied by 2.

    Args:
        value: A number (int or float)

    Returns:
        The value times 2

    Examples:
        >>> double_it(5)
        10
        >>> double_it(3.5)
        7.0
        >>> double_it(0)
        0
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# CHALLENGE B: EASY - Check if Even
# ============================================================

def is_even(number):
    """
    Check if a number is even.

    Args:
        number: An integer

    Returns:
        bool: True if even, False if odd

    Examples:
        >>> is_even(4)
        True
        >>> is_even(7)
        False
        >>> is_even(0)
        True
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# CHALLENGE C: MEDIUM - Greeting Message
# ============================================================

def create_greeting(name, excited=False):
    """
    Create a greeting message for someone.

    Args:
        name: The person's name
        excited: If True, add exclamation marks

    Returns:
        str: The greeting message

    Examples:
        >>> create_greeting("{{hero}}")
        'Hello, {{hero}}!'
        >>> create_greeting("{{heroine}}", excited=True)
        'Hello, {{heroine}}!!!'
        >>> create_greeting("")
        'Hello, stranger!'
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# CHALLENGE D: MEDIUM - Count Occurrences
# ============================================================

def count_char(text, char):
    """
    Count how many times a character appears in text.

    Args:
        text: The string to search in
        char: The character to count

    Returns:
        int: Number of times char appears in text

    Examples:
        >>> count_char("{{spell1}}", "a")
        2  # (depends on actual spell)
        >>> count_char("abracadabra", "a")
        5
        >>> count_char("hello", "z")
        0
        >>> count_char("", "a")
        0
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# CHALLENGE E: MEDIUM - Find Largest
# ============================================================

def find_largest(numbers):
    """
    Find the largest number in a list.

    Args:
        numbers: List of numbers (at least one element)

    Returns:
        The largest number in the list

    Examples:
        >>> find_largest([1, 5, 3, 9, 2])
        9
        >>> find_largest([-5, -1, -10])
        -1
        >>> find_largest([42])
        42
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# CHALLENGE F: HARD - Filter by Length
# ============================================================

def filter_by_length(words, min_length):
    """
    Keep only words that are at least min_length characters.

    Args:
        words: List of strings
        min_length: Minimum length to keep

    Returns:
        list: Words that meet the length requirement

    Examples:
        >>> filter_by_length(["{{hero}}", "Al", "{{heroine}}"], 4)
        ['{{hero}}', '{{heroine}}']  # Names with 4+ chars
        >>> filter_by_length(["a", "bb", "ccc"], 2)
        ['bb', 'ccc']
        >>> filter_by_length(["test"], 10)
        []
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# CHALLENGE G: HARD - Calculate Average
# ============================================================

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers: List of numbers

    Returns:
        float: The average, or 0 if list is empty

    Examples:
        >>> calculate_average([10, 20, 30])
        20.0
        >>> calculate_average([5])
        5.0
        >>> calculate_average([])
        0
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# CHALLENGE H: HARD - Is Palindrome
# ============================================================

def is_palindrome(text):
    """
    Check if text reads the same forwards and backwards.
    Ignore case and spaces.

    Args:
        text: String to check

    Returns:
        bool: True if palindrome, False otherwise

    Examples:
        >>> is_palindrome("radar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("")
        True
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# TESTS
# ============================================================

def run_tests():
    """Run tests for all functions."""
    print("Testing your implementations...\n")

    # Test double_it
    print("A: double_it")
    assert double_it(5) == 10, "double_it(5) should be 10"
    assert double_it(0) == 0, "double_it(0) should be 0"
    assert double_it(-3) == -6, "double_it(-3) should be -6"
    print("   ✓ Passed!\n")

    # Test is_even
    print("B: is_even")
    assert is_even(4) == True, "is_even(4) should be True"
    assert is_even(7) == False, "is_even(7) should be False"
    assert is_even(0) == True, "is_even(0) should be True"
    print("   ✓ Passed!\n")

    # Test create_greeting
    print("C: create_greeting")
    assert create_greeting("{{hero}}") == "Hello, {{hero}}!", "Basic greeting failed"
    assert create_greeting("{{hero}}", excited=True) == "Hello, {{hero}}!!!", "Excited greeting failed"
    assert create_greeting("") == "Hello, stranger!", "Empty name failed"
    print("   ✓ Passed!\n")

    # Test count_char
    print("D: count_char")
    assert count_char("abracadabra", "a") == 5, "count_char abracadabra 'a' should be 5"
    assert count_char("hello", "l") == 2, "count_char hello 'l' should be 2"
    assert count_char("", "a") == 0, "count_char empty should be 0"
    print("   ✓ Passed!\n")

    # Test find_largest
    print("E: find_largest")
    assert find_largest([1, 5, 3]) == 5, "find_largest [1,5,3] should be 5"
    assert find_largest([-5, -1]) == -1, "find_largest negatives failed"
    assert find_largest([42]) == 42, "find_largest single element failed"
    print("   ✓ Passed!\n")

    # Test filter_by_length
    print("F: filter_by_length")
    assert filter_by_length(["a", "bb", "ccc"], 2) == ["bb", "ccc"]
    assert filter_by_length(["test"], 10) == []
    print("   ✓ Passed!\n")

    # Test calculate_average
    print("G: calculate_average")
    assert calculate_average([10, 20, 30]) == 20.0
    assert calculate_average([]) == 0
    print("   ✓ Passed!\n")

    # Test is_palindrome
    print("H: is_palindrome")
    assert is_palindrome("radar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == True
    print("   ✓ Passed!\n")

    print("=" * 40)
    print("All tests passed! 🎉")


def main():
    print("=== Write From Scratch Challenges ===")
    print()
    print("Implement each function based on its docstring.")
    print("When ready, uncomment run_tests() to check your work.")
    print()

    # Uncomment to run tests after implementing:
    # run_tests()


main()
