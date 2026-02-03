# =============================================================================
# Write Code: Loops with Conditionals
# =============================================================================
# Difficulty: 5
# Concepts: Combining for loops with if/elif/else statements
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
    # Count how many numbers from 1 to 10 are greater than 5.
    #
    # Step 1: Create a variable called count with the value 0
    # Step 2: Use a for loop: for num in range(1, 11):
    # Step 3: Inside the loop, write an if statement:
    #         if num > 5:
    #             count = count + 1
    # Step 4: After the loop, print f"Numbers greater than 5: {count}"
    #
    # Expected output:
    #   Numbers greater than 5: 5
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
    # Print whether each number from 1 to 5 is even or odd.
    #
    # Step 1: Use a for loop: for num in range(1, 6):
    # Step 2: Inside the loop, check if num % 2 == 0 (even)
    # Step 3: If even, print f"{num} is even"
    # Step 4: Else, print f"{num} is odd"
    #
    # Hint: % is the modulo operator (remainder after division)
    #       If num % 2 == 0, the number divides evenly by 2 (even)
    #
    # Expected output:
    #   1 is odd
    #   2 is even
    #   3 is odd
    #   4 is even
    #   5 is odd
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
    # {{hero}} is checking inventory. Count valuable items (worth > 50).
    # Use a running total to track total value.
    #
    # Step 1: Create variables:
    #         item_values = [20, 75, 30, 100, 45, 80]  # Note: This is a list!
    #         valuable_count = 0
    #         total_valuable = 0
    #
    # Step 2: Use a for loop: for value in item_values:
    # Step 3: Inside the loop, check if value > 50
    # Step 4: If true:
    #         - Add 1 to valuable_count
    #         - Add value to total_valuable
    #
    # Step 5: After the loop, print:
    #         f"Found {valuable_count} valuable items"
    #         f"Total value: {total_valuable} gold"
    #
    # Note: We're iterating over a list of numbers.
    #       This is a preview of Module 3 (Lists)!
    #
    # Expected output:
    #   Found 3 valuable items
    #   Total value: 255 gold
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
    # Categorize scores using if/elif/else inside a loop.
    # Count how many A's, B's, C's, and F's.
    #
    # Step 1: Create a list of scores:
    #         scores = [95, 82, 67, 73, 88, 91, 55, 78]
    #
    # Step 2: Create counters:
    #         count_a = 0
    #         count_b = 0
    #         count_c = 0
    #         count_f = 0
    #
    # Step 3: Use a for loop: for score in scores:
    # Step 4: Inside the loop, use if/elif/elif/else:
    #         - if score >= 90: count_a += 1
    #         - elif score >= 80: count_b += 1
    #         - elif score >= 70: count_c += 1
    #         - else: count_f += 1
    #
    # Step 5: After the loop, print the counts:
    #         f"A grades: {count_a}"
    #         f"B grades: {count_b}"
    #         f"C grades: {count_c}"
    #         f"F grades: {count_f}"
    #
    # Expected output:
    #   A grades: 2
    #   B grades: 2
    #   C grades: 2
    #   F grades: 2
    pass


# ============================================================
# {{PHASE_5_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_5}}


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # {{hero}} trains at {{school}}. Each day, check conditions and act.
    # Use multiple conditions inside a loop.
    #
    # Step 1: Create starting values:
    #         energy = 100
    #         skill = 0
    #
    # Step 2: Use a for loop: for day in range(1, 6):  # 5 days
    # Step 3: Print f"Day {day}: Energy={energy}, Skill={skill}"
    #
    # Step 4: Inside the loop, check energy and train:
    #         if energy >= 30:
    #             # Train: gain skill, lose energy
    #             skill = skill + 10
    #             energy = energy - 25
    #             print "  {{hero}} trains hard!"
    #         else:
    #             # Rest: regain energy
    #             energy = energy + 20
    #             print "  {{hero}} rests."
    #
    # Step 5: After the loop, print final stats:
    #         f"Final: Energy={energy}, Skill={skill}"
    #
    # Expected output (energy starts at 100):
    #   Day 1: Energy=100, Skill=0
    #     {{hero}} trains hard!
    #   Day 2: Energy=75, Skill=10
    #     {{hero}} trains hard!
    #   Day 3: Energy=50, Skill=20
    #     {{hero}} trains hard!
    #   Day 4: Energy=25, Skill=30
    #     {{hero}} rests.
    #   Day 5: Energy=45, Skill=30
    #     {{hero}} trains hard!
    #   Final: Energy=20, Skill=40
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

    print("\n=== {{PHASE_5_TITLE}} ===")
    exercise_e()

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
