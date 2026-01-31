# Exercise 1: Your First Class!
#
# A class is like a blueprint for creating objects.
# Think of it like a character sheet template that you fill in for each character!


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Create a simple class called Character
    # Give it a class attribute: school = "{{school}}"
    # Then create an instance and print its school
    #
    # Example structure:
    # class Character:
    #     school = "{{school}}"
    #
    # hero = Character()
    # print(hero.school)
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Create a Spell class with these attributes:
    # - name = "{{spell1}}"
    # - power = 10
    # - learned = True
    # Create an instance and print all its attributes
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Create TWO different characters from the same class
    # Give them different names by setting the attribute after creation:
    # hero1 = Character()
    # hero1.name = "{{hero}}"
    # hero2 = Character()
    # hero2.name = "{{heroine}}"
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # Create a Pet class
    # Give it attributes: species, name, owner
    # Create {{pet}} (an owl) owned by {{hero}}
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # Create a class with multiple attributes
    # Class: Student
    # Attributes: name, house, year, wand, pet
    # Create yourself as a student!
    pass


class ExampleCharacter:
    """This is a complete example to study!"""
    school = "{{school}}"
    house = "{{house}}"
    year = 1

    # You can add as many attributes as you want!
    health = 100
    spells_known = []


def show_example():
    print("Here's how to use the example class:")
    student = ExampleCharacter()
    print(f"School: {student.school}")
    print(f"House: {student.house}")
    print(f"Year: {student.year}")

    # You can change attributes!
    student.year = 2
    print(f"After one year: Year {student.year}")


def main():
    print("=== Exercise A: First Class ===")
    exercise_a()

    print("\n=== Exercise B: Spell Class ===")
    exercise_b()

    print("\n=== Exercise C: Multiple Instances ===")
    exercise_c()

    print("\n=== Exercise D: Pet Class ===")
    exercise_d()

    print("\n=== Exercise E: Complex Class ===")
    exercise_e()

    print("\n=== Example to Study ===")
    show_example()


main()
