# %% [markdown]
# {{CONTEXT_ERROR_HANDLING_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# נושא: טיפול בפקודות משחק שגויות בצורה חיננית
# רמת קושי: 3-4
#
# משחקים חייבים לטפל בקלט בצורה חזקה — שחקנים יכולים לכתוב כל דבר!
# גרמי למשחק להגיב בצורה מועילה לקלט לא חוקי.
#
# ## {{HANDLING_1_TITLE}}
# {{CONTEXT_HANDLING_1_NARRATIVE}}
#
# מערכת התנועה הזאת קורסת כשמקבלת כיוון לא חוקי.

# %%
moves = {"north": (0, 1), "south": (0, -1), "east": (1, 0), "west": (-1, 0)}
dx, dy = moves[direction]  # KeyError if direction invalid!
return dx, dy

# %% [markdown]
# {{CONTEXT_HANDLING_HINT_1}}
#
# 1. הגדירי מילון `moves` עם הכיוונים
# 2. המירי את `direction` לאותיות קטנות
# 3. אם הכיוון נמצא ב-`moves`, החזירי את הדלתא
# 4. אחרת, הדפיסי הודעת שגיאה והחזירי `(0, 0)`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{HANDLING_2_TITLE}}
# {{CONTEXT_HANDLING_2_NARRATIVE}}
#
# פקודת ההתקפה הזאת קורסת אם היעד לא קיים.

# %%
for i, enemy in enumerate(enemies):
    if enemy["name"] == target_name:
        enemies[i]["hp"] -= 10
        return True
return False

# %% [markdown]
# {{CONTEXT_HANDLING_HINT_2}}
#
# 1. עברי על רשימת האויבים כדי למצוא את היעד
# 2. אם לא נמצא בסוף הלולאה, החזירי הודעת "לא נמצא"
# 3. אם נמצא אך `hp <= 0`, החזירי הודעת "כבר הובס"
# 4. הורידי נזק
# 5. אם `hp` עכשיו `<= 0`, החזירי הודעת "הובס"
# 6. אחרת, החזירי הודעת פגיעה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{HANDLING_3_TITLE}}
# {{CONTEXT_HANDLING_3_NARRATIVE}}
#
# פקודת השימוש בחפץ הזאת יכולה להיכשל בכמה דרכים.

# %%
inventory.remove(item_name)  # ValueError if not present!
return f"Used {item_name}"

# %% [markdown]
# {{CONTEXT_HANDLING_HINT_3}}
#
# 1. בדקי אם המלאי ריק
# 2. בדקי אם `item_name` נמצא במלאי
# 3. אם נמצא, הסירי אותו והחזירי הודעת הצלחה
# 4. אחרת, החזירי הודעת שגיאה מתאימה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{HANDLING_4_TITLE}}
# {{CONTEXT_HANDLING_4_NARRATIVE}}
#
# מערכת החנות הזאת יכולה להיכשל בכמה דרכים.

# %%
price = item_prices[item_name]
return gold - price, item_name

# %% [markdown]
# {{CONTEXT_HANDLING_HINT_4}}
#
# 1. בדקי אם `item_name` נמצא ב-`item_prices`
# 2. קבלי את המחיר
# 3. בדקי אם לשחקן יש מספיק זהב
# 4. אם הכל בסדר, החזירי את כמות הזהב החדשה והודעת הצלחה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{HANDLING_5_TITLE}}
# {{CONTEXT_HANDLING_5_NARRATIVE}}
#
# בני מנתח פקודות שלם עם בדיקות קלט.
#
# {{CONTEXT_HANDLING_HINT_5}}
#
# 1. נקי רווחים מהפקודה והמירי לאותיות קטנות
# 2. אם הפקודה ריקה, החזירי שגיאה
# 3. פצלי לחלקים
# 4. החלק הראשון הוא הפעולה
# 5. בדקי אם הפעולה חוקית
# 6. לפקודות שדורשות ארגומנטים (`move`, `attack`, `use`):
#    - בדקי שניתנו ארגומנטים
#    - עבור `move`, אמתי שהכיוון חוקי
# 7. החזירי `(action, args)` או הודעת שגיאה מתאימה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_ERROR_HANDLING_INTRO}}")
print("=" * 50)

print("\n=== {{HANDLING_1_TITLE}} ===")
print("Testing safe movement:")
directions = ["north", "SOUTH", "left", "east"]
for d in directions:
    result = safe_move(d)
    print(f"  {d} -> {result}")

print("\n=== {{HANDLING_2_TITLE}} ===")
print("Testing safe attack:")
enemies = [
    {"name": "{{creature}}", "hp": 20},
    {"name": "{{villain}}", "hp": 0}
]
targets = ["{{creature}}", "{{villain}}", "ghost"]
for t in targets:
    result = safe_attack(enemies, t)
    print(f"  Attack {t}: {result}")

print("\n=== {{HANDLING_3_TITLE}} ===")
print("Testing safe use item:")
inv = ["{{item}}", "{{spell1}}"]
items_to_use = ["{{item}}", "{{spell2}}"]
for item in items_to_use:
    result = safe_use_item(inv, item)
    print(f"  Use {item}: {result}")

print("\n=== {{HANDLING_4_TITLE}} ===")
print("Testing safe shop:")
prices = {"{{item}}": 50, "{{spell1}}": 100}
purchases = [("{{item}}", 60), ("{{spell1}}", 50), ("potion", 100)]
for item, gold in purchases:
    new_gold, msg = safe_buy_item(gold, prices, item)
    print(f"  Buy {item} with {gold}g: {msg}")

print("\n=== {{HANDLING_5_TITLE}} ===")
print("Testing command parser:")
commands = ["move north", "attack goblin", "look", "dance", "", "move"]
for cmd in commands:
    result = parse_game_command(cmd)
    print(f"  '{cmd}' -> {result}")

print("\n" + "=" * 50)
print("{{CONTEXT_ROBUSTNESS_COMPLETE}}")
