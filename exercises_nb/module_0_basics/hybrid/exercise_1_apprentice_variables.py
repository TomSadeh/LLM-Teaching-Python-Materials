# =============================================================================
# Hybrid Exercise: The Apprentice - Variables and Strings
# =============================================================================
# Difficulty: 3
# Arc: The Apprentice
# Parts: DISCOVERY -> GUIDANCE -> GROWTH
# Concepts: variables, strings, concatenation, printing
# =============================================================================

# %% [markdown]
# {{CONTEXT_DISCOVERY_INTRO}}
#
# זוהי תרגילה מרובת חלקים. השלימי כל חלק לפי הסדר.
#
# ## חלק 1: גילוי - לימדי מהמורה
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# למדי כיצד המורה של {{hero}} משתמשת במשתנים ומחרוזות.
# נסי לנחש את הפלט לפני שתריצי את הקוד.

# %% locked
title = "Apprentice"
name = "{{hero}}"
full_title = title + " " + name
print(full_title)

# %% locked
school = "{{school}}"
year = 1
print(school, "- Year", year)

# %% locked
item = "{{item}}"
owner = "{{hero}}"
description = "The " + item + " belongs to " + owner
print(description)

# %% [markdown]
# כתבי בדיוק מה כל פונקציית master_code תדפיס.
#
# פלט master_code_1: _______________
# פלט master_code_2: _______________
# פלט master_code_3: _______________
#
# > רמז: שימי לב לרווחים - מאין הם מגיעים?

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: הכוונה - תרגול עם תמיכה
# {{CONTEXT_GUIDANCE_INTRO}}
# {{CONTEXT_GUIDANCE_NARRATIVE}}
#
# עכשיו תתרגלי עם קצת עזרה.
#
# השלימי את החסר:
#
# צרי משתנים והשתמשי בהם כמו שהמורה עשתה.
#
# role = "Guardian"
# hero = "{{hero}}"
# title = role ___ " " ___ hero     # Fill in the operator to join strings
# print(title)
#
# > רמז: השתמשי ב-`+` כדי לחבר (לשרשר) מחרוזות.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# השלימי את החסר:
#
# הדפיסי מספר פריטים עם רווח אוטומטי ביניהם.
#
# location = "{{school}}"
# status = "training"
# print(___,  "is now", ___)        # Fill in the variable names
#
# > רמז: הדפיסי את המשתנים `location` ו-`status`.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: צמיחה - צרי בעצמך
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# עכשיו צרי קוד משלך עם מה שלמדת!
#
# צרי הצגת דמות.
#
# 1. צרי משתנה `hero_name` עם הערך "{{hero}}"
# 2. צרי משתנה `class_type` עם הערך "{{ROLE_TITLE}}"
# 3. צרי משתנה `intro` שמשלב: hero_name + " the " + class_type
# 4. הדפיסי את `intro`
#
# פלט צפוי: {{hero}} the {{ROLE_TITLE}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# צרי דוח סטטוס עבור {{hero}}.
#
# 1. צרי `location` עם הערך "{{school}}"
# 2. צרי `health` עם הערך 100 (מספר!)
# 3. צרי `gold` עם הערך 50 (מספר!)
# 4. הדפיסי עם פסיקים: "Location:", location
# 5. הדפיסי עם פסיקים: "Health:", health, "Gold:", gold
#
# פלט צפוי:
# Location: {{school}}
# Health: 100 Gold: 50

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("=" * 50)
print("PART 1: DISCOVERY - Study the Master's Work")
print("=" * 50)

print("\n--- master_code_1 ---")
master_code_1()

print("\n--- master_code_2 ---")
master_code_2()

print("\n--- master_code_3 ---")
master_code_3()

print("\n--- Your Predictions ---")
your_predictions()

print("\n" + "=" * 50)
print("PART 2: GUIDANCE - Practice with Support")
print("=" * 50)

print("\n--- guided_exercise_a ---")
# guided_exercise_a()  # Uncomment when blanks are filled

print("\n--- guided_exercise_b ---")
# guided_exercise_b()

print("\n" + "=" * 50)
print("PART 3: GROWTH - Create Your Own")
print("=" * 50)

print("\n--- your_creation_a ---")
your_creation_a()

print("\n--- your_creation_b ---")
your_creation_b()

print("\n" + "=" * 50)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
