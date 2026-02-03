"""
{{CONTEXT_COMPARISON_INTRO}}

This is a multi-part exercise where two {{school}} students solved
the same problem with different override strategies. Evaluate
their approaches, implement your own, and determine best practices.

Programming concepts: method overriding, super(), design choices
"""


# ============================================================
# PART 1: Evaluation - Compare Base Class Implementations
# ============================================================
# {{CONTEXT_COMPARISON_DECISION}}
#
# Two students created different base classes for damage calculation.
# Both work, but which design is better?


class DamageCalculatorA:
    """Student A's approach: Simple override."""

    def __init__(self, base_damage):
        self.base_damage = base_damage

    def calculate_damage(self):
        return self.base_damage

    def get_description(self):
        return f"Damage: {self.calculate_damage()}"


class EnhancedCalculatorA(DamageCalculatorA):
    """Student A's subclass: Completely overrides calculate_damage."""

    def __init__(self, base_damage, multiplier):
        super().__init__(base_damage)
        self.multiplier = multiplier

    def calculate_damage(self):
        # Completely replaces parent's calculation
        return self.base_damage * self.multiplier


class DamageCalculatorB:
    """Student B's approach: Designed for extension."""

    def __init__(self, base_damage):
        self.base_damage = base_damage

    def get_base_damage(self):
        return self.base_damage

    def calculate_modifiers(self):
        return 1.0  # No modifiers in base class

    def calculate_damage(self):
        return int(self.get_base_damage() * self.calculate_modifiers())

    def get_description(self):
        return f"Damage: {self.calculate_damage()}"


class EnhancedCalculatorB(DamageCalculatorB):
    """Student B's subclass: Only overrides the modifier method."""

    def __init__(self, base_damage, multiplier):
        super().__init__(base_damage)
        self.multiplier = multiplier

    def calculate_modifiers(self):
        return self.multiplier  # Just change the modifier


def part1_evaluate_designs():
    # ✏️ YOUR ANALYSIS ✏️
    #
    # Test both implementations:
    #     calc_a = EnhancedCalculatorA(100, 1.5)
    #     calc_b = EnhancedCalculatorB(100, 1.5)
    #     print(f"A: {calc_a.calculate_damage()}")  # Should be 150
    #     print(f"B: {calc_b.calculate_damage()}")  # Should be 150
    #
    # Both produce the same result, but which is better?
    #
    # Analysis questions:
    # 1. Which approach is easier to extend further?
    # 2. If you wanted to add ANOTHER modifier (like a bonus), which is easier?
    # 3. Which follows "Open/Closed Principle" better? (Open for extension,
    #    closed for modification)
    #
    # Write your analysis:

    analysis = """
    Better approach: ??? (A or B)

    Reasons:
    1.
    2.

    When A's approach is appropriate:
    -

    When B's approach is appropriate:
    -
    """
    return analysis


# ============================================================
# PART 2: Growth - Implement Your Override
# ============================================================
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# Using the base class design you prefer, create a new subclass.


class BaseCombatant:
    """Base class for combat calculations."""

    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.buffs = []  # List of buff names

    def get_base_power(self):
        return self.power

    def calculate_buff_bonus(self):
        # Each buff adds 10% to power
        return len(self.buffs) * 0.1

    def get_attack_power(self):
        base = self.get_base_power()
        buff_multiplier = 1 + self.calculate_buff_bonus()
        return int(base * buff_multiplier)

    def add_buff(self, buff_name):
        self.buffs.append(buff_name)

    def get_info(self):
        return f"{self.name} - Power: {self.get_attack_power()}"


def part2_implement_override():
    # ✏️ CREATE A SPECIALIZED COMBATANT ✏️
    #
    # Define `CriticalStriker` inheriting from BaseCombatant:
    #
    # __init__(self, name, power, crit_chance):
    #     Call super().__init__
    #     Add self.crit_chance (0.0 to 1.0)
    #     Add self.last_hit_was_crit = False
    #
    # Override calculate_buff_bonus(self):
    #     Get parent's buff bonus using super()
    #     If crit_chance > 0.5, add an extra 0.2 (crit builds benefit more)
    #     Return the total bonus
    #
    # Add critical_strike(self):
    #     Import random if not done
    #     If random.random() < self.crit_chance:
    #         self.last_hit_was_crit = True
    #         Return self.get_attack_power() * 2  # Double damage!
    #     Else:
    #         self.last_hit_was_crit = False
    #         Return self.get_attack_power()
    #
    # Override get_info(self):
    #     Extend parent's info to include crit chance
    #
    # Test:
    #     striker = CriticalStriker("{{hero}}", 50, 0.6)
    #     striker.add_buff("{{spell1}}")
    #     print(striker.get_info())
    #     for i in range(5):
    #         damage = striker.critical_strike()
    #         crit_text = " (CRIT!)" if striker.last_hit_was_crit else ""
    #         print(f"Attack: {damage}{crit_text}")

    pass


# ============================================================
# PART 3: Evaluation - Compare Override Strategies
# ============================================================
# {{CONTEXT_ANALYSIS_PROMPT}}
#
# Two ways to add healing to combatants - which is better?


class HealerTypeA(BaseCombatant):
    """Approach A: Override get_attack_power to sometimes heal instead."""

    def __init__(self, name, power, heal_power):
        super().__init__(name, power)
        self.heal_power = heal_power
        self.mode = "attack"  # or "heal"

    def set_mode(self, mode):
        self.mode = mode

    def get_attack_power(self):
        if self.mode == "heal":
            return -self.heal_power  # Negative = healing
        return super().get_attack_power()


class HealerTypeB(BaseCombatant):
    """Approach B: Add separate healing method, don't override attack."""

    def __init__(self, name, power, heal_power):
        super().__init__(name, power)
        self.heal_power = heal_power

    def get_heal_power(self):
        buff_multiplier = 1 + self.calculate_buff_bonus()
        return int(self.heal_power * buff_multiplier)

    def heal(self, target):
        amount = self.get_heal_power()
        target.health = min(target.health + amount, target.max_health)
        return amount


def part3_compare_strategies():
    # ✏️ YOUR ANALYSIS ✏️
    #
    # Consider these scenarios:
    #
    # Scenario 1: A system expects positive attack values
    # Scenario 2: You want to attack AND heal in the same turn
    # Scenario 3: Other code checks combatant.get_attack_power() for AI decisions
    #
    # Write your analysis:

    analysis = """
    Better approach for healing: ??? (A or B)

    Problems with approach A:
    1.
    2.

    Why approach B is better/worse:
    1.
    2.

    General principle this illustrates:
    -
    """
    return analysis


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("{{CONTEXT_COMPARISON_INTRO}}")
    print("Method Override Challenge")
    print("=" * 60)
    print()

    print(">>> PART 1: Evaluate Design Approaches")
    print()
    # Test both designs
    calc_a = EnhancedCalculatorA(100, 1.5)
    calc_b = EnhancedCalculatorB(100, 1.5)
    print(f"Approach A result: {calc_a.calculate_damage()}")
    print(f"Approach B result: {calc_b.calculate_damage()}")
    print()
    print("Your analysis:")
    print(part1_evaluate_designs())
    print()

    print(">>> PART 2: Implement CriticalStriker")
    print("(Create your own override)")
    part2_implement_override()
    print()

    print(">>> PART 3: Compare Healing Strategies")
    print()
    print("Your analysis:")
    print(part3_compare_strategies())

    print()
    print("=" * 60)
    print("{{CONTEXT_EVALUATION_COMPLETE}}")
    print("=" * 60)


if __name__ == "__main__":
    main()
