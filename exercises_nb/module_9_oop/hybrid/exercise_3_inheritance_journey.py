# %% [markdown]
# {{CONTEXT_DISCOVERY_INTRO}}
#
# זוהי תרגילה מרובת-חלקים שבה {{hero}} מגלה קוד ישן שהותיר {{mentor}}
# וצריכה להבין אותו, להרחיב אותו ולשפר אותו באמצעות ירושה.
#
# מושגי תכנות: ירושה, `super()`, דריסת מתודות, פולימורפיזם
#
# ## חלק 1: גילוי - הבנת מחלקת האב
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# {{mentor}} השאיר מאחוריו את המחלקה הזו. לפני שתרחיבי אותה, את צריכה
# להבין איך היא עובדת. עייני בקוד והשלימי את הניתוח.

# %%
class BaseEntity:
    """The original entity class from {{mentor}}."""

    def __init__(self, name, health, level=1):
        self.name = name
        self.health = health
        self.max_health = health
        self.level = level

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
        return self.health

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)
        return self.health

    def get_stats(self):
        return f"{self.name} (Lv.{self.level}) - HP: {self.health}/{self.max_health}"

# %% [markdown]
# עקבי אחרי ביצוע הקוד הבא:
#
#     entity = BaseEntity("{{hero}}", 100, 5)
#     entity.take_damage(30)
#     entity.heal(15)
#     entity.take_damage(100)
#
# מלאי את טבלת המעקב:
# | שלב | פעולה           | self.health | ערך מוחזר |
# |-----|-----------------|-------------|-----------|
# | 0   | __init__        |             |           |
# | 1   | take_damage(30) |             |           |
# | 2   | heal(15)        |             |           |
# | 3   | take_damage(100)|             |           |
#
# שאלות:
# 1. מדוע `heal(15)` לא משחזרת את הבריאות ל-100?
# 2. מה מונע מהבריאות לרדת מתחת ל-0?
#
# כתבי את הטבלה המלאה ואת התשובות כהערות למטה:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: צמיחה - יצירת מחלקת בת ראשונה
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# צרי מחלקת דמות מתמחה שיורשת מ-`BaseEntity`.
#
# הגדירי את `Warrior` שיורשת מ-`BaseEntity` עם:
#
# `__init__(self, name, health, level, strength)`:
# 1. קראי ל-`super().__init__` עם `name`, `health`, `level`
# 2. הוסיפי `self.strength`
#
# `attack(self, target)`:
# 1. `target` הוא `BaseEntity` או מחלקת בת שלה
# 2. גרמי נזק השווה ל-`self.strength` ל-`target`
# 3. הדפיסי: `"[name] attacks [target.name] for [strength] damage!"`
# 4. החזירי את הבריאות הנותרת של `target`
#
# `get_stats(self)`:
# 1. דרסי כדי לכלול את `strength`
# 2. קראי ל-`super().get_stats()` והוסיפי `" | STR: [strength]"`
#
# בדיקה:
#     warrior = Warrior("{{hero}}", 100, 5, 25)
#     print(warrior.get_stats())
#
#     target = BaseEntity("Training Dummy", 60, 1)
#     warrior.attack(target)
#     print(target.get_stats())

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: צמיחה - יצירת מחלקת בת שנייה
# {{CONTEXT_PHASE_3}}
#
# צרי התמחות שונה עם התנהגות ייחודית משלה.
#
# הגדירי את `Mage` שיורשת מ-`BaseEntity` עם:
#
# `__init__(self, name, health, level, mana, spell_power)`:
# 1. קראי ל-`super().__init__` עם `name`, `health`, `level`
# 2. הוסיפי `self.mana` ו-`self.spell_power`
# 3. קבעי `self.max_mana = mana`
#
# `cast_spell(self, target, mana_cost=10)`:
# 1. אם `self.mana < mana_cost`:
#    הדפיסי: `"[name] has insufficient mana!"`
#    החזירי 0
# 2. אחרת:
#    הפחיתי `mana_cost` מ-`self.mana`
#    גרמי נזק של `self.spell_power` ל-`target`
#    הדפיסי: `"[name] casts a spell on [target.name] for [spell_power] damage!"`
#    החזירי את הנזק שנגרם
#
# `rest(self)`:
# 1. שחזרי 20 מאנה (לא יותר מ-`max_mana`)
# 2. הדפיסי: `"[name] rests and recovers mana. Mana: [current]/[max]"`
#
# `get_stats(self)`:
# 1. דרסי כדי לכלול מאנה
# 2. קראי ל-`super().get_stats()` והוסיפי `" | MP: [mana]/[max_mana]"`
#
# בדיקה:
#     mage = Mage("{{heroine}}", 60, 5, 50, 30)
#     print(mage.get_stats())
#
#     target = BaseEntity("Target", 100, 1)
#     mage.cast_spell(target)
#     mage.cast_spell(target)
#     print(mage.get_stats())
#     mage.rest()

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 4: בעלות - הוספת פונקציונליות משותפת
# {{CONTEXT_MASTERY_INTRO}}
# {{CONTEXT_MASTERY_NARRATIVE}}
#
# צרי מערכת קבוצה שיכולה לעבוד עם כל מחלקת בת של `BaseEntity`.
#
# הגדירי את `Party` (לא יורשת מ-`BaseEntity`):
#
# `__init__(self, name)`:
# 1. `self.name = name`
# 2. `self.members = []`  (רשימת אובייקטי `BaseEntity`)
#
# `add_member(self, entity)`:
# 1. הוסיפי את `entity` ל-`members`
# 2. הדפיסי: `"[entity.name] joined [party name]!"`
#
# `list_members(self)`:
# 1. הדפיסי את שם הקבוצה ואת הסטטיסטיקות של כל חברה
# 2. השתמשי במתודת `get_stats()` של כל חברה
#
# `total_health(self)`:
# 1. החזירי את סכום הבריאות הנוכחית של כל החברות
#
# `heal_all(self, amount)`:
# 1. קראי ל-`heal(amount)` על כל חברה
# 2. הדפיסי: `"Party healed for [amount]!"`
#
# בדיקה עם קבוצה מעורבת:
#     party = Party("{{group}}")
#
#     warrior = Warrior("{{hero}}", 100, 5, 25)
#     mage = Mage("{{heroine}}", 60, 5, 50, 30)
#     ally = BaseEntity("{{friend}}", 80, 3)
#
#     party.add_member(warrior)
#     party.add_member(mage)
#     party.add_member(ally)
#
#     party.list_members()  # כל אחת מציגה את הסטטיסטיקות המיוחדות שלה!
#
#     # הדמיית נזק
#     warrior.take_damage(30)
#     mage.take_damage(20)
#
#     print(f"Total health: {party.total_health()}")
#     party.heal_all(15)
#     party.list_members()

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## ראשי

# %%
print("=" * 60)
print("{{CONTEXT_DISCOVERY_INTRO}}")
print("Inheritance Journey: Extending {{mentor}}'s Legacy")
print("=" * 60)
print()

print(">>> PART 1: Discovery - Understand BaseEntity")
print("(Study the code and complete the trace)")
part1_trace_parent()
print()

print(">>> PART 2: Growth - Create Warrior Subclass")
print("(Inherit from BaseEntity, add strength)")
part2_first_subclass()
print()

print(">>> PART 3: Growth - Create Mage Subclass")
print("(Different specialization with mana)")
part3_second_subclass()
print()

print(">>> PART 4: Ownership - Build Party System")
print("(Work with any BaseEntity subclass)")
part4_party_system()

print()
print("=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print("=" * 60)
