# %% [markdown]
# {{CONTEXT_COMPLETE_FUNCTION_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# Topic: Common file handling patterns
# Difficulty: 2-3
#
# השלימי את הפונקציות הבאות לטיפול בקבצים — הוסיפי את הלוגיקה המרכזית.
# חתימות הפונקציות ו-docstrings כבר מוכנות עבורך.
#
# ## {{FUNCTION_1_TITLE}}
# {{CONTEXT_FUNCTION_1_NARRATIVE}}
#
# השלימי פונקציה שקוראת קובץ ומחזירה את תוכנו.

# %%
# Started for you:
content = ""

# %% [markdown]
# {{CONTEXT_FUNCTION_HINT_1}}
#
# 1. נסי לפתוח את הקובץ עם `with open()`
#
# 2. קראי את התוכן עם `f.read()`
#
# 3. טפלי ב-`FileNotFoundError` על ידי החזרת מחרוזת ריקה
#
# תבנית:
#   try:
#       with open(filename, "r") as f:
#           content = f.read()
#   except FileNotFoundError:
#       content = ""
#   return content

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
pass  # Replace with implementation

# %% [markdown]
# ## {{FUNCTION_2_TITLE}}
# {{CONTEXT_FUNCTION_2_NARRATIVE}}
#
# השלימי פונקציה שכותבת רשימה לקובץ.

# %%
# Started for you:
count = 0

# %% [markdown]
# {{CONTEXT_FUNCTION_HINT_2}}
#
# 1. פתחי את הקובץ לכתיבה
#
# 2. עברי על הפריטים וכתבי כל אחד עם שורה חדשה
#
# 3. ספרי את הפריטים שנכתבו
#
# 4. החזירי את הספירה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
pass  # Replace with implementation

# %% [markdown]
# ## {{FUNCTION_3_TITLE}}
# {{CONTEXT_FUNCTION_3_NARRATIVE}}
#
# השלימי פונקציה שקוראת קובץ לתוך רשימה.

# %%
# Started for you:
lines = []

# %% [markdown]
# {{CONTEXT_FUNCTION_HINT_3}}
#
# 1. נסי לפתוח את הקובץ
#
# 2. קראי שורות והסירי רווחים מיותרים:
#         for line in f:
#             lines.append(line.strip())
#
# 3. טפלי ב-`FileNotFoundError`
#
# 4. החזירי את `lines`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
pass  # Replace with implementation

# %% [markdown]
# ## {{FUNCTION_4_TITLE}}
# {{CONTEXT_FUNCTION_4_NARRATIVE}}
#
# השלימי פונקציה שמוסיפה תוכן לסוף קובץ.
#
# {{CONTEXT_FUNCTION_HINT_4}}
#
# 1. פתחי את הקובץ במצב הוספה `"a"`
#
# 2. כתבי את הטקסט
#
# 3. החזירי `True`
#
# > רמז: מצב הוספה יוצר את הקובץ אם הוא לא קיים

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
pass  # Replace with implementation

# %% [markdown]
# ## {{FUNCTION_5_TITLE}}
# {{CONTEXT_FUNCTION_5_NARRATIVE}}
#
# השלימי פונקציה שסופרת שורות בקובץ.

# %%
# Started for you:
count = 0

# %% [markdown]
# {{CONTEXT_FUNCTION_HINT_5}}
#
# 1. נסי לפתוח את הקובץ
#
# 2. ספרי שורות:
#         for line in f:
#             count += 1
#
# 3. טפלי ב-`FileNotFoundError` (החזירי 0)
#
# 4. החזירי את `count`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
pass  # Replace with implementation

# %% [markdown]
# ## {{FUNCTION_6_TITLE}}
# {{CONTEXT_FUNCTION_6_NARRATIVE}}
#
# השלימי פונקציה שמחפשת טקסט בקובץ.

# %%
# Started for you:
matches = []

# %% [markdown]
# {{CONTEXT_FUNCTION_HINT_6}}
#
# 1. נסי לפתוח את הקובץ
#
# 2. עברי על השורות עם מספור (החל מ-1):
#         for line_num, line in enumerate(f, 1):
#
# 3. בדקי אם `search_term` מופיע בשורה (ללא רגישות לאותיות גדולות/קטנות):
#         if search_term.lower() in line.lower():
#             matches.append((line_num, line.strip()))
#
# 4. טפלי ב-`FileNotFoundError`
#
# 5. החזירי את `matches`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
pass  # Replace with implementation

# %%
print("{{CONTEXT_COMPLETE_FUNCTION_INTRO}}")
print("=" * 50)

print("\n=== Testing File Functions ===")

# Create test data
test_items = ["{{hero}}", "{{heroine}}", "{{friend}}", "{{item}}"]

print("\n--- Testing write_list_to_file ---")
# count = write_list_to_file("test_items.txt", test_items)
# print(f"Wrote {count} items")

print("\n--- Testing read_file_content ---")
# content = read_file_content("test_items.txt")
# print(f"Content:\n{content}")

print("\n--- Testing read_file_to_list ---")
# items = read_file_to_list("test_items.txt")
# print(f"Items: {items}")

print("\n--- Testing append_to_file ---")
# append_to_file("test_items.txt", "{{mentor}}\n")
# items = read_file_to_list("test_items.txt")
# print(f"After append: {items}")

print("\n--- Testing count_lines ---")
# count = count_lines("test_items.txt")
# print(f"Line count: {count}")

print("\n--- Testing search_in_file ---")
# matches = search_in_file("test_items.txt", "{{hero}}")
# print(f"Matches: {matches}")

print("\n" + "=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
