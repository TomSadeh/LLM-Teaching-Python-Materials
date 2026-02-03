# =============================================================================
# Write Code: List Methods
# =============================================================================
# Difficulty: 3
# Concepts: append, pop, insert, remove - building and modifying lists
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
    # {{hero}} builds an inventory using append().
    # append() adds items to the END of the list.
    #
    # Step 1: Create an empty list: inventory = []
    # Step 2: Print f"Empty: {inventory}"
    # Step 3: Use append to add "{{item}}"
    # Step 4: Use append to add "potion"
    # Step 5: Use append to add "key"
    # Step 6: Print f"Full: {inventory}"
    # Step 7: Print f"Items: {len(inventory)}"
    #
    # Expected output:
    #   Empty: []
    #   Full: ['{{item}}', 'potion', 'key']
    #   Items: 3
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
    # {{heroine}} removes items with pop().
    # pop() removes and returns the LAST item.
    # pop(index) removes and returns the item at that index.
    #
    # Step 1: Create items = ["{{spell1}}", "{{spell2}}", "{{spell3}}"]
    # Step 2: Print f"Start: {items}"
    # Step 3: Remove last item: last = items.pop()
    # Step 4: Print f"Removed: {last}"
    # Step 5: Print f"After pop: {items}"
    # Step 6: Remove first item: first = items.pop(0)
    # Step 7: Print f"Removed: {first}"
    # Step 8: Print f"Remaining: {items}"
    #
    # Expected output:
    #   Start: ['{{spell1}}', '{{spell2}}', '{{spell3}}']
    #   Removed: {{spell3}}
    #   After pop: ['{{spell1}}', '{{spell2}}']
    #   Removed: {{spell1}}
    #   Remaining: ['{{spell2}}']
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
    # {{mentor}} shows how insert() places items at specific positions.
    # insert(index, item) puts the item BEFORE the current element at index.
    #
    # Step 1: Create queue = ["{{hero}}", "{{friend}}"]
    # Step 2: Print f"Original: {queue}"
    # Step 3: Insert "{{heroine}}" at index 1: queue.insert(1, "{{heroine}}")
    # Step 4: Print f"After insert at 1: {queue}"
    # Step 5: Insert "{{mentor}}" at index 0: queue.insert(0, "{{mentor}}")
    # Step 6: Print f"After insert at 0: {queue}"
    #
    # Expected output:
    #   Original: ['{{hero}}', '{{friend}}']
    #   After insert at 1: ['{{hero}}', '{{heroine}}', '{{friend}}']
    #   After insert at 0: ['{{mentor}}', '{{hero}}', '{{heroine}}', '{{friend}}']
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
    # {{hero}} uses remove() to delete items by value.
    # remove(value) removes the FIRST occurrence of that value.
    #
    # Step 1: Create duplicates = ["apple", "banana", "apple", "cherry"]
    # Step 2: Print f"Start: {duplicates}"
    # Step 3: Remove "apple": duplicates.remove("apple")
    # Step 4: Print f"After remove: {duplicates}"
    # Step 5: Remove "banana": duplicates.remove("banana")
    # Step 6: Print f"Final: {duplicates}"
    #
    # Note: Only the FIRST "apple" was removed, not both!
    #
    # Expected output:
    #   Start: ['apple', 'banana', 'apple', 'cherry']
    #   After remove: ['banana', 'apple', 'cherry']
    #   Final: ['apple', 'cherry']
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
    # Combine multiple list methods to manage {{house}} roster.
    #
    # Step 1: Create roster = ["{{hero}}"]
    # Step 2: Print f"Initial: {roster}"
    # Step 3: Add "{{heroine}}" to the end (use append)
    # Step 4: Add "{{friend}}" to the end (use append)
    # Step 5: Print f"After joins: {roster}"
    # Step 6: Insert "{{mentor}}" at position 0 (use insert)
    # Step 7: Print f"Leader added: {roster}"
    # Step 8: Remove "{{friend}}" (use remove)
    # Step 9: Print f"After leave: {roster}"
    # Step 10: Pop the last member and store in: departed = roster.pop()
    # Step 11: Print f"{departed} graduated. Final: {roster}"
    #
    # Expected output:
    #   Initial: ['{{hero}}']
    #   After joins: ['{{hero}}', '{{heroine}}', '{{friend}}']
    #   Leader added: ['{{mentor}}', '{{hero}}', '{{heroine}}', '{{friend}}']
    #   After leave: ['{{mentor}}', '{{hero}}', '{{heroine}}']
    #   {{heroine}} graduated. Final: ['{{mentor}}', '{{hero}}']
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
