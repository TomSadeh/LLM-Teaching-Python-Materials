# =============================================================================
# Write Code: f-strings
# =============================================================================
# Difficulty: 4
# Concepts: f-string syntax, expressions in f-strings, formatting
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
    # Create a greeting using an f-string.
    #
    # Step 1: Create `name` with value "{{hero}}"
    # Step 2: Create `message` using an f-string: f"Hello, {name}!"
    # Step 3: Print the message
    #
    # Hint: The f goes before the opening quote: f"..."
    # Variables go inside {curly braces}
    #
    # Expected output: Hello, {{hero}}!
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a status line using multiple variables in an f-string.
    #
    # Step 1: Create `hero` with value "{{hero}}"
    # Step 2: Create `location` with value "{{school}}"
    # Step 3: Create `level` with value 5
    # Step 4: Print an f-string: f"{hero} is at {location}, level {level}"
    #
    # Expected output: {{hero}} is at {{school}}, level 5
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Use expressions inside an f-string.
    #
    # Step 1: Create `base_price` with value 25
    # Step 2: Create `quantity` with value 4
    # Step 3: Print an f-string that calculates the total:
    #         f"Total cost: {base_price * quantity}"
    #
    # Hint: You can do math inside the {braces}!
    #
    # Expected output: Total cost: 100
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create {{hero}}'s character sheet using f-strings.
    #
    # Step 1: Create `name` with value "{{hero}}"
    # Step 2: Create `class_type` with value "Apprentice"
    # Step 3: Create `health` with value 100
    # Step 4: Create `attack` with value 15
    # Step 5: Create `defense` with value 10
    # Step 6: Print f"=== {name} the {class_type} ==="
    # Step 7: Print f"HP: {health} | ATK: {attack} | DEF: {defense}"
    # Step 8: Print f"Power Rating: {attack + defense}"
    #
    # Expected output:
    # === {{hero}} the Apprentice ===
    # HP: 100 | ATK: 15 | DEF: 10
    # Power Rating: 25
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
