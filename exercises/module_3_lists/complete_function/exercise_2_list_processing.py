# =============================================================================
# Complete the Function: List Processing
# =============================================================================
# Difficulty: 3
# Concepts: Iterating, filtering, accumulating with lists
# =============================================================================

"""
{{CONTEXT_COMPLETE_FUNCTION_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# {{FUNCTION_1_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_1_NARRATIVE}}


def count_matches(items, target):
    """
    Count how many times target appears in items.

    Args:
        items: A list of items to search
        target: The value to count

    Returns:
        The number of times target appears in items

    Examples:
        >>> count_matches(["{{item}}", "potion", "{{item}}", "key"], "{{item}}")
        2
        >>> count_matches([1, 2, 3, 2, 2], 2)
        3
        >>> count_matches(["a", "b", "c"], "x")
        0
    """
    # Started for you:
    count = 0

    # COMPLETE THIS FUNCTION
    #
    # Loop through each item in items.
    # If the item equals target, add 1 to count.
    # Return the final count.
    #
    # Hint: for item in items: if item == target: count = count + 1

    pass  # Replace with implementation


# ============================================================
# {{FUNCTION_2_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_2_NARRATIVE}}


def find_all_above(numbers, threshold):
    """
    Return all numbers greater than threshold.

    Args:
        numbers: A list of numbers
        threshold: The minimum value (exclusive)

    Returns:
        A new list with only numbers > threshold

    Examples:
        >>> find_all_above([10, 25, 5, 30, 15], 20)
        [25, 30]
        >>> find_all_above([1, 2, 3, 4, 5], 3)
        [4, 5]
        >>> find_all_above([5, 5, 5], 5)
        []
    """
    # Started for you:
    result = []

    # COMPLETE THIS FUNCTION
    #
    # Loop through each number in numbers.
    # If number > threshold, append it to result.
    # Return result.

    pass  # Replace with implementation


# ============================================================
# {{FUNCTION_3_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_3_NARRATIVE}}


def get_longest_string(strings):
    """
    Return the longest string in the list.

    Args:
        strings: A list of strings (at least one)

    Returns:
        The string with the most characters

    Examples:
        >>> get_longest_string(["{{hero}}", "{{heroine}}", "{{friend}}"])
        '{{heroine}}'  # Assuming heroine is longest
        >>> get_longest_string(["cat", "elephant", "dog"])
        'elephant'
        >>> get_longest_string(["one"])
        'one'
    """
    # Started for you:
    longest = strings[0]  # Start with first string

    # COMPLETE THIS FUNCTION
    #
    # Loop through each string in strings.
    # If len(string) > len(longest), update longest = string.
    # Return longest.
    #
    # Hint: Start from strings[1:] since we already have the first

    pass  # Replace with implementation


# ============================================================
# {{FUNCTION_4_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_4_NARRATIVE}}


def double_all(numbers):
    """
    Return a new list with all numbers doubled.

    Args:
        numbers: A list of numbers

    Returns:
        A new list where each number is multiplied by 2

    Examples:
        >>> double_all([1, 2, 3, 4])
        [2, 4, 6, 8]
        >>> double_all([10, 20, 30])
        [20, 40, 60]
        >>> double_all([])
        []
    """
    # COMPLETE THIS FUNCTION
    #
    # Create an empty result list.
    # Loop through each number in numbers.
    # Append number * 2 to result.
    # Return result.

    pass  # Replace with implementation


# ============================================================
# {{FUNCTION_5_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_5_NARRATIVE}}


def index_of_first(items, target):
    """
    Find the index of the first occurrence of target.

    Args:
        items: A list to search
        target: The value to find

    Returns:
        The index of first occurrence, or -1 if not found

    Examples:
        >>> index_of_first(["{{spell1}}", "{{spell2}}", "{{spell3}}"], "{{spell2}}")
        1
        >>> index_of_first([10, 20, 30, 20], 20)
        1
        >>> index_of_first(["a", "b", "c"], "x")
        -1
    """
    # COMPLETE THIS FUNCTION
    #
    # Loop through indices using range(len(items)).
    # If items[i] == target, return i immediately.
    # If loop completes without finding, return -1.
    #
    # Hint: Use "for i in range(len(items)):"

    pass  # Replace with implementation


def main():
    print("{{CONTEXT_COMPLETE_FUNCTION_INTRO}}")
    print("=" * 50)

    print("\n=== Testing {{FUNCTION_1_TITLE}} ===")
    result1 = count_matches(["{{item}}", "potion", "{{item}}", "key"], "{{item}}")
    print(f"count_matches([...], '{{item}}'): {result1}")
    result2 = count_matches([1, 2, 3, 2, 2], 2)
    print(f"count_matches([1,2,3,2,2], 2): {result2}")

    print("\n=== Testing {{FUNCTION_2_TITLE}} ===")
    result3 = find_all_above([10, 25, 5, 30, 15], 20)
    print(f"find_all_above([10,25,5,30,15], 20): {result3}")
    result4 = find_all_above([1, 2, 3, 4, 5], 3)
    print(f"find_all_above([1,2,3,4,5], 3): {result4}")

    print("\n=== Testing {{FUNCTION_3_TITLE}} ===")
    result5 = get_longest_string(["cat", "elephant", "dog"])
    print(f"get_longest_string(['cat','elephant','dog']): {result5}")

    print("\n=== Testing {{FUNCTION_4_TITLE}} ===")
    result6 = double_all([1, 2, 3, 4])
    print(f"double_all([1, 2, 3, 4]): {result6}")

    print("\n=== Testing {{FUNCTION_5_TITLE}} ===")
    result7 = index_of_first([10, 20, 30, 20], 20)
    print(f"index_of_first([10,20,30,20], 20): {result7}")
    result8 = index_of_first(["a", "b", "c"], "x")
    print(f"index_of_first(['a','b','c'], 'x'): {result8}")

    print("\n" + "=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
