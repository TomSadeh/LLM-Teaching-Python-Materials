# Exercise 1: Complete the Function - List Functions
#
# Each function is partially written. Read the docstring and
# the starter code, then complete the implementation.
#
# Theme: Managing {{hero}}'s magical inventory


def find_maximum(numbers):
    """
    Find the largest number in a list.

    Args:
        numbers: A list of numbers

    Returns:
        The largest number in the list

    Examples:
        >>> find_maximum([3, 7, 2, 9, 4])
        9
        >>> find_maximum([10, 10, 10])
        10
        >>> find_maximum([-5, -2, -8])
        -2
    """
    # Started for you:
    if not numbers:
        return None

    maximum = numbers[0]

    # ✏️ COMPLETE THIS FUNCTION ✏️
    # Hint: Loop through the list and update maximum
    # when you find something bigger

    pass  # Replace with implementation


def filter_even_numbers(numbers):
    """
    Return a new list containing only the even numbers.

    Args:
        numbers: A list of integers

    Returns:
        A new list with only even numbers

    Examples:
        >>> filter_even_numbers([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
        >>> filter_even_numbers([1, 3, 5])
        []
        >>> filter_even_numbers([2, 4, 6])
        [2, 4, 6]
    """
    # Started for you:
    evens = []

    # ✏️ COMPLETE THIS FUNCTION ✏️
    # Hint: A number is even if number % 2 == 0

    pass  # Replace with implementation

    return evens


def count_occurrences(items, target):
    """
    Count how many times target appears in the list.

    Args:
        items: A list of items
        target: The item to count

    Returns:
        The count of how many times target appears

    Examples:
        >>> count_occurrences(["{{spell1}}", "{{spell2}}", "{{spell1}}"], "{{spell1}}")
        2
        >>> count_occurrences([1, 2, 1, 1, 3], 1)
        3
        >>> count_occurrences(["a", "b", "c"], "z")
        0
    """
    # Started for you:
    count = 0

    # ✏️ COMPLETE THIS FUNCTION ✏️
    # Hint: Loop through items, increment count when item equals target

    pass  # Replace with implementation

    return count


def remove_duplicates(items):
    """
    Return a new list with duplicates removed, keeping first occurrence.

    Args:
        items: A list that may contain duplicates

    Returns:
        A new list with only unique items (in original order)

    Examples:
        >>> remove_duplicates([1, 2, 2, 3, 1, 4])
        [1, 2, 3, 4]
        >>> remove_duplicates(["{{hero}}", "{{friend}}", "{{hero}}"])
        ["{{hero}}", "{{friend}}"]
    """
    # Started for you:
    unique = []

    # ✏️ COMPLETE THIS FUNCTION ✏️
    # Hint: Only append if item is not already in unique list

    pass  # Replace with implementation

    return unique


def sum_above_threshold(numbers, threshold):
    """
    Sum all numbers that are above the threshold.

    Args:
        numbers: A list of numbers
        threshold: Only sum numbers greater than this

    Returns:
        The sum of all numbers above threshold

    Examples:
        >>> sum_above_threshold([10, 5, 20, 3, 15], 10)
        35  # 20 + 15
        >>> sum_above_threshold([1, 2, 3], 10)
        0
        >>> sum_above_threshold([100, 200, 50], 0)
        350
    """
    # Started for you:
    total = 0

    # ✏️ COMPLETE THIS FUNCTION ✏️
    # Hint: Add to total only when number > threshold

    pass  # Replace with implementation

    return total


def main():
    print("=== Complete the Function: List Functions ===")
    print()

    # Test find_maximum
    print("Test find_maximum:")
    result = find_maximum([3, 7, 2, 9, 4])
    print(f"  find_maximum([3, 7, 2, 9, 4]) = {result}")
    print(f"  Expected: 9")
    print()

    # Test filter_even_numbers
    print("Test filter_even_numbers:")
    result = filter_even_numbers([1, 2, 3, 4, 5, 6])
    print(f"  filter_even_numbers([1, 2, 3, 4, 5, 6]) = {result}")
    print(f"  Expected: [2, 4, 6]")
    print()

    # Test count_occurrences
    print("Test count_occurrences:")
    result = count_occurrences([1, 2, 1, 1, 3], 1)
    print(f"  count_occurrences([1, 2, 1, 1, 3], 1) = {result}")
    print(f"  Expected: 3")
    print()

    # Test remove_duplicates
    print("Test remove_duplicates:")
    result = remove_duplicates([1, 2, 2, 3, 1, 4])
    print(f"  remove_duplicates([1, 2, 2, 3, 1, 4]) = {result}")
    print(f"  Expected: [1, 2, 3, 4]")
    print()

    # Test sum_above_threshold
    print("Test sum_above_threshold:")
    result = sum_above_threshold([10, 5, 20, 3, 15], 10)
    print(f"  sum_above_threshold([10, 5, 20, 3, 15], 10) = {result}")
    print(f"  Expected: 35")


main()
