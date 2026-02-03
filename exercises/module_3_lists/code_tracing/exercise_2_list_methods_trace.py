# =============================================================================
# Code Tracing: List Methods
# =============================================================================
# Difficulty: 3
# Concepts: append, pop, insert, remove - tracking list state changes
# =============================================================================

"""
{{CONTEXT_CODE_TRACING_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# {{TRACE_1_TITLE}}
# ============================================================
# {{CONTEXT_TRACE_1_NARRATIVE}}
# Track how append() and pop() change the list.


def code_to_trace_a():
    """Study this code - don't run it yet!"""
    inventory = ["{{item}}"]
    print(f"Start: {inventory}")

    inventory.append("potion")
    print(f"After append: {inventory}")

    inventory.append("key")
    print(f"After append: {inventory}")

    removed = inventory.pop()
    print(f"Popped: {removed}")
    print(f"After pop: {inventory}")


def trace_table_a():
    # FILL IN THE TRACING TABLE
    #
    # append() adds to the END of the list.
    # pop() removes and returns the LAST element.
    #
    # | Step | inventory                     | removed | Output              |
    # |------|-------------------------------|---------|---------------------|
    # | 1    | ['{{item}}']                  | -       | Start: ?            |
    # | 2    | ?                             | -       | After append: ?     |
    # | 3    | ?                             | -       | After append: ?     |
    # | 4    | ?                             | ?       | Popped: ?           |
    # | 5    | (same)                        |         | After pop: ?        |
    #
    # Fill in the ? values.

    pass


# ============================================================
# {{TRACE_2_TITLE}}
# ============================================================
# {{CONTEXT_TRACE_2_NARRATIVE}}
# Track how insert() places items at specific positions.


def code_to_trace_b():
    """Study this code - don't run it yet!"""
    team = ["{{hero}}", "{{mentor}}"]
    print(f"Start: {team}")

    team.insert(1, "{{heroine}}")
    print(f"After insert at 1: {team}")

    team.insert(0, "{{friend}}")
    print(f"After insert at 0: {team}")


def trace_table_b():
    # FILL IN THE TRACING TABLE
    #
    # insert(index, item) puts the item BEFORE the current element at that index.
    # Everything at index and after shifts right.
    #
    # | Step | team                                            | Output               |
    # |------|-------------------------------------------------|----------------------|
    # | 1    | ['{{hero}}', '{{mentor}}']                      | Start: ?             |
    # | 2    | ?                                               | After insert at 1: ? |
    # | 3    | ?                                               | After insert at 0: ? |
    #
    # Hint for step 2: {{heroine}} goes at index 1, pushing {{mentor}} to index 2.
    # Hint for step 3: {{friend}} goes at index 0, pushing everyone else right.

    pass


# ============================================================
# {{TRACE_3_TITLE}}
# ============================================================
# {{CONTEXT_TRACE_3_NARRATIVE}}
# Track how remove() deletes by VALUE (not index).


def code_to_trace_c():
    """Study this code - don't run it yet!"""
    abilities = ["{{spell1}}", "{{spell2}}", "{{spell1}}", "{{spell3}}"]
    print(f"Start: {abilities}")

    abilities.remove("{{spell1}}")
    print(f"After remove: {abilities}")

    abilities.remove("{{spell2}}")
    print(f"After remove: {abilities}")


def trace_table_c():
    # FILL IN THE TRACING TABLE
    #
    # remove(value) removes the FIRST occurrence of that value.
    # Note: We have "{{spell1}}" twice at the start!
    #
    # | Step | abilities                                  | Output         |
    # |------|--------------------------------------------|----------------|
    # | 1    | ['{{spell1}}','{{spell2}}','{{spell1}}','{{spell3}}'] | Start: ? |
    # | 2    | ?                                          | After remove: ?|
    # | 3    | ?                                          | After remove: ?|
    #
    # Hint: remove() only removes the FIRST match, not all matches.

    pass


# ============================================================
# {{TRACE_4_TITLE}}
# ============================================================
# {{CONTEXT_TRACE_4_NARRATIVE}}
# Combine multiple methods in sequence.


def code_to_trace_d():
    """Study this code - don't run it yet!"""
    items = []
    items.append("{{item}}")
    items.append("potion")
    items.append("map")
    print(f"After appends: {items}")

    items.insert(1, "key")
    print(f"After insert: {items}")

    removed = items.pop(0)
    print(f"Removed {removed}: {items}")


def trace_table_d():
    # FILL IN THE TRACING TABLE
    #
    # Note: pop(0) removes the item at index 0 (first item).
    #
    # | Step | items                             | removed | Output               |
    # |------|-----------------------------------|---------|----------------------|
    # | 1    | []                                | -       |                      |
    # | 2    | ['{{item}}']                      | -       |                      |
    # | 3    | ?                                 | -       |                      |
    # | 4    | ?                                 | -       | After appends: ?     |
    # | 5    | ?                                 | -       | After insert: ?      |
    # | 6    | ?                                 | ?       | Removed ?: ?         |
    #
    # Fill in the ? values.

    pass


def verify_traces():
    """Run this after completing your traces to check your work"""
    print("=== {{TRACE_1_TITLE}} - Actual Execution ===")
    code_to_trace_a()

    print("\n=== {{TRACE_2_TITLE}} - Actual Execution ===")
    code_to_trace_b()

    print("\n=== {{TRACE_3_TITLE}} - Actual Execution ===")
    code_to_trace_c()

    print("\n=== {{TRACE_4_TITLE}} - Actual Execution ===")
    code_to_trace_d()


def main():
    print("{{CONTEXT_CODE_TRACING_INTRO}}")
    print("=" * 50)
    print()
    print("Complete the tracing tables in trace_table_X functions first!")
    print("Then uncomment the line below to verify your answers.")
    print()

    # Uncomment this line AFTER completing your traces:
    # verify_traces()

    print("{{CONTEXT_VERIFICATION_COMPLETE}}")


main()
