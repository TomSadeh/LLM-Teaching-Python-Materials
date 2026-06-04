# =============================================================================
# Hybrid Exercise: The Inheritance - The Sorting System
# =============================================================================
# Difficulty: 3-4
# Arc: The Inheritance
# Parts: DISCOVERY -> OWNERSHIP -> INVESTIGATION
# Concepts: if/elif/else, understanding existing code, extending systems
# =============================================================================

# %% [markdown]
# {{CONTEXT_DISCOVERY_INTRO}}
#
# זוהי תרגילה בת מספר חלקים. השלימי כל חלק לפי הסדר.
#
# ## חלק 1: גילוי - הבן את הקוד הקיים
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# {{mentor}} עזב את {{school}} והעביר ל-{{hero}} את מערכת המיון שלו.
# למדי איך היא עובדת לפני שתוכלי להרחיב אותה.

# %% locked
# The old sorting system for {{school}}
# It assigns students to houses based on their primary attribute score

# Example student data
student = "{{friend}}"
courage = 70
wisdom = 85
kindness = 60

# Find the highest attribute
if courage > wisdom and courage > kindness:
    house = "House of Warriors"
    trait = "courage"
elif wisdom > courage and wisdom > kindness:
    house = "House of Scholars"
    trait = "wisdom"
else:
    house = "House of Healers"
    trait = "kindness"

print(f"{student} sorted into {house}")
print(f"Dominant trait: {trait}")

# %% [markdown]
# למדי את `inherited_sorting_system` וענעי על השאלות הבאות:
#
# 1. לכמה בתים אפשר למיין תלמידים? ___
#
# 2. מה קורה אם `courage = 70`, `wisdom = 85`, `kindness = 60`?
#    - `courage > wisdom`? (70 > 85) _____ (True/False)
#    - `wisdom > courage`? (85 > 70) _____ (True/False)
#    - `wisdom > kindness`? (85 > 60) _____ (True/False)
#    - לאיזה בית? _____________________
#
# 3. מה קורה אם שני מאפיינים שווים ומובילים?
#    לדוגמה: `courage = 80`, `wisdom = 80`, `kindness = 60`
#    - `courage > wisdom`? (80 > 80) _____ (True/False)
#    - התנאי הראשון נכשל, בודקים `elif`...
#    - `wisdom > courage`? (80 > 80) _____ (True/False)
#    - גם ה-`elif` נכשל, אז... _____________________
#
# 4. האם זה הוגן? מה קורה אם `kindness` היא בעצם הנמוכה ביותר אבל בכל זאת מוקצית?
#    _____________________________________________________

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: בעלות - הוסיפי תכונה משלך
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# {{hero}} רוצה להוסיף בית חדש: `"House of Adventurers"` לתלמידים
# שהתכונה הגבוהה ביותר שלהם היא `bravery`. הרחיבי את המערכת!
#
# צרי מערכת מיון משופרת עם ארבעה בתים:
# - `House of Warriors` (כאשר `courage` הגבוה ביותר)
# - `House of Scholars` (כאשר `wisdom` הגבוה ביותר)
# - `House of Healers` (כאשר `kindness` הגבוה ביותר)
# - `House of Adventurers` (כאשר `bravery` הגבוה ביותר) <-- חדש!
#
# 1. צרי משתנים לתלמידת בדיקה:
#    `student = "{{hero}}"`
#    `courage = 60`
#    `wisdom = 70`
#    `kindness = 55`
#    `bravery = 85`  <-- תכונה חדשה
#
# 2. כתבי `if`/`elif`/`elif`/`elif`/`else` כדי למצוא את הגבוה ביותר:
#    (תצטרכי לבדוק 4 תנאים)
#    - אם `bravery` הגבוה מכל 4: `"House of Adventurers"`
#    - אחרת אם `courage` הגבוה: `"House of Warriors"`
#    - אחרת אם `wisdom` הגבוה: `"House of Scholars"`
#    - אחרת אם `kindness` הגבוה: `"House of Healers"`
#    - אחרת: `"House of Balance"` (לשוויון או מקרי קצה)
#
# 3. הדפיסי את התוצאה
#
# > רמז: כדי לבדוק אם `bravery` הגבוה מכל 4:
# >       `if bravery > courage and bravery > wisdom and bravery > kindness:`
#
# פלט צפוי עבור ערכי הבדיקה:
#   `{{hero}} sorted into House of Adventurers`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: חקירה - מצאי את הבאג הנסתר
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# {{hero}} מגלה שבמערכת המקורית יש באג שגורם
# למיון לא הוגן במקרים מסוימים. מצאי והביני אותו!

