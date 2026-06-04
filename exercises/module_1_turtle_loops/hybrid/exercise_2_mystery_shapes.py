# =============================================================================
# Hybrid Exercise: The Mystery - Strange Shapes
# =============================================================================
# Difficulty: 4-5
# Arc: The Mystery
# Parts: DISCOVERY -> INVESTIGATION -> IMPROVEMENT
# Concepts: debugging loops, tracing, fixing turtle programs
# =============================================================================

# %% [markdown]
# {{CONTEXT_DISCOVERY_INTRO}}
#
# זוהי תרגיל רב-חלקי. השלימי כל חלק לפי הסדר.

# %%
import turtle

# %% [markdown]
# ## חלק 1: גילוי - שימי לב למשהו לא צפוי
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# {{hero}} מצאה קצת קוד ציור ב-{{school}}.
# הקוד אמור לצייר ריבוע, אבל משהו לא בסדר!
# עיייני בפלט ושימי לב לבעיה.

# %%
# This should draw a square... but does it?
t = turtle.Turtle()
t.speed(0)
for i in range(4):
    t.forward(80)
    t.right(80)  # Something's off!

# %%
# This should count 1 to 5, but look at the output!
for num in range(5):
    print(f"Count: {num}")

# %%
# This should draw a growing spiral...
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(150, 50)
t.pendown()
for i in range(1, 6):
    length = 20  # All lines are the same!
    t.forward(length)
    t.right(90)

# %% [markdown]
# ## התצפיות שלי
#
# mystery_code_1:
#   ציפינו: ריבוע סגור
#   בפועל: ________________________________
#   מה נראה שגוי? ________________________________
#
# mystery_code_2:
#   ציפינו: מדפיס 1, 2, 3, 4, 5
#   בפועל: ________________________________
#   מה נראה שגוי? ________________________________
#
# mystery_code_3:
#   ציפינו: קווים מתארכים (20, 40, 60, 80, 100)
#   בפועל: ________________________________
#   מה נראה שגוי? ________________________________

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: חקירה - עקבי אחרי הקוד
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# עכשיו עקבי אחרי כל תעלומה כדי להבין בדיוק למה
# הקוד מתנהג בצורה לא צפויה.
#
# ## עקבי אחרי הקוד
#
# mystery_code_1 משתמש ב-`right(80)` במקום `right(90)`.
#
# | איטרציה | סך הזווית שנפנתה |
# |---------|-----------------|
# | 1       | 80               |
# | 2       |                  |
# | 3       |                  |
# | 4       |                  |
#
# סך הזווית: ___ מעלות
# לצורה סגורה: צריך להיות ___ מעלות
#
# הבאג: ________________________________

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## עקבי אחרי הקוד
#
# `range(5)` מייצר: ___, ___, ___, ___, ___
# אבל רצינו: 1, 2, 3, 4, 5
#
# כדי לקבל 1 עד 5, צריך להשתמש ב: `range(___, ___)`
#
# הבאג: ________________________________

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## עקבי אחרי הקוד
#
# | איטרציה | i | אורך (כפי שצריך) | אורך (בפועל) |
# |---------|---|-----------------|-------------|
# | 1       | 1 | 20               | 20          |
# | 2       | 2 | 40               | 20          |
# | 3       | 3 | 60               | 20          |
# | 4       | 4 | 80               | 20          |
# | 5       | 5 | 100              | 20          |
#
# הקוד מגדיר `length = 20` ישירות, ומתעלם מ-`i`.
# צריך להיות: `length = i * ___`
#
# הבאג: ________________________________

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: שיפור - תקני את הבעיות
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# עכשיו שהבנת את הבאגים, תקני אותם!
#
# ## תקני את הבאג
#
# תקני את הזווית כך שהריבוע ייסגר כראוי.
#
# התיקון שלי:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## תקני את הבאג
#
# תקני את ה-`range` כך שיספור מ-1 עד 5.
#
# התיקון שלי:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## תקני את הבאג
#
# תקני את חישוב האורך כך שהקווים יתארכו.
#
# התיקון שלי:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("=" * 50)
print("PART 1: DISCOVERY - Observe the Unexpected")
print("=" * 50)

print("\n--- mystery_code_1 ---")
print("This should draw a square...")
mystery_code_1()

print("\n--- mystery_code_2 ---")
print("This should count 1 to 5...")
mystery_code_2()

print("\n--- mystery_code_3 ---")
print("This should draw a growing spiral...")
mystery_code_3()

print("\n--- Your Observations ---")
your_observations()

print("\n" + "=" * 50)
print("PART 2: INVESTIGATION - Trace the Code")
print("=" * 50)

print("\n--- trace_mystery_1 ---")
trace_mystery_1()

print("\n--- trace_mystery_2 ---")
trace_mystery_2()

print("\n--- trace_mystery_3 ---")
trace_mystery_3()

print("\n" + "=" * 50)
print("PART 3: IMPROVEMENT - Fix the Issues")
print("=" * 50)

print("\n--- fixed_code_1 ---")
# fixed_code_1()  # Uncomment when fixed

print("\n--- fixed_code_2 ---")
# fixed_code_2()

print("\n--- fixed_code_3 ---")
# fixed_code_3()

print("\n" + "=" * 50)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
turtle.done()
