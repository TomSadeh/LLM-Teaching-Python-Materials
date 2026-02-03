"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn the fundamentals of dictionaries:
creating them, accessing values, and understanding key-value pairs.
"""


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a dictionary to store information about {{hero}}.
    #
    # Step 1: Create a dictionary called `profile` with these keys and values:
    #         - "name" -> the string "{{hero}}"
    #         - "skill" -> the string "{{spell1}}"
    #         - "level" -> the integer 1
    #
    # Step 2: Print the entire dictionary
    #
    # Step 3: Print just the value associated with "name"
    #
    # Example output format:
    #   {'name': '...', 'skill': '...', 'level': 1}
    #   ...
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a dictionary to store scores for multiple characters.
    #
    # Step 1: Create a dictionary called `scores` with:
    #         - "{{hero}}" -> 100
    #         - "{{heroine}}" -> 150
    #         - "{{friend}}" -> 75
    #
    # Step 2: Print each character's score using an f-string
    #         Format: "[name] has [score] points"
    #
    # Step 3: Calculate and print the total of all scores
    #
    # Hint: Access values with scores["key_name"]
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a dictionary to represent {{item}} attributes.
    #
    # Step 1: Create a dictionary called `item_stats` with:
    #         - "name" -> "{{item}}"
    #         - "power" -> 50
    #         - "durability" -> 100
    #         - "rarity" -> "uncommon"
    #
    # Step 2: Check if the power is greater than 30
    #         If yes, print: "[item name] is powerful!"
    #         If no, print: "[item name] needs upgrading."
    #
    # Step 3: Print all the keys in the dictionary
    #         Hint: Use the .keys() method
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

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
