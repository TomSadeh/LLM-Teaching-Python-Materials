# Exercise 6: Inheritance - Creating Specialized Classes!
#
# Inheritance lets you create new classes based on existing ones.
# A Wizard IS a Character, but with extra magic abilities!


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Create a base Character class, then a Wizard that inherits from it:
    #
    # class Character:
    #     def __init__(self, name):
    #         self.name = name
    #         self.health = 100
    #
    # class Wizard(Character):  # Wizard inherits from Character!
    #     pass
    #
    # merlin = Wizard("{{mentor}}")
    # print(merlin.name)    # Works because Wizard inherits from Character!
    # print(merlin.health)
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Add extra attributes to the child class:
    #
    # class Wizard(Character):
    #     def __init__(self, name):
    #         super().__init__(name)  # Call parent's __init__
    #         self.mana = 100         # Add wizard-specific attribute
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Create THREE character types from one base:
    # - Wizard: has mana, can cast spells
    # - Warrior: has rage, can use heavy attacks
    # - Healer: has faith, can heal others
    # All inherit health and name from Character
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # Override a method from the parent!
    #
    # class Character:
    #     def attack(self, target):
    #         print(f"{self.name} attacks!")
    #
    # class Wizard(Character):
    #     def attack(self, target):
    #         print(f"{self.name} casts a spell!")  # Different attack!
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # Use super() to extend parent behavior:
    #
    # class Wizard(Character):
    #     def attack(self, target):
    #         super().attack(target)  # Do normal attack
    #         print("✨ Magic sparkles fly everywhere!")  # Add extra!
    pass


def exercise_f():
    # ✏️ YOUR CODE HERE ✏️
    # Create a creature hierarchy:
    # Creature (base): name, health
    # ├── FriendlyCreature: can be_petted()
    # │   └── Pet: has owner, can follow()
    # └── HostileCreature: can attack()
    #     └── Boss: has special_attack()
    pass


class ExampleHierarchy:
    """Example character hierarchy"""

    class Character:
        def __init__(self, name, health=100):
            self.name = name
            self.health = health

        def introduce(self):
            print(f"I am {self.name}!")

        def attack(self, target):
            damage = 10
            target.health -= damage
            print(f"{self.name} attacks for {damage} damage!")

    class Wizard(Character):
        def __init__(self, name, health=80):
            super().__init__(name, health)
            self.mana = 100

        def cast_spell(self, spell_name):
            if self.mana >= 10:
                self.mana -= 10
                print(f"{self.name} casts {spell_name}!")
            else:
                print(f"{self.name} is out of mana!")

        def attack(self, target):
            # Override to use magic instead
            print(f"✨ {self.name} hurls a magic bolt!")
            target.health -= 15

    class Warrior(Character):
        def __init__(self, name, health=120):
            super().__init__(name, health)
            self.rage = 0

        def attack(self, target):
            super().attack(target)  # Normal attack
            self.rage += 10
            if self.rage >= 50:
                print(f"⚔️ {self.name} enters a battle fury!")


def show_example():
    Character = ExampleHierarchy.Character
    Wizard = ExampleHierarchy.Wizard
    Warrior = ExampleHierarchy.Warrior

    # Create different character types
    wizard = Wizard("{{heroine}}")
    warrior = Warrior("{{hero}}")
    enemy = Character("{{villain}}")

    wizard.introduce()
    wizard.cast_spell("{{spell3}}")

    warrior.attack(enemy)
    warrior.attack(enemy)
    warrior.attack(enemy)


def main():
    print("=== Exercise A: Basic Inheritance ===")
    exercise_a()

    print("\n=== Exercise B: Extended __init__ ===")
    exercise_b()

    print("\n=== Exercise C: Multiple Subclasses ===")
    exercise_c()

    print("\n=== Exercise D: Override Methods ===")
    exercise_d()

    print("\n=== Exercise E: Extend with super() ===")
    exercise_e()

    print("\n=== Exercise F: Creature Hierarchy ===")
    exercise_f()

    print("\n=== Example Hierarchy ===")
    show_example()


main()
