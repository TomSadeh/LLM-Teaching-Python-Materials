# %% [markdown]
# {{CONTEXT_FIX_STYLE_INTRO}}
#
# זוהי תרגילה רב-שלבית שבה את מזהה בעיות סגנון,
# מתקנת אותן, ואז מסדרת מחדש את הקוד למבנה מחלקה תקין.
#
# מושגי תכנות: מוסכמות OOP, שיפוץ קוד, ארגון קוד
#
# חלק 1: הערכה - מה לא בסדר כאן?
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# קוד ישן מהמערכת הישנה של {{school}}. הוא עובד, אבל יש בו בעיות.

# %%
class data:
    def __init__(s, N, v1, v2, v3):
        s.N = N
        s.v1 = v1
        s.v2 = v2
        s.v3 = v3

    def ProcessData(s, x):
        s.v1 = s.v1 + x
        if s.v1 > 100:
            s.v1 = 100

    def DoOther(s, y):
        if s.v2 >= y:
            s.v2 = s.v2 - y
            s.v3 = s.v3 + 1
            return True
        return False

    def Info(s):
        return s.N + ": " + str(s.v1) + "/" + str(s.v2) + "/" + str(s.v3)

# %% [markdown]
# רשמי את כל הבעיות בקוד למעלה:
#
# בעיות בשם המחלקה:
# 1.
#
# בעיות בשמות הפרמטרים:
# 2.
# 3.
#
# בעיות בשמות המשתנים (attributes):
# 4.
# 5.
#
# בעיות בשמות המתודות:
# 6.
# 7.
#
# בעיות נוספות:
# 8. (> רמז: תסתכלי על הפרמטר `self`)
# 9. (> רמז: עיצוב מחרוזות)
#
# לדעתך, מה המחלקה הזו מייצגת בעצם?
# (נראה שה-attributes הם: שם, ערך כלשהו עד 100,
#  משאב שמתכלה, ומונה)
#
# הניחוש שלך: _______________

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# חלק 2: שיפור - תיקון השמות
# {{CONTEXT_STYLE_FIX_1}}
#
# החלי מוסכמות שמות נכונות על הקוד.
#
# כתבי מחדש את המחלקה עם מוסכמות נכונות:
#
# נניח שזו דמות עם:
# - שם (N)
# - בריאות (v1) עד 100
# - אנרגיה (v2) שמתכלה בפעולות
# - מונה פעולות שהושלמו (v3)
#
# החלי את התיקונים הבאים:
# 1. שם המחלקה: PascalCase, משמעותי (ActionTracker? Character?)
# 2. `self`, לא `s`
# 3. שמות פרמטרים ו-attributes תיאוריים
# 4. שמות מתודות ב-snake_case
# 5. שמות מתודות משמעותיים (`heal` במקום `ProcessData`, וכו')
# 6. f-strings לעיצוב מחרוזות
#
# כתבי את הגרסה המתוקנת שלך:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# חלק 3: צמיחה - ארגון מחדש למבנה נכון
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# עכשיו שפצי את הקוד למחלקה מסודרת עם אחריות ברורה.
#
# צרי מחלקה עם מבנה תקין:
#
# class Character:
#     """A character that can perform actions at {{school}}.
#
#     Attributes:
#         name: The character's name
#         health: Current health (0-100)
#         max_health: Maximum health (default 100)
#         energy: Current energy for actions
#         actions_completed: Count of successful actions
#     """
#
#     def __init__(self, name, health, energy):
#         """Initialize a new character."""
#         # Your code here
#         pass
#
#     def heal(self, amount):
#         """Restore health, capped at max_health.
#
#         Args:
#             amount: Health points to restore
#
#         Returns:
#             The new health value
#         """
#         # Your code here
#         pass
#
#     def perform_action(self, energy_cost):
#         """Attempt to perform an action that costs energy.
#
#         Args:
#             energy_cost: Energy required for the action
#
#         Returns:
#             True if action was performed, False if not enough energy
#         """
#         # Your code here
#         pass
#
#     def get_status(self):
#         """Get a formatted status string."""
#         # Your code here
#         pass
#
#     def __str__(self):
#         """Return string representation."""
#         # Your code here
#         pass
#
# בדקי את המחלקה המסודרת שלך:
#     char = Character("{{hero}}", 50, 30)
#     print(char)
#
#     char.heal(30)
#     print(f"After healing: {char.get_status()}")
#
#     char.perform_action(10)
#     char.perform_action(10)
#     print(f"After 2 actions: {char}")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## ראשי

# %%
print("=" * 60)
print("{{CONTEXT_FIX_STYLE_INTRO}}")
print("Legacy Code Refactoring")
print("=" * 60)
print()

print(">>> PART 1: Identify What's Wrong")
print()
print("Original code:")
d = data("{{hero}}", 50, 30, 0)
d.ProcessData(30)
d.DoOther(10)
print(d.Info())
print()
print("(List the style problems you found)")
part1_identify_problems()
print()

print(">>> PART 2: Fix the Naming")
print("(Rewrite with proper conventions)")
part2_fix_naming()
print()

print(">>> PART 3: Reorganize Into Proper Structure")
print("(Create a well-documented, properly structured class)")
part3_reorganize()

print()
print("=" * 60)
print("{{CONTEXT_IMPROVEMENT_COMPLETE}}")
print("=" * 60)
