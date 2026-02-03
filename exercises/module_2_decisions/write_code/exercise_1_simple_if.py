# =============================================================================
# Write Code: Simple if Statements
# =============================================================================
# Difficulty: 1
# Concepts: Basic if statement, conditional execution, indentation
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
    # {{hero}} is training at {{school}}.
    # Write an if statement that checks if their energy level is above 50.
    #
    # Step 1: Create a variable called energy with the value 75
    # Step 2: Write an if statement: if energy > 50:
    # Step 3: Inside the if block, print "{{hero}} is ready to train!"
    #
    # Hint: Remember the colon after the condition and indent the print.
    #
    # Expected output when energy is 75:
    #   {{hero}} is ready to train!
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
    # {{hero}} found a {{item}} with a certain value.
    # Check if the value is high enough to keep.
    #
    # Step 1: Create a variable called item_value with the value 120
    # Step 2: Print f"Found {{item}} worth {item_value} gold"
    # Step 3: Write an if statement: if item_value > 100:
    # Step 4: Inside the if block, print "This {{item}} is valuable!"
    # Step 5: After the if block (no indent), print "Search complete."
    #
    # Expected output when item_value is 120:
    #   Found {{item}} worth 120 gold
    #   This {{item}} is valuable!
    #   Search complete.
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
    # {{hero}} is checking their health before a mission.
    # Multiple actions can happen when a condition is true.
    #
    # Step 1: Create a variable called health with the value 80
    # Step 2: Create a variable called min_health with the value 60
    # Step 3: Write an if statement: if health > min_health:
    # Step 4: Inside the if block, print two lines:
    #         "Health check passed!"
    #         "{{hero}} can proceed to {{location}}."
    # Step 5: After the if block, print f"Current health: {health}"
    #
    # Hint: Both print statements inside the if need to be indented.
    #
    # Expected output when health is 80:
    #   Health check passed!
    #   {{hero}} can proceed to {{location}}.
    #   Current health: 80
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
    # {{mentor}} is testing {{hero}}'s knowledge.
    # Check if the answer is correct using == (equality).
    #
    # Step 1: Create a variable called answer with the value 42
    # Step 2: Create a variable called correct_answer with the value 42
    # Step 3: Print "Checking your answer..."
    # Step 4: Write an if statement: if answer == correct_answer:
    # Step 5: Inside the if block, print "{{exclamation}} Correct!"
    #
    # Hint: Use == to check if two values are equal (not =).
    #
    # Expected output when both are 42:
    #   Checking your answer...
    #   {{exclamation}} Correct!
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
