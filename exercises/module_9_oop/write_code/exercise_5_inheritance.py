# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי ירושה - יצירת מחלקות חדשות שמרחיבות מחלקות קיימות.
# המחלקה הילדה יורשת את כל המשתנים והמתודות מהמחלקה ההורה,
# ויכולה להוסיף משלה או לדרוס את הקיימות.
#
# {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
#
# מחלקת הורה (מוכנה עבורך)

# %%
class Entity:
    """Base class for all game entities at {{school}}."""

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def describe(self):
        return f"{self.name} (HP: {self.health})"

# %% [markdown]
# צרי מחלקה ילדה שיורשת מ-`Entity`.
#
# 1. הגדירי מחלקה בשם `Character` שיורשת מ-`Entity`:
#         class Character(Entity):
#
# 2. ב-`__init__` של `Character`, קראי ל-`__init__` של ההורה:
#         def __init__(self, name, health, role):
#             super().__init__(name, health)
#             self.role = role
#
# 3. הוסיפי מתודה ייחודית ל-`Character`:
#         def introduce(self):
#             return f"I am {self.name}, a {self.role}."
#
# 4. בדקי את הירושה:
#         hero = Character("{{hero}}", 100, "{{ROLE_TITLE}}")
#         print(hero.describe())  # ירושה מ-Entity!
#         print(hero.introduce())  # מתודה של Character

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
#
# מחלקת הורה (מוכנה עבורך)

# %%
class Item:
    """Base class for all items."""

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_info(self):
        return f"{self.name} (worth {self.value} gold)"

# %% [markdown]
# צרי שתי מחלקות ילדות שונות מאותה מחלקת הורה.
#
# 1. הגדירי `Weapon` שיורשת מ-`Item`:
#         הוסיפי משתנה `damage` ב-`__init__` (אחרי קריאה ל-`super`)
#         הוסיפי מתודה `attack_info(self)` שמחזירה:
#         "[name]: deals [damage] damage"
#
# 2. הגדירי `Armor` שיורשת מ-`Item`:
#         הוסיפי משתנה `defense` ב-`__init__`
#         הוסיפי מתודה `defense_info(self)` שמחזירה:
#         "[name]: provides [defense] defense"
#
# 3. צרי אובייקטים ובדקי:
#         sword = Weapon("{{item}}", 150, 25)
#         print(sword.get_info())  # ירושה
#         print(sword.attack_info())  # ייחודי ל-Weapon
#
#         shield = Armor("{{spell1}}", 100, 15)
#         print(shield.get_info())  # ירושה
#         print(shield.defense_info())  # ייחודי ל-Armor

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# צרי היררכיית מחלקות עם שלושה רמות.
#
# 1. הגדירי מחלקת בסיס `Being`:
#         __init__(self, name)
#         שמרי את self.name
#
# 2. הגדירי `LivingBeing` שיורשת מ-`Being`:
#         __init__(self, name, health)
#         קראי ל-super().__init__(name)
#         הוסיפי self.health
#         הוסיפי מתודה is_alive(self) שמחזירה health > 0
#
# 3. הגדירי `Combatant` שיורשת מ-`LivingBeing`:
#         __init__(self, name, health, power)
#         קראי ל-super().__init__(name, health)
#         הוסיפי self.power
#         הוסיפי מתודה battle_cry(self) שמחזירה:
#         "[name] with power [power] is ready!"
#
# 4. בדקי את ההיררכיה:
#         fighter = Combatant("{{hero}}", 100, 50)
#         print(f"Name: {fighter.name}")  # מ-Being
#         print(f"Alive: {fighter.is_alive()}")  # מ-LivingBeing
#         print(fighter.battle_cry())  # מ-Combatant

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# צרי תת-מחלקות מיוחדות עם יכולות ייחודיות.
#
# 1. הגדירי מחלקת בסיס `Ability`:
#         __init__(self, name, power_cost)
#         שמרי את שני המשתנים
#         הוסיפי מתודה describe(self) שמחזירה:
#         "[name] (costs [power_cost] energy)"
#
# 2. הגדירי `AttackAbility` שיורשת מ-`Ability`:
#         __init__(self, name, power_cost, damage)
#         קראי ל-`super` והוסיפי self.damage
#         הוסיפי מתודה use(self, target) שמדפיסה:
#             "[name] deals [damage] damage to [target]!"
#
# 3. הגדירי `HealAbility` שיורשת מ-`Ability`:
#         __init__(self, name, power_cost, heal_amount)
#         קראי ל-`super` והוסיפי self.heal_amount
#         הוסיפי מתודה use(self, target) שמדפיסה:
#             "[name] heals [target] for [heal_amount]!"
#
# 4. בדקי את היכולות שלך:
#         fireball = AttackAbility("{{spell2}}", 30, 50)
#         print(fireball.describe())  # ירושה
#         fireball.use("{{villain}}")  # מתודה של AttackAbility
#
#         heal = HealAbility("{{spell1}}", 20, 35)
#         print(heal.describe())  # ירושה
#         heal.use("{{hero}}")  # מתודה של HealAbility

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
