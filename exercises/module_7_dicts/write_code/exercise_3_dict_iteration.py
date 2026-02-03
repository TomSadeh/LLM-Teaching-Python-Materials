"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn to iterate over dictionaries using
.keys(), .values(), and .items() methods.
"""


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Practice iterating over dictionary keys.
    #
    # Step 1: Create this roster dictionary:
    #         roster = {
    #             "{{hero}}": "active",
    #             "{{heroine}}": "active",
    #             "{{mentor}}": "retired",
    #             "{{friend}}": "training"
    #         }
    #
    # Step 2: Print all the names (keys) in the roster
    #         Use: for name in roster.keys():
    #
    # Step 3: Count how many people are in the roster
    #         Hint: Use len(roster)

    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Practice iterating over dictionary values.
    #
    # Step 1: Create this scores dictionary:
    #         scores = {
    #             "{{hero}}": 85,
    #             "{{heroine}}": 92,
    #             "{{friend}}": 78
    #         }
    #
    # Step 2: Calculate the total of all scores
    #         Use a for loop: for score in scores.values():
    #
    # Step 3: Calculate the average score
    #
    # Step 4: Print: "Total: [total], Average: [average]"
    #
    # Alternative: You could also use sum(scores.values())

    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Practice iterating over key-value pairs with .items()
    #
    # Step 1: Create this inventory dictionary:
    #         inventory = {
    #             "{{item}}": 5,
    #             "{{spell1}}": 3,
    #             "{{spell2}}": 1
    #         }
    #
    # Step 2: Print each item and its quantity using .items()
    #         Use: for item_name, quantity in inventory.items():
    #         Format: "[item_name]: [quantity]"
    #
    # Step 3: Find and print the item with the highest quantity
    #         Hint: Track the max as you iterate

    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Use iteration to filter and transform dictionary data.
    #
    # Step 1: Create this status dictionary:
    #         status = {
    #             "{{hero}}": "healthy",
    #             "{{heroine}}": "{{harmful_status}}",
    #             "{{friend}}": "healthy",
    #             "{{mentor}}": "{{harmful_status}}"
    #         }
    #
    # Step 2: Create a list of all characters who are "healthy"
    #         Use a for loop with .items() and an if statement
    #
    # Step 3: Print: "Healthy characters: [list]"
    #
    # Step 4: Count how many characters are "{{harmful_status}}"

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
