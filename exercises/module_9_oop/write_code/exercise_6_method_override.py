"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn to override methods - replacing or extending
parent class behavior in child classes. Overriding allows subclasses to
provide specialized implementations while maintaining the same interface.
"""


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


# Parent class (provided for you)
class Character:
    """Base character class."""

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def get_attack_power(self):
        """Default attack power is 10."""
        return 10

    def describe(self):
        """Default description."""
        return f"{self.name} (HP: {self.health})"


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a subclass that OVERRIDES a method.
    #
    # Step 1: Define `Warrior` that inherits from Character:
    #         class Warrior(Character):
    #
    # Step 2: In __init__, call super() and add self.strength attribute
    #
    # Step 3: Override get_attack_power to return strength instead of 10:
    #         def get_attack_power(self):
    #             return self.strength
    #
    # Step 4: Test that the override works:
    #         base = Character("Guard", 50)
    #         print(f"Character attack: {base.get_attack_power()}")  # 10
    #
    #         warrior = Warrior("{{hero}}", 100, 25)
    #         print(f"Warrior attack: {warrior.get_attack_power()}")  # 25
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


# Parent class (provided for you)
class Entity:
    """Base entity class."""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Entity: {self.name}"

    def make_sound(self):
        return "..."


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create multiple subclasses that override the same method differently.
    #
    # Step 1: Define `Hero` that inherits from Entity:
    #         Override make_sound() to return "[name] says: For justice!"
    #         Override __str__ to return "[name] the Hero"
    #
    # Step 2: Define `Creature` that inherits from Entity:
    #         Override make_sound() to return "[name] growls menacingly!"
    #         Override __str__ to return "[name] the Creature"
    #
    # Step 3: Test polymorphism - different behavior, same method name:
    #         hero = Hero("{{hero}}")
    #         creature = Creature("{{creature}}")
    #
    #         entities = [hero, creature]
    #         for entity in entities:
    #             print(entity)  # Uses __str__
    #             print(f"  Sound: {entity.make_sound()}")
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


# Parent class (provided for you)
class BaseCalculator:
    """Base calculator for game mechanics."""

    def __init__(self, base_value):
        self.base_value = base_value

    def calculate(self):
        """Return the base value."""
        return self.base_value

    def describe_calculation(self):
        return f"Base: {self.base_value}"


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Override a method and EXTEND it using super().
    #
    # Step 1: Define `BonusCalculator` inheriting from BaseCalculator:
    #         Add a bonus attribute in __init__
    #
    # Step 2: Override calculate() to ADD the bonus to the base value:
    #         def calculate(self):
    #             base = super().calculate()  # Get parent's result
    #             return base + self.bonus    # Add to it
    #
    # Step 3: Override describe_calculation() to extend the description:
    #         def describe_calculation(self):
    #             parent_desc = super().describe_calculation()
    #             return f"{parent_desc} + Bonus: {self.bonus}"
    #
    # Step 4: Test the extension:
    #         basic = BaseCalculator(100)
    #         print(f"Basic: {basic.calculate()}")  # 100
    #         print(basic.describe_calculation())
    #
    #         with_bonus = BonusCalculator(100, 25)
    #         print(f"With bonus: {with_bonus.calculate()}")  # 125
    #         print(with_bonus.describe_calculation())
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a hierarchy with specialized behavior at each level.
    #
    # Step 1: Define base class `Unit`:
    #         __init__(self, name)
    #         Method get_info() returning just the name
    #         Method get_power() returning 0
    #
    # Step 2: Define `CombatUnit` inheriting from Unit:
    #         __init__(self, name, attack)
    #         Override get_power() to return self.attack
    #         Override get_info() to return:
    #             super().get_info() + f" (ATK: {self.attack})"
    #
    # Step 3: Define `EliteUnit` inheriting from CombatUnit:
    #         __init__(self, name, attack, special_power)
    #         Override get_power() to return attack + special_power
    #         Override get_info() to return:
    #             super().get_info() + f" [ELITE +{self.special_power}]"
    #
    # Step 4: Test the hierarchy:
    #         basic = Unit("Recruit")
    #         print(f"{basic.get_info()} - Power: {basic.get_power()}")
    #
    #         combat = CombatUnit("Soldier", 15)
    #         print(f"{combat.get_info()} - Power: {combat.get_power()}")
    #
    #         elite = EliteUnit("{{hero}}", 20, 10)
    #         print(f"{elite.get_info()} - Power: {elite.get_power()}")
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
