# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
#
# זוהי תרגילה מרובת-חלקים שבה תבני מערכת ניהול של {{creature}} באמצעות מחלקות.
# תיצרי יצורים, תציגי אותם, תנהלי אוספים ותממשי אינטראקציות.
#
# מושגי תכנות: מחלקות, `__str__`, אוספי אובייקטים, אינטראקציות
#
# ## חלק 1: צמיחה - יצירת מחלקת הבסיס של יצור
# {{CONTEXT_PHASE_1}}
#
# התחילי ביצירת מחלקה שמייצגת יצור יחיד.
#
# הגדירי מחלקה בשם `Creature` עם:
#
# `__init__(self, name, species, power, health)`:
#     שמרי את כל הפרמטרים כתכונות של האובייקט
#     כמו כן הגדירי `self.is_tamed = False`
#
# `tame(self)`:
#     קבעי את `self.is_tamed` ל-`True`
#     הדפיסי: `"[name] has been tamed!"`
#
# בדיקה:
#     `creature = Creature("Fang", "{{creature}}", 45, 80)`
#     `print(f"Name: {creature.name}")`
#     `print(f"Species: {creature.species}")`
#     `print(f"Tamed: {creature.is_tamed}")`
#     `creature.tame()`
#     `print(f"Tamed: {creature.is_tamed}")`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: צמיחה - הוספת ייצוג טקסטואלי
# {{CONTEXT_PHASE_2}}
#
# הוסיפי מתודת `__str__` כדי להציג את פרטי היצור בצורה יפה.
#
# העתיקי את מחלקת `Creature` מחלק 1 והוסיפי:
#
# `__str__(self)`:
#     אם מאולף: `"[name] the [species] (Power: [power], HP: [health]) [TAMED]"`
#     אם פרא: `"[name] the [species] (Power: [power], HP: [health]) [WILD]"`
#
# בדיקה:
#     `creature1 = Creature("Fang", "{{creature}}", 45, 80)`
#     `print(creature1)`  # אמורה להציג [WILD]
#
#     `creature1.tame()`
#     `print(creature1)`  # אמורה להציג [TAMED]

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: צמיחה - יצירת מחלקת אוסף
# {{CONTEXT_PHASE_3}}
#
# צרי מחלקה לניהול מספר יצורים.
#
# ראשית, שמרי את מחלקת `Creature` מחלק 2.
#
# לאחר מכן הגדירי מחלקה בשם `CreatureCollection` עם:
#
# `__init__(self, owner_name)`:
#     `self.owner_name = owner_name`
#     `self.creatures = []`  # רשימת אובייקטי Creature
#
# `add_creature(self, creature)`:
#     הוסיפי את היצור לרשימה `self.creatures`
#     הדפיסי: `"[owner_name] added [creature.name] to collection!"`
#
# `list_creatures(self)`:
#     הדפיסי: `"[owner_name]'s Creatures:"`
#     עבור כל יצור ברשימה:
#         הדפיסי את היצור (משתמש ב-`__str__`)
#     אם אין יצורים: הדפיסי `"  (empty)"`
#
# `count_tamed(self)`:
#     החזירי את מספר היצורים שבהם `is_tamed` הוא `True`
#
# בדיקה:
#     `collection = CreatureCollection("{{hero}}")`
#     `collection.add_creature(Creature("Fang", "{{creature}}", 45, 80))`
#     `collection.add_creature(Creature("Spark", "{{creature}}", 30, 60))`
#     `collection.list_creatures()`
#     `print(f"Tamed: {collection.count_tamed()}")`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 4: בעלות - הוספת אינטראקציה בין יצורים
# {{CONTEXT_PHASE_4}}
#
# הוסיפי יכולת לקרבות בין יצורים.
#
# שדרגי את מחלקת `Creature` עם:
#
# `battle(self, other)`:
#     - `other` הוא אובייקט `Creature` נוסף
#     - השווי רמות כוח:
#         אם `self.power > other.power`:
#             הפחיתי מ-`other.health` את `(self.power - other.power)`
#             החזירי את `self` (המנצחת)
#         אחרת אם `other.power > self.power`:
#             הפחיתי מ-`self.health` את `(other.power - self.power)`
#             החזירי את `other` (המנצחת)
#         אחרת:
#             החזירי `None` (תיקו)
#     - הדפיסי את תוצאת הקרב
#
# הוסיפי ל-`CreatureCollection`:
#
# `find_strongest(self)`:
#     החזירי את היצור עם הכוח הגבוה ביותר (או `None` אם האוסף ריק)
#
# בדיקת קרבות:
#     `creature1 = Creature("Fang", "{{creature}}", 45, 80)`
#     `creature2 = Creature("Spark", "{{creature}}", 30, 60)`
#
#     `winner = creature1.battle(creature2)`
#     `if winner:`
#         `print(f"Winner: {winner.name}")`
#
#     `print(f"After battle:")`
#     `print(creature1)`
#     `print(creature2)`
#
# בדיקת find_strongest:
#     `collection = CreatureCollection("{{hero}}")`
#     # הוסיפי מספר יצורים...
#     `strongest = collection.find_strongest()`
#     `print(f"Strongest: {strongest.name if strongest else 'None'}")`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## MAIN

# %%
print("=" * 60)
print("{{CONTEXT_PROJECT_INTRO}}")
print("Building a {{creature}} Management System")
print("=" * 60)
print()

print(">>> PART 1: Base Creature Class")
print("(Create the basic Creature class)")
part1_base_creature()
print()

print(">>> PART 2: String Representation")
print("(Add __str__ for nice display)")
part2_str_method()
print()

print(">>> PART 3: Collection Management")
print("(Create CreatureCollection class)")
part3_collection()
print()

print(">>> PART 4: Creature Interactions")
print("(Add battle and find_strongest)")
part4_interaction()

print()
print("=" * 60)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
print("=" * 60)
