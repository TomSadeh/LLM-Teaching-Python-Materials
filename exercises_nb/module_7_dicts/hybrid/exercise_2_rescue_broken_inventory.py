# %% [markdown]
# {{CONTEXT_SETBACK_INTRO}}
#
# זו תרגילה רב-חלקית שבה תצילי מערכת מלאי שבורה.
# תאבחני את השגיאות, תעקבי אחרי הבעיה, ותתקני אותה כמו שצריך.
#
# מושגי תכנות: מילונים, `KeyError`, `.get()`, דפוסי גישה בטוחה
#
# ## חלק 1: הכישלון - אבחון הקריסה
# {{CONTEXT_SETBACK_NARRATIVE}}
#
# מערכת המלאי קורסת! קראי את הודעת השגיאה
# והביני מה השתבש.
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "inventory.py", line 15, in <module>
#     use_item(inventory, "{{spell3}}")
#   File "inventory.py", line 8, in use_item
#     inventory[item_name] -= 1
# KeyError: '{{spell3}}'

# %%
# This crashes when item_name doesn't exist!
inventory[item_name] -= 1
print(f"Used one {{{{item_name}}}}. Remaining: {inventory[item_name]}")

# %% [markdown]
# ענִי על השאלות הבאות בתגובות:
#
# 1. איזה סוג שגיאה התרחשה?
#    תשובה:
#
# 2. באיזה שורה התרחשה השגיאה?
#    תשובה:
#
# 3. למה השגיאה הזאת קרתה?
#    תשובה:
#
# 4. לאיזה פריט הקוד ניסה לגשת?
#    תשובה:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: חקירה - מעקב אחרי הבעיה
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# עקבי אחרי רצף הפעולות כדי לראות
# היכן מצב המלאי משתבש.

# %%
inventory = {"{{item}}": 3, "{{spell1}}": 1}

# These work fine
inventory["{{item}}"] -= 1
inventory["{{spell1}}"] -= 1

# This would crash! (commented out)
# inventory["{{spell2}}"] -= 1

print(inventory)

# %% [markdown]
# השלימי את טבלת המעקב:
#
# | שלב | תוכן המלאי                          | הערות                           |
# |-----|-------------------------------------|---------------------------------|
# | 0   | {"{{item}}": 3, "{{spell1}}": 1}    | מצב התחלתי                      |
# | 1   |                                     | אחרי שימוש ב-{{item}}           |
# | 2   |                                     | אחרי שימוש ב-{{spell1}}         |
# | 3   | ???                                 | מה יקרה אם ננסה {{spell2}}?     |
#
# הסבירי: למה שלב 3 יקרוס אם נבטל את ה-`#`?

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: שיפור - תיקון עם `.get()`
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# כתבי מחדש את מערכת המלאי תוך שימוש ב-`.get()` כדי לגרום לה לעמוד בפני שגיאות.
#
# 1. קבלי את הכמות הנוכחית באמצעות `.get(item_name, 0)`
#
# 2. אם הכמות גדולה מ-0:
#    - הפחיתי את המלאי ב-1
#    - הדפיסי: `"Used one [item]. Remaining: [count]"`
#    - החזירי `True`
#
# 3. אחרת:
#    - הדפיסי: `"[item] not available!"`
#    - החזירי `False`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# השתמשי בתבנית: `inventory[item] = inventory.get(item, 0) + quantity`
# הדפיסי: `"Added [quantity] [item]. Total: [new_total]"`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# השתמשי ב-`.get()` כדי להחזיר את הכמות בצורה בטוחה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 4: בדיקת המערכת המתוקנת

# %%
print("=== Testing Fixed Inventory System ===")
print()

inventory = {}

# Add some items
print("--- Adding items ---")
safe_add_item(inventory, "{{item}}", 3)
safe_add_item(inventory, "{{spell1}}", 2)
safe_add_item(inventory, "{{item}}", 1)  # Add more of same item

print()
print(f"Current inventory: {inventory}")
print()

# Use items
print("--- Using items ---")
safe_use_item(inventory, "{{item}}")
safe_use_item(inventory, "{{spell2}}")  # Doesn't exist - should NOT crash!
safe_use_item(inventory, "{{spell1}}")
safe_use_item(inventory, "{{spell1}}")
safe_use_item(inventory, "{{spell1}}")  # Out of stock - should handle gracefully

print()
print(f"Final inventory: {inventory}")

# Check quantities
print()
print("--- Checking inventory ---")
print(f"{{{{item}}}}: {check_inventory(inventory, '{{item}}')}")
print(f"{{{{spell2}}}}: {check_inventory(inventory, '{{spell2}}')}")

# %% [markdown]
# ## תוכנית ראשית

# %%
print("=" * 60)
print("{{CONTEXT_SETBACK_INTRO}}")
print("=" * 60)
print()

print(">>> PART 1: Diagnose the crash...")
print("(Read the error message and complete diagnose_error())")
print()

print(">>> PART 2: Trace the problem...")
print("(Complete trace_the_problem())")
# Uncomment to see actual execution:
# code_to_trace()
print()

print(">>> PART 3: Fix the system...")
print("(Implement safe_use_item, safe_add_item, check_inventory)")
print()

print(">>> PART 4: Test your fixes...")
# Uncomment after implementing Part 3:
# test_fixed_inventory()

print()
print("=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print("=" * 60)
