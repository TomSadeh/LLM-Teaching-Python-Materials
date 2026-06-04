# =============================================================================
# Bug Hunt: Drawing Bugs
# =============================================================================
# Difficulty: 5
# Concepts: multi-step drawing errors, accumulator bugs, pen state errors
# =============================================================================

# %% [markdown]
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_MISSION}}

# %%
import turtle

# %% [markdown]
# {{CASE_1_TITLE}}
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# **מה אמור לקרות:**
# לצייר שני ריבועים נפרדים עם רווח ביניהם.
#
# **מה קורה בפועל:**
# הריבועים מחוברים בקו! אמור להיות אין קו
# ביניהם.
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

# %%
# {{hero}} wants two separate squares at {{school}}
t = turtle.Turtle()
t.speed(0)

# Draw first square
for i in range(4):
    t.forward(50)
    t.right(90)

# Move to next position (BUG: forgot something!)
t.forward(70)

# Draw second square
for i in range(4):
    t.forward(50)
    t.right(90)

# %% [markdown]
# מה גיליתי: ________________________________
# > רמז: כדי לזוז בלי לצייר, צריך להרים את העט קודם!
# > השתמשי ב-`t.penup()` לפני הזוז וב-`t.pendown()` אחריו.
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{CASE_2_TITLE}}
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# **מה אמור לקרות:**
# לחשב total = 10 + 20 + 30 + 40 = 100 ולהדפיס אותו.
#
# **מה קורה בפועל:**
# התוכנית מדפיסה 0 בסוף! הסכום שגוי.
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}

# %%
# Calculate total distance for {{creature}}
total = 0
for i in range(1, 5):
    distance = i * 10
    total = 0 + distance  # Bug is here!
print("Total distance:", total)

# %% [markdown]
# מה גיליתי: ________________________________
# > רמז: התבנית הנכונה של המצבר היא: `total = total + distance`
# > ולא: `total = 0 + distance` (שמאפסת לערך האחרון)
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{CASE_3_TITLE}}
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# **מה אמור לקרות:**
# לצייר צורת כוכב עם 5 איטרציות ופניות של 144 מעלות.
#
# **מה קורה בפועל:**
# התוכנית קורסת עם `NameError`!
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}

# %%
# Drawing a star at {{location}}
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(100, 100)
t.pendown()
for i in range(5):
    t.forward(80)
    turtle.right(144)  # Bug is here!

# %% [markdown]
# מה גיליתי: ________________________________
# > רמז: יצרנו צב בשם `t`, אבל שורה אחת משתמשת ב-`turtle`
# > במקום ב-`t`. שמות משתנים חייבים להיות עקביים!
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{CASE_4_TITLE}}
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# **מה אמור לקרות:**
# לצייר ספירלה עם קווים שמתארכים: 10, 20, 30, 40, 50.
#
# **מה קורה בפועל:**
# כל הקווים באותו אורך! הספירלה לא גדלה.
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}

# %%
# Creating a spiral for {{hero}} at {{place}}
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-100, -100)
t.pendown()
for i in range(1, 6):
    length = 10  # Bug is here!
    t.forward(length)
    t.right(90)

# %% [markdown]
# מה גיליתי: ________________________________
# > רמז: האורך צריך להשתנות בהתאם ל-`i`.
# > לספירלה גדלה: `length = i * 10`
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{CASE_5_TITLE}}
# {{CONTEXT_CASE_5_NARRATIVE}}
#
# **מה אמור לקרות:**
# לצייר 5 מקפים עם רווחים ביניהם.
#
# **מה קורה בפועל:**
# אחרי המקף הראשון, שום דבר לא מצטייר!
#
# {{CONTEXT_INVESTIGATION_PROMPT_5}}

# %%
# Creating a dashed line at {{school}}
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200, -50)
t.pendown()
for i in range(5):
    t.forward(30)   # Draw dash
    t.penup()       # Lift pen
    t.forward(15)   # Move gap

# %% [markdown]
# ## שגיאה: שכחו לשים את העט בחזרה למטה!
#
# מה גיליתי: ________________________________
# > רמז: אחרי הזזת הרווח, צריך `t.pendown()` כדי לצייר שוב!
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
# fix_a()

print("\n=== {{CASE_2_TITLE}} ===")
print("Buggy version:")
buggy_b()
print("\nFixed version:")
# fix_b()

print("\n=== {{CASE_3_TITLE}} ===")
print("Buggy version:")
# buggy_c()  # This one crashes!
print("(Skipped - would crash)")
print("\nFixed version:")
# fix_c()

print("\n=== {{CASE_4_TITLE}} ===")
print("Buggy version:")
buggy_d()
print("\nFixed version:")
# fix_d()

print("\n=== {{CASE_5_TITLE}} ===")
print("Buggy version:")
buggy_e()
print("\nFixed version:")
# fix_e()

print("\n" + "=" * 50)
print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
turtle.done()
