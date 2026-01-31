# Exercise 3: Methods - Making Objects DO Things!
#
# Methods are functions that belong to a class.
# They let your objects perform actions!


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Create a Character class with a greet() method
    #
    # class Character:
    #     def __init__(self, name):
    #         self.name = name
    #
    #     def greet(self):
    #         print(f"{{greeting}} I'm {self.name}!")
    #
    # hero = Character("{{hero}}")
    # hero.greet()
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Create a Character with a take_damage(amount) method
    # The method should subtract amount from health
    # Print how much damage was taken and remaining health
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Create a Character with:
    # - heal(amount) method - adds health (but max 100!)
    # - is_alive() method - returns True if health > 0
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # Create a Wizard class with:
    # - __init__(name) - also sets mana = 100
    # - cast_spell(spell_name, cost) - uses mana if enough available
    # Try casting spells until mana runs out!
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # Create an Inventory class with methods:
    # - add_item(item) - adds to the list
    # - remove_item(item) - removes from list if present
    # - show_items() - prints all items
    # - has_item(item) - returns True/False
    pass


def exercise_f():
    # ✏️ YOUR CODE HERE ✏️
    # Create a Pet class with:
    # - __init__(name, species) - also sets happiness = 50
    # - feed() - increases happiness by 10
    # - play() - increases happiness by 20
    # - status() - prints how the pet is feeling based on happiness
    pass


class ExampleCharacter:
    """A character with multiple methods"""

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.level = 1
        self.xp = 0

    def attack(self, target):
        damage = 10 * self.level
        print(f"{self.name} attacks {target} for {damage} damage!")
        return damage

    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self.name} gained {amount} XP!")

        # Level up check
        if self.xp >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp -= 100
        self.health += 20
        print(f"🎉 {self.name} reached level {self.level}!")


def show_example():
    hero = ExampleCharacter("{{hero}}")
    hero.attack("{{villain}}")
    hero.gain_xp(50)
    hero.gain_xp(60)  # This should trigger level up!


def main():
    print("=== Exercise A: Simple Method ===")
    exercise_a()

    print("\n=== Exercise B: Take Damage ===")
    exercise_b()

    print("\n=== Exercise C: Heal and Check ===")
    exercise_c()

    print("\n=== Exercise D: Wizard Spells ===")
    exercise_d()

    print("\n=== Exercise E: Inventory System ===")
    exercise_e()

    print("\n=== Exercise F: Pet Care ===")
    exercise_f()

    print("\n=== Example to Study ===")
    show_example()


main()
