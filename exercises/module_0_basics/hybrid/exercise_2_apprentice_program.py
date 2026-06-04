# =============================================================================
# Hybrid Exercise: The Apprentice - Complete Program
# =============================================================================
# Difficulty: 4-5
# Arc: The Apprentice
# Parts: DISCOVERY -> GUIDANCE -> GROWTH
# Concepts: All Module 0 - variables, strings, numbers, input, f-strings
# =============================================================================

# %% [markdown]
# {{CONTEXT_DISCOVERY_INTRO}}
#
# זו תרגיל מרובה-חלקים. השלימי כל חלק לפי הסדר.
# תלמדי תוכנית שלמה, תתרגלי עם הנחיות, ואז תבני משלך!
#
# ## חלק 1: גילוי - לומדים את תוכנית המאסטר
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# למדי את תוכנית יצירת הדמות המלאה הזו.
# נסי לנחש מה היא תעשה לפני שתריצי אותה.

# %% locked
# Character setup
name = "{{hero}}"
character_class = "Apprentice"

# Stats
health = 100
strength = 10
defense = 8

# Calculated stats
power = strength + defense

# Display character sheet
print(f"=== {name} the {character_class} ===")
print(f"Health: {health}")
print(f"Strength: {strength}")
print(f"Defense: {defense}")
print(f"Power Rating: {power}")
print("=" * 30)

# %% [markdown]
# לפני שתריצי את התוכנית, נחשי:
#
# 1. כמה שורות יודפסו? ___
# 2. מה יהיה ה-`Power Rating`? ___
# 3. איזה סוג מרכאות התוכנית משתמשת בפלט? ___
#
# הריצי את התוכנית כדי לבדוק את הניחושים שלך!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: הנחיה - תרגול עם פיגומים
# {{CONTEXT_GUIDANCE_INTRO}}
# {{CONTEXT_GUIDANCE_NARRATIVE}}
#
# השלימי את הפונקציות האלה על ידי מילוי החלקים החסרים.
#
# השתמשי ב-f-string כדי ליצור את הכותרת.
# תבנית: `"=== {name} the {title} ==="`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# השתמשי ב-f-string: `f"{stat_name}: {stat_value}"`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: צמיחה - יוצרים משלך
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# עכשיו צרי תוכנית יצירת דמות משלך מאפס!
#
# דרישות:
# 1. צרי לפחות 5 משתנים (שם, מחלקה, ו-3+ סטטיסטיקות)
# 2. חשבי לפחות סטטיסטיקה נגזרת אחת (כמו `power = str + def`)
# 3. השתמשי ב-f-strings לכל הפלט
# 4. הדפיסי כותרת עם שם הדמות והמחלקה שלה
# 5. הדפיסי את כל הסטטיסטיקות בצורה מסודרת
# 6. הדפיסי קו מפריד בסוף
#
# דוגמה לפלט:
# `=== Maya the {{ROLE_TITLE}} ===`
# `Health: 120`
# `Strength: 15`
# `Defense: 12`
# `Speed: 8`
# `Total Power: 27`
# `==============================`
#
# היי יצירתית! הוסיפי סטטיסטיקות וסגנון משלך.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## אתגר בונוס
#
# צרי גרסה אינטראקטיבית שמבקשת קלט מהמשתמשת!
#
# השתמשי ב-`input()` כדי לשאול על:
# - שם הדמות
# - מחלקת הדמות
# - לפחות ערך סטטיסטיקה אחד
#
# ואז הציגי את דף הדמות באמצעות f-strings.
#
# דוגמה לאינטראקציה:
# `Enter character name: Luna`
# `Enter character class: {{ROLE_TITLE}}`
# `Enter power level: 25`
#
# `=== Luna the {{ROLE_TITLE}} ===`
# `Power Level: 25`
# `(etc...)`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("=" * 50)
print("PART 1: DISCOVERY - Study the Master's Program")
print("=" * 50)

print("\n--- master_program output ---")
master_program()

print("\n--- Your Predictions ---")
your_predictions()

print("\n" + "=" * 50)
print("PART 2: GUIDANCE - Practice with Scaffolding")
print("=" * 50)

print("\n--- Testing guided_character_header ---")
result1 = guided_character_header("{{hero}}", "{{ROLE_TITLE}}")
print("Result:", result1)
print("Expected: === {{hero}} the {{ROLE_TITLE}} ===")

print("\n--- Testing guided_stat_line ---")
result2 = guided_stat_line("Health", 100)
print("Result:", result2)
print("Expected: Health: 100")

print("\n" + "=" * 50)
print("PART 3: GROWTH - Create Your Own")
print("=" * 50)

print("\n--- my_character_creator ---")
my_character_creator()

print("\n--- my_interactive_creator (BONUS) ---")
# Uncomment to test interactive version:
# my_interactive_creator()
print("(Uncomment the line above to test!)")

print("\n" + "=" * 50)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
