# %% [markdown]
# {{CONTEXT_COMPARISON_INTRO}}
# {{CONTEXT_COMPARISON_DECISION}}
#
# נשווה בין גישה המבוססת על מילון לבין גישה המבוססת על רשימה כדי לפתור
# את אותה בעיה. מתי כדאי להשתמש בכל מבנה נתונים?
#
# השוואה 1: חיפוש מידע
# {{CONTEXT_APPROACH_1_NARRATIVE}}
#
# אנחנו צריכות למצוא את הניקוד של דמות לפי שמה.
#
# ## {{APPROACH_1_NAME}}: רשימת טאפלים

# %%
# Data stored as list of tuples
# data = [("{{hero}}", 100), ("{{heroine}}", 150), ("{{friend}}", 75)]

for name, score in data:
    if name == target_name:
        return score
return None  # Not found

# %% [markdown]
# ## {{APPROACH_2_NAME}}: מילון

# %%
# Data stored as dictionary
# data = {"{{hero}}": 100, "{{heroine}}": 150, "{{friend}}": 75}

return data.get(target_name, None)

# %% [markdown]
# {{CONTEXT_ANALYSIS_PROMPT}}
# שימי לב: {{CONTEXT_DECISION_GUIDANCE}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
analysis = """
Which is better for lookups?

List approach:
- Pros:
- Cons:

Dictionary approach:
- Pros:
- Cons:

Better choice: ??? (explain why)
"""
return analysis

# %% [markdown]
# השוואה 2: ספירת הופעות
# {{CONTEXT_APPROACH_2_NARRATIVE}}
#
# נספור כמה פעמים כל פריט מופיע באוסף.

# %%
items_found = ["{{item}}", "{{spell1}}", "{{item}}", "{{spell1}}", "{{item}}"]

# %% [markdown]
# ## גישה א׳: שימוש ברשימה

# %%
counts = []  # Will be like [["{{item}}", 3], ["{{spell1}}", 2]]

for item in items:
    found = False
    for pair in counts:
        if pair[0] == item:
            pair[1] = pair[1] + 1
            found = True
            break
    if not found:
        counts.append([item, 1])

return counts

# %% [markdown]
# ## גישה ב׳: שימוש במילון

# %%
counts = {}

for item in items:
    counts[item] = counts.get(item, 0) + 1

return counts

# %% [markdown]
# השווי בין שתי גישות הספירה.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
analysis = """
Which is better for counting?

List approach:
- Lines of code:
- Easy to understand?
- Efficient?

Dictionary approach:
- Lines of code:
- Easy to understand?
- Efficient?

Better choice: ??? (explain why)
"""
return analysis

# %% [markdown]
# השוואה 3: אחסון נתוני דמויות
# {{CONTEXT_APPROACH_3_NARRATIVE}}
#
# נאחסן מספר תכונות עבור כל דמות.
#
# ## גישה א׳: רשימות מקבילות

# %%
names = ["{{hero}}", "{{heroine}}", "{{friend}}"]
levels = [5, 7, 3]
health = [100, 120, 80]

# To get {{hero}}'s data:
hero_index = names.index("{{hero}}")
hero_level = levels[hero_index]
hero_health = health[hero_index]

return f"{{{{hero}}}}: level {hero_level}, health {hero_health}"

# %% [markdown]
# ## גישה ב׳: מילון של מילונים

# %%
characters = {
    "{{hero}}": {"level": 5, "health": 100},
    "{{heroine}}": {"level": 7, "health": 120},
    "{{friend}}": {"level": 3, "health": 80}
}

# To get {{hero}}'s data:
hero_data = characters["{{hero}}"]
hero_level = hero_data["level"]
hero_health = hero_data["health"]

return f"{{{{hero}}}}: level {hero_level}, health {hero_health}"

# %% [markdown]
# השווי בין שתי גישות ארגון הנתונים.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
analysis = """
Which is better for storing character data?

Parallel lists:
- Easy to add a new character?
- Easy to add a new attribute?
- Can the lists get out of sync?

Dictionary of dictionaries:
- Easy to add a new character?
- Easy to add a new attribute?
- Data stays together?

Better choice: ??? (explain why)

When might parallel lists actually be better?
-
"""
return analysis

# %% [markdown]
# ## סיכום: מתי להשתמש בכל אחד
#
# כתבי את הסיכום שלך כאן.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
summary = """
USE A LIST WHEN:
-
-
-

USE A DICTIONARY WHEN:
-
-
-
"""
return summary

# %%
print("{{CONTEXT_COMPARISON_INTRO}}")
print("=" * 50)

print("\n=== Comparison 1: Lookups ===")
list_data = [("{{hero}}", 100), ("{{heroine}}", 150)]
dict_data = {"{{hero}}": 100, "{{heroine}}": 150}
print(f"List lookup: {lookup_with_list(list_data, '{{hero}}')}")
print(f"Dict lookup: {lookup_with_dict(dict_data, '{{hero}}')}")
print(f"\nYour analysis:{analysis_1()}")

print("\n=== Comparison 2: Counting ===")
print(f"List count: {count_with_list(items_found)}")
print(f"Dict count: {count_with_dict(items_found)}")
print(f"\nYour analysis:{analysis_2()}")

print("\n=== Comparison 3: Character Data ===")
print(f"Parallel lists: {parallel_lists_approach()}")
print(f"Dict of dicts: {dict_of_dicts_approach()}")
print(f"\nYour analysis:{analysis_3()}")

print("\n=== Your Summary ===")
print(final_summary())

print("\n" + "=" * 50)
print("{{CONTEXT_EVALUATION_COMPLETE}}")
