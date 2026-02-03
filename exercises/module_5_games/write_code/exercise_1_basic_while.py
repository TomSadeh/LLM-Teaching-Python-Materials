"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

Topic: Basic while loops with counter variables
Difficulty: 1-2

In this exercise, you'll learn the fundamental pattern of while loops:
setting up a counter, checking a condition, and updating the counter.
"""


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}
#
# A while loop repeats as long as its condition is True.
# The pattern: initialize -> check condition -> do work -> update


def countdown_from_five():
    """
    Print a countdown from 5 to 1, then print a final message.

    Expected output:
        5
        4
        3
        2
        1
        {{exclamation}}
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Create a variable called 'count' starting at 5
    # Step 2: While count is greater than 0:
    #         - Print the current count
    #         - Decrease count by 1
    # Step 3: After the loop, print "{{exclamation}}"
    #
    # Hint: Don't forget to decrease count, or the loop never ends!
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}
#
# While loops are perfect for counting up to a target.


def count_up_to(target):
    """
    Print numbers from 1 up to and including target.

    Args:
        target: The number to count up to

    Example:
        count_up_to(4) prints:
        1
        2
        3
        4
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Create a variable called 'current' starting at 1
    # Step 2: While current is less than or equal to target:
    #         - Print current
    #         - Increase current by 1
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}
#
# While loops can track totals as they iterate.


def sum_until_limit(limit):
    """
    Add numbers 1, 2, 3, ... until the sum would exceed the limit.
    Return the sum and how many numbers were added.

    Args:
        limit: Stop before the sum exceeds this value

    Returns:
        tuple: (final_sum, count_of_numbers)

    Example:
        sum_until_limit(10) returns (10, 4)
        Because: 1+2+3+4=10, and 1+2+3+4+5=15 would exceed 10
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Initialize total = 0, next_number = 1, count = 0
    # Step 2: While total + next_number <= limit:
    #         - Add next_number to total
    #         - Increase count by 1
    #         - Increase next_number by 1
    # Step 3: Return (total, count)
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}
#
# While loops with multiple conditions using 'and' or 'or'.


def process_batch(items_to_process, max_iterations):
    """
    Process items one at a time, but stop early if you run out of items
    OR if you reach max_iterations.

    Args:
        items_to_process: Starting number of items
        max_iterations: Maximum number of processing rounds

    Returns:
        tuple: (items_processed, iterations_used)

    Example:
        process_batch(3, 10) returns (3, 3)  # Ran out of items
        process_batch(100, 5) returns (5, 5)  # Hit iteration limit
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Initialize items_left = items_to_process, iterations = 0
    # Step 2: While items_left > 0 AND iterations < max_iterations:
    #         - Decrease items_left by 1
    #         - Increase iterations by 1
    #         - Print f"Processed item. {items_left} remaining."
    # Step 3: Return (iterations, iterations)  # items processed = iterations
    pass


# ============================================================
# {{PHASE_5_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_5}}
#
# Accumulating results in a list while looping.


def generate_sequence(start, multiplier, length):
    """
    Generate a sequence where each number is the previous times multiplier.

    Args:
        start: First number in sequence
        multiplier: What to multiply by each time
        length: How many numbers to generate

    Returns:
        list: The generated sequence

    Example:
        generate_sequence(2, 3, 4) returns [2, 6, 18, 54]
        Because: 2, 2*3=6, 6*3=18, 18*3=54
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Create an empty list called 'sequence'
    # Step 2: Set current = start
    # Step 3: While len(sequence) < length:
    #         - Append current to sequence
    #         - Multiply current by multiplier
    # Step 4: Return sequence
    pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)

    print("\n=== {{PHASE_1_TITLE}} ===")
    print("Countdown:")
    countdown_from_five()

    print("\n=== {{PHASE_2_TITLE}} ===")
    print("Counting to 5:")
    count_up_to(5)

    print("\n=== {{PHASE_3_TITLE}} ===")
    result = sum_until_limit(10)
    print(f"Sum until 10: {result}")

    print("\n=== {{PHASE_4_TITLE}} ===")
    print("Processing batch of 7 items with max 5 iterations:")
    result = process_batch(7, 5)
    print(f"Result: {result}")

    print("\n=== {{PHASE_5_TITLE}} ===")
    seq = generate_sequence(2, 3, 5)
    print(f"Sequence: {seq}")

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
