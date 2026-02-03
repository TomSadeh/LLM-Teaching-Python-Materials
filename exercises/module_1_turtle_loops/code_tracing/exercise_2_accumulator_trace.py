# =============================================================================
# Code Tracing: Accumulator Trace
# =============================================================================
# Difficulty: 4
# Concepts: tracking accumulator values, running totals through iterations
# =============================================================================

"""
{{CONTEXT_CODE_TRACING_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# --- {{TRACE_1_TITLE}} ---
# {{CONTEXT_TRACE_1_NARRATIVE}}


def code_to_trace_a():
    """Study this code - don't run it yet!"""
    # {{hero}} calculates total energy at {{school}}
    total = 0
    for i in range(1, 4):
        total = total + i
        print(f"After adding {i}: total = {total}")


def trace_table_a():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # Track `i` and `total` through each iteration.
    #
    # | Before/After | i | total (before) | total (after) | Output |
    # |--------------|---|----------------|---------------|--------|
    # | Start        | - | 0              | -             | -      |
    # | Iteration 1  |   |                |               |        |
    # | Iteration 2  |   |                |               |        |
    # | Iteration 3  |   |                |               |        |
    #
    # Hint: total starts at 0. Each iteration, we add i to total.
    # range(1, 4) gives: 1, 2, 3
    #
    # {{CONTEXT_TRACE_HINT_1}}
    pass


# --- {{TRACE_2_TITLE}} ---
# {{CONTEXT_TRACE_2_NARRATIVE}}


def code_to_trace_b():
    """Study this code - don't run it yet!"""
    # Calculating distances for {{creature}}
    distance = 0
    for step in range(1, 5):
        move = step * 10
        distance = distance + move
        print(f"Step {step}: moved {move}, total distance = {distance}")


def trace_table_b():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # Track `step`, `move`, and `distance`.
    #
    # | Iteration | step | move (step*10) | distance (before) | distance (after) |
    # |-----------|------|----------------|-------------------|------------------|
    # | Start     | -    | -              | 0                 | -                |
    # | 1         |      |                |                   |                  |
    # | 2         |      |                |                   |                  |
    # | 3         |      |                |                   |                  |
    # | 4         |      |                |                   |                  |
    #
    # Hint: move is calculated each iteration, distance accumulates.
    #
    # {{CONTEXT_TRACE_HINT_2}}
    pass


# --- {{TRACE_3_TITLE}} ---
# {{CONTEXT_TRACE_3_NARRATIVE}}


def code_to_trace_c():
    """Study this code - don't run it yet!"""
    # Tracking angles at {{location}}
    total_angle = 0
    for side in range(4):
        turn = 90
        total_angle = total_angle + turn
        print(f"After side {side}: turned {total_angle} degrees total")


def trace_table_c():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # Track `side` and `total_angle`.
    #
    # | Iteration | side | turn | total_angle (before) | total_angle (after) |
    # |-----------|------|------|----------------------|---------------------|
    # | Start     | -    | -    | 0                    | -                   |
    # | 1         |      | 90   |                      |                     |
    # | 2         |      | 90   |                      |                     |
    # | 3         |      | 90   |                      |                     |
    # | 4         |      | 90   |                      |                     |
    #
    # Hint: Note that side starts at 0 (from range(4): 0, 1, 2, 3)
    # turn is always 90, total_angle grows by 90 each time.
    #
    # {{CONTEXT_TRACE_HINT_3}}
    pass


# --- {{TRACE_4_TITLE}} ---
# {{CONTEXT_TRACE_4_NARRATIVE}}


def code_to_trace_d():
    """Study this code - don't run it yet!"""
    # Building a message for {{hero}} at {{place}}
    message = ""
    for count in range(1, 4):
        message = message + str(count) + "! "
        print(f"Message so far: '{message}'")


def trace_table_d():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # Track `count` and `message`.
    #
    # | Iteration | count | message (before) | message (after) |
    # |-----------|-------|------------------|-----------------|
    # | Start     | -     | ""               | -               |
    # | 1         |       |                  |                 |
    # | 2         |       |                  |                 |
    # | 3         |       |                  |                 |
    #
    # Hint: Strings can be accumulated too!
    # Each iteration adds: str(count) + "! "
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
