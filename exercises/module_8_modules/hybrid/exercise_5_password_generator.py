# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
#
# זוהי תרגילה רב-שלבית שבה {{hero}} בונה מחוללי סיסמאות וקודים מאובטחים
# תוך שימוש במודולים `string` ו-`random` יחד.
#
# מושגי תכנות: מודול `string`, מודול `random`, עיצוב פונקציות
# רמת קושי: 2-3

# %%
import string

# %%
import random

# %% [markdown]
# ## חלק 1: צמיחה - מחולל קודים בסיסי
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# למדי להשתמש בקבועי `string` כמאגרי תווים.
#
# 1. קבלי את ספרות המחרוזת: `string.digits = "0123456789"`
#
# 2. בני את הקוד בעזרת לולאה:
#         code = ""
#         for i in range(length):
#             code = code + random.choice(string.digits)
#
# 3. החזירי את הקוד

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. בחרי את קבוצת התווים המתאימה לפי `case`:
#         if case == "upper":
#             chars = string.ascii_uppercase
#         elif case == "lower":
#             chars = string.ascii_lowercase
#         else:
#             chars = string.ascii_letters
#
# 2. בני והחזירי את הקוד

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. שלבי קבוצות תווים:
#         chars = string.ascii_letters + string.digits
#
# 2. בני והחזירי את הקוד

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: צמיחה - שילוב מודולים ליצירת סיסמאות
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# צרי מחוללי סיסמאות מתוחכמים יותר.
#
# 1. בני מאגר תווים:
#         chars = string.ascii_letters + string.digits
#         if include_special:
#             chars = chars + string.punctuation
#
# 2. צרי סיסמה בעזרת לולאה או `sample`
#
# 3. החזירי את הסיסמה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. צרי רשימת מילים:
#         words = ["flame", "river", "stone", "cloud", "star",
#                  "moon", "sun", "wind", "wave", "tree"]
#
# 2. השתמשי ב-`random.sample()` לבחירת מילים
#
# 3. חברי את המילים עם ספרות אקראיות ביניהן:
#         result = ""
#         for i, word in enumerate(selected_words):
#             result = result + word
#             if i < len(selected_words) - 1:
#                 result = result + random.choice(string.digits)
#
# 4. החזירי את התוצאה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. צרי רשימת מילים גדולה יותר
#
# 2. השתמשי ב-`random.sample()` לבחירת מילים
#
# 3. חברי עם מפריד: `separator.join(selected_words)`
#
# 4. החזירי את התוצאה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: שיפור - אימות ואבטחה
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# הוסיפי אימות כדי לוודא שהסיסמאות עומדות בדרישות.
#
# 1. בדקי אורך >= 8
#
# 2. בדקי אם יש אות גדולה (כל תו ב-`string.ascii_uppercase`):
#         has_upper = False
#         for char in password:
#             if char in string.ascii_uppercase:
#                 has_upper = True
#                 break
#
# 3. בדקי בצורה דומה אם יש אות קטנה וספרה
#
# 4. החזירי tuple מתאים:
#         (True, "Password meets all requirements")
#         (False, "Password must be at least 8 characters")
#         וכן הלאה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. וודאי אורך מינימלי:
#         if length < 8:
#             length = 8
#
# 2. התחילי עם תווים חובה:
#         password = [
#             random.choice(string.ascii_uppercase),
#             random.choice(string.ascii_lowercase),
#             random.choice(string.digits),
#         ]
#
# 3. מלאי את השאר בתווים אקראיים:
#         all_chars = string.ascii_letters + string.digits
#         for i in range(length - 3):
#             password.append(random.choice(all_chars))
#
# 4. ערבבי כדי שתווי החובה לא יהיו תמיד ראשונים:
#         random.shuffle(password)
#
# 5. המירי רשימה למחרוזת והחזירי:
#         return "".join(password)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## MAIN

# %%
print("=" * 60)
print("{{CONTEXT_PROJECT_INTRO}}")
print("Password Generator for {{school}}")
print("=" * 60)
print()

print(">>> PART 1: Basic Code Generation")
print("-" * 40)
# Uncomment to test:
# print(f"Numeric (6): {generate_numeric_code(6)}")
# print(f"Alpha upper (4): {generate_alpha_code(4, 'upper')}")
# print(f"Alpha lower (4): {generate_alpha_code(4, 'lower')}")
# print(f"Alpha mixed (4): {generate_alpha_code(4, 'mixed')}")
# print(f"Alphanumeric (8): {generate_alphanumeric_code(8)}")
print()

print(">>> PART 2: Password Generation")
print("-" * 40)
# Uncomment to test:
# print(f"Password (12): {generate_password(12)}")
# print(f"Password (12, no special): {generate_password(12, False)}")
# print(f"Memorable: {generate_memorable_password(3)}")
# print(f"Passphrase: {generate_passphrase(4, '-')}")
print()

print(">>> PART 3: Validation")
print("-" * 40)
# Uncomment to test:
# test_passwords = ["abc", "abcdefgh", "Abcdefgh", "Abcdefg1"]
# for pwd in test_passwords:
#     valid, msg = validate_password(pwd)
#     status = "PASS" if valid else "FAIL"
#     print(f"  '{pwd}': {status} - {msg}")
# print()
# print(f"Secure password: {generate_secure_password(12)}")
print()

print("=" * 60)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
print("=" * 60)
