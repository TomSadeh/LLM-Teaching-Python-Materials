"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn the fundamentals of classes:
defining a class, writing the __init__ method, and using self
to create instance attributes.
"""


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create your first class to represent a character at {{school}}.
    #
    # Step 1: Define a class called `Character` using:
    #         class Character:
    #
    # Step 2: Inside the class, define the __init__ method:
    #         def __init__(self, name, level):
    #
    # Step 3: In __init__, store the parameters as instance attributes:
    #         self.name = name
    #         self.level = level
    #
    # Step 4: Create an instance of Character for {{hero}}:
    #         hero = Character("{{hero}}", 1)
    #
    # Step 5: Print the hero's name and level using dot notation:
    #         print(f"Name: {hero.name}, Level: {hero.level}")
    #
    # Hint: The class keyword starts a class definition, like def starts
    #       a function. self refers to the specific object being created.
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a class with more attributes.
    #
    # Step 1: Define a class called `Item` with __init__ that takes:
    #         - self (always first!)
    #         - name (the item's name)
    #         - power (integer for power rating)
    #         - rarity (string like "common" or "rare")
    #
    # Step 2: Store all three as instance attributes using self
    #
    # Step 3: Create two instances:
    #         item1 = Item("{{item}}", 50, "uncommon")
    #         item2 = Item("{{spell1}}", 25, "common")
    #
    # Step 4: Print both items' attributes:
    #         "[name] - Power: [power], Rarity: [rarity]"
    #
    # Note: Each instance has its own separate values!
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a class with default parameter values.
    #
    # Step 1: Define a class called `Student` with __init__ that takes:
    #         - self
    #         - name
    #         - house (default: "{{house}}")
    #         - year (default: 1)
    #
    # Step 2: Store all as instance attributes
    #
    # Step 3: Create three students:
    #         student1 = Student("{{hero}}")  # Uses defaults
    #         student2 = Student("{{heroine}}", "{{house}}", 2)
    #         student3 = Student("{{friend}}", year=3)  # Named argument
    #
    # Step 4: Print each student's info:
    #         "[name] is in [house], year [year]"
    #
    # Hint: Default parameters work the same way as in regular functions!
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
