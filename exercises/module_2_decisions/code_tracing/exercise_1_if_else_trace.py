# =============================================================================
# Code Tracing: if/else Variable Tracking
# =============================================================================
# Difficulty: 2
# Concepts: if/else, tracking variable values, understanding branches
# =============================================================================

"""
{{CONTEXT_CODE_TRACING_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# --- {{TRACE_1_TITLE}} ---
# {{CONTEXT_TRACE_1_NARRATIVE}}
# Track which branch executes and how variables change.

def code_to_trace_a():
    """Study this code - don't run it yet!"""
    health = 30
    boost_amount = 50
    if health < 50:
        health = health + boost_amount
        print(f"{{hero}} recovers! Health: {health}")
    else:
        print("{{hero}} is healthy enough")
    print(f"Final health: {health}")


def trace_table_a():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # {{CONTEXT_TRACE_HINT_1}}
    #
    # | Step | health | boost_amount | Condition (health < 50) | Output |
    # |------|--------|--------------|------------------------|--------|
    # | 1    | 30     | -            | -                      | -      |
    # | 2    | 30     | 50           | -                      | -      |
    # | 3    | 30     | 50           | True                   | -      |
    # | 4    | ___    | 50           | -                      | ___    |
    # | 5    | ___    | 50           | -                      | ___    |
    #
    # Which branch executed? (if / else): _______________
    # Final value of health: _______________
    pass


# --- {{TRACE_2_TITLE}} ---
# {{CONTEXT_TRACE_2_NARRATIVE}}
# Track what happens when the condition is False.

def code_to_trace_b():
    """Study this code - don't run it yet!"""
    score = 85
    passing = 60
    result = ""
    if score < passing:
        result = "Failed"
        print(f"{{hero}} scored {score}. {result}!")
    else:
        result = "Passed"
        print(f"{{hero}} scored {score}. {result}!")
    print(f"{{mentor}} records: {result}")


def trace_table_b():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # {{CONTEXT_TRACE_HINT_2}}
    #
    # | Step | score | passing | result | Condition (score < passing) | Output |
    # |------|-------|---------|--------|----------------------------|--------|
    # | 1    | 85    | -       | -      | -                          | -      |
    # | 2    | 85    | 60      | -      | -                          | -      |
    # | 3    | 85    | 60      | ""     | -                          | -      |
    # | 4    | 85    | 60      | ""     | _____ (True/False?)        | -      |
    # | 5    | 85    | 60      | ____   | -                          | ___    |
    # | 6    | 85    | 60      | ____   | -                          | ___    |
    #
    # Which branch executed? (if / else): _______________
    # Why? _______________________________________________
    pass


# --- {{TRACE_3_TITLE}} ---
# {{CONTEXT_TRACE_3_NARRATIVE}}
# Trace a purchase decision at {{school}}.

def code_to_trace_c():
    """Study this code - don't run it yet!"""
    gold = 45
    item_cost = 50
    print(f"{{hero}} has {gold} gold")
    print(f"{{item}} costs {item_cost} gold")
    if gold >= item_cost:
        gold = gold - item_cost
        print(f"Purchased! Remaining gold: {gold}")
    else:
        needed = item_cost - gold
        print(f"Need {needed} more gold")
    print(f"{{hero}} leaves with {gold} gold")


def trace_table_c():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # {{CONTEXT_TRACE_HINT_3}}
    #
    # | Step | gold | item_cost | needed | Condition (gold >= item_cost) | Output |
    # |------|------|-----------|--------|------------------------------|--------|
    # | 1    | 45   | -         | -      | -                            | -      |
    # | 2    | 45   | 50        | -      | -                            | -      |
    # | 3    | 45   | 50        | -      | -                            | "{{hero}} has 45 gold" |
    # | 4    | 45   | 50        | -      | -                            | "{{item}} costs 50 gold" |
    # | 5    | 45   | 50        | -      | _____ (True/False?)          | -      |
    # | 6    | 45   | 50        | ___    | -                            | ___    |
    # | 7    | ___  | 50        | ___    | -                            | ___    |
    #
    # Which branch executed? (if / else): _______________
    # Final value of gold: _______________
    # Was 'needed' ever assigned? _______________
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
