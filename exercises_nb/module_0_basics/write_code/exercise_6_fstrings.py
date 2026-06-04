# =============================================================================
# Write Code: f-strings
# =============================================================================
# Difficulty: 4
# Concepts: f-string syntax, expressions in f-strings, formatting
# =============================================================================

# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# צרי ברכה באמצעות f-string.
#
# 1. צרי משתנה `name` עם הערך "{{hero}}"
# 2. צרי משתנה `message` באמצעות f-string: f"Hello, {name}!"
# 3. הדפיסי את `message`
#
# > רמז: האות f מופיעה לפני גרשיים הפותחים: f"..."
# > משתנים נכתבים בתוך {סוגריים מסולסלים}
#
# פלט צפוי: Hello, {{hero}}!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# צרי שורת סטטוס עם כמה משתנים בתוך f-string אחת.
#
# 1. צרי משתנה `hero` עם הערך "{{hero}}"
# 2. צרי משתנה `location` עם הערך "{{school}}"
# 3. צרי משתנה `level` עם הערך 5
# 4. הדפיסי f-string: f"{hero} is at {location}, level {level}"
#
# פלט צפוי: {{hero}} is at {{school}}, level 5

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# השתמשי בביטויים חשבוניים בתוך f-string.
#
# 1. צרי משתנה `base_price` עם הערך 25
# 2. צרי משתנה `quantity` עם הערך 4
# 3. הדפיסי f-string שמחשבת את הסכום:
#    f"Total cost: {base_price * quantity}"
#
# > רמז: אפשר לעשות חישובים ישירות בתוך {הסוגריים המסולסלים}!
#
# פלט צפוי: Total cost: 100

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# צרי דף דמות של {{hero}} באמצעות f-strings.
#
# 1. צרי משתנה `name` עם הערך "{{hero}}"
# 2. צרי משתנה `class_type` עם הערך "Apprentice"
# 3. צרי משתנה `health` עם הערך 100
# 4. צרי משתנה `attack` עם הערך 15
# 5. צרי משתנה `defense` עם הערך 10
# 6. הדפיסי f"=== {name} the {class_type} ==="
# 7. הדפיסי f"HP: {health} | ATK: {attack} | DEF: {defense}"
# 8. הדפיסי f"Power Rating: {attack + defense}"
#
# פלט צפוי:
# === {{hero}} the Apprentice ===
# HP: 100 | ATK: 15 | DEF: 10
# Power Rating: 25

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
