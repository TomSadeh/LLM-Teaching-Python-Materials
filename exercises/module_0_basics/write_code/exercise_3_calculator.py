# =============================================================================
# Write Code: Calculator
# =============================================================================
# Difficulty: 2-3
# Concepts: arithmetic operators (+, -, *, /, //, %, **)
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
    # Calculate the total cost of {{item}}s at {{school}}.
    #
    # Step 1: Create a variable `price` with value 15
    # Step 2: Create a variable `quantity` with value 4
    # Step 3: Create a variable `total` that multiplies price by quantity
    # Step 4: Print "Total cost:" followed by the total variable
    #
    # Expected output: Total cost: 60
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Calculate how to divide {{item}}s among {{hero}}'s friends.
    #
    # Step 1: Create `items` with value 17
    # Step 2: Create `friends` with value 5
    # Step 3: Create `each_gets` using // (integer division)
    # Step 4: Create `leftover` using % (remainder)
    # Step 5: Print "Each friend gets:" followed by each_gets
    # Step 6: Print "Leftover:" followed by leftover
    #
    # Expected output:
    # Each friend gets: 3
    # Leftover: 2
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Calculate {{hero}}'s power level at {{school}}.
    #
    # Step 1: Create `base_power` with value 2
    # Step 2: Create `level` with value 5
    # Step 3: Create `total_power` using ** (exponentiation): base_power ** level
    # Step 4: Print "Power level:" followed by total_power
    #
    # Hint: 2 ** 5 means 2 * 2 * 2 * 2 * 2
    #
    # Expected output: Power level: 32
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Calculate {{hero}}'s score with bonuses.
    #
    # Step 1: Create `base_score` with value 100
    # Step 2: Create `bonus` with value 25
    # Step 3: Create `penalty` with value 10
    # Step 4: Create `final_score` = base_score + bonus - penalty
    # Step 5: Print "Final score:" followed by final_score
    #
    # Expected output: Final score: 115
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
