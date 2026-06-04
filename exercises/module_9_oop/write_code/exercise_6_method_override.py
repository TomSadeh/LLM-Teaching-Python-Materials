# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי לדרוס (override) מתודות — להחליף או להרחיב
# את ההתנהגות של מחלקת-אב בתוך מחלקת-ילד. דריסה מאפשרת למחלקות-ילד
# לספק מימושים מיוחדים תוך שמירה על אותו ממשק.
#
# {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
#
# מחלקת-האב (מסופקת עבורך)

# %%
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

# %% [markdown]
# צרי מחלקת-ילד שדורסת מתודה.
#
# 1. הגדירי `Warrior` שיורשת מ-`Character`:
#    `class Warrior(Character):`
#
# 2. ב-`__init__`, קראי ל-`super()` והוסיפי את המשתנה `self.strength`
#
# 3. דרסי את `get_attack_power` כדי להחזיר את `strength` במקום `10`:
#    `def get_attack_power(self):`
#        `return self.strength`
#
# 4. בדקי שהדריסה עובדת:
#    `base = Character("Guard", 50)`
#    `print(f"Character attack: {base.get_attack_power()}")`  # 10
#
#    `warrior = Warrior("{{hero}}", 100, 25)`
#    `print(f"Warrior attack: {warrior.get_attack_power()}")`  # 25

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
#
# מחלקת-האב (מסופקת עבורך)

# %%
class Entity:
    """Base entity class."""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Entity: {self.name}"

    def make_sound(self):
        return "..."

# %% [markdown]
# צרי כמה מחלקות-ילד שדורסות את אותה מתודה בצורות שונות.
#
# 1. הגדירי `Hero` שיורשת מ-`Entity`:
#    דרסי את `make_sound()` כך שתחזיר `"[name] says: For justice!"`
#    דרסי את `__str__` כך שתחזיר `"[name] the Hero"`
#
# 2. הגדירי `Creature` שיורשת מ-`Entity`:
#    דרסי את `make_sound()` כך שתחזיר `"[name] growls menacingly!"`
#    דרסי את `__str__` כך שתחזיר `"[name] the Creature"`
#
# 3. בדקי פולימורפיזם — התנהגות שונה, אותו שם מתודה:
#    `hero = Hero("{{hero}}")`
#    `creature = Creature("{{creature}}")`
#
#    `entities = [hero, creature]`
#    `for entity in entities:`
#        `print(entity)`  # משתמש ב-`__str__`
#        `print(f"  Sound: {entity.make_sound()}")`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
#
# מחלקת-האב (מסופקת עבורך)

# %%
class BaseCalculator:
    """Base calculator for game mechanics."""

    def __init__(self, base_value):
        self.base_value = base_value

    def calculate(self):
        """Return the base value."""
        return self.base_value

    def describe_calculation(self):
        return f"Base: {self.base_value}"

# %% [markdown]
# דרסי מתודה והרחיבי אותה בעזרת `super()`.
#
# 1. הגדירי `BonusCalculator` שיורשת מ-`BaseCalculator`:
#    הוסיפי משתנה `bonus` ב-`__init__`
#
# 2. דרסי את `calculate()` כך שתוסיף את ה-bonus לערך הבסיס:
#    `def calculate(self):`
#        `base = super().calculate()`  # קבלי את תוצאת האב
#        `return base + self.bonus`    # הוסיפי אליה
#
# 3. דרסי את `describe_calculation()` כדי להרחיב את התיאור:
#    `def describe_calculation(self):`
#        `parent_desc = super().describe_calculation()`
#        `return f"{parent_desc} + Bonus: {self.bonus}"`
#
# 4. בדקי את ההרחבה:
#    `basic = BaseCalculator(100)`
#    `print(f"Basic: {basic.calculate()}")`  # 100
#    `print(basic.describe_calculation())`
#
#    `with_bonus = BonusCalculator(100, 25)`
#    `print(f"With bonus: {with_bonus.calculate()}")`  # 125
#    `print(with_bonus.describe_calculation())`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# צרי היררכיה עם התנהגות מיוחדת בכל רמה.
#
# 1. הגדירי מחלקת-בסיס `Unit`:
#    `__init__(self, name)`
#    מתודה `get_info()` שמחזירה רק את השם
#    מתודה `get_power()` שמחזירה `0`
#
# 2. הגדירי `CombatUnit` שיורשת מ-`Unit`:
#    `__init__(self, name, attack)`
#    דרסי את `get_power()` כך שתחזיר `self.attack`
#    דרסי את `get_info()` כך שתחזיר:
#        `super().get_info() + f" (ATK: {self.attack})"`
#
# 3. הגדירי `EliteUnit` שיורשת מ-`CombatUnit`:
#    `__init__(self, name, attack, special_power)`
#    דרסי את `get_power()` כך שתחזיר `attack + special_power`
#    דרסי את `get_info()` כך שתחזיר:
#        `super().get_info() + f" [ELITE +{self.special_power}]"`
#
# 4. בדקי את ההיררכיה:
#    `basic = Unit("Recruit")`
#    `print(f"{basic.get_info()} - Power: {basic.get_power()}")`
#
#    `combat = CombatUnit("Soldier", 15)`
#    `print(f"{combat.get_info()} - Power: {combat.get_power()}")`
#
#    `elite = EliteUnit("{{hero}}", 20, 10)`
#    `print(f"{elite.get_info()} - Power: {elite.get_power()}")`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
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