# %%
# What if ALL traits are equal?
student = "{{villain}}"
courage = 75
wisdom = 75
kindness = 75

# Original logic:
if courage > wisdom and courage > kindness:
    house = "House of Warriors"
elif wisdom > courage and wisdom > kindness:
    house = "House of Scholars"
else:
    house = "House of Healers"

print(f"{student}: courage={courage}, wisdom={wisdom}, kindness={kindness}")
print(f"Sorted into: {house}")
print("Is this fair when all traits are equal?")

# %% [markdown]
# עיקבי אחרי הבאג:
#
# כאשר `courage = 75`, `wisdom = 75`, `kindness = 75`:
#
# בדיקה 1: `courage > wisdom AND courage > kindness`
#           75 > 75 = _____ AND 75 > 75 = _____
#           ביחד: _____ AND _____ = _____ (True/False)
#           הענף הראשון מתבצע? _____
#
# בדיקה 2: `wisdom > courage AND wisdom > kindness`
#           75 > 75 = _____ AND 75 > 75 = _____
#           ביחד: _____ AND _____ = _____
#           הענף השני מתבצע? _____
#
# מכיוון ששני התנאים הם `False`, מה רץ? _____
#
# הבאג: כאשר כל התכונות שוות, התלמידה מוקצית ל-
# _____________________ למרות ש-`kindness` לא בהכרח החוזק שלה!
#
# גישה טובה יותר תהיה: _____________________________________

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# תקני את הבאג:
#
# צרי מערכת הוגנת יותר שמטפלת בשוויון במפורש.
#
# 1. צרי ערכי תכונות שווים:
#    `student = "{{friend}}"`
#    `courage = 75`
#    `wisdom = 75`
#    `kindness = 75`
#
# 2. בדקי קודם שוויון (כל התכונות שוות):
#    `if courage == wisdom and wisdom == kindness:`
#        הדפיסי `f"{student} has balanced traits!"`
#        הדפיסי `"Special placement: House of Balance"`
#
# 3. אחרת, השתמשי בלוגיקה המקורית עם `elif`:
#    `elif courage > wisdom and courage > kindness:`
#        ... (Warriors)
#    `elif wisdom > courage and wisdom > kindness:`
#        ... (Scholars)
#    `else:`
#        ... (Healers)
#
# פלט צפוי כאשר כל התכונות הן 75:
#   `{{friend}} has balanced traits!`
#   `Special placement: House of Balance`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("=" * 50)
print("PART 1: DISCOVERY - Understand the Inherited Code")
print("=" * 50)

print("\n--- inherited_sorting_system ---")
inherited_sorting_system()

print("\n--- Your Understanding ---")
your_understanding()

print("\n" + "=" * 50)
print("PART 2: OWNERSHIP - Add Your Own Feature")
print("=" * 50)

print("\n--- your_extended_system ---")
your_extended_system()

print("\n" + "=" * 50)
print("PART 3: INVESTIGATION - Find the Hidden Bug")
print("=" * 50)

print("\n--- buggy_edge_case ---")
buggy_edge_case()

print("\n--- trace_the_bug ---")
trace_the_bug()

print("\n--- your_fixed_system ---")
# your_fixed_system()  # Uncomment after fixing

print("\n" + "=" * 50)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
