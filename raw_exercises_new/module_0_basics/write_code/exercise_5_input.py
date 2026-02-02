# =============================================================================
# Write Code: Input
# =============================================================================
# Difficulty: 3-4
# Concepts: input(), type conversion, interactive programs
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
    # Get {{hero}}'s name and greet them.
    #
    # Step 1: Use input() to ask "What is your name? " and store in `name`
    # Step 2: Print "Welcome to {{school}}," followed by name
    #
    # Example interaction:
    # What is your name? Maya
    # Welcome to {{school}}, Maya
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Calculate the total cost of {{item}}s.
    #
    # Step 1: Use input() to ask "How many {{item}}s? " and store in `quantity_text`
    # Step 2: Convert quantity_text to an integer: quantity = int(quantity_text)
    # Step 3: Create `price` with value 10
    # Step 4: Create `total` = quantity * price
    # Step 5: Print "Total cost:" followed by total
    #
    # Example interaction:
    # How many {{item}}s? 5
    # Total cost: 50
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a character stats calculator.
    #
    # Step 1: Ask "Enter strength: " and convert to int, store in `strength`
    # Step 2: Ask "Enter defense: " and convert to int, store in `defense`
    # Step 3: Calculate `power` = strength * 2 + defense
    # Step 4: Print "Power level:" followed by power
    #
    # Tip: You can combine int() and input():
    #      strength = int(input("Enter strength: "))
    #
    # Example interaction:
    # Enter strength: 10
    # Enter defense: 5
    # Power level: 25
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a personalized {{school}} ID card.
    #
    # Step 1: Ask "Student name: " and store in `name`
    # Step 2: Ask "Student age: " and convert to int, store in `age`
    # Step 3: Ask "Favorite subject: " and store in `subject`
    # Step 4: Print "=== {{school}} ID ==="
    # Step 5: Print "Name:" followed by name
    # Step 6: Print "Age:" followed by age
    # Step 7: Print "Specialty:" followed by subject
    #
    # Example interaction:
    # Student name: {{hero}}
    # Student age: 12
    # Favorite subject: Coding
    # === {{school}} ID ===
    # Name: {{hero}}
    # Age: 12
    # Specialty: Coding
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
