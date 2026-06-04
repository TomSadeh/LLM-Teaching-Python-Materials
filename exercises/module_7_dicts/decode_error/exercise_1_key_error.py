# %% [markdown]
# {{CONTEXT_DECODE_ERROR_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי להבין ולתקן `KeyError`,
# אחת השגיאות הנפוצות ביותר כשעובדים עם מילונים.
#
# ## {{ERROR_1_TITLE}}
# {{CONTEXT_ERROR_1_NARRATIVE}}
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "registry.py", line 8, in <module>
#     print(registry["{{spell3}}"])
# KeyError: '{{spell3}}'

# %%
registry = {
    "{{spell1}}": "basic",
    "{{spell2}}": "intermediate"
}

# This line causes the error
print(registry["{{spell3}}"])

# %% [markdown]
# קודם כל, הסבירי מה גרם לשגיאה:
# השגיאה קרתה כי: _______________
#
# {{CONTEXT_ERROR_HINT_1}}
#
# 1. הוסיפי את המפתח החסר למילון
# 2. בדקי אם המפתח קיים לפני הגישה אליו
# 3. השתמשי במתודה `.get()` עם ערך ברירת מחדל
#
# בחרי גישה אחת וכתבי את הקוד המתוקן:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{ERROR_2_TITLE}}
# {{CONTEXT_ERROR_2_NARRATIVE}}
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "scores.py", line 6, in <module>
#     print(f"Score: {scores[player_name]}")
# KeyError: 'unknown_player'

# %%
scores = {
    "{{hero}}": 100,
    "{{heroine}}": 150
}

player_name = "unknown_player"  # This name isn't in the dictionary
print(f"Score: {scores[player_name]}")

# %% [markdown]
# השגיאה קרתה כי: _______________
#
# {{CONTEXT_ERROR_HINT_2}}
#
# זהו תבנית נפוצה: גישה למילון עם קלט ממשתמש —
# המפתח עלול שלא להיות קיים! כתבי קוד שמטפל בזה בצורה נכונה.
#
# > רמז: השתמשי ב-`in` כדי לבדוק אם מפתח קיים: `if key in dictionary:`
# >       או השתמשי ב-`.get(key, default_value)`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{ERROR_3_TITLE}}
# {{CONTEXT_ERROR_3_NARRATIVE}}
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "inventory.py", line 9, in <module>
#     inventory[item] += 1
# KeyError: '{{item}}'

# %%
inventory = {}

items_found = ["{{spell1}}", "{{item}}", "{{spell1}}"]

for item in items_found:
    # Trying to increment, but key doesn't exist yet!
    inventory[item] += 1

print(inventory)

# %% [markdown]
# השגיאה קרתה כי: _______________
#
# {{CONTEXT_ERROR_HINT_3}}
#
# זוהי "תבנית הספירה" — צריך לטפל בהופעה הראשונה של כל פריט בנפרד.
#
# > רמז לתיקון עם `.get()`: `inventory[item] = inventory.get(item, 0) + 1`
# > זה מחזיר 0 אם המפתח לא קיים, ואז מוסיף 1.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_DECODE_ERROR_INTRO}}")
print("=" * 50)
print()
print("For each exercise:")
print("1. Read the error message carefully")
print("2. Identify what caused the error")
print("3. Fix the code in the fix_code_X function")
print()

print("=== {{ERROR_1_TITLE}} ===")
# Uncomment to test after fixing:
# fix_code_a()

print("\n=== {{ERROR_2_TITLE}} ===")
# fix_code_b()

print("\n=== {{ERROR_3_TITLE}} ===")
# fix_code_c()

print("\n" + "=" * 50)
print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
