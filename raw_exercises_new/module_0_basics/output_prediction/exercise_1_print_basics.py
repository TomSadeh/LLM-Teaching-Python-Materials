# =============================================================================
# Output Prediction: Print Basics
# =============================================================================
# Difficulty: 1
# Concepts: print() function, string literals, commas in print
# =============================================================================

"""
{{CONTEXT_PREDICTION_INTRO}}
{{CONTEXT_PREDICTION_PURPOSE}}
"""


# --- {{CHALLENGE_1_TITLE}} ---
# {{CONTEXT_CHALLENGE_1_NARRATIVE}}


def challenge_a_code():
    """DO NOT MODIFY - Just read and predict"""
    print("Hello, world!")
    print("Welcome to {{school}}")


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
    print("{{hero}}", "is learning")
    print("Python" + " programming")


def challenge_b_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Line 1: _______________
    # Line 2: _______________
    #
    # Hint: Notice the difference between comma (,) and plus (+).
    # Comma adds a space between items, plus joins them directly.
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_2}}
    pass


# --- {{CHALLENGE_3_TITLE}} ---
# {{CONTEXT_CHALLENGE_3_NARRATIVE}}


def challenge_c_code():
    """DO NOT MODIFY - Just read and predict"""
    message = "{{greeting}}"
    print(message)
    print("message")


def challenge_c_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Line 1: _______________
    # Line 2: _______________
    #
    # Hint: Notice the difference between a variable name (no quotes)
    # and a string literal (with quotes).
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_3}}
    pass


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

    print("\n=== {{CHALLENGE_3_TITLE}} ===")
    print("-- Actual Output --")
    challenge_c_code()
    print("\n-- Your Prediction --")
    challenge_c_prediction()

    print("\n" + "=" * 50)
    print("{{CONTEXT_VERIFICATION_COMPLETE}}")


main()
