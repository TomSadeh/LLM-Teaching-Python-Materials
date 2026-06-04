# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי איך אובייקטים יכולים לתקשר אחד עם השני.
# מתודות יכולות לקבל אובייקטים אחרים כפרמטרים, וכך אובייקטים
# יכולים לתקשר זה עם זה ולשנות את המצב של כל אחד.
#
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# צרי שתי מחלקות שמתקשרות אחת עם השנייה.
#
# 1. הגדירי מחלקה בשם `Character` עם `__init__` שמקבלת:
#    - `self`, `name`, `gold=0`
#    שמרי אותן כמשתני אובייקט.
#
# 2. הוסיפי מתודה `give_gold(self, other, amount)`:
#    - `other` הוא אובייקט `Character` אחר
#    - אם `self.gold >= amount`:
#      הפחיתי את `amount` מ-`self.gold`
#      הוסיפי את `amount` ל-`other.gold`
#      החזירי `True`
#    - אחרת החזירי `False`
#
# 3. בדקי את האינטראקציה:
#    ```
#    hero = Character("{{hero}}", 100)
#    friend = Character("{{friend}}", 20)
#
#    print(f"{hero.name}: {hero.gold} gold")
#    print(f"{friend.name}: {friend.gold} gold")
#
#    hero.give_gold(friend, 30)
#
#    print(f"After transfer:")
#    print(f"{hero.name}: {hero.gold} gold")
#    print(f"{friend.name}: {friend.gold} gold")
#    ```

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# צרי אובייקטים שמשפיעים על המצב של זה של זה.
#
# 1. הגדירי מחלקה בשם `Combatant` עם `__init__`:
#    - `self`, `name`, `health`, `attack_power`
#    שמרי את כולם כמשתני אובייקט.
#    הוסיפי גם: `self.is_alive = True`
#
# 2. הוסיפי מתודה `attack(self, target)`:
#    - `target` הוא אובייקט `Combatant` אחר
#    - הפחיתי מ-`target.health` את `self.attack_power`
#    - אם `target.health <= 0`:
#      קבעי `target.health = 0`
#      קבעי `target.is_alive = False`
#    - הדפיסי: `"[self.name] attacks [target.name] for [power] damage!"`
#
# 3. הוסיפי מתודה `get_status(self)`:
#    - החזירי: `"[name]: [health] HP (Alive)"` או `"(Defeated)"`
#
# 4. סמלצי קרב:
#    ```
#    hero = Combatant("{{hero}}", 100, 25)
#    enemy = Combatant("{{villain}}", 60, 15)
#
#    while hero.is_alive and enemy.is_alive:
#        hero.attack(enemy)
#        if enemy.is_alive:
#            enemy.attack(hero)
#        print(f"  {hero.get_status()}")
#        print(f"  {enemy.get_status()}")
#    ```

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# צרי מחלקה שמנהלת אוסף של אובייקטים אחרים.
#
# 1. הגדירי מחלקה בשם `Item` עם `__init__`:
#    - `self`, `name`, `value`
#    שמרי אותן כמשתני אובייקט.
#
# 2. הגדירי מחלקה בשם `Shop` עם `__init__`:
#    - `self`, `name`
#    קבעי `self.name = name`
#    קבעי `self.inventory = []` (רשימה של אובייקטי `Item`)
#
# 3. הוסיפי ל-`Shop` מתודה `add_item(self, item)`:
#    - `item` הוא אובייקט `Item`
#    - הוסיפי אותו ל-`self.inventory`
#
# 4. הוסיפי ל-`Shop` מתודה `sell_to(self, item_name, buyer)`:
#    - `buyer` הוא אובייקט `Character` (עם מאפיין `.gold`)
#    - מצאי את הפריט עם השם המתאים ב-`self.inventory`
#    - אם נמצא ו-`buyer.gold >= item.value`:
#      הסירי את הפריט מהמלאי
#      הפחיתי את הערך מ-`buyer.gold`
#      החזירי את הפריט
#    - אחרת החזירי `None`
#
# 5. בדקי את החנות:
#    ```
#    shop = Shop("{{location}}")
#    shop.add_item(Item("{{item}}", 50))
#    shop.add_item(Item("{{spell1}}", 30))
#
#    buyer = Character("{{hero}}", 100)
#    purchased = shop.sell_to("{{item}}", buyer)
#    if purchased:
#        print(f"Bought {purchased.name}!")
#        print(f"Gold remaining: {buyer.gold}")
#    ```

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# צרי אינטראקציה מורכבת יותר בין אובייקטים.
#
# 1. הגדירי מחלקה בשם `Healer` עם:
#    - `__init__(self, name, heal_power, energy)`
#    שמרי את כולם כמשתני אובייקט.
#
# 2. הוסיפי מתודה `heal(self, target)`:
#    - `target` הוא אובייקט כלשהו עם מאפיינים `.health` ו-`.max_health`
#    - אם `self.energy >= 10`:
#      הפחיתי 10 מ-`self.energy`
#      הוסיפי את `self.heal_power` ל-`target.health`
#      אם `target.health > target.max_health`:
#        קבעי `target.health = target.max_health`
#      הדפיסי: `"[self.name] heals [target.name] for [amount]!"`
#      החזירי את כמות הריפוי
#    - אחרת:
#      הדפיסי: `"[self.name] has no energy!"`
#      החזירי `0`
#
# 3. הגדירי מחלקה בשם `Warrior` עם:
#    - `__init__(self, name, health, max_health)`
#    שמרי את כולם כמשתני אובייקט.
#
# 4. בדקי את אינטראקציית הריפוי:
#    ```
#    healer = Healer("{{heroine}}", 30, 50)
#    warrior = Warrior("{{hero}}", 40, 100)
#
#    print(f"{warrior.name}: {warrior.health}/{warrior.max_health}")
#    healer.heal(warrior)
#    print(f"{warrior.name}: {warrior.health}/{warrior.max_health}")
#    healer.heal(warrior)
#    print(f"{warrior.name}: {warrior.health}/{warrior.max_health}")
#    ```

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

print("\n=== {{PHASE_4_TITLE}} ===")
exercise_d()

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
