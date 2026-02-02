# =============================================================================
# Output Prediction: Arithmetic
# =============================================================================
# Difficulty: 2-3
# Concepts: arithmetic operators, order of operations, integer vs float division
# =============================================================================

"""
{{CONTEXT_PREDICTION_INTRO}}
{{CONTEXT_PREDICTION_PURPOSE}}
"""


# --- {{CHALLENGE_1_TITLE}} ---
# {{CONTEXT_CHALLENGE_1_NARRATIVE}}


def challenge_a_code():
    """DO NOT MODIFY - Just read and predict"""
    gold = 100
    spent = 25
    remaining = gold - spent
    print(remaining)


def challenge_a_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Output: _______________
    #
    # Hint: Subtraction works just like in math.
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_1}}
    pass


# --- {{CHALLENGE_2_TITLE}} ---
# {{CONTEXT_CHALLENGE_2_NARRATIVE}}


def challenge_b_code():
    """DO NOT MODIFY - Just read and predict"""
    items = 3
    price = 10
    total = items * price
    print("Total cost:", total)


def challenge_b_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Output: _______________
    #
    # Hint: The * symbol means multiplication.
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_2}}
    pass


# --- {{CHALLENGE_3_TITLE}} ---
# {{CONTEXT_CHALLENGE_3_NARRATIVE}}


def challenge_c_code():
    """DO NOT MODIFY - Just read and predict"""
    cookies = 10
    people = 3
    each_gets = cookies // people
    leftover = cookies % people
    print("Each person gets:", each_gets)
    print("Leftover:", leftover)


def challenge_c_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Line 1: _______________
    # Line 2: _______________
    #
    # Hint: // gives the whole number part of division.
    # % gives the remainder after division.
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_3}}
    pass


# --- {{CHALLENGE_4_TITLE}} ---
# {{CONTEXT_CHALLENGE_4_NARRATIVE}}


def challenge_d_code():
    """DO NOT MODIFY - Just read and predict"""
    base = 2
    power = base ** 3
    print(power)


def challenge_d_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Output: _______________
    #
    # Hint: ** means exponentiation (power).
    # 2 ** 3 means 2 * 2 * 2
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_4}}
    pass


# --- {{CHALLENGE_5_TITLE}} ---
# {{CONTEXT_CHALLENGE_5_NARRATIVE}}


def challenge_e_code():
    """DO NOT MODIFY - Just read and predict"""
    result = 2 + 3 * 4
    print(result)


def challenge_e_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Output: _______________
    #
    # Hint: Python follows math order of operations.
    # Multiplication happens before addition.
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_5}}
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

    print("\n=== {{CHALLENGE_4_TITLE}} ===")
    print("-- Actual Output --")
    challenge_d_code()
    print("\n-- Your Prediction --")
    challenge_d_prediction()

    print("\n=== {{CHALLENGE_5_TITLE}} ===")
    print("-- Actual Output --")
    challenge_e_code()
    print("\n-- Your Prediction --")
    challenge_e_prediction()

    print("\n" + "=" * 50)
    print("{{CONTEXT_VERIFICATION_COMPLETE}}")


main()
