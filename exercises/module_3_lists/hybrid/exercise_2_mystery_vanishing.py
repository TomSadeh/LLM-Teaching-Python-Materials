# =============================================================================
# Hybrid Exercise: The Mystery - The Vanishing Element
# =============================================================================
# Difficulty: 3
# Arc: Mystery (DISCOVERY -> INVESTIGATION -> IMPROVEMENT)
# Concepts: List mutation, unexpected behavior with methods
# =============================================================================

# %% [markdown]
# {{CONTEXT_DISCOVERY_INTRO}}
#
# זוהי תרגילה בת מספר חלקים. השלימי כל חלק לפי הסדר.
#
# ## חלק 1: גילוי - נצפי בהתנהגות מפתיעה
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# משהו מוזר קורה עם המלאי של {{hero}}.
# למדי את הקוד הזה וחזי מה הוא ידפיס.

# %%
inventory = ["{{item}}", "potion", "key", "map"]
print(f"Step 1 - Start: {inventory}")

# {{hero}} saves the inventory
saved = inventory

# {{heroine}} removes an item
inventory.remove("potion")
print(f"Step 2 - After remove: {inventory}")

# {{hero}} checks saved inventory
print(f"Step 3 - Saved copy: {saved}")

# %% [markdown]
# ## הניחושים שלך:
# 1. שלב 1 - התחלה: _______________
# 2. שלב 2 - אחרי `remove`: _______________
# 3. שלב 3 - העתק השמור: _______________
#
# הפתעה: האם גם המלאי ה"שמור" השתנה? למה?

# %%
# RECORD YOUR OBSERVATIONS
#
# After running the code, answer these questions:

observations = {
    "did_saved_change": "?",  # "yes" or "no"
    "why_do_you_think": "Because...",
    "is_saved_independent": "?",  # "yes" or "no"
}

return observations

# %% [markdown]
# ## חלק 2: חקירה - עקבי אחרי הקוד כדי למצוא את הסיבה
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# עקבי אחרי הקוד הזה שלב אחרי שלב כדי להבין למה
# שני המשתנים מצביעים על אותה רשימה.

# %%
original = ["A", "B", "C"]
print(f"Original ID: {id(original)}")

# Assignment creates an ALIAS, not a copy!
alias = original
print(f"Alias ID: {id(alias)}")
print(f"Same object? {original is alias}")

# Modifying one affects both
original.append("D")
print(f"Original: {original}")
print(f"Alias: {alias}")

# %%
# FILL IN THE TRACING TABLE
#
# Track what happens at each step.
#
# | Step | original        | alias           | Are they the same object? |
# |------|-----------------|-----------------|---------------------------|
# | 1    | ['A','B','C']   | -               | -                         |
# | 2    | ['A','B','C']   | points to same  | Yes (same id)             |
# | 3    | ?               | ?               | ?                         |
#
# Key insight: "alias = original" does NOT copy the list.
# Both variables point to the SAME list in memory.

pass

# %% [markdown]
# ## חלק 3: שיפור - תקני את הבאג
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# עכשיו תקני את התעלומה המקורית! {{hero}} רוצה לשמור
# גיבוי אמיתי של המלאי לפני ש-{{heroine}} מסירה פריטים.

# %%
inventory = ["{{item}}", "potion", "key", "map"]
print(f"Original: {inventory}")

# BUG: This creates an alias, not a copy!
backup = inventory

inventory.remove("potion")
inventory.remove("key")
print(f"Modified: {inventory}")
print(f"Backup: {backup}")  # Oops! Backup changed too!

# %%
# FIX THE BUG
#
# There are multiple ways to create a TRUE copy:
# 1. backup = inventory[:]      (slice creates a copy)
# 2. backup = list(inventory)   (list() creates a copy)
# 3. backup = inventory.copy()  (explicit copy method)
#
# Choose one and implement the fix:

inventory = ["{{item}}", "potion", "key", "map"]
print(f"Original: {inventory}")

# YOUR CODE HERE
# Create a REAL backup (not an alias)
backup = None  # Fix this line!

inventory.remove("potion")
inventory.remove("key")
print(f"Modified: {inventory}")
print(f"Backup: {backup}")  # Should still have all 4 items!

pass

# %%
# VERIFICATION
#
# After fixing, the output should be:
# Original: ['{{item}}', 'potion', 'key', 'map']
# Modified: ['{{item}}', 'map']
# Backup: ['{{item}}', 'potion', 'key', 'map']
#
# The backup should be UNCHANGED!

pass

# %%
print("=" * 60)
print("THE MYSTERY: The Vanishing Element")
print("=" * 60)

print("\n--- PART 1: DISCOVERY ---")
print("{{CONTEXT_DISCOVERY_INTRO}}")
print("\nRun this mysterious code:")
mysterious_code()
print("\nYour observations:", part_1_observations())

print("\n--- PART 2: INVESTIGATION ---")
print("{{CONTEXT_INVESTIGATION_INTRO}}")
print("\nTracing the cause:")
investigation_code()

print("\n--- PART 3: IMPROVEMENT ---")
print("{{CONTEXT_IMPROVEMENT_INTRO}}")
print("\nBuggy version:")
buggy_inventory()
print("\nFixed version:")
# fixed_inventory()  # Uncomment after fixing!

print("\n" + "=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
