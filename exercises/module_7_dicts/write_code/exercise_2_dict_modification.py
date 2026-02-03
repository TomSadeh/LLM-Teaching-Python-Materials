"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn to modify dictionaries:
adding new entries, updating existing values, and deleting entries.
"""


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Learn to add and update dictionary entries.
    #
    # Step 1: Create an empty dictionary called `stats`
    #
    # Step 2: Add these entries one by one:
    #         stats["name"] = "{{hero}}"
    #         stats["health"] = 100
    #         stats["strength"] = 10
    #
    # Step 3: Print the dictionary
    #
    # Step 4: Update the health to 150 (use the same key)
    #
    # Step 5: Print the dictionary again to see the change

    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Practice incrementing and decrementing dictionary values.
    #
    # Step 1: Create this inventory dictionary:
    #         inventory = {"{{item}}": 5, "{{spell1}}": 3, "{{spell2}}": 1}
    #
    # Step 2: Add 2 more of "{{item}}" (increment the value)
    #         Hint: inventory["{{item}}"] = inventory["{{item}}"] + 2
    #
    # Step 3: Use 1 "{{spell1}}" (decrement the value)
    #
    # Step 4: Add a new item "{{spell3}}" with quantity 1
    #
    # Step 5: Print the final inventory
    #
    # Step 6: Print the total number of items
    #         Hint: Use sum() with inventory.values()

    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Practice removing entries from dictionaries.
    #
    # Step 1: Create this registry dictionary:
    #         registry = {
    #             "active": ["{{hero}}", "{{heroine}}"],
    #             "retired": ["{{mentor}}"],
    #             "temporary": ["visitor"]
    #         }
    #
    # Step 2: Print all the keys before modification
    #
    # Step 3: Remove the "temporary" key using: del registry["temporary"]
    #
    # Step 4: Print all the keys after modification
    #
    # Step 5: Add {{friend}} to the "active" list
    #         Hint: registry["active"].append("{{friend}}")
    #
    # Step 6: Print the final registry

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
