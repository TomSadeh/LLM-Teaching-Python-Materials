# %% [markdown]
# ## {{CONTEXT_EVALUATION_INTRO}}
#
# זוהי תרגיל רב-חלקי שמשווה בין גישות שונות לאחסון נתוני דמויות.
# בני, השווי, ובחרי בחוכמה!
#
# מושגי תכנות: מילונים, נתונים מקוננים, עיצוב מבני נתונים
#
# חלק 1: הערכה — השוואת מבני נתונים
# {{CONTEXT_EVALUATION_NARRATIVE}}
#
# קיימות שתי גישות לאחסון נתוני דמויות.
# איזו גישה עדיפה לפעולות שונות?
#
# ## גישה א׳: רשימה של מילונים

# %%
characters_list = [
    {"name": "{{hero}}", "level": 5, "health": 100, "class": "warrior"},
    {"name": "{{heroine}}", "level": 7, "health": 120, "class": "mage"},
    {"name": "{{friend}}", "level": 3, "health": 80, "class": "rogue"}
]

# %%
for char in char_list:
    if char["name"] == name:
        return char
return None

# %% [markdown]
# ## גישה ב׳: מילון של מילונים

# %%
characters_dict = {
    "{{hero}}": {"level": 5, "health": 100, "class": "warrior"},
    "{{heroine}}": {"level": 7, "health": 120, "class": "mage"},
    "{{friend}}": {"level": 3, "health": 80, "class": "rogue"}
}

# %%
return char_dict.get(name)

# %% [markdown]

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
analysis = """
OPERATION: Find character by name

List approach:
- How many steps to find "{{friend}}"?
- What if there are 1000 characters?

Dict approach:
- How many steps to find "{{friend}}"?
- What if there are 1000 characters?

Better for lookups: ___

---

OPERATION: Get all characters

List approach:
- Easy to iterate?
- Maintains insertion order?

Dict approach:
- Easy to iterate?
- What do you iterate over? (keys, values, items?)

Better for iteration: ___

---

OPERATION: Add new character

List approach:
- How? (char_list.append({...}))
- Need to check for duplicates manually?

Dict approach:
- How? (char_dict["name"] = {...})
- Automatically prevents duplicates by name?

Better for adding: ___
"""
return analysis

# %% [markdown]
# חלק 2: צמיחה — בניית מערכת עם גישת המילון
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# מִמשי מערכת ניהול דמויות מלאה תוך שימוש במילונים.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# בדקי אם השם כבר קיים.
# אם חדש, הוסיפי עם כל המאפיינים והחזירי `True`.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# בדקי אם הדמות קיימת.
# אם נמצאה, העלי את הרמה ב-1 ואת הבריאות ב-10.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# עברי על `db.items()` ואספי את השמות התואמים.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# חלק 3: צמיחה — הוספת פעולות מתקדמות
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# מִמשי פעולות מורכבות יותר שמרוויחות מהמבנה של המילון.
#
# עברי ועקבי אחרי הרמה הגבוהה ביותר שנראתה.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. ספרי דמויות וסכמי רמות לפי מחלקה
# 2. חשבי ממוצעים
#
# פורמט תוצאה: `{"warrior": {"count": 2, "avg_level": 6.0}, ...}`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# בדקי שתי הדמויות קיימות.
# בדקי שלמקור יש מספיק בריאות.
# העבירי את הבריאות.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# חלק 4: הערכה — השוואה סופית
# {{CONTEXT_EVALUATION_NARRATIVE}}
#
# חשבי מתי כל גישה עדיפה.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
evaluation = """
FINAL VERDICT:

USE LIST OF DICTS WHEN:
1.
2.
3.

USE DICT OF DICTS WHEN:
1.
2.
3.

FOR A CHARACTER DATABASE, I CHOOSE: ___

BECAUSE:
-

ONE DOWNSIDE OF MY CHOICE:
-

HOW I WOULD MITIGATE THAT DOWNSIDE:
-
"""
return evaluation

# %% [markdown]
# ## ראשי

# %%
print("=" * 60)
print("{{CONTEXT_EVALUATION_INTRO}}")
print("=" * 60)
print()

print(">>> PART 1: Compare data structures...")
print()
print("List approach:")
print(f"  Find {{{{hero}}}}: {find_in_list(characters_list, '{{hero}}')}")
print()
print("Dict approach:")
print(f"  Find {{{{hero}}}}: {find_in_dict(characters_dict, '{{hero}}')}")
print()
print("Your analysis:")
print(analysis_part_1())

print()
print(">>> PART 2: Build the dictionary-based system...")
print("(Implement create_character_db, add_character, get_character, level_up, get_by_class)")
print()
# Uncomment after implementing:
# db = create_character_db()
# add_character(db, "{{hero}}", 5, 100, "warrior")
# add_character(db, "{{heroine}}", 7, 120, "mage")
# add_character(db, "{{friend}}", 3, 80, "rogue")
# add_character(db, "{{mentor}}", 15, 200, "mage")
# print(f"Database: {db}")
# print(f"Get {{{{hero}}}}: {get_character(db, '{{hero}}')}")
# level_up(db, "{{hero}}")
# print(f"After level up: {get_character(db, '{{hero}}')}")
# print(f"Mages: {get_by_class(db, 'mage')}")

print()
print(">>> PART 3: Add advanced operations...")
print("(Implement get_highest_level, get_class_stats, transfer_health)")
# Uncomment after implementing:
# print(f"Highest level: {get_highest_level(db)}")
# print(f"Class stats: {get_class_stats(db)}")
# transfer_health(db, "{{mentor}}", "{{friend}}", 50)
# print(f"After transfer: {{{{friend}}}} health = {db['{{friend}}']['health']}")

print()
print(">>> PART 4: Final evaluation...")
print()
print(final_evaluation())

print()
print("=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print("=" * 60)
