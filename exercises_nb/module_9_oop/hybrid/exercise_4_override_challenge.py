# %% [markdown]
# {{CONTEXT_COMPARISON_INTRO}}
#
# זוהי תרגיל רב-חלקי שבו שתי תלמידות מ-{{school}} פתרו
# את אותה בעיה עם אסטרטגיות override שונות. העריכי
# את הגישות שלהן, מימשי גישה משלך, וקבעי מהן שיטות העבודה הטובות ביותר.
#
# מושגי תכנות: דריסת מתודות (method overriding), `super()`, בחירות עיצוביות
#
# ## חלק 1: הערכה - השוואת מימושי מחלקת בסיס
# {{CONTEXT_COMPARISON_DECISION}}
#
# שתי תלמידות יצרו מחלקות בסיס שונות לחישוב נזק.
# שתיהן עובדות, אבל איזה עיצוב עדיף?

# %%
class DamageCalculatorA:
    """Student A's approach: Simple override."""

    def __init__(self, base_damage):
        self.base_damage = base_damage

    def calculate_damage(self):
        return self.base_damage

    def get_description(self):
        return f"Damage: {self.calculate_damage()}"

# %%
class EnhancedCalculatorA(DamageCalculatorA):
    """Student A's subclass: Completely overrides calculate_damage."""

    def __init__(self, base_damage, multiplier):
        super().__init__(base_damage)
        self.multiplier = multiplier

    def calculate_damage(self):
        # Completely replaces parent's calculation
        return self.base_damage * self.multiplier

# %%
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

# %%
class EnhancedCalculatorB(DamageCalculatorB):
    """Student B's subclass: Only overrides the modifier method."""

    def __init__(self, base_damage, multiplier):
        super().__init__(base_damage)
        self.multiplier = multiplier

    def calculate_modifiers(self):
        return self.multiplier  # Just change the modifier

# %% [markdown]
# ## הניתוח שלך
#
# בדקי את שני המימושים:
#     calc_a = EnhancedCalculatorA(100, 1.5)
#     calc_b = EnhancedCalculatorB(100, 1.5)
#     print(f"A: {calc_a.calculate_damage()}")  # Should be 150
#     print(f"B: {calc_b.calculate_damage()}")  # Should be 150
#
# שתיהן מייצרות את אותה תוצאה, אבל איזו עדיפה?
#
# שאלות לניתוח:
# 1. איזו גישה קל יותר להרחיב?
# 2. אם רצית להוסיף עוד מחליש (כמו בונוס), באיזו גישה זה קל יותר?
# 3. איזו גישה עוקבת טוב יותר אחרי "עיקרון פתוח/סגור"? (פתוח להרחבה,
#    סגור לשינוי)
#
# כתבי את הניתוח שלך:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
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

# %% [markdown]
# ## חלק 2: יצירה - מימשי Override משלך
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# בעזרת עיצוב מחלקת הבסיס שאת מעדיפה, צרי מחלקת משנה חדשה.

# %%
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

# %% [markdown]
# ## צרי לוחמת מיוחדת
#
# הגדירי `CriticalStriker` שיורשת מ-`BaseCombatant`:
#
# 1. `__init__(self, name, power, crit_chance)`:
#     קראי ל-`super().__init__`
#     הוסיפי `self.crit_chance` (בין 0.0 ל-1.0)
#     הוסיפי `self.last_hit_was_crit = False`
#
# 2. דרסי את `calculate_buff_bonus(self)`:
#     קבלי את בונוס הבאפים של ההורה בעזרת `super()`
#     אם `crit_chance > 0.5`, הוסיפי עוד 0.2 (בנייות קריט מרוויחות יותר)
#     החזירי את הסכום הכולל
#
# 3. הוסיפי `critical_strike(self)`:
#     ייבאי `random` אם עוד לא עשית
#     אם `random.random() < self.crit_chance`:
#         `self.last_hit_was_crit = True`
#         החזירי `self.get_attack_power() * 2`  # נזק כפול!
#     אחרת:
#         `self.last_hit_was_crit = False`
#         החזירי `self.get_attack_power()`
#
# 4. דרסי את `get_info(self)`:
#     הרחיבי את המידע של ההורה כך שיכלול את אחוז הקריט
#
# בדיקה:
#     striker = CriticalStriker("{{hero}}", 50, 0.6)
#     striker.add_buff("{{spell1}}")
#     print(striker.get_info())
#     for i in range(5):
#         damage = striker.critical_strike()
#         crit_text = " (CRIT!)" if striker.last_hit_was_crit else ""
#         print(f"Attack: {damage}{crit_text}")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: הערכה - השוואת אסטרטגיות Override
# {{CONTEXT_ANALYSIS_PROMPT}}
#
# שתי דרכים להוסיף ריפוי ללוחמות - איזו עדיפה?

# %%
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

# %%
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

# %% [markdown]
# ## הניתוח שלך
#
# שקלי את התרחישים הבאים:
#
# תרחיש 1: מערכת שמצפה לערכי תקיפה חיוביים
# תרחיש 2: את רוצה לתקוף וגם לרפא באותה תור
# תרחיש 3: קוד אחר בודק `combatant.get_attack_power()` להחלטות AI
#
# כתבי את הניתוח שלך:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
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

# %% [markdown]
# ## הרצה ראשית

# %%
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
