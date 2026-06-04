# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# נושא: בניית פונקציות קלט חכמות
# רמת קושי: 3
#
# כתבי פונקציות קלט שאפשר להשתמש בהן שוב ושוב — בכל משחק או תוכנית אינטראקטיבית!
#
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# כתבי פונקציה שמקבלת מספר שלם בטווח מסוים.
#
# 1. התחילי לולאת `while True`
# 2. הדפיסי את הטקסט וקבלי קלט מהמשתמש
# 3. בדקי אם הקלט הוא מספר באמצעות `.lstrip('-').isdigit()`
#    אם לא — הדפיסי `"Please enter a number."` והמשיכי
# 4. המירי למספר שלם (`int`)
# 5. בדקי אם המספר בטווח
#    אם לא — הדפיסי `f"Must be between {min_val} and {max_val}."` והמשיכי
# 6. החזירי את המספר התקין

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# כתבי פונקציה שמקבלת בחירה מתוך רשימת אפשרויות.
#
# 1. הדפיסי את הטקסט של הבחירה
# 2. הדפיסי את רשימת האפשרויות עם מספרים
# 3. התחילי לולאת `while True`
# 4. קבלי קלט (המירי לאותיות קטנות להשוואה)
# 5. בדקי אם הקלט הוא מספר תקין (בין 1 ל-`len(options)`)
#    אם כן — החזירי את `options[int(input) - 1]`
# 6. בדקי אם הקלט תואם אפשרות כלשהי (ללא רגישות לאותיות גדולות/קטנות)
#    אם כן — החזירי את האפשרות המקורית
# 7. הדפיסי `"Invalid choice. Try again."`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# כתבי פונקציה שמקבלת תשובת כן/לא עם טקסטים מותאמים אישית.
#
# 1. התחילי לולאת `while True`
# 2. הדפיסי `f"{question} ({yes_text}/{no_text}): "` וקבלי קלט
# 3. המירי לאותיות קטנות והסירי רווחים מיותרים
# 4. אם הקלט תואם את `yes_text` או האות הראשונה שלו — החזירי `True`
# 5. אם הקלט תואם את `no_text` או האות הראשונה שלו — החזירי `False`
# 6. הדפיסי `f"Please enter {yes_text} or {no_text}."`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# כתבי פונקציה שמקבלת מחרוזת עם אימות מותאם אישית.
#
# 1. התחילי לולאת `while True`
# 2. הדפיסי את הטקסט וקבלי קלט
# 3. אם `validator_func(input)` מחזיר `True` — החזירי את הקלט
# 4. אחרת — הדפיסי את `error_message`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_5_TITLE}}
# {{CONTEXT_PHASE_5}}
#
# השתמשי בפונקציות הקלט שלך כדי לבנות יוצרת דמויות.

# %%
print("=" * 40)
print("   CHARACTER CREATOR")
print("=" * 40)
print()

# %% [markdown]
# 1. קבלי שם באמצעות `get_validated_string`
#    (אימות: אורך >= 2, שגיאה: `"Name must be at least 2 characters"`)
# 2. קבלי מחלקת דמות באמצעות `get_choice_from_list`
# 3. קבלי רמה באמצעות `get_integer_in_range`
# 4. הציגי סיכום
# 5. אשרי עם `get_yes_no`
# 6. אם אושר — החזירי `dict` עם שם, מחלקה ורמה
# 7. אם לא אושר — החזירי `None`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_PROJECT_INTRO}}")
print("=" * 50)

print("\n=== {{PHASE_1_TITLE}} ===")
print("Testing integer range input:")
# level = get_integer_in_range("Enter level (1-10): ", 1, 10)
# print(f"Level selected: {level}")

print("\n=== {{PHASE_2_TITLE}} ===")
print("Testing choice from list:")
# abilities = ["{{spell1}}", "{{spell2}}", "{{spell3}}"]
# choice = get_choice_from_list("Select ability:", abilities)
# print(f"Selected: {choice}")

print("\n=== {{PHASE_3_TITLE}} ===")
print("Testing yes/no:")
# answer = get_yes_no("Do you want to continue?")
# print(f"Answer: {answer}")

print("\n=== {{PHASE_4_TITLE}} ===")
print("Testing validated string:")
# def is_long_enough(s):
#     return len(s) >= 3
# name = get_validated_string("Enter name (3+ chars): ", is_long_enough, "Too short!")
# print(f"Name: {name}")

print("\n=== {{PHASE_5_TITLE}} ===")
print("Testing character creator:")
# character = create_character()
# if character:
#     print(f"\nCreated: {character}")
# else:
#     print("\nCancelled.")

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
