# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# נושא: שימוש ב-`break` כדי לצאת מלולאות מוקדם
# רמת קושי: 2-3
#
# הפקודה `break` יוצאת מיד מהלולאה הנוכחית.
# השתמשי בה כשמצאת את מה שחיפשת, או כשצריך לעצור מוקדם.
#
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# השתמשי ב-`break` כדי לצאת מלולאה כשמתקיים תנאי מסוים.
#
# 1. הגדירי `result = None`
# 2. עברי על כל מספר ב-`numbers`
# 3. אם המספר שלילי:
#    - הכניסי אותו ל-`result`
#    - צאי מהלולאה עם `break`
# 4. החזירי את `result`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# השתמשי ב-`break` עם קלט מהמשתמש כדי ליצור תנאי יציאה.
#
# 1. צרי רשימה ריקה לשמות
# 2. התחילי לולאה אינסופית (`while True`)
# 3. בקשי קלט
# 4. אם הקלט הוא `'done'`, צאי עם `break`
# 5. אחרת, הוסיפי את השם לרשימה
# 6. אחרי הלולאה, החזירי את הרשימה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# השתמשי ב-`break` בחיפוש כדי לעצור ברגע שמצאת את היעד.
#
# 1. עברי על `inventory` עם אינדקס (השתמשי ב-`range(len(...))`)
# 2. הדפיסי `f"Checking: {item}"`
# 3. אם ה-`item` שווה ל-`target`:
#    - הדפיסי `f"Found {target}!"`
#    - החזירי את האינדקס (עם `break` או `return` ישיר)
# 4. אחרי הלולאה, הדפיסי `f"{target} not found."`
# 5. החזירי `-1`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# השתמשי ב-`break` עם מגבלת מונה כדי למנוע לולאות אינסופיות.

# %%
secret = "{{password}}"
max_attempts = 5

# %% [markdown]
# 1. הגדירי `attempts = 0`
# 2. כל עוד `attempts < max_attempts`:
#    - הגדילי את `attempts`
#    - בקשי ניחוש
#    - אם הניחוש שווה ל-`secret`, הדפיסי הצלחה והחזירי `True`
# 3. אחרי הלולאה, הדפיסי הודעת כישלון
# 4. החזירי `False`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_5_TITLE}}
# {{CONTEXT_PHASE_5}}
#
# שלבי `break` עם תנאים מורכבים.
#
# 1. צרי רשימה ריקה לתוצאות
# 2. עברי על כל `item` ב-`data`
# 3. אם ה-`item` הוא `"ERROR"`, `""`, או `None`:
#    - הדפיסי `f"Error encountered! Stopping."`
#    - צאי עם `break`
# 4. עבדי את ה-`item` (המירי לאותיות גדולות) והוסיפי לתוצאות
#    - הדפיסי `f"Processed: {processed_item}"`
# 5. החזירי את התוצאות

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_PROJECT_INTRO}}")
print("=" * 50)

print("\n=== {{PHASE_1_TITLE}} ===")
numbers = [5, 12, 8, -3, 7, -1]
result = find_first_negative(numbers)
print(f"First negative in {numbers}: {result}")

print("\n=== {{PHASE_2_TITLE}} ===")
print("Collecting names (type 'done' to finish):")
# Uncomment to test:
# names = collect_names_until_done()
# print(f"Collected: {names}")

print("\n=== {{PHASE_3_TITLE}} ===")
inventory = ["{{item}}", "{{pet}}", "{{creature}}", "{{transport}}"]
index = search_inventory(inventory, "{{creature}}")
print(f"Found at index: {index}")

print("\n=== {{PHASE_4_TITLE}} ===")
print("Guess the secret word:")
# Uncomment to test:
# success = safe_guess_loop()
# print(f"Result: {'Success!' if success else 'Failed'}")

print("\n=== {{PHASE_5_TITLE}} ===")
test_data = ["{{hero}}", "{{heroine}}", "ERROR", "{{friend}}"]
processed = process_until_error(test_data)
print(f"Processed items: {processed}")

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
