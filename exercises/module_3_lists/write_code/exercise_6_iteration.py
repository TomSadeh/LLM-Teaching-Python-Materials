# =============================================================================
# Write Code: List Iteration
# =============================================================================
# Difficulty: 3
# Concepts: for loops over lists, iterating by element vs by index
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
    # {{hero}} visits each member of the team.
    # Use "for item in list" to iterate directly over elements.
    #
    # Step 1: Create team = ["{{hero}}", "{{heroine}}", "{{friend}}"]
    # Step 2: Use a for loop to print each member:
    #         for member in team:
    #             print(f"Visiting: {member}")
    #
    # Expected output:
    #   Visiting: {{hero}}
    #   Visiting: {{heroine}}
    #   Visiting: {{friend}}
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
    # {{heroine}} calculates the total value of items.
    # Use a loop to accumulate a sum.
    #
    # Step 1: Create values = [100, 50, 75, 25]
    # Step 2: Create total = 0
    # Step 3: Use a for loop to add each value to total:
    #         for value in values:
    #             total = total + value
    # Step 4: Print f"Total value: {total}"
    #
    # Expected output:
    #   Total value: 250
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
    # {{mentor}} needs to number each item in a list.
    # Use range(len(list)) to iterate with indices.
    #
    # Step 1: Create items = ["{{spell1}}", "{{spell2}}", "{{spell3}}"]
    # Step 2: Use a for loop with range:
    #         for i in range(len(items)):
    #             print(f"{i + 1}. {items[i]}")
    #
    # Expected output:
    #   1. {{spell1}}
    #   2. {{spell2}}
    #   3. {{spell3}}
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
    # {{hero}} filters items based on a condition.
    # Build a new list from elements that pass a test.
    #
    # Step 1: Create scores = [85, 42, 91, 67, 38, 95, 73]
    # Step 2: Create passing = [] (empty list for results)
    # Step 3: Loop through scores:
    #         for score in scores:
    #             if score >= 60:
    #                 passing.append(score)
    # Step 4: Print f"Original: {scores}"
    # Step 5: Print f"Passing (>=60): {passing}"
    # Step 6: Print f"Pass rate: {len(passing)}/{len(scores)}"
    #
    # Expected output:
    #   Original: [85, 42, 91, 67, 38, 95, 73]
    #   Passing (>=60): [85, 91, 67, 95, 73]
    #   Pass rate: 5/7
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
    # {{heroine}} transforms each item in a list.
    # Create a new list with modified values.
    #
    # Step 1: Create levels = [1, 2, 3, 4, 5]
    # Step 2: Create doubled = [] (empty list for results)
    # Step 3: Loop through levels:
    #         for level in levels:
    #             doubled.append(level * 2)
    # Step 4: Print f"Original: {levels}"
    # Step 5: Print f"Doubled: {doubled}"
    #
    # Expected output:
    #   Original: [1, 2, 3, 4, 5]
    #   Doubled: [2, 4, 6, 8, 10]
    pass


# ============================================================
# {{PHASE_6_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_6}}


def exercise_f():
    # YOUR CODE HERE
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # Combine iteration with conditions.
    # Count items that match a criteria.
    #
    # Step 1: Create inventory = ["{{item}}", "potion", "{{item}}", "key", "{{item}}"]
    # Step 2: Create count = 0
    # Step 3: Loop through inventory:
    #         for item in inventory:
    #             if item == "{{item}}":
    #                 count = count + 1
    # Step 4: Print f"Inventory: {inventory}"
    # Step 5: Print f"Number of {{item}}s: {count}"
    #
    # Expected output:
    #   Inventory: ['{{item}}', 'potion', '{{item}}', 'key', '{{item}}']
    #   Number of {{item}}s: 3
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

    print("\n=== {{PHASE_6_TITLE}} ===")
    exercise_f()

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
