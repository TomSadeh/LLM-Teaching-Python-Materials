# =============================================================================
# Write Code: Variables
# =============================================================================
# Difficulty: 2
# Concepts: variable creation, assignment, using variables in print
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
    # Create a variable called `hero_name` and store "{{hero}}" in it.
    # Then print the variable.
    #
    # Step 1: Create the variable: hero_name = "{{hero}}"
    # Step 2: Print it: print(hero_name)
    #
    # Expected output: {{hero}}
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create two variables and print them together.
    #
    # Step 1: Create a variable `location` with value "{{school}}"
    # Step 2: Create a variable `activity` with value "learning Python"
    # Step 3: Print both using: print(location, "-", activity)
    #
    # Expected output: {{school}} - learning Python
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create variables for {{hero}}'s inventory.
    #
    # Step 1: Create `item_name` with value "{{item}}"
    # Step 2: Create `item_count` with value 3 (a number, no quotes!)
    # Step 3: Print a message like: "{{hero}} has 3 {{item}}s"
    #         Use: print("{{hero}} has", item_count, item_name + "s")
    #
    # Expected output: {{hero}} has 3 {{item}}s
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Update a variable's value.
    #
    # Step 1: Create `level` with value 1
    # Step 2: Print "Starting level:" followed by the level variable
    # Step 3: Change `level` to 2 (assign a new value)
    # Step 4: Print "New level:" followed by the level variable
    #
    # Expected output:
    # Starting level: 1
    # New level: 2
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
