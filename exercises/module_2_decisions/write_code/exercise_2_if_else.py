# =============================================================================
# Write Code: if/else Statements
# =============================================================================
# Difficulty: 2
# Concepts: if/else, two-branch decisions, mutual exclusion
# =============================================================================

"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""

# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # {{hero}} needs to check if they can enter {{location}}.
    # Entry requires at least 100 gold.
    #
    # Step 1: Create a variable called gold with the value 150
    # Step 2: Write an if statement: if gold >= 100:
    # Step 3: Inside the if block, print "{{hero}} enters {{location}}"
    # Step 4: Add an else clause
    # Step 5: Inside the else block, print "{{hero}} cannot afford entry"
    #
    # Expected output when gold is 150:
    #   {{hero}} enters {{location}}
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # {{mentor}} is grading {{hero}}'s exam.
    # A score of 60 or higher is passing.
    #
    # Step 1: Create a variable called score with the value 55
    # Step 2: Print f"{{hero}}'s score: {score}"
    # Step 3: Write an if/else to check if score >= 60
    # Step 4: If true, print "Congratulations! You passed!"
    # Step 5: Else, print "Keep practicing. You'll get it next time!"
    # Step 6: After the if/else, print "{{mentor}} records the result."
    #
    # Expected output when score is 55:
    #   {{hero}}'s score: 55
    #   Keep practicing. You'll get it next time!
    #   {{mentor}} records the result.
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # Check if {{hero}} knows the password to enter {{school}}.
    # Use == to compare strings.
    #
    # Step 1: Create a variable called secret with the value "{{password}}"
    # Step 2: Create a variable called attempt with the value "{{password}}"
    # Step 3: Write an if/else to check if attempt == secret
    # Step 4: If true, print "{{greeting}}"
    # Step 5: Else, print "Access denied. Incorrect password."
    #
    # Expected output when passwords match:
    #   {{greeting}}
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # {{hero}} wants to buy a {{item}} that costs 80 gold.
    # Update gold if purchase is successful.
    #
    # Step 1: Create a variable called gold with the value 100
    # Step 2: Create a variable called price with the value 80
    # Step 3: Print f"{{hero}} has {gold} gold"
    # Step 4: Write an if/else to check if gold >= price
    # Step 5: If true:
    #         - Subtract price from gold: gold = gold - price
    #         - Print "Purchased {{item}}!"
    # Step 6: Else:
    #         - Print "Not enough gold!"
    # Step 7: After if/else, print f"Remaining gold: {gold}"
    #
    # Expected output when gold is 100 and price is 80:
    #   {{hero}} has 100 gold
    #   Purchased {{item}}!
    #   Remaining gold: 20
    pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)

    print("\n=== {{PHASE_1_TITLE}} ===")
    exercise_a()

    print("\n=== {{PHASE_2_TITLE}} ===")
    exercise_b()

    print("\n=== {{PHASE_3_TITLE}} ===")
    exercise_c()

    print("\n=== {{PHASE_4_TITLE}} ===")
    exercise_d()

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
