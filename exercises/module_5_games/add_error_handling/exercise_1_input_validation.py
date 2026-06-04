# %% [markdown]
# {{CONTEXT_ERROR_HANDLING_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# נושא: הוספת לולאות אימות קלט
# רמת קושי: 3
#
# אימות קלט מבטיח שהמשתמשת מספקת נתונים תקינים לפני שממשיכים.
# השתמשי בלולאות `while` עם בדיקות מחרוזת כדי לאמת את הקלט.
#
# הערה: אנחנו משתמשות בלולאות `while` ובשיטות מחרוזת (כמו `.isdigit()`) לאימות,
# ולא בבלוקים של `try/except`. כך לומדים את הדפוס הבסיסי של לולאות אימות.
#
# {{HANDLING_1_TITLE}}
# {{CONTEXT_HANDLING_1_NARRATIVE}}
#
# הפונקציה הזו מקבלת כל קלט ומתרסקת כשמזינים מספרים לא תקינים.

# %%
user_input = input("Enter a number: ")
number = int(user_input)  # Crashes on "abc"!
return number

# %% [markdown]
# {{CONTEXT_HANDLING_HINT_1}}
#
# 1. התחילי לולאת `while True`
# 2. קבלי קלט מהמשתמשת
# 3. בדקי אם הקלט תקין:
#    - למספר חיובי: `input.isdigit()`
#    - למספר שלילי: `input.startswith('-')` ו-`input[1:].isdigit()`
# 4. אם תקין, המירי והחזירי את הערך
# 5. אם לא תקין, הדפיסי הודעת שגיאה (הלולאה תמשיך)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{HANDLING_2_TITLE}}
# {{CONTEXT_HANDLING_2_NARRATIVE}}
#
# הפונקציה הזו מקבלת מספרים מחוץ לטווח התקין.

# %%
score = int(input("Enter score (0-100): "))
return score

# %% [markdown]
# {{CONTEXT_HANDLING_HINT_2}}
#
# 1. התחילי לולאת `while True`
# 2. קבלי קלט מהמשתמשת
# 3. בדקי אם הקלט מספרי (השתמשי ב-`.isdigit()`)
#    אם לא, הדפיסי `"Please enter a number."` והמשיכי
# 4. המירי ל-`int`
# 5. בדקי אם הערך נמצא בטווח 0-100
#    אם לא, הדפיסי `"Score must be between 0 and 100."` והמשיכי
# 6. החזירי את הציון התקין

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{HANDLING_3_TITLE}}
# {{CONTEXT_HANDLING_3_NARRATIVE}}
#
# הפונקציה הזו מקבלת כל טקסט, אפילו מחרוזות ריקות.

# %%
name = input("Enter your name: ")
return name

# %% [markdown]
# {{CONTEXT_HANDLING_HINT_3}}
#
# 1. התחילי לולאת `while True`
# 2. קבלי קלט והסירי רווחים מיותרים (`.strip()`)
# 3. אם המחרוזת ריקה, הדפיסי `"Name cannot be empty."` והמשיכי
# 4. החזירי את השם לאחר ניקוי הרווחים

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{HANDLING_4_TITLE}}
# {{CONTEXT_HANDLING_4_NARRATIVE}}
#
# הפונקציה הזו מקבלת כל בחירה, לא רק אפשרויות תקינות.

# %%
print("Choose: (a) {{spell1}}, (b) {{spell2}}, (c) {{spell3}}")
choice = input("Your choice: ")
return choice

# %% [markdown]
# {{CONTEXT_HANDLING_HINT_4}}
#
# 1. הגדירי `valid_choices = ['a', 'b', 'c']`
# 2. הדפיסי את התפריט
# 3. התחילי לולאת `while True`
# 4. קבלי קלט והמירי לאותיות קטנות
# 5. אם הבחירה נמצאת ב-`valid_choices`, החזירי אותה
# 6. אחרת הדפיסי `"Invalid choice. Please enter a, b, or c."`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{HANDLING_5_TITLE}}
# {{CONTEXT_HANDLING_5_NARRATIVE}}
#
# הפונקציה הזו של אישור כן/לא מקבלת כל קלט שהוא.

# %%
response = input("Confirm? (yes/no): ")
return response == "yes"

# %% [markdown]
# {{CONTEXT_HANDLING_HINT_5}}
#
# 1. התחילי לולאת `while True`
# 2. הדפיסי את ההנחיה וקבלי קלט (אותיות קטנות, ללא רווחים)
# 3. אם התשובה היא `'yes'` או `'y'`, החזירי `True`
# 4. אם התשובה היא `'no'` או `'n'`, החזירי `False`
# 5. אחרת הדפיסי `"Please enter yes or no."`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_ERROR_HANDLING_INTRO}}")
print("=" * 50)

print("\n=== {{HANDLING_1_TITLE}} ===")
print("Getting a valid number:")
# number = safe_get_number()
# print(f"You entered: {number}")

print("\n=== {{HANDLING_2_TITLE}} ===")
print("Getting a valid score:")
# score = safe_get_score()
# print(f"Score recorded: {score}")

print("\n=== {{HANDLING_3_TITLE}} ===")
print("Getting a valid name:")
# name = safe_get_name()
# print(f"Hello, {name}!")

print("\n=== {{HANDLING_4_TITLE}} ===")
print("Getting a valid choice:")
# choice = safe_get_choice()
# print(f"You chose: {choice}")

print("\n=== {{HANDLING_5_TITLE}} ===")
print("Getting confirmation:")
# if safe_confirm("Do you want to continue? (yes/no): "):
#     print("Continuing...")
# else:
#     print("Cancelled.")

print("\n" + "=" * 50)
print("{{CONTEXT_ROBUSTNESS_COMPLETE}}")
