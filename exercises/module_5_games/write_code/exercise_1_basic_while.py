# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# נושא: לולאות `while` בסיסיות עם משתני מונה
# רמת קושי: 1-2
#
# בתרגיל הזה תלמדי את התבנית הבסיסית של לולאות `while`:
# הגדרת מונה, בדיקת תנאי ועדכון המונה.
#
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# לולאת `while` חוזרת כל עוד התנאי שלה הוא `True`.
# התבנית: אתחול ← בדיקת תנאי ← עבודה ← עדכון
#
# 1. צרי משתנה בשם `count` שמתחיל ב-5
# 2. כל עוד `count` גדול מ-0:
#    - הדפיסי את ערך `count` הנוכחי
#    - הקטיני את `count` ב-1
# 3. אחרי הלולאה, הדפיסי את `"{{exclamation}}"`
#
# > רמז: אל תשכחי להקטין את `count`, אחרת הלולאה לעולם לא תסתיים!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# לולאות `while` מעולות לספירה עד ערך יעד.
#
# 1. צרי משתנה בשם `current` שמתחיל ב-1
# 2. כל עוד `current` קטן מ- או שווה ל-`target`:
#    - הדפיסי את `current`
#    - הגדילי את `current` ב-1

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# לולאות `while` יכולות לעקוב אחרי סכומים כשהן רצות.
#
# 1. אתחלי: `total = 0`, `next_number = 1`, `count = 0`
# 2. כל עוד `total + next_number <= limit`:
#    - הוסיפי את `next_number` ל-`total`
#    - הגדילי את `count` ב-1
#    - הגדילי את `next_number` ב-1
# 3. החזירי `(total, count)`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# לולאות `while` עם מספר תנאים בעזרת `and` או `or`.
#
# 1. אתחלי: `items_left = items_to_process`, `iterations = 0`
# 2. כל עוד `items_left > 0` וגם `iterations < max_iterations`:
#    - הקטיני את `items_left` ב-1
#    - הגדילי את `iterations` ב-1
#    - הדפיסי `f"Processed item. {items_left} remaining."`
# 3. החזירי `(iterations, iterations)`  # פריטים שעובדו = iterations

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_5_TITLE}}
# {{CONTEXT_PHASE_5}}
#
# איסוף תוצאות ברשימה תוך כדי ריצת הלולאה.
#
# 1. צרי רשימה ריקה בשם `sequence`
# 2. קבעי `current = start`
# 3. כל עוד `len(sequence) < length`:
#    - הוסיפי את `current` לרשימה `sequence`
#    - הכפילי את `current` ב-`multiplier`
# 4. החזירי את `sequence`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_PROJECT_INTRO}}")
print("=" * 50)

print("\n=== {{PHASE_1_TITLE}} ===")
print("Countdown:")
countdown_from_five()

print("\n=== {{PHASE_2_TITLE}} ===")
print("Counting to 5:")
count_up_to(5)

print("\n=== {{PHASE_3_TITLE}} ===")
result = sum_until_limit(10)
print(f"Sum until 10: {result}")

print("\n=== {{PHASE_4_TITLE}} ===")
print("Processing batch of 7 items with max 5 iterations:")
result = process_batch(7, 5)
print(f"Result: {result}")

print("\n=== {{PHASE_5_TITLE}} ===")
seq = generate_sequence(2, 3, 5)
print(f"Sequence: {seq}")

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
