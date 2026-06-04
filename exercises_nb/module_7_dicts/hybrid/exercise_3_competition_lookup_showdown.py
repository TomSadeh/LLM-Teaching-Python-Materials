# %% [markdown]
# {{CONTEXT_EVALUATION_INTRO}}
#
# זוהי תרגיל מרובה-חלקים שמשווה בין גישה מבוססת רשימות לבין גישה מבוססת מילונים
# לחיפוש נתונים. תעריכי, תממשי ותשקפי.
#
# מושגי תכנות: מילונים מול רשימות, ביצועי חיפוש, עיצוב נתונים
#
# חלק 1: הערכה - השוואה בין הגישות הקיימות
# {{CONTEXT_EVALUATION_NARRATIVE}}
#
# קיימות שתי גישות לחיפוש נתוני דמות.
# למדי אותן והחליטי איזו עדיפה.
#
# ## גישה א׳: חיפוש ברשימה

# %%
for name, level, status in roster_list:
    if name == target_name:
        return {"name": name, "level": level, "status": status}
return None

# %% [markdown]
# ## גישה ב׳: חיפוש במילון

# %%
if target_name in roster_dict:
    data = roster_dict[target_name]
    return {"name": target_name, "level": data["level"], "status": data["status"]}
return None

# %% [markdown]
# השוואה בין שתי הגישות:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
analysis = """
LIST APPROACH:
- How does it find the target? (describe the process)
- What if the list has 1000 entries?
- What if the target is at the end?

DICTIONARY APPROACH:
- How does it find the target?
- What if the dict has 1000 entries?
- Is position in dict relevant?

BETTER FOR LOOKUPS: ??? (explain)

WHEN MIGHT LISTS BE PREFERRED?
-
"""
return analysis

# %% [markdown]
# חלק 2: צמיחה - מימוש גישת המילון
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# בני מערכת חיפוש דמויות שלמה באמצעות מילונים.
#
# צרי רשימת דמויות עם לפחות 4 דמויות.
# מבנה:
# {
#     "{{hero}}": {"level": 5, "status": "active"},
#     "{{heroine}}": {"level": 7, "status": "active"},
#     ...
# }

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# השתמשי ב-`.get()` לגישה בטוחה.
# החזירי את מילון הנתונים של הדמות, או `None` אם לא נמצאה.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# עברי על `roster.items()`
# ואספי שמות של דמויות שה-status שלהן תואם.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# עברי על `roster.items()`
# ועקבי אחרי הרמה הגבוהה ביותר שנראתה ומי מחזיקה בה.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# חלק 3: הערכה - שיקוף על פשרות עיצוביות
# {{CONTEXT_EVALUATION_NARRATIVE}}
#
# עכשיו שמימשת, שקפי את בחירות העיצוב.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
reflection = """
AFTER IMPLEMENTING:

1. Was the dictionary approach easy to code?
   -

2. How would you add a new character to each approach?
   List:
   Dict:

3. How would you remove a character?
   List:
   Dict:

4. What if you need to iterate in a specific ORDER?
   List:
   Dict:

5. What if you need to allow DUPLICATE names?
   List:
   Dict:

FINAL VERDICT:
For a character roster, I would choose ___ because:
-
"""
return reflection

# %% [markdown]
# ## ראשי

# %%
print("=" * 60)
print("{{CONTEXT_EVALUATION_INTRO}}")
print("=" * 60)
print()

# Sample data for testing
roster_list = [
    ("{{hero}}", 5, "active"),
    ("{{heroine}}", 7, "active"),
    ("{{friend}}", 3, "training"),
    ("{{mentor}}", 10, "retired")
]

roster_dict = {
    "{{hero}}": {"level": 5, "status": "active"},
    "{{heroine}}": {"level": 7, "status": "active"},
    "{{friend}}": {"level": 3, "status": "training"},
    "{{mentor}}": {"level": 10, "status": "retired"}
}

print(">>> PART 1: Compare approaches...")
print()
print("List approach result:", lookup_list(roster_list, "{{hero}}"))
print("Dict approach result:", lookup_dict(roster_dict, "{{hero}}"))
print()
print("Your analysis:")
print(analysis_part_1())

print()
print(">>> PART 2: Implement dictionary system...")
print("(Implement create_roster, find_character, find_by_status, find_highest_level)")
print()
# Uncomment after implementing:
# roster = create_roster()
# print(f"Roster: {roster}")
# print(f"Find {{{{hero}}}}: {find_character(roster, '{{hero}}')}")
# print(f"Active characters: {find_by_status(roster, 'active')}")
# print(f"Highest level: {find_highest_level(roster)}")

print()
print(">>> PART 3: Reflect on trade-offs...")
print()
print("Your reflection:")
print(analysis_part_3())

print()
print("=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print("=" * 60)
