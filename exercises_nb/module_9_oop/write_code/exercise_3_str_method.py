# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי לממש את `__str__` — מתודה מיוחדת
# שקובעת איך האובייקטים שלך נראים כשמדפיסים אותם או ממירים אותם
# למחרוזת. זה הופך את הניפוי וההצגה של מידע להרבה יותר נוח.
#
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# צרי קלאס עם מתודת `__str__`.
#
# 1. הגדירי קלאס בשם `Item` עם `__init__` שמקבלת:
#    - `self`, `name`, `value`
#    שמרי את שניהם כמאפייני מופע.
#
# 2. הגדירי את מתודת `__str__`:
#    ```
#    def __str__(self):
#        return f"[מחרוזת מעוצבת כלשהי]"
#    ```
#    החזירי מחרוזת בסגנון: `"Item: [name] (worth [value] gold)"`
#
# 3. צרי פריט ובדקי את `__str__`:
#    ```
#    item = Item("{{item}}", 100)
#    print(item)  # This automatically calls __str__!
#    ```
#
# שימי לב: בלי `__str__`, הפקודה `print(item)` הייתה מציגה משהו כמו:
#           `<__main__.Item object at 0x...>`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# צרי קלאס עם `__str__` מורכב יותר שמציג מצב.
#
# 1. הגדירי קלאס בשם `Character` עם `__init__` שמקבלת:
#    - `self`, `name`, `health`, `max_health`, `level`
#    שמרי את כולם כמאפייני מופע.
#
# 2. הגדירי את `__str__` כך שתציג את כל פרטי הדמות:
#    פורמט: `"[name] (Lv.[level]) - HP: [health]/[max_health]"`
#
# 3. צרי כמה דמויות והדפיסי אותן:
#    ```
#    hero = Character("{{hero}}", 75, 100, 5)
#    print(hero)  # Should show formatted info
#
#    friend = Character("{{friend}}", 50, 80, 3)
#    print(friend)
#    ```
#
# 4. שני את נקודות החיים של הגיבורה והדפיסי שוב:
#    ```
#    hero.health = 100
#    print(hero)  # __str__ shows current state!
#    ```

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# צרי קלאס שמשתמש ב-`__str__` להצגת רשימת פריטים.
#
# 1. הגדירי קלאס בשם `Inventory` עם `__init__` שמקבלת:
#    - `self`, `owner`
#    קבעי `self.owner = owner`
#    קבעי `self.items = []` (רשימה ריקה)
#
# 2. הוסיפי מתודה בשם `add_item` שמוסיפה לרשימה `self.items`
#
# 3. הגדירי את `__str__` להצגת תכולת המלאי:
#    - אם ריק: `"[owner]'s Inventory: (empty)"`
#    - אם יש פריטים: `"[owner]'s Inventory: [item1], [item2], ..."`
#
# > רמז: השתמשי ב-`", ".join(self.items)` לעיצוב הרשימה
#
# 4. בדקי את המלאי:
#    ```
#    inv = Inventory("{{hero}}")
#    print(inv)  # Should show empty
#
#    inv.add_item("{{item}}")
#    inv.add_item("{{spell1}}")
#    print(inv)  # Should show items
#    ```

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# צרי קלאס שבו `__str__` מעצב תצוגה של מספר שורות.
#
# 1. הגדירי קלאס בשם `ProfileCard` עם `__init__` שמקבלת:
#    - `self`, `name`, `role`, `level`, `skills` (רשימה)
#    שמרי את כולם כמאפייני מופע.
#
# 2. הגדירי את `__str__` להחזרת כרטיס רב-שורתי:
#    ```
#    ┌─────────────────────┐
#    │ [name]              │
#    │ Role: [role]        │
#    │ Level: [level]      │
#    │ Skills: [s1], [s2]  │
#    └─────────────────────┘
#    ```
#    גרסה פשוטה (בלי מסגרת) מקובלת לגמרי:
#    `"[name]\nRole: [role]\nLevel: [level]\nSkills: [s1], [s2]"`
#
# 3. צרי כרטיס פרופיל והדפיסי אותו:
#    ```
#    card = ProfileCard("{{hero}}", "{{ROLE_TITLE}}", 10,
#                      ["{{spell1}}", "{{spell2}}"])
#    print(card)
#    ```
#
# > רמז: השתמשי ב-`\n` לירידות שורה במחרוזת שאת מחזירה

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
