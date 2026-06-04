# %% [markdown]
# {{CONTEXT_DECODE_ERROR_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי להבין ולתקן שגיאות
# שקורות כשעובדים עם מילונים מקוננים.
#
# {{ERROR_1_TITLE}}
# {{CONTEXT_ERROR_1_NARRATIVE}}
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "config.py", line 8, in <module>
#     volume = settings["audio"]["volume"]
# KeyError: 'audio'

# %%
settings = {
    "display": {"brightness": 80, "resolution": "1080p"},
    "controls": {"sensitivity": 5}
}

# Trying to access audio settings that don't exist
volume = settings["audio"]["volume"]
print(f"Volume: {volume}")

# %% [markdown]
# קודם כל, הסבירי מה גרם לשגיאה:
# השגיאה קרתה כי: _______________
#
# {{CONTEXT_ERROR_HINT_1}}
#
# 1. הוסיפי את המפתח החסר `"audio"` למילון `settings`
# 2. בדקי אם `"audio"` קיים לפני הגישה אליו
# 3. השתמשי ב-`.get()` עם ערך ברירת מחדל
#
# כתבי גרסה שמטפלת בצורה נאותה במפתחות מקוננים חסרים:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{ERROR_2_TITLE}}
# {{CONTEXT_ERROR_2_NARRATIVE}}
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "profile.py", line 7, in <module>
#     health = characters["{{hero}}"]["stats"]["health"]
# TypeError: 'NoneType' object is not subscriptable

# %%
characters = {
    "{{hero}}": None,  # Character data not loaded yet!
    "{{heroine}}": {"stats": {"health": 100, "mana": 50}}
}

# This crashes because characters["{{hero}}"] is None
health = characters["{{hero}}"]["stats"]["health"]
print(f"Health: {health}")

# %% [markdown]
# השגיאה קרתה כי: _______________
#
# {{CONTEXT_ERROR_HINT_2}}
#
# הודעת השגיאה אומרת `"NoneType object is not subscriptable"`
# כלומר ניסינו להשתמש ב-`["stats"]` על `None`.
#
# תקני על ידי בדיקה אם נתוני הדמות קיימים לפני הגישה אליהם:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{ERROR_3_TITLE}}
# {{CONTEXT_ERROR_3_NARRATIVE}}
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "inventory.py", line 10, in <module>
#     player_data["inventory"]["{{item}}"] += 1
# KeyError: '{{item}}'

# %%
player_data = {
    "name": "{{hero}}",
    "inventory": {
        "{{spell1}}": 3
    }
}

# Trying to add to an item that doesn't exist in inventory
player_data["inventory"]["{{item}}"] += 1
print(player_data["inventory"])

# %% [markdown]
# השגיאה קרתה כי: _______________
#
# {{CONTEXT_ERROR_HINT_3}}
#
# המילון המקונן קיים (`inventory`), אבל המפתח
# `"{{item}}"` לא קיים בתוכו.
#
# השתמשי ב-`.get()` על המילון הפנימי:
# player_data["inventory"]["{{item}}"] = player_data["inventory"].get("{{item}}", 0) + 1

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{ERROR_4_TITLE}}
# {{CONTEXT_ERROR_4_NARRATIVE}}
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "game.py", line 8, in <module>
#     abilities["{{hero}}"]["{{spell1}}"]["power"] = 20
# KeyError: '{{spell1}}'

# %%
abilities = {
    "{{hero}}": {},  # Empty dict - no abilities yet!
    "{{heroine}}": {"{{spell1}}": {"power": 10}}
}

# Trying to set a value in a nested dict that doesn't exist
abilities["{{hero}}"]["{{spell1}}"]["power"] = 20

# %% [markdown]
# השגיאה קרתה כי: _______________
#
# {{CONTEXT_ERROR_HINT_4}}
#
# מילון היכולות של {{hero}} ריק - `"{{spell1}}"` לא קיים.
# צריך ליצור את כל המבנה המקונן.
#
# אפשרות אחת: לבדוק וליצור כל רמה בנפרד
# אפשרות אחרת: להקצות את כל המילון המקונן בבת אחת

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_DECODE_ERROR_INTRO}}")
print("=" * 50)
print()
print("Nested dictionary errors are trickier because the problem")
print("might be at any level of the nesting!")
print()
print("For each exercise:")
print("1. Identify WHICH key caused the error")
print("2. Understand WHY that key is problematic")
print("3. Fix the code to handle missing data gracefully")
print()

print("=== {{ERROR_1_TITLE}} ===")
# Uncomment to test after fixing:
# fix_code_a()

print("\n=== {{ERROR_2_TITLE}} ===")
# fix_code_b()

print("\n=== {{ERROR_3_TITLE}} ===")
# fix_code_c()

print("\n=== {{ERROR_4_TITLE}} ===")
# fix_code_d()

print("\n" + "=" * 50)
print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
