# Exercise 2: The __init__ Method (Constructor!)
#
# The __init__ method runs automatically when you create an object.
# It's perfect for setting up your character with their starting stats!


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Create a Character class with an __init__ method
    # that takes a name parameter
    #
    # class Character:
    #     def __init__(self, name):
    #         self.name = name
    #
    # hero = Character("{{hero}}")
    # print(hero.name)
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Create a Character with multiple init parameters:
    # - name
    # - house
    # - year
    # Create {{heroine}} in {{house}}, year 5
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Use DEFAULT values in __init__!
    # def __init__(self, name, health=100, level=1):
    # Create a character with just a name (uses defaults)
    # Create another with custom health and level
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # Create a Spell class where __init__ calculates something!
    # Parameters: name, base_power, level
    # In __init__, calculate: actual_power = base_power * level
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # Create a Student class that initializes a list!
    # Each student starts with an empty spell list:
    # def __init__(self, name):
    #     self.name = name
    #     self.spells = []  # Empty list for each student!
    # Create two students and add different spells to each
    pass


def exercise_f():
    # ✏️ YOUR CODE HERE ✏️
    # Create a comprehensive Character class:
    # __init__ takes: name, character_class (wizard/warrior/healer)
    # Based on character_class, set different starting stats:
    # - wizard: health=80, magic=100, strength=30
    # - warrior: health=120, magic=20, strength=100
    # - healer: health=100, magic=80, strength=40
    pass


class ExampleCharacter:
    """Study this example!"""

    def __init__(self, name, house="{{house}}"):
        # 'self' refers to the object being created
        self.name = name
        self.house = house
        # You can set attributes that aren't parameters too!
        self.health = 100
        self.inventory = []

        # You can even print when an object is created!
        print(f"✨ {name} has joined {house}!")


def show_example():
    print("Creating characters with __init__:")
    hero = ExampleCharacter("{{hero}}")
    friend = ExampleCharacter("{{friend}}", "{{house}}")

    print(f"\n{hero.name}'s house: {hero.house}")
    print(f"{friend.name}'s house: {friend.house}")


def main():
    print("=== Exercise A: Basic __init__ ===")
    exercise_a()

    print("\n=== Exercise B: Multiple Parameters ===")
    exercise_b()

    print("\n=== Exercise C: Default Values ===")
    exercise_c()

    print("\n=== Exercise D: Calculated Attributes ===")
    exercise_d()

    print("\n=== Exercise E: Initialize Lists ===")
    exercise_e()

    print("\n=== Exercise F: Class-Based Stats ===")
    exercise_f()

    print("\n=== Example to Study ===")
    show_example()


main()
