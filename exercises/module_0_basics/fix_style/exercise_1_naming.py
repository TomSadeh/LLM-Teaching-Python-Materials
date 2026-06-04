# =============================================================================
# Fix the Style: Naming Conventions
# =============================================================================
# Difficulty: 5
# Concepts: PEP 8 naming, readable code, meaningful variable names
# =============================================================================

# %% [markdown]
# {{CONTEXT_FIX_STYLE_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# {{STYLE_1_TITLE}}
# {{CONTEXT_STYLE_1_NARRATIVE}}

# %%
x = "{{hero}}"
y = "{{school}}"
z = 100
print(x, "studies at", y, "with", z, "points")

# %% [markdown]
# {{CONTEXT_STYLE_FIX_1}}
#
# כתבי מחדש את הקוד למעלה עם סגנון נכון.
# שינויים לביצוע:
# 1. שנמי את `x` לשם משמעותי (כמו `hero_name`)
# 2. שנמי את `y` לשם משמעותי (כמו `school_name`)
# 3. שנמי את `z` לשם משמעותי (כמו `points`)
#
# הפלט צריך להישאר בדיוק אותו דבר!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{STYLE_2_TITLE}}
# {{CONTEXT_STYLE_2_NARRATIVE}}

# %%
a=10
b=5
c=a+b
d=a*b
print("Sum:",c,"Product:",d)

# %% [markdown]
# {{CONTEXT_STYLE_FIX_2}}
#
# שינויים לביצוע:
# 1. הוסיפי רווחים מסביב לסימני `=`
# 2. הוסיפי רווחים מסביב לאופרטורים `+` ו-`*`
# 3. הוסיפי רווח אחרי הנקודתיים בתוך `print`
# 4. השתמשי בשמות משתנים משמעותיים

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{STYLE_3_TITLE}}
# {{CONTEXT_STYLE_3_NARRATIVE}}

# %%
n = "{{hero}}"
l = 5
h = 100
g = 50
print(n)
print("Level:" + str(l))
print("HP:" + str(h))
print("Gold:" + str(g))

# %% [markdown]
# {{CONTEXT_STYLE_FIX_3}}
#
# שינויים לביצוע:
# 1. השתמשי בשמות משתנים משמעותיים (`name`, `level`, `health`, `gold`)
# 2. השתמשי ב-f-strings במקום חיבור מחרוזות
# 3. הוסיפי רווח אחרי הנקודתיים בפלט

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_FIX_STYLE_INTRO}}")
print("=" * 50)

print("\n=== {{STYLE_1_TITLE}} ===")
print("Original (poor style):")
original_a()
print("\nFixed (your version):")
fixed_a()

print("\n=== {{STYLE_2_TITLE}} ===")
print("Original (poor style):")
original_b()
print("\nFixed (your version):")
fixed_b()

print("\n=== {{STYLE_3_TITLE}} ===")
print("Original (poor style):")
original_c()
print("\nFixed (your version):")
fixed_c()

print("\n" + "=" * 50)
print("{{CONTEXT_IMPROVEMENT_COMPLETE}}")
