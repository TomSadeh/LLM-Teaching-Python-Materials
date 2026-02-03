# =============================================================================
# Code Tracing: Slicing Operations
# =============================================================================
# Difficulty: 3-4
# Concepts: list[start:stop], list[start:stop:step], slice boundaries
# =============================================================================

"""
{{CONTEXT_CODE_TRACING_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# {{TRACE_1_TITLE}}
# ============================================================
# {{CONTEXT_TRACE_1_NARRATIVE}}
# Basic slicing: list[start:stop] extracts elements from start UP TO (not including) stop.


def code_to_trace_a():
    """Study this code - don't run it yet!"""
    items = ["{{item}}", "potion", "key", "map", "coin"]
    print(f"Full list: {items}")

    first_two = items[0:2]
    print(f"items[0:2]: {first_two}")

    middle = items[1:4]
    print(f"items[1:4]: {middle}")

    last_two = items[3:5]
    print(f"items[3:5]: {last_two}")


def trace_table_a():
    # FILL IN THE TRACING TABLE
    #
    # Remember: slice[start:stop] includes start but EXCLUDES stop!
    # items = ["{{item}}", "potion", "key", "map", "coin"]
    # indices:     0          1        2      3       4
    #
    # | Slice      | Start | Stop | Elements Included | Result |
    # |------------|-------|------|-------------------|--------|
    # | items[0:2] | 0     | 2    | indices 0, 1      | ?      |
    # | items[1:4] | 1     | 4    | indices 1, 2, 3   | ?      |
    # | items[3:5] | 3     | 5    | indices 3, 4      | ?      |
    #
    # What will each print statement output?

    pass


# ============================================================
# {{TRACE_2_TITLE}}
# ============================================================
# {{CONTEXT_TRACE_2_NARRATIVE}}
# Shorthand slicing: omit start (defaults to 0) or stop (defaults to end).


def code_to_trace_b():
    """Study this code - don't run it yet!"""
    team = ["{{hero}}", "{{heroine}}", "{{friend}}", "{{mentor}}"]
    print(f"Full team: {team}")

    first_three = team[:3]
    print(f"team[:3]: {first_three}")

    last_two = team[2:]
    print(f"team[2:]: {last_two}")

    copy = team[:]
    print(f"team[:]: {copy}")


def trace_table_b():
    # FILL IN THE TRACING TABLE
    #
    # Shorthand rules:
    # - team[:3] means team[0:3] (from start to index 3)
    # - team[2:] means team[2:end] (from index 2 to the end)
    # - team[:] means team[0:end] (entire list copy)
    #
    # | Slice    | Equivalent | Result                        |
    # |----------|------------|-------------------------------|
    # | team[:3] | team[0:3]  | ?                             |
    # | team[2:] | team[2:4]  | ?                             |
    # | team[:]  | team[0:4]  | ?                             |
    #
    # Fill in the ? results.

    pass


# ============================================================
# {{TRACE_3_TITLE}}
# ============================================================
# {{CONTEXT_TRACE_3_NARRATIVE}}
# Negative indices in slices work too!


def code_to_trace_c():
    """Study this code - don't run it yet!"""
    abilities = ["{{spell1}}", "{{spell2}}", "{{spell3}}", "{{spell4}}"]
    print(f"All abilities: {abilities}")

    all_but_last = abilities[:-1]
    print(f"abilities[:-1]: {all_but_last}")

    last_two = abilities[-2:]
    print(f"abilities[-2:]: {last_two}")

    middle = abilities[1:-1]
    print(f"abilities[1:-1]: {middle}")


def trace_table_c():
    # FILL IN THE TRACING TABLE
    #
    # Negative index mapping for 4-element list:
    # Positive: 0, 1, 2, 3
    # Negative: -4, -3, -2, -1
    #
    # | Slice          | Start | Stop | Elements        | Result |
    # |----------------|-------|------|-----------------|--------|
    # | abilities[:-1] | 0     | -1   | 0, 1, 2         | ?      |
    # | abilities[-2:] | -2    | end  | -2, -1 (= 2, 3) | ?      |
    # | abilities[1:-1]| 1     | -1   | 1, 2            | ?      |
    #
    # Fill in the ? results.

    pass


# ============================================================
# {{TRACE_4_TITLE}}
# ============================================================
# {{CONTEXT_TRACE_4_NARRATIVE}}
# Step slicing: list[start:stop:step] skips elements.


def code_to_trace_d():
    """Study this code - don't run it yet!"""
    numbers = [0, 1, 2, 3, 4, 5, 6, 7]
    print(f"All: {numbers}")

    every_other = numbers[::2]
    print(f"numbers[::2]: {every_other}")

    every_third = numbers[::3]
    print(f"numbers[::3]: {every_third}")

    reversed_list = numbers[::-1]
    print(f"numbers[::-1]: {reversed_list}")


def trace_table_d():
    # FILL IN THE TRACING TABLE
    #
    # Step slicing picks every Nth element.
    # Step of -1 reverses the list.
    #
    # numbers = [0, 1, 2, 3, 4, 5, 6, 7]
    #
    # | Slice        | Step | Elements Selected | Result          |
    # |--------------|------|-------------------|-----------------|
    # | numbers[::2] | 2    | 0, 2, 4, 6        | ?               |
    # | numbers[::3] | 3    | 0, 3, 6           | ?               |
    # | numbers[::-1]| -1   | reversed          | ?               |
    #
    # Fill in the ? results.

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
