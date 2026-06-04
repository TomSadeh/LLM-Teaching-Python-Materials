# =============================================================================
# Which is Better: Copy vs Alias
# =============================================================================
# Difficulty: 4
# Concepts: List aliasing, copying, mutability implications
# =============================================================================

# %% [markdown]
# {{CONTEXT_COMPARISON_INTRO}}
# {{CONTEXT_COMPARISON_DECISION}}
#
# {{APPROACH_1_NAME}}
# {{CONTEXT_APPROACH_1_NARRATIVE}}
#
# גרסה א׳: השמה ישירה (יוצרת כינוי)

# %%
backup = inventory  # This creates an ALIAS
return backup

# %%
inventory = ["{{item}}", "potion", "key"]
print(f"Original: {inventory}")

backup = inventory  # Alias!

# Modify original
inventory.append("map")
inventory.remove("potion")

print(f"After modifications:")
print(f"  Inventory: {inventory}")
print(f"  Backup: {backup}")
print(f"  Same object? {inventory is backup}")

# %% [markdown]
# {{APPROACH_2_NAME}}
# {{CONTEXT_APPROACH_2_NARRATIVE}}
#
# גרסה ב׳: העתקה עם פרוסה (יוצרת עותק עצמאי)

# %%
backup = inventory[:]  # This creates a COPY
return backup

# %%
inventory = ["{{item}}", "potion", "key"]
print(f"Original: {inventory}")

backup = inventory[:]  # Copy!

# Modify original
inventory.append("map")
inventory.remove("potion")

print(f"After modifications:")
print(f"  Inventory: {inventory}")
print(f"  Backup: {backup}")
print(f"  Same object? {inventory is backup}")

# %% [markdown]
# {{APPROACH_3_NAME}}
# {{CONTEXT_APPROACH_3_NARRATIVE}}
#
# גרסה ג׳: הבנאי `list()` (גם הוא יוצר עותק)

# %%
backup = list(inventory)  # This creates a COPY
return backup

# %% [markdown]
# ## הניתוח שלך

# %%
# YOUR ANALYSIS
#
# Consider these questions:
# 1. When would you WANT changes to affect both variables?
# 2. When would you NEED an independent copy?
# 3. Is there a performance difference?

analysis = """
When to use ALIAS (direct assignment):
-

When to use COPY (slice or list()):
-

Performance consideration:
-

Most common mistake beginners make:
-
"""
return analysis

# %% [markdown]
# השוואה 2: העברת רשימות לפונקציות
#
# מה קורה כשמעבירים רשימה לפונקציה?

# %%
items.append("new item")
items[0] = "changed"

# %% [markdown]
# ## אין צורך ב-`return` — המקור עצמו משתנה

# %%
result = items[:]  # Work on a copy
result.append("new item")
result[0] = "changed"
return result

# %%
print("=== Version 1: Direct Modification ===")
inventory1 = ["{{item}}", "potion"]
print(f"Before: {inventory1}")
modify_in_function_v1(inventory1)
print(f"After: {inventory1}")

print("\n=== Version 2: Copy and Return ===")
inventory2 = ["{{item}}", "potion"]
print(f"Before: {inventory2}")
new_inventory = modify_in_function_v2(inventory2)
print(f"Original after: {inventory2}")
print(f"Returned: {new_inventory}")

# %%
# YOUR ANALYSIS
#
# Which approach is better for functions?

analysis = """
Version 1 (modify in place) is better when:
-

Version 2 (copy and return) is better when:
-

Which is safer for beginners?
-

Which is more "functional" style?
-
"""
return analysis

# %% [markdown]
# ## השוואה 3: בנייה הדרגתית לעומת יצירה ישירה

# %%
items = []
items.append("{{item}}")
items.append("potion")
items.append("key")
return items

# %%
items = []
new_items = ["{{item}}", "potion", "key"]
items = items + new_items  # Creates a new list
return items

# %%
items = ["{{item}}", "potion", "key"]
return items

# %%
# YOUR ANALYSIS
#
# All three create the same result. Which is best?

analysis = """
Version 1 (append one by one):
- Good when:
- Less ideal when:

Version 2 (concatenation):
- Good when:
- Less ideal when:

Version 3 (direct creation):
- Good when:
- Less ideal when:

General recommendation:
-
"""
return analysis

# %%
print("{{CONTEXT_COMPARISON_INTRO}}")
print("=" * 50)

print("\n=== COMPARISON 1: Alias vs Copy ===")
print("\nVersion A (Alias):")
demo_alias()
print("\nVersion B (Copy):")
demo_copy()
print(f"\nYour analysis:{analysis_backup()}")

print("\n=== COMPARISON 2: Functions ===")
demo_function_modifications()
print(f"\nYour analysis:{analysis_function()}")

print("\n=== COMPARISON 3: Building Lists ===")
print(f"V1 result: {collect_items_v1()}")
print(f"V2 result: {collect_items_v2()}")
print(f"V3 result: {collect_items_v3()}")
print(f"\nYour analysis:{analysis_building()}")

print("\n" + "=" * 50)
print("{{CONTEXT_EVALUATION_COMPLETE}}")
