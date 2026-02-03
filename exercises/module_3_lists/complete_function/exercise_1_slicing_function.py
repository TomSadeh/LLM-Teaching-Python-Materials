# =============================================================================
# Complete the Function: Slicing Functions
# =============================================================================
# Difficulty: 3-4
# Concepts: Using slicing to extract and manipulate list portions
# =============================================================================

"""
{{CONTEXT_COMPLETE_FUNCTION_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# {{FUNCTION_1_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_1_NARRATIVE}}


def get_first_and_last(items):
    """
    Return a list containing only the first and last elements.

    Args:
        items: A list with at least 2 elements

    Returns:
        A new list with [first_element, last_element]

    Examples:
        >>> get_first_and_last(["{{hero}}", "{{heroine}}", "{{friend}}"])
        ['{{hero}}', '{{friend}}']
        >>> get_first_and_last([1, 2, 3, 4, 5])
        [1, 5]
        >>> get_first_and_last(["start", "end"])
        ['start', 'end']
    """
    # Started for you:
    first = items[0]

    # COMPLETE THIS FUNCTION
    #
    # Step 1: Get the last element using negative indexing
    # Step 2: Return a new list containing first and last
    #
    # Hint: Use items[-1] to get the last element

    pass  # Replace with implementation


# ============================================================
# {{FUNCTION_2_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_2_NARRATIVE}}


def split_in_half(items):
    """
    Split a list into two halves.

    Args:
        items: A list to split

    Returns:
        A tuple of two lists: (first_half, second_half)
        For odd-length lists, first half gets the extra element.

    Examples:
        >>> split_in_half([1, 2, 3, 4])
        ([1, 2], [3, 4])
        >>> split_in_half(["A", "B", "C", "D", "E"])
        (['A', 'B', 'C'], ['D', 'E'])
        >>> split_in_half(["{{item}}"])
        (['{{item}}'], [])
    """
    # Started for you:
    length = len(items)
    midpoint = (length + 1) // 2  # Rounds up for odd lengths

    # COMPLETE THIS FUNCTION
    #
    # Step 1: Use slicing to get the first half (indices 0 to midpoint)
    # Step 2: Use slicing to get the second half (indices midpoint to end)
    # Step 3: Return both halves as a tuple
    #
    # Hint: items[:midpoint] and items[midpoint:]

    pass  # Replace with implementation


# ============================================================
# {{FUNCTION_3_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_3_NARRATIVE}}


def get_every_nth(items, n):
    """
    Return every nth element from the list.

    Args:
        items: A list of elements
        n: Take every nth element (n=2 means every other)

    Returns:
        A new list with every nth element

    Examples:
        >>> get_every_nth([1, 2, 3, 4, 5, 6], 2)
        [1, 3, 5]
        >>> get_every_nth(["A", "B", "C", "D", "E", "F"], 3)
        ['A', 'D']
        >>> get_every_nth(["{{spell1}}", "{{spell2}}", "{{spell3}}", "{{spell4}}"], 2)
        ['{{spell1}}', '{{spell3}}']
    """
    # COMPLETE THIS FUNCTION
    #
    # Use step slicing: items[start:stop:step]
    # To get every nth element starting from the first, use items[::n]
    #
    # Hint: You only need one line using slice notation

    pass  # Replace with implementation


# ============================================================
# {{FUNCTION_4_TITLE}}
# ============================================================
# {{CONTEXT_FUNCTION_4_NARRATIVE}}


def reverse_and_trim(items, trim_count):
    """
    Reverse a list and remove elements from both ends.

    Args:
        items: A list to process
        trim_count: Number of elements to remove from each end after reversing

    Returns:
        The reversed list with trim_count elements removed from each end

    Examples:
        >>> reverse_and_trim([1, 2, 3, 4, 5], 1)
        [4, 3, 2]
        >>> reverse_and_trim(["A", "B", "C", "D", "E", "F"], 2)
        ['D', 'C']
        >>> reverse_and_trim([1, 2, 3], 0)
        [3, 2, 1]
    """
    # Started for you:
    reversed_list = items[::-1]

    # COMPLETE THIS FUNCTION
    #
    # Step 1: If trim_count is 0, just return the reversed list
    # Step 2: Otherwise, slice to remove trim_count from each end
    #
    # Hint: To remove N from each end, use [N:-N]
    # But be careful with trim_count of 0 ([:0] would give empty list)

    pass  # Replace with implementation


def main():
    print("{{CONTEXT_COMPLETE_FUNCTION_INTRO}}")
    print("=" * 50)

    print("\n=== Testing {{FUNCTION_1_TITLE}} ===")
    result1 = get_first_and_last(["{{hero}}", "{{heroine}}", "{{friend}}"])
    print(f"get_first_and_last(['{{hero}}', '{{heroine}}', '{{friend}}']): {result1}")
    result2 = get_first_and_last([1, 2, 3, 4, 5])
    print(f"get_first_and_last([1, 2, 3, 4, 5]): {result2}")

    print("\n=== Testing {{FUNCTION_2_TITLE}} ===")
    result3 = split_in_half([1, 2, 3, 4])
    print(f"split_in_half([1, 2, 3, 4]): {result3}")
    result4 = split_in_half(["A", "B", "C", "D", "E"])
    print(f"split_in_half(['A', 'B', 'C', 'D', 'E']): {result4}")

    print("\n=== Testing {{FUNCTION_3_TITLE}} ===")
    result5 = get_every_nth([1, 2, 3, 4, 5, 6], 2)
    print(f"get_every_nth([1, 2, 3, 4, 5, 6], 2): {result5}")
    result6 = get_every_nth(["A", "B", "C", "D", "E", "F"], 3)
    print(f"get_every_nth(['A', 'B', 'C', 'D', 'E', 'F'], 3): {result6}")

    print("\n=== Testing {{FUNCTION_4_TITLE}} ===")
    result7 = reverse_and_trim([1, 2, 3, 4, 5], 1)
    print(f"reverse_and_trim([1, 2, 3, 4, 5], 1): {result7}")
    result8 = reverse_and_trim(["A", "B", "C", "D", "E", "F"], 2)
    print(f"reverse_and_trim(['A', 'B', 'C', 'D', 'E', 'F'], 2): {result8}")

    print("\n" + "=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
