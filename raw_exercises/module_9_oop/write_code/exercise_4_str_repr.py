# Exercise 4: __str__ and __repr__ - Making Objects Printable!
#
# When you print() an object, Python calls its __str__ method.
# This lets you control how your objects look when printed!


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Create a Character class with a __str__ method
    #
    # class Character:
    #     def __init__(self, name, house):
    #         self.name = name
    #         self.house = house
    #
    #     def __str__(self):
    #         return f"{self.name} of {self.house}"
    #
    # hero = Character("{{hero}}", "{{house}}")
    # print(hero)  # This now prints nicely!
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Create a Spell class with __str__ that shows:
    # "Spell: [name] (Power: [power])"
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Create a Character with health bar in __str__!
    # Example output:
    # "{{hero}} [████████░░] 80/100 HP"
    # Hint: Use █ and ░ characters
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # Create a detailed character card!
    # __str__ returns a multi-line string:
    # ╔══════════════════╗
    # ║   {{hero}}        ║
    # ║   Level: 5       ║
    # ║   House: {{house}} ║
    # ╚══════════════════╝
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # Create an Inventory class where __str__ lists all items nicely:
    # "Inventory: {{item}}, potion x3, gold (50)"
    pass


def exercise_f():
    # ✏️ YOUR CODE HERE ✏️
    # Create a Battle class that shows both fighters:
    # __str__ shows:
    # "Battle: {{hero}} (100 HP) vs {{villain}} (150 HP)"
    pass


class ExampleCharacter:
    """Example with both __str__ and __repr__"""

    def __init__(self, name, house, level=1):
        self.name = name
        self.house = house
        self.level = level
        self.health = 100

    def __str__(self):
        # User-friendly output
        bar_length = 10
        filled = int((self.health / 100) * bar_length)
        health_bar = "█" * filled + "░" * (bar_length - filled)
        return f"{self.name} [{health_bar}] {self.health}/100 HP"

    def __repr__(self):
        # Developer-friendly output (for debugging)
        return f"Character(name='{self.name}', house='{self.house}', level={self.level})"


def show_example():
    hero = ExampleCharacter("{{hero}}", "{{house}}", level=5)

    print("Using print() calls __str__:")
    print(hero)

    print("\nUsing repr() calls __repr__:")
    print(repr(hero))

    print("\nIn a list, Python uses __repr__:")
    characters = [hero, ExampleCharacter("{{friend}}", "{{house}}")]
    print(characters)


def main():
    print("=== Exercise A: Basic __str__ ===")
    exercise_a()

    print("\n=== Exercise B: Spell String ===")
    exercise_b()

    print("\n=== Exercise C: Health Bar ===")
    exercise_c()

    print("\n=== Exercise D: Character Card ===")
    exercise_d()

    print("\n=== Exercise E: Inventory Display ===")
    exercise_e()

    print("\n=== Exercise F: Battle Display ===")
    exercise_f()

    print("\n=== Example to Study ===")
    show_example()


main()
