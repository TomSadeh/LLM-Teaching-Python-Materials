"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

Topic: Using continue to skip iterations
Difficulty: 2-3

The 'continue' statement skips the rest of the current iteration
and moves to the next one. Use it to skip unwanted items.
"""


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}
#
# Use continue to skip items that don't match criteria.


def print_positive_only(numbers):
    """
    Print only the positive numbers from a list.
    Skip zeros and negative numbers using continue.

    Args:
        numbers: A list of integers

    Example:
        print_positive_only([3, -1, 0, 5, -2, 8])
        Prints:
            3
            5
            8
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Loop through each number in numbers
    # Step 2: If number is less than or equal to 0, continue
    # Step 3: Print the number
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}
#
# Use continue to filter during processing.


def filter_and_transform(items):
    """
    Process items but skip any that are empty strings.
    Transform valid items to uppercase.

    Args:
        items: A list of strings

    Returns:
        list: Uppercase versions of non-empty strings

    Example:
        filter_and_transform(["{{hero}}", "", "{{villain}}", ""])
        Returns: ["{{HERO}}", "{{VILLAIN}}"]  # (uppercase versions)
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Create an empty result list
    # Step 2: Loop through each item
    # Step 3: If item is an empty string "", continue
    # Step 4: Convert to uppercase and add to result
    # Step 5: Return result
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}
#
# Use continue with index-based loops.


def process_every_other(values):
    """
    Process only items at even indices (0, 2, 4, ...).
    Skip items at odd indices using continue.

    Args:
        values: A list of values

    Returns:
        list: Items from even indices only

    Example:
        process_every_other(["A", "B", "C", "D", "E"])
        Returns: ["A", "C", "E"]  # indices 0, 2, 4
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Create an empty result list
    # Step 2: Loop with index: for i in range(len(values))
    # Step 3: If i is odd (i % 2 != 0), continue
    # Step 4: Add values[i] to result
    # Step 5: Return result
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}
#
# Combine continue with while loops.


def sum_valid_inputs():
    """
    Collect numbers from user and sum them.
    Skip invalid inputs (non-numeric) using continue.
    Stop when user enters 'done'.

    Returns:
        int: Sum of all valid numbers entered

    The function should:
    - Ask for input repeatedly
    - If input is 'done', stop and return the sum
    - If input is not a valid integer, print error and continue
    - If input is valid, add to sum
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Set total = 0
    # Step 2: While True:
    #         - Get input
    #         - If input is 'done', break
    #         - If input.isdigit() or (input.startswith('-') and input[1:].isdigit()):
    #           Add int(input) to total
    #         - Else: print "Invalid number, skipping." and continue
    # Step 3: Return total
    #
    # Note: Use .lstrip('-').isdigit() to check for negative numbers
    pass


# ============================================================
# {{PHASE_5_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_5}}
#
# Use continue with complex skip conditions.


def process_approved_items(items, blocked_list):
    """
    Process items unless they are in the blocked list.
    Skip blocked items using continue.

    Args:
        items: List of items to process
        blocked_list: List of items to skip

    Returns:
        list: Processed (lowercase) items that weren't blocked

    Example:
        process_approved_items(
            ["{{hero}}", "{{villain}}", "{{friend}}"],
            ["{{villain}}"]
        )
        Returns: ["{{hero}}", "{{friend}}"]  # lowercase versions
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Create an empty result list
    # Step 2: Loop through each item
    # Step 3: If item is in blocked_list:
    #         - Print f"Blocked: {item}"
    #         - Continue
    # Step 4: Process item (convert to lowercase) and add to result
    #         - Print f"Approved: {item}"
    # Step 5: Return result
    pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)

    print("\n=== {{PHASE_1_TITLE}} ===")
    numbers = [5, -3, 0, 8, -1, 12, 0, -7]
    print(f"Numbers: {numbers}")
    print("Positive only:")
    print_positive_only(numbers)

    print("\n=== {{PHASE_2_TITLE}} ===")
    items = ["{{hero}}", "", "{{villain}}", "", "{{friend}}"]
    result = filter_and_transform(items)
    print(f"Filtered and transformed: {result}")

    print("\n=== {{PHASE_3_TITLE}} ===")
    values = ["A", "B", "C", "D", "E", "F"]
    result = process_every_other(values)
    print(f"Every other item: {result}")

    print("\n=== {{PHASE_4_TITLE}} ===")
    print("Sum numbers (type 'done' to finish):")
    # Uncomment to test:
    # total = sum_valid_inputs()
    # print(f"Sum: {total}")

    print("\n=== {{PHASE_5_TITLE}} ===")
    all_items = ["{{hero}}", "{{villain}}", "{{friend}}", "{{mentor}}"]
    blocked = ["{{villain}}"]
    result = process_approved_items(all_items, blocked)
    print(f"Approved items: {result}")

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
