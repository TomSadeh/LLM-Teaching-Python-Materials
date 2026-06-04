# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תחקרי פונקציות מתקדמות של מודול `random`
# מעבר ל-`randint()` שכבר מכירה. הן חיוניות
# למשחקים, סימולציות וכל פיצ'ר אקראי שתרצי לבנות.
#
# נושא: מודול random מורחב (`choice`, `shuffle`, `sample`)
# רמת קושי: 2

# %%
import random

# %% [markdown]
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# למדי את `random.choice()` — בחירת פריט אקראי מתוך רצף.
#
# 1. צרי רשימת אפשרויות:
#    `options = ["{{spell1}}", "{{spell2}}", "{{spell3}}", "{{spell4}}"]`
#
# 2. השתמשי ב-`random.choice()` לבחור אחת:
#    `selected = random.choice(options)`
#
# 3. הדפיסי: `"Selected: [selected]"`
#
# 4. בצעי 5 בחירות אקראיות והדפיסי כל אחת
#    השתמשי בלולאה: `for i in range(5):`
#
# > רמז: `choice()` עובדת עם כל רצף — רשימה, מחרוזת, קבוצה (tuple)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# למדי את `random.shuffle()` — ערבוב סדר הפריטים ברשימה.
#
# 1. צרי רשימה לערבוב:
#    `items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
#
# 2. הדפיסי את הרשימה המקורית:
#    `print(f"Original: {items}")`
#
# 3. ערבבי את הרשימה במקום (IN PLACE):
#    `random.shuffle(items)`
#
# 4. הדפיסי את הרשימה המעורבבת:
#    `print(f"Shuffled: {items}")`
#
# 5. צרי וערבבי רשימת דמויות:
#    `characters = ["{{hero}}", "{{heroine}}", "{{friend}}", "{{mentor}}"]`
#    `random.shuffle(characters)`
#    `print(f"Turn order: {characters}")`
#
# > רמז: `shuffle()` מחזירה `None` — היא משנה את הרשימה המקורית ישירות

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# למדי את `random.sample()` — בחירת מספר פריטים ייחודיים.
#
# 1. צרי מאגר פריטים:
#    `pool = ["{{item}}", "gold", "gem", "key", "scroll", "potion"]`
#
# 2. שלפי 3 פריטים ייחודיים (ללא חזרות):
#    `rewards = random.sample(pool, 3)`
#    `print(f"You found: {rewards}")`
#
# 3. ההבדל בין `choice()` ל-`sample()`:
#    - `choice()` בוחרת פריט אחד
#    - `sample(list, n)` בוחרת n פריטים ייחודיים
#    - `sample()` לא משנה את הרשימה המקורית
#
# 4. נסי לשלוף מתוך טווח:
#    `lottery = random.sample(range(1, 50), 6)`
#    `print(f"Lottery numbers: {sorted(lottery)}")`
#
# 5. מה יקרה אם תנסי `sample(pool, 10)`?
#    (אי אפשר לשלוף יותר פריטים ממה שיש — זו שגיאה!)
#    פשוט הדפיסי: `"Can't sample 10 from a list of 6 items"`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_PROJECT_INTRO}}")
print("=" * 50)

print("\n=== {{PHASE_1_TITLE}} ===")
print("random.choice() - Pick one random item")
exercise_a()

print("\n=== {{PHASE_2_TITLE}} ===")
print("random.shuffle() - Randomize order")
exercise_b()

print("\n=== {{PHASE_3_TITLE}} ===")
print("random.sample() - Pick multiple unique items")
exercise_c()

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
print()
print("Summary:")
print("  choice(seq)      -> 1 random item")
print("  shuffle(list)    -> reorder in place")
print("  sample(seq, n)   -> n unique items (new list)")
