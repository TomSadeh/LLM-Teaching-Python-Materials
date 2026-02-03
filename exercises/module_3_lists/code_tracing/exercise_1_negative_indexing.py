# =============================================================================
# Code Tracing: Negative Indexing
# =============================================================================
# Difficulty: 2-3
# Concepts: Negative indices, accessing elements from the end
# =============================================================================

"""
{{CONTEXT_CODE_TRACING_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# {{TRACE_1_TITLE}}
# ============================================================
# {{CONTEXT_TRACE_1_NARRATIVE}}


def code_to_trace_a():
    """Study this code - don't run it yet!"""
    team = ["{{hero}}", "{{heroine}}", "{{friend}}", "{{mentor}}"]
    print(team[-1])
    print(team[-2])
    print(team[-4])


def trace_table_a():
    # FILL IN THE TRACING TABLE
    #
    # Negative indices count from the end: -1 is last, -2 is second-to-last.
    #
    # The list has 4 elements at indices 0, 1, 2, 3
    # Negative indices: -4, -3, -2, -1
    #
    # | Index | Position from End | Value |
    # |-------|-------------------|-------|
    # | -1    | last              | ?     |
    # | -2    | second-to-last    | ?     |
    # | -3    | third-to-last     | ?     |
    # | -4    | fourth-to-last    | ?     |
    #
    # What will the three print statements output?
    # Line 1: _______________
    # Line 2: _______________
    # Line 3: _______________

    pass


# ============================================================
# {{TRACE_2_TITLE}}
# ============================================================
# {{CONTEXT_TRACE_2_NARRATIVE}}


def code_to_trace_b():
    """Study this code - don't run it yet!"""
    abilities = ["{{spell1}}", "{{spell2}}", "{{spell3}}"]
    first = abilities[0]
    last = abilities[-1]
    print(f"First: {first}")
    print(f"Last: {last}")
    print(f"Same? {first == last}")


def trace_table_b():
    # FILL IN THE TRACING TABLE
    #
    # Track the variables step by step.
    #
    # | Step | abilities             | first | last | Output |
    # |------|-----------------------|-------|------|--------|
    # | 1    | created with 3 items  | -     | -    |        |
    # | 2    | unchanged             | ?     | -    |        |
    # | 3    | unchanged             | ?     | ?    |        |
    # | 4    |                       |       |      | ?      |
    # | 5    |                       |       |      | ?      |
    # | 6    |                       |       |      | ?      |
    #
    # Fill in the ? values.

    pass


# ============================================================
# {{TRACE_3_TITLE}}
# ============================================================
# {{CONTEXT_TRACE_3_NARRATIVE}}


def code_to_trace_c():
    """Study this code - don't run it yet!"""
    items = ["{{item}}", "potion", "key", "map", "coin"]
    print(f"First: {items[0]}, Last: {items[-1]}")
    print(f"Second: {items[1]}, Second-to-last: {items[-2]}")
    print(f"Middle: {items[2]}")
    print(f"Length: {len(items)}")


def trace_table_c():
    # FILL IN THE TRACING TABLE
    #
    # Map positive and negative indices to the same elements.
    #
    # | Positive Index | Negative Index | Value    |
    # |----------------|----------------|----------|
    # | 0              | -5             | {{item}} |
    # | 1              | -4             | ?        |
    # | 2              | -3             | ?        |
    # | 3              | -2             | ?        |
    # | 4              | -1             | ?        |
    #
    # What will each print statement output?
    # Line 1: First: _____, Last: _____
    # Line 2: Second: _____, Second-to-last: _____
    # Line 3: Middle: _____
    # Line 4: Length: _____

    pass


def verify_traces():
    """Run this after completing your traces to check your work"""
    print("=== {{TRACE_1_TITLE}} - Actual Execution ===")
    code_to_trace_a()

    print("\n=== {{TRACE_2_TITLE}} - Actual Execution ===")
    code_to_trace_b()

    print("\n=== {{TRACE_3_TITLE}} - Actual Execution ===")
    code_to_trace_c()


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
