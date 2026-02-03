# =============================================================================
# Output Prediction: Simple if Statements
# =============================================================================
# Difficulty: 1
# Concepts: Basic if statement, conditional execution
# =============================================================================

"""
{{CONTEXT_PREDICTION_INTRO}}
{{CONTEXT_PREDICTION_PURPOSE}}
"""


# --- {{CHALLENGE_1_TITLE}} ---
# {{CONTEXT_CHALLENGE_1_NARRATIVE}}
# Does the code inside the if block execute?

def challenge_a_code():
    """DO NOT MODIFY - Just read and predict"""
    power_level = 100
    if power_level > 50:
        print("{{hero}} is strong enough!")


def challenge_a_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Line 1: _______________
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_1}}
    # Hint: Is 100 > 50? If yes, the print statement runs.
    pass


# --- {{CHALLENGE_2_TITLE}} ---
# {{CONTEXT_CHALLENGE_2_NARRATIVE}}
# Will anything be printed when the condition is False?

def challenge_b_code():
    """DO NOT MODIFY - Just read and predict"""
    score = 30
    if score > 50:
        print("{{hero}} passed the test!")
    print("The test is complete.")


def challenge_b_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Line 1: _______________
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_2}}
    # Hint: Is 30 > 50? The code AFTER the if block always runs.
    pass


# --- {{CHALLENGE_3_TITLE}} ---
# {{CONTEXT_CHALLENGE_3_NARRATIVE}}
# Pay attention to what's inside vs outside the if block.

def challenge_c_code():
    """DO NOT MODIFY - Just read and predict"""
    points = 75
    print(f"{{hero}} earned {points} points")
    if points > 60:
        print("That's a good score!")
        print("{{mentor}} is pleased.")
    print("Training session ended.")


def challenge_c_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Line 1: _______________
    # Line 2: _______________
    # Line 3: _______________
    # Line 4: _______________
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_3}}
    # Hint: Count carefully - how many print statements are INSIDE the if?
    pass


# --- {{CHALLENGE_4_TITLE}} ---
# {{CONTEXT_CHALLENGE_4_NARRATIVE}}
# Variables can be compared to each other too.

def challenge_d_code():
    """DO NOT MODIFY - Just read and predict"""
    hero_strength = 45
    required_strength = 50
    if hero_strength > required_strength:
        print("{{hero}} can enter {{location}}!")
    print(f"Strength: {hero_strength}/{required_strength}")


def challenge_d_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    # Write EXACTLY what you think will be printed above.
    #
    # Line 1: _______________
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_4}}
    # Hint: Compare the two numbers - is 45 > 50?
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
