# =============================================================================
# Write Code: List Slicing
# =============================================================================
# Difficulty: 3-4
# Concepts: Slicing syntax [start:stop:step], extracting sublists
# =============================================================================

"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""

# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    # YOUR CODE HERE
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # {{hero}} learns basic slicing.
    # list[start:stop] extracts elements from start UP TO (not including) stop.
    #
    # Step 1: Create items = ["{{item}}", "potion", "key", "map", "coin"]
    # Step 2: Extract first three: first_three = items[0:3]
    # Step 3: Print f"First three: {first_three}"
    # Step 4: Extract middle three: middle = items[1:4]
    # Step 5: Print f"Middle three: {middle}"
    # Step 6: Extract last two: last_two = items[3:5]
    # Step 7: Print f"Last two: {last_two}"
    #
    # Expected output:
    #   First three: ['{{item}}', 'potion', 'key']
    #   Middle three: ['potion', 'key', 'map']
    #   Last two: ['map', 'coin']
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # YOUR CODE HERE
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # {{heroine}} uses shorthand slicing.
    # Omit start = starts from 0. Omit stop = goes to end.
    #
    # Step 1: Create team = ["{{hero}}", "{{heroine}}", "{{friend}}", "{{mentor}}"]
    # Step 2: Get first two: first = team[:2]
    # Step 3: Print f"First two: {first}"
    # Step 4: Get last two: last = team[2:]
    # Step 5: Print f"Last two: {last}"
    # Step 6: Get all (copy): all_copy = team[:]
    # Step 7: Print f"Copy: {all_copy}"
    #
    # Expected output:
    #   First two: ['{{hero}}', '{{heroine}}']
    #   Last two: ['{{friend}}', '{{mentor}}']
    #   Copy: ['{{hero}}', '{{heroine}}', '{{friend}}', '{{mentor}}']
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # YOUR CODE HERE
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # {{mentor}} shows negative indices in slices.
    # Negative -1 is the last element, -2 is second-to-last, etc.
    #
    # Step 1: Create abilities = ["{{spell1}}", "{{spell2}}", "{{spell3}}", "{{spell4}}"]
    # Step 2: Get all except last: most = abilities[:-1]
    # Step 3: Print f"All but last: {most}"
    # Step 4: Get last two: end = abilities[-2:]
    # Step 5: Print f"Last two: {end}"
    # Step 6: Get middle (skip first and last): middle = abilities[1:-1]
    # Step 7: Print f"Middle: {middle}"
    #
    # Expected output:
    #   All but last: ['{{spell1}}', '{{spell2}}', '{{spell3}}']
    #   Last two: ['{{spell3}}', '{{spell4}}']
    #   Middle: ['{{spell2}}', '{{spell3}}']
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # YOUR CODE HERE
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # {{hero}} learns step slicing.
    # list[start:stop:step] picks every Nth element.
    #
    # Step 1: Create numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Step 2: Get every other number: evens = numbers[::2]
    # Step 3: Print f"Every other: {evens}"
    # Step 4: Get odd positions: odds = numbers[1::2]
    # Step 5: Print f"Odd indices: {odds}"
    # Step 6: Reverse the list: reversed_nums = numbers[::-1]
    # Step 7: Print f"Reversed: {reversed_nums}"
    #
    # Expected output:
    #   Every other: [0, 2, 4, 6, 8]
    #   Odd indices: [1, 3, 5, 7, 9]
    #   Reversed: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    pass


# ============================================================
# {{PHASE_5_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_5}}


def exercise_e():
    # YOUR CODE HERE
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # Combine slicing techniques to solve a problem.
    # {{heroine}} needs to reorganize a party roster.
    #
    # Step 1: Create roster = ["A", "B", "C", "D", "E", "F"]
    # Step 2: Print f"Original: {roster}"
    # Step 3: Get first half: first_half = roster[:3]
    # Step 4: Get second half: second_half = roster[3:]
    # Step 5: Print f"First half: {first_half}"
    # Step 6: Print f"Second half: {second_half}"
    # Step 7: Swap halves: swapped = second_half + first_half
    # Step 8: Print f"Swapped: {swapped}"
    #
    # Expected output:
    #   Original: ['A', 'B', 'C', 'D', 'E', 'F']
    #   First half: ['A', 'B', 'C']
    #   Second half: ['D', 'E', 'F']
    #   Swapped: ['D', 'E', 'F', 'A', 'B', 'C']
    pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)

    print("\n=== {{PHASE_1_TITLE}} ===")
    exercise_a()

    print("\n=== {{PHASE_2_TITLE}} ===")
    exercise_b()

    print("\n=== {{PHASE_3_TITLE}} ===")
    exercise_c()

    print("\n=== {{PHASE_4_TITLE}} ===")
    exercise_d()

    print("\n=== {{PHASE_5_TITLE}} ===")
    exercise_e()

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
