# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי לכתוב מתודות מופע — פונקציות בתוך מחלקות שיכולות לקרוא
# ולשנות את המאפיינים של האובייקט באמצעות `self`.
#
# {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# ## צרי מחלקה עם מתודות שקוראות מאפיינים
#
# 1. הגדירי מחלקה בשם `Character` עם `__init__` שמקבלת:
#    - `self`, `name`, `health`, `max_health`
#    שמרי את כולם כמאפייני מופע.
#
# 2. הוסיפי מתודה בשם `get_status`:
#    `def get_status(self):`
#    היא תחזיר מחרוזת בתבנית: `"[name]: [health]/[max_health] HP"`
#
# 3. הוסיפי מתודה בשם `is_healthy`:
#    `def is_healthy(self):`
#    היא תחזיר `True` אם `health > max_health / 2`, אחרת `False`
#
# 4. צרי דמות ובדקי את המתודות:
#    `hero = Character("{{hero}}", 75, 100)`
#    `print(hero.get_status())`  # תדפיס את הסטטוס
#    `print(hero.is_healthy())`  # תדפיס True
#
# > רמז: מתודות תמיד מקבלות `self` כפרמטר הראשון!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# ## צרי מחלקה עם מתודות שמשנות מאפיינים
#
# 1. הגדירי מחלקה בשם `Counter` עם `__init__` שמקבלת:
#    - `self`, `name`, `start_value=0`
#    שמרי כ-`self.name` ו-`self.value`
#
# 2. הוסיפי מתודה `increment` שמגדילה את הערך ב-1:
#    `def increment(self):`
#        `self.value += 1`
#
# 3. הוסיפי מתודה `add` שמקבלת פרמטר `amount`:
#    `def add(self, amount):`
#    היא תוסיף את `amount` ל-`self.value`
#
# 4. הוסיפי מתודה `reset` שמחזירה את הערך ל-0
#
# 5. בדקי את המונה שלך:
#    `counter = Counter("{{spell1}} uses")`
#    `counter.increment()`
#    `counter.add(5)`
#    `print(f"{counter.name}: {counter.value}")`  # צריך להיות 6
#    `counter.reset()`
#    `print(f"After reset: {counter.value}")`  # צריך להיות 0

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# ## צרי מחלקה שבה מתודות גם מחזירות ערכים וגם משנות מצב
#
# 1. הגדירי מחלקה בשם `Wallet` עם `__init__` שמקבלת:
#    - `self`, `owner`, `initial_gold=0`
#    שמרי כ-`self.owner` ו-`self.gold`
#
# 2. הוסיפי מתודה `deposit` שמקבלת `amount`:
#    - הוסיפי את `amount` ל-`self.gold`
#    - החזירי את הסכום החדש
#
# 3. הוסיפי מתודה `withdraw` שמקבלת `amount`:
#    - אם `amount > self.gold`, הדפיסי `"Not enough gold!"` והחזירי 0
#    - אחרת, הפחיתי את `amount` מ-`self.gold` והחזירי את `amount`
#
# 4. הוסיפי מתודה `check_balance` שמחזירה את `self.gold`
#
# 5. בדקי את הארנק:
#    `wallet = Wallet("{{hero}}", 50)`
#    `print(f"Deposited, new balance: {wallet.deposit(30)}")`  # 80
#    `print(f"Withdrew: {wallet.withdraw(20)}")`  # 20
#    `print(f"Balance: {wallet.check_balance()}")`  # 60
#    `wallet.withdraw(100)`  # צריך להדפיס "Not enough gold!"

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_PROJECT_INTRO}}")
print("=" * 50)

print("\n=== {{PHASE_1_TITLE}} ===")
exercise_a()

print("\n=== {{PHASE_2_TITLE}} ===")
exercise_b()

print("\n=== {{PHASE_3_TITLE}} ===")
exercise_c()

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
