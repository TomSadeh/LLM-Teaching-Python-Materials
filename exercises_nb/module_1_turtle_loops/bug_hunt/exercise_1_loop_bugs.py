# =============================================================================
# Bug Hunt: Loop Bugs
# =============================================================================
# Difficulty: 5
# Concepts: loop errors, off-by-one, wrong angles, incorrect range
# =============================================================================

# %% [markdown]
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_MISSION}}

# %%
import turtle

# %% [markdown]
# ## {{CASE_1_TITLE}}
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# **התנהגות צפויה:**
# לצייר ריבוע (4 צלעות, כל פנייה 90 מעלות).
# הצורה אמורה להיסגר לגמרי.
#
# **מה שקורה בפועל:**
# הצב מצייר רק 3 צלעות ולא סוגר את הריבוע!
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

# %%
# {{hero}} wanted to draw a square at {{school}}
t = turtle.Turtle()
t.speed(0)
for i in range(3):  # Bug is here!
    t.forward(80)
    t.right(90)

# %% [markdown]
# מה מצאתי: ________________________________
# > רמז: כמה צלעות יש לריבוע?
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CASE_2_TITLE}}
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# **התנהגות צפויה:**
# לצייר משולש שווה-צלעות (3 צלעות שוות).
# הצורה אמורה להיסגר לגמרי.
#
# **מה שקורה בפועל:**
# הצב מצייר צורה כלשהי אבל היא לא נסגרת כמו שצריך!
# זה נראה יותר כמו קו מעוקל מאשר משולש.
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}

# %%
# {{creature}} tried to draw a triangle
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(150, 0)
t.pendown()
for i in range(3):
    t.forward(70)
    t.right(60)  # Bug is here!

# %% [markdown]
# מה מצאתי: ________________________________
# > רמז: הזווית החיצונית של משולש היא 120 מעלות, לא 60.
# > חשבי: 360 / 3 = ?
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CASE_3_TITLE}}
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# **התנהגות צפויה:**
# להדפיס את המספרים 1, 2, 3, 4, 5 (כל אחד בשורה נפרדת).
#
# **מה שקורה בפועל:**
# מדפיס 0, 1, 2, 3, 4 במקום!
# מספר ההתחלה שגוי.
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}

# %%
# Counting {{item}} items for {{hero}}
for i in range(5):  # Bug is here!
    print(i)

# %% [markdown]
# מה מצאתי: ________________________________
# > רמז: `range(5)` מתחיל מ-0, לא מ-1.
# > כדי לקבל 1-5, השתמשי ב-`range(start, stop)`.
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CASE_4_TITLE}}
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# **התנהגות צפויה:**
# לצייר משושה (6 צלעות) ב-{{location}}.
#
# **מה שקורה בפועל:**
# הצורה נסגרת מוקדם מדי! היא נראית כמו מחומש!
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}

# %%
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-150, 0)
t.pendown()
for i in range(6):
    t.forward(50)
    t.left(72)  # Bug is here!

# %% [markdown]
# מה מצאתי: ________________________________
# > רמז: למשושה יש 6 צלעות, אז הזווית צריכה להיות 360/6 = 60.
# > הקוד משתמש ב-72, שזו הזווית של מחומש (360/5).
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_INVESTIGATION_INTRO}}")
print("=" * 50)

print("\n=== {{CASE_1_TITLE}} ===")
print("Buggy version:")
buggy_a()
print("\nFixed version:")
# fix_a()  # Uncomment when fixed

print("\n=== {{CASE_2_TITLE}} ===")
print("Buggy version:")
buggy_b()
print("\nFixed version:")
# fix_b()

print("\n=== {{CASE_3_TITLE}} ===")
print("Buggy version:")
buggy_c()
print("\nFixed version:")
# fix_c()

print("\n=== {{CASE_4_TITLE}} ===")
print("Buggy version:")
buggy_d()
print("\nFixed version:")
# fix_d()

print("\n" + "=" * 50)
print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
turtle.done()
