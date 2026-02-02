# =============================================================================
# TEMPLATE: Output Prediction
# =============================================================================
#
# PURPOSE: Students predict what code will print WITHOUT running it.
# SKILL: Mental execution, understanding program flow
#
# STRUCTURE:
#   - Show complete, runnable code
#   - Student writes what they think will be printed
#   - Verification section (commented out) to check answers
#
# GUIDELINES:
#   - Code should be SHORT (5-15 lines per challenge)
#   - Include a mix of: obvious outputs, tricky edge cases, common misconceptions
#   - Good topics: loops with counters, string operations, conditional branches,
#     list mutations, function return vs print, off-by-one scenarios
#   - Avoid: overly complex nested logic (save for advanced), external dependencies
#
# DIFFICULTY SCALING:
#   - Easy: Linear code, simple loops, basic string/math
#   - Medium: Conditionals inside loops, multiple variables interacting
#   - Hard: Nested loops, mutable state, recursion
#
# =============================================================================
# CONTEXT BLOCKS TO USE:
# =============================================================================
#
# Docstring/Introduction:
#   {{CONTEXT_PREDICTION_INTRO}}     - Main intro for prediction exercises
#   {{CONTEXT_PREDICTION_PURPOSE}}   - Why prediction matters
#
# Per-Challenge:
#   {{CHALLENGE_N_TITLE}}            - Title for challenge N (1, 2, 3...)
#   {{CONTEXT_CHALLENGE_N_NARRATIVE}} - Story/context for challenge N
#   {{CONTEXT_PREDICTION_GUIDANCE_N}} - Hint for challenge N
#
# Closing:
#   {{CONTEXT_VERIFICATION_COMPLETE}} - Completion message
#
# Layer 1 entities (use within explanatory text):
#   {{hero}}, {{school}}, {{spell1}}, {{item}}, etc.
#
# =============================================================================

"""
{{CONTEXT_PREDICTION_INTRO}}
{{CONTEXT_PREDICTION_PURPOSE}}
"""


# --- {{CHALLENGE_1_TITLE}} ---
# {{CONTEXT_CHALLENGE_1_NARRATIVE}}

def challenge_a_code():
    """DO NOT MODIFY - Just read and predict"""
    # [ACTUAL CODE HERE]
    # - Should produce interesting/non-obvious output
    # - Should test a specific concept or common pitfall
    pass


def challenge_a_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Line 1: _______________
    # Line 2: _______________
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_1}}
    pass


# --- {{CHALLENGE_2_TITLE}} ---
# {{CONTEXT_CHALLENGE_2_NARRATIVE}}

def challenge_b_code():
    """DO NOT MODIFY - Just read and predict"""
    pass


def challenge_b_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_2}}
    pass


# [REPEAT PATTERN FOR CHALLENGES C, D, ETC.]


def main():
    print("=== {{CHALLENGE_1_TITLE}} ===")
    print("-- Actual Output --")
    challenge_a_code()
    print("\n-- Your Prediction --")
    challenge_a_prediction()

    print("\n=== {{CHALLENGE_2_TITLE}} ===")
    print("-- Actual Output --")
    challenge_b_code()
    print("\n-- Your Prediction --")
    challenge_b_prediction()

    print("\n" + "=" * 50)
    print("{{CONTEXT_VERIFICATION_COMPLETE}}")


main()


# =============================================================================
# EXAMPLE CONCEPTS TO BUILD CHALLENGES AROUND:
# =============================================================================
#
# BEGINNER:
#   - print() with different data types
#   - String concatenation vs comma separation in print
#   - Basic for loop iteration counts
#   - range() start/stop/step behavior
#
# INTERMEDIATE:
#   - Loop variable scope after loop ends
#   - Mutable default arguments
#   - String immutability (method returns new string)
#   - Integer division vs float division
#   - Short-circuit evaluation in and/or
#
# ADVANCED:
#   - List aliasing vs copying
#   - Nested loop iteration order
#   - Generator exhaustion
#   - Exception handling flow
#
# =============================================================================
