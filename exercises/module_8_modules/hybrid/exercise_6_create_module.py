# %% [markdown]
# {{CONTEXT_DISCOVERY_INTRO}}
#
# זוהי תרגילה מרובת חלקים שבה תלמדי ליצור מודולים משלך ב-Python.
# תביני את מבנה המודול, תבני קוד שניתן לשימוש חוזר,
# ותלמדי את הדפוס החשוב `__name__ == "__main__"`.
#
# מושגי תכנות: יצירת מודולים, ארגון קוד, דפוס `__name__`
# רמת קושי: 3-4
#
# ## חלק 1: גילוי — הבנת מבנה המודול
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# מודול Python הוא פשוט קובץ `.py` שמכיל קוד.
# כאשר מייבאים אותו, Python מריץ את הקובץ ומאפשר גישה לתוכנו.
#
# אנטומיה של מודול (כדאי ללמוד בעל פה):
#
# מודול אופייני מכיל:
# 1. docstring של המודול (מה המודול עושה)
# 2. ייבואים (מודולים שהמודול הזה תלוי בהם)
# 3. קבועים (ערכים שלא משתנים)
# 4. פונקציות (קוד לשימוש חוזר)
# 5. מחלקות (נלמד בהמשך — לא עכשיו!)
# 6. בלוק ראשי (קוד שרץ רק כשמריצים את הקובץ ישירות)
#
# דוגמה למבנה:
#     '''Module docstring'''
#
#     import math  # Imports
#
#     PI = 3.14159  # Constants
#
#     def my_function():  # Functions
#         pass
#
#     if __name__ == "__main__":  # Main block
#         # Only runs when this file is executed directly
#         # NOT when imported
#         pass
#
# כתבי docstring שמסביר מה הופך מודול לטוב.
#
# כתבי מחרוזת מרובת שורות שמסבירה:
# 1. מהו מודול Python
# 2. מה אפשר לשים במודול
# 3. למה מודולים שימושיים
#
# הדפיסי את ההסבר שלך

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: בעלות — צרי פונקציות מודול משלך
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# כתבי פונקציות שיכולות להיות חלק ממודול לשימוש חוזר.
# הפונקציות צריכות להיות כלליות ומתועדות היטב.
#
# ## קבועי המודול

# %%
DEFAULT_GREETING = "Welcome to {{school}}!"

# %%
VERSION = "1.0.0"

# %% [markdown]
# 1. צרי מחרוזת ברכה תוך שימוש בשם
# 2. החזירי אותה
#
# פורמט: `"Welcome to {{school}}, [name]!"`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# נוסחה: `(base * multiplier) + bonus`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# החזירי: `"[label]: [value]"`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: צמיחה — הדפוס `__name__ == "__main__"`
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# הדפוס הזה הוא קריטי לכך שמודולים יעבדו נכון.
#
# משתנה `__name__`:
#
# Python מגדיר את `__name__` כך:
# - `"__main__"` כאשר מריצים את הקובץ ישירות: `python mymodule.py`
# - שם המודול כאשר מייבאים: `import mymodule`
#
# למה זה חשוב:
#
# כאשר מריצים:
#     python mymodule.py
#
# Python מגדיר `__name__ = "__main__"`, והקוד בתוך
# הבלוק `if __name__ == "__main__":` רץ.
#
# כאשר מישהו מייבא את המודול שלך:
#     import mymodule
#
# Python מגדיר `__name__ = "mymodule"`, כך שהקוד בתוך
# הבלוק `if __name__ == "__main__":` לא רץ.
#
# זה מאפשר לך:
# 1. לכלול קוד בדיקות שרץ רק בזמן בדיקה
# 2. לספק הדגמה כאשר מריצים ישירות
# 3. לשמור על ייבואים נקיים (ללא תופעות לוואי)
#
# 1. הדפיסי את הערך של `__name__`
#
# 2. הסבירי מה המשמעות:
#         if __name__ == "__main__":
#             print("This file is being run directly")
#         else:
#             print("This file was imported as a module")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 4: בעלות — שימוש במודול שלך
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# הדגימי איך המודול שלך ייראה בשימוש.
#
# 1. הדפיסי מידע על המודול:
#         print(f"Module Version: {VERSION}")
#         print(f"Default Greeting: {DEFAULT_GREETING}")
#
# 2. הדגימי את `greet()`:
#         print(greet("{{hero}}"))
#         print(greet("{{heroine}}"))
#
# 3. הדגימי את `calculate_score()`:
#         score1 = calculate_score(100)
#         score2 = calculate_score(100, 1.5)
#         score3 = calculate_score(100, 1.5, 25)
#         הדפיסי כל תוצאה
#
# 4. הדגימי את `format_result()`:
#         print(format_result(score3, "Final Score"))

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## בלוק ראשי — רץ רק כאשר הקובץ מורץ ישירות

# %%
print("=" * 60)
print("{{CONTEXT_DISCOVERY_INTRO}}")
print("Creating Your Own Module")
print("=" * 60)
print()

print(">>> PART 1: Understanding Module Structure")
print("-" * 40)
explain_module_structure()
print()

print(">>> PART 2: Your Module Functions")
print("-" * 40)
# Uncomment to test your functions:
# print(f"Greeting: {greet('{{hero}}')}")
# print(f"Score: {calculate_score(100, 1.5, 10)}")
# print(f"Formatted: {format_result(42, 'Points')}")
print()

print(">>> PART 3: The __name__ Variable")
print("-" * 40)
demonstrate_name_variable()
print()

print(">>> PART 4: Module Demo")
print("-" * 40)
module_demo()
print()

print("=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print()
print("Key Takeaways:")
print("  1. A module is just a .py file")
print("  2. Include docstrings for documentation")
print("  3. Use __name__ == '__main__' for demo/test code")
print("  4. Functions should be general and reusable")
print("=" * 60)

# %% [markdown]
# ## זהו הדפוס המרכזי — כדאי ללמוד אותו!
