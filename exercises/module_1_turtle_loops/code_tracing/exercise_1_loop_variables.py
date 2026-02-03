# =============================================================================
# Code Tracing: Loop Variables
# =============================================================================
# Difficulty: 3
# Concepts: loop variable changes, tracking iterations
# =============================================================================

"""
{{CONTEXT_CODE_TRACING_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# --- {{TRACE_1_TITLE}} ---
# {{CONTEXT_TRACE_1_NARRATIVE}}


def code_to_trace_a():
    """Study this code - don't run it yet!"""
    # {{hero}} tracks steps taken at {{school}}
    for step in range(4):
        print(f"Step {step}")


def trace_table_a():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # Track the value of `step` in each iteration.
    #
    # | Iteration | step | Output |
    # |-----------|------|--------|
    # | 1         |      |        |
    # | 2         |      |        |
    # | 3         |      |        |
    # | 4         |      |        |
    #
    # Hint: range(4) produces the values 0, 1, 2, 3.
    # Each iteration, `step` takes the next value.
    #
    # {{CONTEXT_TRACE_HINT_1}}
    pass


# --- {{TRACE_2_TITLE}} ---
# {{CONTEXT_TRACE_2_NARRATIVE}}


def code_to_trace_b():
    """Study this code - don't run it yet!"""
    # Counting down for {{creature}} at {{location}}
    for num in range(3, 0, -1):
        print(f"T-minus {num}")
    print("Launch!")


def trace_table_b():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # Track the value of `num` in each iteration.
    #
    # | Iteration | num | Output |
    # |-----------|-----|--------|
    # | 1         |     |        |
    # | 2         |     |        |
    # | 3         |     |        |
    # | After loop |  - | ????   |
    #
    # Hint: range(3, 0, -1) counts backwards: 3, 2, 1.
    # After the loop ends, the final print() runs.
    #
    # {{CONTEXT_TRACE_HINT_2}}
    pass


# --- {{TRACE_3_TITLE}} ---
# {{CONTEXT_TRACE_3_NARRATIVE}}


def code_to_trace_c():
    """Study this code - don't run it yet!"""
    # Drawing segments for {{hero}}'s path
    for i in range(1, 4):
        length = i * 10
        print(f"Segment {i}: {length} units")


def trace_table_c():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # Track BOTH `i` AND `length` in each iteration.
    #
    # | Iteration | i | length (i * 10) | Output |
    # |-----------|---|-----------------|--------|
    # | 1         |   |                 |        |
    # | 2         |   |                 |        |
    # | 3         |   |                 |        |
    #
    # Hint: length is calculated INSIDE the loop, so it changes
    # based on the current value of i.
    #
    # {{CONTEXT_TRACE_HINT_3}}
    pass


# --- {{TRACE_4_TITLE}} ---
# {{CONTEXT_TRACE_4_NARRATIVE}}


def code_to_trace_d():
    """Study this code - don't run it yet!"""
    # Calculating angles for shapes at {{place}}
    for sides in range(3, 6):
        angle = 360 // sides
        print(f"{sides} sides: turn {angle} degrees")


def trace_table_d():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # Track `sides` and `angle` in each iteration.
    # Remember: // is integer division (no decimals).
    #
    # | Iteration | sides | angle (360 // sides) | Output |
    # |-----------|-------|----------------------|--------|
    # | 1         |       |                      |        |
    # | 2         |       |                      |        |
    # | 3         |       |                      |        |
    #
    # Hint: 360 // 3 = 120, 360 // 4 = 90, 360 // 5 = 72
    #
    # {{CONTEXT_TRACE_HINT_4}}
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
