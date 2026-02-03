# =============================================================================
# Code Tracing: if/elif/else Chains
# =============================================================================
# Difficulty: 3
# Concepts: if/elif/else, first match wins, order matters
# =============================================================================

"""
{{CONTEXT_CODE_TRACING_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# --- {{TRACE_1_TITLE}} ---
# {{CONTEXT_TRACE_1_NARRATIVE}}
# Only ONE branch executes in an if/elif/else chain.

def code_to_trace_a():
    """Study this code - don't run it yet!"""
    score = 85
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"{{hero}}'s grade: {grade}")


def trace_table_a():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # {{CONTEXT_TRACE_HINT_1}}
    #
    # | Condition | Check | Result |
    # |-----------|-------|--------|
    # | score >= 90 | 85 >= 90 | _____ |
    # | score >= 80 | 85 >= 80 | _____ |
    # | score >= 70 | (skipped because above matched) | - |
    # | else | (skipped because above matched) | - |
    #
    # Which branch executed? _______________
    # What is grade? _______________
    # What gets printed? _______________
    #
    # Key insight: Once a condition is True, we skip all remaining branches!
    pass


# --- {{TRACE_2_TITLE}} ---
# {{CONTEXT_TRACE_2_NARRATIVE}}
# The order of conditions matters!

def code_to_trace_b():
    """Study this code - don't run it yet!"""
    temperature = 35
    if temperature >= 30:
        status = "Hot"
    elif temperature >= 20:
        status = "Warm"
    elif temperature >= 10:
        status = "Cool"
    else:
        status = "Cold"
    print(f"Weather at {{location}}: {status}")


def trace_table_b():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # {{CONTEXT_TRACE_HINT_2}}
    #
    # | Condition | Check | Result |
    # |-----------|-------|--------|
    # | temperature >= 30 | 35 >= 30 | _____ |
    # | temperature >= 20 | (checked/skipped?) | _____ |
    # | temperature >= 10 | (checked/skipped?) | _____ |
    # | else | (checked/skipped?) | _____ |
    #
    # What is status? _______________
    # What gets printed? _______________
    #
    # Note: 35 is also >= 20 and >= 10, but we stop at first match!
    pass


# --- {{TRACE_3_TITLE}} ---
# {{CONTEXT_TRACE_3_NARRATIVE}}
# Trace when none of the if/elif match (else runs).

def code_to_trace_c():
    """Study this code - don't run it yet!"""
    level = 3
    if level == 10:
        rank = "Master"
    elif level == 7:
        rank = "Expert"
    elif level == 5:
        rank = "Intermediate"
    else:
        rank = "Beginner"
    print(f"{{hero}}'s rank: {rank}")


def trace_table_c():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # {{CONTEXT_TRACE_HINT_3}}
    #
    # | Condition | Check | Result |
    # |-----------|-------|--------|
    # | level == 10 | 3 == 10 | _____ |
    # | level == 7 | 3 == 7 | _____ |
    # | level == 5 | 3 == 5 | _____ |
    # | else | (all above were False) | executes |
    #
    # What is rank? _______________
    # What gets printed? _______________
    #
    # Key insight: else only runs if ALL if/elif conditions are False.
    pass


# --- {{TRACE_4_TITLE}} ---
# {{CONTEXT_TRACE_4_NARRATIVE}}
# Trace with variables that change before the check.

def code_to_trace_d():
    """Study this code - don't run it yet!"""
    gold = 100
    gold = gold + 50  # {{hero}} finds treasure!
    if gold >= 200:
        tier = "Rich"
    elif gold >= 100:
        tier = "Comfortable"
    elif gold >= 50:
        tier = "Modest"
    else:
        tier = "Poor"
    print(f"{{hero}} with {gold} gold: {tier}")


def trace_table_d():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # {{CONTEXT_TRACE_HINT_4}}
    #
    # | Step | gold | Action |
    # |------|------|--------|
    # | 1    | 100  | Initialize gold |
    # | 2    | ___  | Add 50 to gold |
    #
    # Now check conditions with gold = ___:
    # | Condition | Check | Result |
    # |-----------|-------|--------|
    # | gold >= 200 | ___ >= 200 | _____ |
    # | gold >= 100 | ___ >= 100 | _____ |
    # | (rest skipped?) | | |
    #
    # What is tier? _______________
    # What gets printed? _______________
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
