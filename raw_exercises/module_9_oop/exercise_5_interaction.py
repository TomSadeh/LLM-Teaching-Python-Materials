# Exercise 5: Objects Interacting with Each Other!
#
# The real power of OOP is when objects interact!
# Characters can attack each other, trade items, cast spells on targets...


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Create a Character class where one can attack another:
    #
    # class Character:
    #     def __init__(self, name, health=100, power=10):
    #         ...
    #
    #     def attack(self, target):
    #         # target is another Character object!
    #         target.health -= self.power
    #         print(f"{self.name} attacks {target.name}!")
    #
    # hero = Character("{{hero}}", power=20)
    # villain = Character("{{villain}}", health=50)
    # hero.attack(villain)
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Create a Healer class that can heal other characters:
    # healer.heal(target) adds health to target
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Create a trade system!
    # Characters have an inventory (list)
    # character.give_item(item, other_character)
    # moves an item from one inventory to another
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # Create a Wizard that can cast spells ON a target:
    # wizard.cast(spell_name, target)
    # Different spells have different effects:
    # - "{{spell1}}": no damage, just print "The area lights up!"
    # - "{{spell2}}": disarm target (remove {{item}} if they have it)
    # - "{{spell3}}": heal the target if ally, damage if enemy
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # Team battle!
    # Create a Team class that holds multiple Characters
    # team.add_member(character)
    # team.attack(enemy_team) - each member attacks a random enemy
    pass


class ExampleCombat:
    """Example of objects interacting in combat"""

    class Character:
        def __init__(self, name, health=100, power=15):
            self.name = name
            self.health = health
            self.power = power
            self.is_defending = False

        def attack(self, target):
            damage = self.power
            if target.is_defending:
                damage = damage // 2
                print(f"{target.name} blocks some damage!")

            target.health -= damage
            target.is_defending = False
            print(f"{self.name} hits {target.name} for {damage} damage!")
            print(f"{target.name} has {target.health} HP remaining")

            if target.health <= 0:
                print(f"💀 {target.name} has been defeated!")

        def defend(self):
            self.is_defending = True
            print(f"{self.name} takes a defensive stance!")

        def is_alive(self):
            return self.health > 0


def show_example():
    # Create the class inside the example
    Character = ExampleCombat.Character

    hero = Character("{{hero}}", health=100, power=20)
    villain = Character("{{villain}}", health=80, power=25)

    print("=== Battle! ===")
    villain.defend()
    hero.attack(villain)
    villain.attack(hero)
    hero.attack(villain)
    hero.attack(villain)


def main():
    print("=== Exercise A: Attack System ===")
    exercise_a()

    print("\n=== Exercise B: Healing ===")
    exercise_b()

    print("\n=== Exercise C: Trading ===")
    exercise_c()

    print("\n=== Exercise D: Spell Casting ===")
    exercise_d()

    print("\n=== Exercise E: Team Battle ===")
    exercise_e()

    print("\n=== Example Combat ===")
    show_example()


main()
