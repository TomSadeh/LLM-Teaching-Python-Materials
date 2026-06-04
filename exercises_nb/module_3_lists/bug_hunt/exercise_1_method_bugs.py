# =============================================================================
# Bug Hunt: List Method Bugs
# =============================================================================
# Difficulty: 3
# Concepts: Common mistakes with append, pop, insert, remove
# =============================================================================

# %% [markdown]
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_MISSION}}
#
# ## {{CASE_1_TITLE}}
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# **התנהגות צפויה:**
# בניית רשימת קבוצה והדפסתה.
# פלט צפוי: `['{{hero}}', '{{heroine}}', '{{friend}}']`
#
# **התנהגות בפועל:**
# מדפיס: `None`
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

# %%
team = []
team = team.append("{{hero}}")
team = team.append("{{heroine}}")
team = team.append("{{friend}}")
print(team)

# %%
# FIX THE BUG
#
# What I found: ________________________________
#
# Hint: append() modifies the list IN PLACE and returns None.
# You don't need to reassign the result.
#
# The fix:

pass

# %% [markdown]
# ## {{CASE_2_TITLE}}
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# **התנהגות צפויה:**
# הסרת הפריט `"potion"` מהמלאי.
# פלט צפוי: `After: ['{{item}}', 'key']`
#
# **התנהגות בפועל:**
# `ValueError: list.remove(x): x not in list`
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}

# %%
inventory = ["{{item}}", "potion", "key"]
print(f"Before: {inventory}")
inventory.remove(1)  # BUG: remove() takes a VALUE, not an index!
print(f"After: {inventory}")

# %%
# FIX THE BUG
#
# What I found: ________________________________
#
# Hint: remove() takes a VALUE to find and remove.
# To remove by index, use pop(index) instead.
#
# The fix:

pass

# %% [markdown]
# ## {{CASE_3_TITLE}}
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# **התנהגות צפויה:**
# שליפת הפריט האחרון מהרשימה והדפסת מה שהוסר.
# פלט צפוי:
#   `Removed: {{spell3}}`
#   `Remaining: ['{{spell1}}', '{{spell2}}']`
#
# **התנהגות בפועל:**
#   `Removed: ['{{spell1}}', '{{spell2}}']`
#   `Remaining: {{spell3}}`
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}

# %%
abilities = ["{{spell1}}", "{{spell2}}", "{{spell3}}"]
removed = abilities
abilities = abilities.pop()
print(f"Removed: {removed}")
print(f"Remaining: {abilities}")

# %%
# FIX THE BUG
#
# What I found: ________________________________
#
# Hint: The variables got swapped! pop() returns the removed item.
# The list is modified in place - it doesn't need reassignment.
#
# The fix:

pass

# %% [markdown]
# ## {{CASE_4_TITLE}}
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# **התנהגות צפויה:**
# הוספת `"{{mentor}}"` במיקום 1 (המיקום השני).
# פלט צפוי: `['{{hero}}', '{{mentor}}', '{{heroine}}', '{{friend}}']`
#
# **התנהגות בפועל:**
# מדפיס: `None`
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}

# %%
team = ["{{hero}}", "{{heroine}}", "{{friend}}"]
team = team.insert(1, "{{mentor}}")
print(team)

# %%
# FIX THE BUG
#
# What I found: ________________________________
#
# Hint: Just like append(), insert() modifies the list in place
# and returns None.
#
# The fix:

pass

# %% [markdown]
# ## {{CASE_5_TITLE}}
# {{CONTEXT_CASE_5_NARRATIVE}}
#
# **התנהגות צפויה:**
# הסרת כל המופעים של `"coin"` מהרשימה.
# פלט צפוי: `['{{item}}', 'key']`
#
# **התנהגות בפועל:**
# פלט: `['{{item}}', 'coin', 'key']`  (מטבע אחד נשאר!)
#
# {{CONTEXT_INVESTIGATION_PROMPT_5}}

# %%
items = ["{{item}}", "coin", "coin", "key"]
print(f"Before: {items}")
items.remove("coin")
print(f"After: {items}")

# %%
# FIX THE BUG
#
# What I found: ________________________________
#
# Hint: remove() only removes the FIRST occurrence.
# To remove all, you'd need to call it multiple times.
# (A loop with "in" check, or use a different approach)
#
# The fix (remove both coins):

pass

# %%
print("{{CONTEXT_INVESTIGATION_INTRO}}")
print("=" * 50)

print("\n=== {{CASE_1_TITLE}} ===")
print("Buggy version:")
buggy_a()
print("\nFixed version:")
# fix_a()

print("\n=== {{CASE_2_TITLE}} ===")
print("Buggy version:")
# buggy_b()  # Uncomment to see the error
print("\nFixed version:")
# fix_b()

print("\n=== {{CASE_3_TITLE}} ===")
print("Buggy version:")
buggy_c()
print("\nFixed version:")
# fix_c()

print("\n=== {{CASE_4_TITLE}} ===")
print("Buggy version:")
buggy_d()
print("\nFixed version:")
# fix_d()

print("\n=== {{CASE_5_TITLE}} ===")
print("Buggy version:")
buggy_e()
print("\nFixed version:")
# fix_e()

print("\n" + "=" * 50)
print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
