# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# נושא: שימוש ב-`continue` לדילוג על איטרציות
# רמת קושי: 2-3
#
# הפקודה `continue` מדלגת על שאר הקוד באיטרציה הנוכחית
# ועוברת ישירות לאיטרציה הבאה. השתמשי בה כדי לדלג על פריטים לא רצויים.
#
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# השתמשי ב-`continue` כדי לדלג על פריטים שלא עומדים בקריטריון.
#
# 1. עברי על כל מספר ברשימה `numbers`
# 2. אם המספר קטן מאפס או שווה לאפס, השתמשי ב-`continue`
# 3. הדפיסי את המספר

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# השתמשי ב-`continue` כדי לסנן פריטים תוך כדי עיבוד.
#
# 1. צרי רשימת תוצאות ריקה
# 2. עברי על כל פריט
# 3. אם הפריט הוא מחרוזת ריקה `""`, השתמשי ב-`continue`
# 4. המירי לאותיות גדולות והוסיפי לרשימת התוצאות
# 5. החזירי את התוצאה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# השתמשי ב-`continue` בלולאות עם אינדקס.
#
# 1. צרי רשימת תוצאות ריקה
# 2. כתבי לולאה עם אינדקס: `for i in range(len(values))`
# 3. אם `i` הוא אי-זוגי (`i % 2 != 0`), השתמשי ב-`continue`
# 4. הוסיפי את `values[i]` לרשימת התוצאות
# 5. החזירי את התוצאה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# שלבי `continue` עם לולאות `while`.
#
# 1. קבעי `total = 0`
# 2. `while True`:
#    - קבלי קלט מהמשתמשת
#    - אם הקלט הוא `'done'`, צאי מהלולאה עם `break`
#    - אם הקלט הוא מספר (`.isdigit()` או מספר שלילי), הוסיפי לסכום
#    - אחרת: הדפיסי `"Invalid number, skipping."` והמשיכי עם `continue`
# 3. החזירי את הסכום
#
# > רמז: השתמשי ב-`.lstrip('-').isdigit()` כדי לבדוק אם מספר שלילי

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_5_TITLE}}
# {{CONTEXT_PHASE_5}}
#
# השתמשי ב-`continue` עם תנאי דילוג מורכבים.
#
# 1. צרי רשימת תוצאות ריקה
# 2. עברי על כל פריט
# 3. אם הפריט נמצא ב-`blocked_list`:
#    - הדפיסי `f"Blocked: {item}"`
#    - המשיכי עם `continue`
# 4. עבדי את הפריט (המירי לאותיות קטנות) והוסיפי לרשימה
#    - הדפיסי `f"Approved: {item}"`
# 5. החזירי את התוצאה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_PROJECT_INTRO}}")
print("=" * 50)

print("\n=== {{PHASE_1_TITLE}} ===")
numbers = [5, -3, 0, 8, -1, 12, 0, -7]
print(f"Numbers: {numbers}")
print("Positive only:")
print_positive_only(numbers)

print("\n=== {{PHASE_2_TITLE}} ===")
items = ["{{hero}}", "", "{{villain}}", "", "{{friend}}"]
result = filter_and_transform(items)
print(f"Filtered and transformed: {result}")

print("\n=== {{PHASE_3_TITLE}} ===")
values = ["A", "B", "C", "D", "E", "F"]
result = process_every_other(values)
print(f"Every other item: {result}")

print("\n=== {{PHASE_4_TITLE}} ===")
print("Sum numbers (type 'done' to finish):")
# Uncomment to test:
# total = sum_valid_inputs()
# print(f"Sum: {total}")

print("\n=== {{PHASE_5_TITLE}} ===")
all_items = ["{{hero}}", "{{villain}}", "{{friend}}", "{{mentor}}"]
blocked = ["{{villain}}"]
result = process_approved_items(all_items, blocked)
print(f"Approved items: {result}")

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
