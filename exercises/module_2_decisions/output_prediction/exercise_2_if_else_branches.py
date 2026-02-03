# =============================================================================
# Output Prediction: if/else Branches
# =============================================================================
# Difficulty: 2
# Concepts: if/else, two-branch decisions, mutual exclusion
# =============================================================================

"""
{{CONTEXT_PREDICTION_INTRO}}
{{CONTEXT_PREDICTION_PURPOSE}}
"""


# --- {{CHALLENGE_1_TITLE}} ---
# {{CONTEXT_CHALLENGE_1_NARRATIVE}}
# With if/else, exactly ONE branch executes.

def challenge_a_code():
    """DO NOT MODIFY - Just read and predict"""
    age = 15
    if age >= 18:
        print("{{hero}} is an adult")
    else:
        print("{{hero}} is still training")


def challenge_a_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Line 1: _______________
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_1}}
    # Hint: Is 15 >= 18? If no, the else branch runs instead.
    pass


# --- {{CHALLENGE_2_TITLE}} ---
# {{CONTEXT_CHALLENGE_2_NARRATIVE}}
# Watch what happens before and after the if/else.

def challenge_b_code():
    """DO NOT MODIFY - Just read and predict"""
    score = 85
    print("Checking score...")
    if score >= 70:
        print("{{hero}} passed!")
        print("{{mentor}} is proud.")
    else:
        print("{{hero}} needs more practice.")
    print("Result recorded.")


def challenge_b_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Line 1: _______________
    # Line 2: _______________
    # Line 3: _______________
    # Line 4: _______________
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_2}}
    # Hint: Code before if and after else always runs. Only ONE branch runs.
    pass


# --- {{CHALLENGE_3_TITLE}} ---
# {{CONTEXT_CHALLENGE_3_NARRATIVE}}
# The condition uses == to check equality.

def challenge_c_code():
    """DO NOT MODIFY - Just read and predict"""
    password = "{{password}}"
    entered = "wrong"
    if password == entered:
        print("Access granted to {{location}}")
    else:
        print("Access denied!")


def challenge_c_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Line 1: _______________
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_3}}
    # Hint: Are "{{password}}" and "wrong" the same string?
    pass


# --- {{CHALLENGE_4_TITLE}} ---
# {{CONTEXT_CHALLENGE_4_NARRATIVE}}
# Variables are compared at the time the if runs.

def challenge_d_code():
    """DO NOT MODIFY - Just read and predict"""
    gold = 100
    price = 75
    if gold >= price:
        print(f"{{hero}} buys the {{item}} for {price} gold")
        gold = gold - price
    else:
        print("Not enough gold!")
    print(f"Gold remaining: {gold}")


def challenge_d_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Line 1: _______________
    # Line 2: _______________
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_4}}
    # Hint: Is 100 >= 75? What is 100 - 75?
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

    print("\n" + "=" * 50)
    print("{{CONTEXT_VERIFICATION_COMPLETE}}")


main()
