# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי על קבועי המחרוזות המועילים של מודול `string`.
# אלו הם אוספי תווים מוגדרים מראש שעוזרים באימות קלט, יצירת מחרוזות ועיבוד טקסט.
#
# נושא: קבועי מודול string
# רמת קושי: 2

# %%
import string

# %% [markdown]
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# חקרי את קבועי התווים של מודול `string`.
#
# 1. הדפיסי כל קבוע כדי לראות מה הוא מכיל:
#
#         print("Letters:", string.ascii_letters)
#         print("Lowercase:", string.ascii_lowercase)
#         print("Uppercase:", string.ascii_uppercase)
#         print("Digits:", string.digits)
#         print("Punctuation:", string.punctuation)
#
# 2. בדקי את האורך של כל קבוע:
#         print(f"Letters count: {len(string.ascii_letters)}")
#         print(f"Digits count: {len(string.digits)}")
#
# הקבועים האלה שימושיים ל:
# - אימות קלט (האם הטקסט מורכב רק מאותיות? רק מספרות?)
# - יצירת מחרוזות אקראיות (סיסמאות, קודים)
# - עיבוד טקסט

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# השתמשי בקבועי `string` כדי לאמת קלט.
#
# 1. צרי פונקציה שבודקת אם טקסט מורכב רק מאותיות:
#
#         def is_all_letters(text):
#             for char in text:
#                 if char not in string.ascii_letters:
#                     return False
#             return True
#
# 2. בדקי אותה עם קלטים שונים:
#         print(is_all_letters("Hello"))        # True
#         print(is_all_letters("Hello123"))     # False
#         print(is_all_letters("Hello World"))  # False (space)
#
# 3. צרי פונקציה דומה לאלפאנומרי:
#
#         def is_alphanumeric(text):
#             valid_chars = string.ascii_letters + string.digits
#             for char in text:
#                 if char not in valid_chars:
#                     return False
#             return True
#
# 4. בדקי אותה:
#         print(is_alphanumeric("User123"))     # True
#         print(is_alphanumeric("User_123"))    # False (underscore)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# שלבי קבועי `string` עם `random` עבור {{school}}.
#
# 1. ייבאי את `random` בתחילת הפתרון שלך
#
# 2. צרי גנרטור קודים פשוט:
#
#         def generate_code(length):
#             """Generate a random alphanumeric code."""
#             characters = string.ascii_uppercase + string.digits
#             code = ""
#             for i in range(length):
#                 code = code + random.choice(characters)
#             return code
#
# 3. צרי והדפיסי מספר קודים:
#         print(f"Access code: {generate_code(6)}")
#         print(f"Long code: {generate_code(10)}")
#
# 4. צרי גרסה שמשתמשת רק בספרות:
#
#         def generate_pin(length):
#             pin = ""
#             for i in range(length):
#                 pin = pin + random.choice(string.digits)
#             return pin
#
#         print(f"PIN: {generate_pin(4)}")
#
# 5. צרי גרסה שמשתמשת רק באותיות:
#         צרי "שם" בן 5 אותיות באמצעות אותיות קטנות

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_PROJECT_INTRO}}")
print("=" * 50)

print("\n=== {{PHASE_1_TITLE}} ===")
print("Exploring string constants")
exercise_a()

print("\n=== {{PHASE_2_TITLE}} ===")
print("Validation with string constants")
exercise_b()

print("\n=== {{PHASE_3_TITLE}} ===")
print("Code generation for {{school}}")
exercise_c()

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
print()
print("String Constants Summary:")
print("  string.ascii_letters  - a-z and A-Z")
print("  string.ascii_lowercase - a-z")
print("  string.ascii_uppercase - A-Z")
print("  string.digits         - 0-9")
print("  string.punctuation    - !@#$... etc")
