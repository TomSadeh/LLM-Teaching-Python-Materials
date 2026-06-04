# =============================================================================
# Write Code: Input
# =============================================================================
# Difficulty: 3-4
# Concepts: input(), type conversion, interactive programs
# =============================================================================

# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# קבלי את השם של {{hero}} וברכי אותה.
#
# 1. השתמשי ב-`input()` כדי לשאול `"What is your name? "` ושמרי את התשובה במשתנה `name`
# 2. הדפיסי `"Welcome to {{school}},"` ואחריו את `name`
#
# דוגמה לאינטראקציה:
# `What is your name? Maya`
# `Welcome to {{school}}, Maya`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# חשבי את העלות הכוללת של {{item}}s.
#
# 1. השתמשי ב-`input()` כדי לשאול `"How many {{item}}s? "` ושמרי את התשובה במשתנה `quantity_text`
# 2. המירי את `quantity_text` למספר שלם: `quantity = int(quantity_text)`
# 3. צרי משתנה `price` עם הערך `10`
# 4. צרי משתנה `total` = `quantity * price`
# 5. הדפיסי `"Total cost:"` ואחריו את `total`
#
# דוגמה לאינטראקציה:
# `How many {{item}}s? 5`
# `Total cost: 50`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# צרי מחשבון נתוני דמות.
#
# 1. שאלי `"Enter strength: "` והמירי לשלם, שמרי ב-`strength`
# 2. שאלי `"Enter defense: "` והמירי לשלם, שמרי ב-`defense`
# 3. חשבי `power` = `strength * 2 + defense`
# 4. הדפיסי `"Power level:"` ואחריו את `power`
#
# > רמז: אפשר לשלב את `int()` ו-`input()` בשורה אחת:
# >      `strength = int(input("Enter strength: "))`
#
# דוגמה לאינטראקציה:
# `Enter strength: 10`
# `Enter defense: 5`
# `Power level: 25`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# צרי תעודת זהות מותאמת אישית של {{school}}.
#
# 1. שאלי `"Student name: "` ושמרי ב-`name`
# 2. שאלי `"Student age: "` והמירי לשלם, שמרי ב-`age`
# 3. שאלי `"Favorite subject: "` ושמרי ב-`subject`
# 4. הדפיסי `"=== {{school}} ID ==="`
# 5. הדפיסי `"Name:"` ואחריו את `name`
# 6. הדפיסי `"Age:"` ואחריו את `age`
# 7. הדפיסי `"Specialty:"` ואחריו את `subject`
#
# דוגמה לאינטראקציה:
# `Student name: {{hero}}`
# `Student age: 12`
# `Favorite subject: Coding`
# `=== {{school}} ID ===`
# `Name: {{hero}}`
# `Age: 12`
# `Specialty: Coding`

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
