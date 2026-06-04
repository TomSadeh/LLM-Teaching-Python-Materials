# %% [markdown]
# {{CONTEXT_COMPLETE_FUNCTION_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תשלימי פונקציות שמעבדות
# פריטים ממילון תוך שימוש בשיטות איטרציה.
#
# ## {{FUNCTION_1_TITLE}}
# {{CONTEXT_FUNCTION_1_NARRATIVE}}

# %%
# Started for you:
count = 0

# %% [markdown]
# {{CONTEXT_FUNCTION_HINT_1}}
#
# עברי על ערכי המילון וספרי את ההתאמות.
# השתמשי בלולאה: `for status in roster.values():`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{FUNCTION_2_TITLE}}
# {{CONTEXT_FUNCTION_2_NARRATIVE}}

# %%
# Started for you:
matches = []

# %% [markdown]
# {{CONTEXT_FUNCTION_HINT_2}}
#
# עברי על פריטי המילון עם `.items()` ובדקי כל ערך.
# `for key, value in data.items():`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{FUNCTION_3_TITLE}}
# {{CONTEXT_FUNCTION_3_NARRATIVE}}

# %%
# Started for you:
total = 0

# %% [markdown]
# {{CONTEXT_FUNCTION_HINT_3}}
#
# עברי על הערכים והוסיפי לסכום רק את אלה שמעל הסף.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{FUNCTION_4_TITLE}}
# {{CONTEXT_FUNCTION_4_NARRATIVE}}

# %%
# Started for you:
result = {}

# %% [markdown]
# {{CONTEXT_FUNCTION_HINT_4}}
#
# עברי על פריטי המילון עם `.items()` ובני את המילון החדש.
# `result[key] = value * multiplier`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{FUNCTION_5_TITLE}}
# {{CONTEXT_FUNCTION_5_NARRATIVE}}

# %%
# Started for you:
result = {}

# %% [markdown]
# {{CONTEXT_FUNCTION_HINT_5}}
#
# 1. הוסיפי את כל הפריטים מ-`inv1` ל-`result`
# 2. עברי על כל פריט ב-`inv2`:
#    - אם הפריט כבר קיים ב-`result`, הוסיפי את הכמויות
#    - אחרת, פשוט הוסיפי אותו ל-`result`
#
# > רמז: `result[item] = result.get(item, 0) + quantity`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_COMPLETE_FUNCTION_INTRO}}")
print("=" * 50)

print("\n=== Testing {{FUNCTION_1_TITLE}} ===")
roster = {
    "{{hero}}": "active",
    "{{heroine}}": "active",
    "{{mentor}}": "retired"
}
print(f"Active count: {count_by_status(roster, 'active')}")
print(f"Retired count: {count_by_status(roster, 'retired')}")

print("\n=== Testing {{FUNCTION_2_TITLE}} ===")
scores = {"{{hero}}": 100, "{{heroine}}": 100, "{{friend}}": 75}
print(f"Score 100: {find_by_value(scores, 100)}")
print(f"Score 75: {find_by_value(scores, 75)}")

print("\n=== Testing {{FUNCTION_3_TITLE}} ===")
data = {"{{hero}}": 85, "{{heroine}}": 92, "{{friend}}": 70}
print(f"Sum above 80: {sum_above_threshold(data, 80)}")
print(f"Sum above 90: {sum_above_threshold(data, 90)}")

print("\n=== Testing {{FUNCTION_4_TITLE}} ===")
stats = {"power": 10, "speed": 8}
print(f"Doubled: {transform_values(stats, 2)}")

print("\n=== Testing {{FUNCTION_5_TITLE}} ===")
inv1 = {"{{item}}": 5, "{{spell1}}": 2}
inv2 = {"{{spell1}}": 3, "{{spell2}}": 1}
print(f"Merged: {merge_inventories(inv1, inv2)}")

print("\n" + "=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
