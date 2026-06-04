# %% [markdown]
# {{CONTEXT_EVALUATION_INTRO}}
#
# This is a multi-part exercise comparing different data structure approaches
# for a character management system. Build, compare, and choose wisely!
#
# Programming concepts: dictionaries, nested data, data design trade-offs
#
# PART 1: Evaluation - Compare Data Structures
# {{CONTEXT_EVALUATION_NARRATIVE}}
#
# Two approaches exist for storing character data.
# Which is better for different operations?
#
# ## Approach A: List of Dictionaries

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
# ## Approach B: Dictionary of Dictionaries

# %%
characters_dict = {
    "{{hero}}": {"level": 5, "health": 100, "class": "warrior"},
    "{{heroine}}": {"level": 7, "health": 120, "class": "mage"},
    "{{friend}}": {"level": 3, "health": 80, "class": "rogue"}
}

# %%
return char_dict.get(name)

# %% [markdown]
# ✏️ YOUR ANALYSIS ✏️

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
# PART 2: Growth - Build with Dictionary Approach
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Implement a complete character management system using dictionaries.
#
# ✏️ YOUR CODE HERE ✏️

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Check if name already exists.
# If new, add with all attributes and return True.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Check if character exists.
# If found, increase level by 1 and health by 10.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Iterate through db.items() and collect matching names.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 3: Growth - Add Advanced Operations
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Implement more complex operations that benefit from the dict structure.
#
# ✏️ YOUR CODE HERE ✏️
#
# Iterate and track the highest level seen.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Count characters and sum levels by class
# Step 2: Calculate averages
#
# Result format: {"warrior": {"count": 2, "avg_level": 6.0}, ...}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Check both characters exist.
# Check source has enough health.
# Transfer the health.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 4: Evaluation - Final Comparison
# {{CONTEXT_EVALUATION_NARRATIVE}}
#
# Reflect on when each approach is best.
#
# ✏️ YOUR FINAL EVALUATION ✏️

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
# ## MAIN

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
