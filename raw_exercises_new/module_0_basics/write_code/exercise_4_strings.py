# =============================================================================
# Write Code: Strings
# =============================================================================
# Difficulty: 3
# Concepts: string creation, concatenation, combining with print
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
    # Create a welcome message for {{school}}.
    #
    # Step 1: Create a variable `school` with value "{{school}}"
    # Step 2: Create a variable `message` that combines "Welcome to " with school
    #         Use the + operator: message = "Welcome to " + school
    # Step 3: Print the message
    #
    # Expected output: Welcome to {{school}}
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a greeting for {{hero}} at {{school}}.
    #
    # Step 1: Create `hero` with value "{{hero}}"
    # Step 2: Create `location` with value "{{school}}"
    # Step 3: Print using commas: print(hero, "is studying at", location)
    #
    # Hint: Commas automatically add spaces between items.
    #
    # Expected output: {{hero}} is studying at {{school}}
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Build {{hero}}'s {{item}} description.
    #
    # Step 1: Create `item` with value "{{item}}"
    # Step 2: Create `color` with value "golden"
    # Step 3: Create `description` by combining: "a " + color + " " + item
    # Step 4: Print: "{{hero}} found" followed by description
    #
    # Expected output: {{hero}} found a golden {{item}}
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Mix strings and numbers in output.
    #
    # Step 1: Create `hero` with value "{{hero}}"
    # Step 2: Create `level` with value 5 (a number, no quotes!)
    # Step 3: Print using commas: print(hero, "reached level", level)
    #
    # Note: Using commas in print() handles the number automatically.
    # You don't need to convert it to a string!
    #
    # Expected output: {{hero}} reached level 5
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
