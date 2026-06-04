# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# נושא: שימוש במודול `random`
# רמת קושי: 2-3
#
# המודול `random` מאפשר לך לייצר מספרים אקראיים ולבחור פריטים באקראי.
# הכרחי למשחקים עם אלמנטים של הפתעה!

# %%
import random

# %% [markdown]
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# `random.randint(a, b)` מחזירה מספר שלם אקראי בין a ל-b כולל.
# בניגוד ל-`range()`, שני הקצוות נכללים!
#
# השתמשי ב-`random.randint(1, num_sides)` כדי לקבל מספר בין 1 ל-num_sides

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. אתחלי `total = 0`
# 2. עברי בלולאה `num_dice` פעמים
# 3. הוסיפי לזריקה אקראית ל-`total`
# 4. החזירי את `total`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# `random.choice(sequence)` בוחרת פריט אקראי מרשימה או מחרוזת.
#
# השתמשי ב-`random.choice(items)`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. צרי את רשימת התארים (adjectives)
# 2. צרי את רשימת השמות (nouns)
# 3. בחרי תואר אקראי עם `random.choice()`
# 4. בחרי שם אקראי עם `random.choice()`
# 5. החזירי `f"{adjective} {noun}"`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# `random.random()` מחזירה מספר עשרוני בין 0.0 ל-1.0 (לא כולל 1.0).
# שימושי לחישוב סיכויים באחוזים.
#
# אם `random.random() < probability`, החזירי `True`
# אחרת החזירי `False`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# השתמשי ב-`chance_event()` כדי לבדוק אם הפעולה הצליחה
# הדפיסי את ההודעה המתאימה
# החזירי `"success"` או `"failure"`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# שלבי פונקציות `random` שונות כדי ליצור מכניקות משחק.
#
# 1. קבלי מספר עשרוני אקראי עם `random.random()`
# 2. עקבי אחר ההסתברות המצטברת
# 3. עברי בלולאה על האפשרויות והמשקלים יחד
#    - הוסיפי את המשקל למצטבר
#    - אם הערך האקראי < המצטבר, החזירי את האפשרות הנוכחית
# 4. החזירי את האפשרות האחרונה (ביטחון)
#
# > רמז: השתמשי ב-`zip(options, weights)` כדי לעבור על שניהם יחד

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. הגדירי רשימת נדירויות (rarities) ומשקלים (weights)
# 2. השתמשי ב-`weighted_random_choice` כדי לבחור נדירות
# 3. צרי שם פריט על פי הנדירות שנבחרה
# 4. החזירי `(item_name, rarity)`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_5_TITLE}}
# {{CONTEXT_PHASE_5}}
#
# ייצרי מספרים אקראיים בטווחים שונים לתרחישי משחק.
#
# 1. ייצרי כל סטטיסטיקה בסיסית עם `random.randint()`
# 2. חשבי סטטיסטיקות נגזרות
# 3. החזירי מילון עם כל הסטטיסטיקות

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# חשבי את נזק התוקף
# חשבי את נזק המגן
# החזירי את שניהם כ-tuple

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_PROJECT_INTRO}}")
print("=" * 50)

print("\n=== {{PHASE_1_TITLE}} ===")
print(f"Rolling a 6-sided die: {roll_dice(6)}")
print(f"Rolling a 20-sided die: {roll_dice(20)}")
print(f"Rolling 3d6: {roll_multiple_dice(3, 6)}")

print("\n=== {{PHASE_2_TITLE}} ===")
characters = ["{{hero}}", "{{villain}}", "{{friend}}", "{{mentor}}"]
print(f"Random character: {pick_random_item(characters)}")
print(f"Random name: {generate_random_name()}")

print("\n=== {{PHASE_3_TITLE}} ===")
print("Attempting action with 75% success rate:")
attempt_action(0.75)

print("\n=== {{PHASE_4_TITLE}} ===")
print("Generating loot:")
item, rarity = generate_loot()
print(f"Found: {item} ({rarity})")

print("\n=== {{PHASE_5_TITLE}} ===")
print("Generating character stats:")
stats = generate_stats()
print(f"Stats: {stats}")
print("\nSimulating battle round (power 15 vs 12):")
atk_dmg, def_dmg = simulate_battle_round(15, 12)
print(f"Attacker dealt {atk_dmg}, Defender dealt {def_dmg}")

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
