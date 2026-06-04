# %% [markdown]
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_MISSION}}
#
# נושא: מציאת באגים עם `break` ו-`continue`
# רמת קושי: 2-3
#
# `break` ו-`continue` הם כלים חזקים, אבל הם יכולים לגרום לבאגים עדינים
# כשהם ממוקמים במקום הלא נכון או כשהלוגיקה הפוכה.
#
# ## {{CASE_1_TITLE}}
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# פונקציית החיפוש הזו אמורה למצוא פריט ולהחזיר את האינדקס שלו.
#
# התנהגות צפויה:
# להחזיר את האינדקס שבו נמצא ה-`target`, או 1- אם לא נמצא
#
# התנהגות בפועל:
# תמיד מחזירה 1-, אפילו כשהפריט קיים
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

# %%
index = 0
while index < len(items):
    if items[index] == target:
        break  # Found it!
    index += 1
return -1  # BUG: Always returns -1, never returns the found index

# %% [markdown]
# מה מצאתי: ________________________________
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CASE_2_TITLE}}
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# הפונקציה הזו אמורה לדלג על מספרים שליליים ולסכום את החיוביים.
#
# התנהגות צפויה:
# לסכום רק את המספרים החיוביים, ולדלג על השליליים
#
# התנהגות בפועל:
# מחזירה 0 כי היא מפסיקה בשלילי הראשון
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}

# %%
total = 0
for num in numbers:
    if num < 0:
        break  # BUG: Should be continue, not break!
    total += num
return total

# %% [markdown]
# מה מצאתי: ________________________________
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CASE_3_TITLE}}
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# האוסף הזה אמור לעצור כשהמשתמשת מקלידה `'quit'`.
#
# התנהגות צפויה:
# לאסוף פריטים עד שהמשתמשת מקלידה `'quit'`, ואז להחזיר את הרשימה
#
# התנהגות בפועל:
# לא עוצר לעולם, ממשיך לשאול לנצח
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}

# %%
items = []
while True:
    user_input = input("Enter item (or 'quit'): ")
    if user_input == "quit":
        continue  # BUG: Should be break, not continue!
    items.append(user_input)
return items

# %% [markdown]
# מה מצאתי: ________________________________
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CASE_4_TITLE}}
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# הבודק הזה אמור לעצור לאחר מציאת שגיאה אחת.
#
# התנהגות צפויה:
# לבדוק פריטים עד שמוצאים פריט לא תקין, ואז לעצור
#
# התנהגות בפועל:
# ה-`break` נמצא בתוך ה-`else`, אז הוא עוצר על פריטים תקינים
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}

# %%
valid_items = []
for item in items:
    if item == "" or item is None:
        print(f"Invalid item found!")
    else:
        valid_items.append(item)
        break  # BUG: Break is in wrong branch!
return valid_items

# %% [markdown]
# מה מצאתי: ________________________________
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CASE_5_TITLE}}
# {{CONTEXT_CASE_5_NARRATIVE}}
#
# הפונקציה הזו אמורה למצוא את הפריט הראשון שעומד בתנאי.
#
# התנהגות צפויה:
# להחזיר את הפריט הראשון שאורכו גדול מ-5 תווים
#
# התנהגות בפועל:
# מדלגת על פריטים שמתאימים! מחזירה תוצאה שגויה.
#
# {{CONTEXT_INVESTIGATION_PROMPT_5}}

# %%
for item in items:
    if len(item) > 5:
        continue  # BUG: Should return item, not continue!
    # Falls through without returning the match
return None

# %% [markdown]
# מה מצאתי: ________________________________
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_INVESTIGATION_INTRO}}")
print("=" * 50)

print("\n=== {{CASE_1_TITLE}} ===")
print("Testing search:")
items = ["{{item}}", "{{pet}}", "{{creature}}"]
buggy_result = buggy_search(items, "{{pet}}")
print(f"Buggy result: {buggy_result} (should be 1)")
# fixed_result = fix_search(items, "{{pet}}")
# print(f"Fixed result: {fixed_result}")

print("\n=== {{CASE_2_TITLE}} ===")
print("Testing sum positives:")
numbers = [5, -3, 10, -1, 7]
buggy_result = buggy_sum_positives(numbers)
print(f"Buggy result: {buggy_result} (should be 22)")
# fixed_result = fix_sum_positives(numbers)
# print(f"Fixed result: {fixed_result}")

print("\n=== {{CASE_3_TITLE}} ===")
print("Testing collector:")
print("(Buggy version would loop forever - don't run!)")
# fixed_items = fix_collector()
# print(f"Collected: {fixed_items}")

print("\n=== {{CASE_4_TITLE}} ===")
print("Testing validator:")
test_items = ["{{hero}}", "{{villain}}", "", "{{friend}}"]
buggy_result = buggy_validator(test_items.copy())
print(f"Buggy result: {buggy_result} (should be ['{{{{hero}}}}', '{{{{villain}}}}'])")
# fixed_result = fix_validator(test_items)
# print(f"Fixed result: {fixed_result}")

print("\n=== {{CASE_5_TITLE}} ===")
print("Testing find long item:")
words = ["cat", "elephant", "dog", "hippopotamus"]
buggy_result = buggy_find_long_item(words)
print(f"Buggy result: {buggy_result} (should be 'elephant')")
# fixed_result = fix_find_long_item(words)
# print(f"Fixed result: {fixed_result}")

print("\n" + "=" * 50)
print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
