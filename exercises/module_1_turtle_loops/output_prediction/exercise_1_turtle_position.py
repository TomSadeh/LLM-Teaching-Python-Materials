# =============================================================================
# Output Prediction: Turtle Position
# =============================================================================
# Difficulty: 1
# Concepts: turtle movement, direction, forward(), backward(), right(), left()
# =============================================================================

"""
{{CONTEXT_PREDICTION_INTRO}}
{{CONTEXT_PREDICTION_PURPOSE}}
"""

import turtle


# --- {{CHALLENGE_1_TITLE}} ---
# {{CONTEXT_CHALLENGE_1_NARRATIVE}}


def challenge_a_code():
    """DO NOT MODIFY - Just read and predict"""
    # {{hero}} commands the {{creature}} to move forward
    t = turtle.Turtle()
    t.forward(100)
    t.forward(50)
    print(f"Final X position: {t.xcor()}")


def challenge_a_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    # The turtle starts at position (0, 0) facing right (East).
    # After moving forward 100, it's at (100, 0).
    # After moving forward 50 more, where is it?
    #
    # Final X position: _______________
    #
    # Hint: forward() adds to the position in the direction the turtle faces.
    # The turtle starts facing right, so forward moves right (increases X).
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_1}}
    pass


# --- {{CHALLENGE_2_TITLE}} ---
# {{CONTEXT_CHALLENGE_2_NARRATIVE}}


def challenge_b_code():
    """DO NOT MODIFY - Just read and predict"""
    # Navigating through {{location}}
    t = turtle.Turtle()
    t.forward(80)
    t.backward(30)
    print(f"Final X position: {t.xcor()}")


def challenge_b_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    # Starting at (0, 0), facing right:
    # - forward(80) moves to X = ?
    # - backward(30) moves back, so X = ?
    #
    # Final X position: _______________
    #
    # Hint: backward() moves in the OPPOSITE direction the turtle faces,
    # but the turtle keeps facing the same way.
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_2}}
    pass


# --- {{CHALLENGE_3_TITLE}} ---
# {{CONTEXT_CHALLENGE_3_NARRATIVE}}


def challenge_c_code():
    """DO NOT MODIFY - Just read and predict"""
    # Charting a path to {{place}}
    t = turtle.Turtle()
    t.right(90)
    t.forward(60)
    print(f"Final Y position: {t.ycor()}")


def challenge_c_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    # The turtle starts facing right (East).
    # right(90) turns it 90 degrees clockwise - now facing which direction?
    # Then forward(60) moves it 60 units in that direction.
    #
    # Final Y position: _______________
    #
    # Hint: Turning right from East points you South.
    # In turtle graphics, South means Y decreases (negative Y direction).
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_3}}
    pass


# --- {{CHALLENGE_4_TITLE}} ---
# {{CONTEXT_CHALLENGE_4_NARRATIVE}}


def challenge_d_code():
    """DO NOT MODIFY - Just read and predict"""
    # A journey around {{school}}
    t = turtle.Turtle()
    t.forward(50)
    t.left(90)
    t.forward(50)
    print(f"Position: ({t.xcor()}, {t.ycor()})")


def challenge_d_prediction():
    # ✏️ YOUR PREDICTION HERE ✏️
    # Starting at (0, 0), facing right (East):
    # - forward(50) moves to position (?, ?)
    # - left(90) turns 90 degrees counter-clockwise - now facing ?
    # - forward(50) moves to position (?, ?)
    #
    # Position: (_____, _____)
    #
    # Hint: Turning left from East points you North.
    # North means Y increases (positive Y direction).
    #
    # {{CONTEXT_PREDICTION_GUIDANCE_4}}
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
    turtle.done()


main()
