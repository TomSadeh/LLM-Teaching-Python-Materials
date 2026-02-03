"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn to implement __str__ - a special method
that defines how your objects are displayed when printed or converted
to strings. This makes debugging and displaying information much easier.
"""


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a class with a __str__ method.
    #
    # Step 1: Define a class called `Item` with __init__ that takes:
    #         - self, name, value
    #         Store both as instance attributes.
    #
    # Step 2: Define the __str__ method:
    #         def __str__(self):
    #             return f"[some formatted string]"
    #
    #         Return a string like: "Item: [name] (worth [value] gold)"
    #
    # Step 3: Create an item and test __str__:
    #         item = Item("{{item}}", 100)
    #         print(item)  # This automatically calls __str__!
    #
    # Note: Without __str__, print(item) would show something like:
    #       <__main__.Item object at 0x...>
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a class with a more complex __str__ that shows state.
    #
    # Step 1: Define a class called `Character` with __init__ that takes:
    #         - self, name, health, max_health, level
    #         Store all as instance attributes.
    #
    # Step 2: Define __str__ to show all the character info:
    #         Format: "[name] (Lv.[level]) - HP: [health]/[max_health]"
    #
    # Step 3: Create several characters and print them:
    #         hero = Character("{{hero}}", 75, 100, 5)
    #         print(hero)  # Should show formatted info
    #
    #         friend = Character("{{friend}}", 50, 80, 3)
    #         print(friend)
    #
    # Step 4: Modify the hero's health and print again:
    #         hero.health = 100
    #         print(hero)  # __str__ shows current state!
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a class that uses __str__ to display a list of items.
    #
    # Step 1: Define a class called `Inventory` with __init__ that takes:
    #         - self, owner
    #         Set self.owner = owner
    #         Set self.items = []  (empty list)
    #
    # Step 2: Add an `add_item` method that appends to self.items
    #
    # Step 3: Define __str__ to display the inventory contents:
    #         If empty: "[owner]'s Inventory: (empty)"
    #         If has items: "[owner]'s Inventory: [item1], [item2], ..."
    #
    #         Hint: Use ", ".join(self.items) to format the list
    #
    # Step 4: Test the inventory:
    #         inv = Inventory("{{hero}}")
    #         print(inv)  # Should show empty
    #
    #         inv.add_item("{{item}}")
    #         inv.add_item("{{spell1}}")
    #         print(inv)  # Should show items
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a class where __str__ formats a multi-line display.
    #
    # Step 1: Define a class called `ProfileCard` with __init__ that takes:
    #         - self, name, role, level, skills (list)
    #         Store all as instance attributes.
    #
    # Step 2: Define __str__ to return a multi-line card:
    #         ┌─────────────────────┐
    #         │ [name]              │
    #         │ Role: [role]        │
    #         │ Level: [level]      │
    #         │ Skills: [s1], [s2]  │
    #         └─────────────────────┘
    #
    #         Simplified version (without borders) is fine:
    #         "[name]\nRole: [role]\nLevel: [level]\nSkills: [s1], [s2]"
    #
    # Step 3: Create a profile card and print it:
    #         card = ProfileCard("{{hero}}", "{{ROLE_TITLE}}", 10,
    #                           ["{{spell1}}", "{{spell2}}"])
    #         print(card)
    #
    # Hint: Use \n for newlines in the return string
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
