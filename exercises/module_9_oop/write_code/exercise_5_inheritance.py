"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn inheritance - creating new classes that
extend existing ones. The child class inherits all attributes and methods
from the parent, and can add its own or override existing ones.
"""


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


# Parent class (provided for you)
class Entity:
    """Base class for all game entities at {{school}}."""

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def describe(self):
        return f"{self.name} (HP: {self.health})"


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a child class that inherits from Entity.
    #
    # Step 1: Define a class called `Character` that inherits from Entity:
    #         class Character(Entity):
    #
    # Step 2: In Character's __init__, call the parent's __init__:
    #         def __init__(self, name, health, role):
    #             super().__init__(name, health)
    #             self.role = role
    #
    # Step 3: Add a method unique to Character:
    #         def introduce(self):
    #             return f"I am {self.name}, a {self.role}."
    #
    # Step 4: Test inheritance:
    #         hero = Character("{{hero}}", 100, "{{ROLE_TITLE}}")
    #         print(hero.describe())  # Inherited from Entity!
    #         print(hero.introduce())  # Character's own method
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


# Parent class (provided for you)
class Item:
    """Base class for all items."""

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_info(self):
        return f"{self.name} (worth {self.value} gold)"


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create two different child classes from the same parent.
    #
    # Step 1: Define `Weapon` that inherits from Item:
    #         Add a `damage` attribute in __init__ (after calling super)
    #         Add a method `attack_info(self)` that returns:
    #         "[name]: deals [damage] damage"
    #
    # Step 2: Define `Armor` that inherits from Item:
    #         Add a `defense` attribute in __init__
    #         Add a method `defense_info(self)` that returns:
    #         "[name]: provides [defense] defense"
    #
    # Step 3: Create instances and test:
    #         sword = Weapon("{{item}}", 150, 25)
    #         print(sword.get_info())  # Inherited
    #         print(sword.attack_info())  # Weapon-specific
    #
    #         shield = Armor("{{spell1}}", 100, 15)
    #         print(shield.get_info())  # Inherited
    #         print(shield.defense_info())  # Armor-specific
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a class hierarchy with three levels.
    #
    # Step 1: Define a base class `Being`:
    #         __init__(self, name)
    #         Store self.name
    #
    # Step 2: Define `LivingBeing` that inherits from Being:
    #         __init__(self, name, health)
    #         Call super().__init__(name)
    #         Add self.health
    #         Add method is_alive(self) returning health > 0
    #
    # Step 3: Define `Combatant` that inherits from LivingBeing:
    #         __init__(self, name, health, power)
    #         Call super().__init__(name, health)
    #         Add self.power
    #         Add method battle_cry(self) that returns:
    #         "[name] with power [power] is ready!"
    #
    # Step 4: Test the hierarchy:
    #         fighter = Combatant("{{hero}}", 100, 50)
    #         print(f"Name: {fighter.name}")  # From Being
    #         print(f"Alive: {fighter.is_alive()}")  # From LivingBeing
    #         print(fighter.battle_cry())  # From Combatant
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create specialized subclasses with unique abilities.
    #
    # Step 1: Define a base class `Ability`:
    #         __init__(self, name, power_cost)
    #         Store both attributes
    #         Add method describe(self) returning:
    #         "[name] (costs [power_cost] energy)"
    #
    # Step 2: Define `AttackAbility` inheriting from Ability:
    #         __init__(self, name, power_cost, damage)
    #         Call super and add self.damage
    #         Add method use(self, target) that:
    #             Prints "[name] deals [damage] damage to [target]!"
    #
    # Step 3: Define `HealAbility` inheriting from Ability:
    #         __init__(self, name, power_cost, heal_amount)
    #         Call super and add self.heal_amount
    #         Add method use(self, target) that:
    #             Prints "[name] heals [target] for [heal_amount]!"
    #
    # Step 4: Test your abilities:
    #         fireball = AttackAbility("{{spell2}}", 30, 50)
    #         print(fireball.describe())  # Inherited
    #         fireball.use("{{villain}}")  # AttackAbility's method
    #
    #         heal = HealAbility("{{spell1}}", 20, 35)
    #         print(heal.describe())  # Inherited
    #         heal.use("{{hero}}")  # HealAbility's method
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
