# =============================================================================
# Code Ordering: Shape Sequence
# =============================================================================
# Difficulty: 2
# Concepts: turtle setup, for loop structure, loop body order
# =============================================================================

# %% [markdown]
# {{CONTEXT_CODE_ORDERING_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}

# %%
import turtle

# %% [markdown]
# ## {{ORDERING_1_TITLE}}
# {{CONTEXT_ORDERING_1_NARRATIVE}}
#
# עזרי ל-{{hero}} לצייר משולש. סדרי את השורות הבאות בסדר הנכון:
#
# SCRAMBLED LINES:
#   for i in range(3):
#       t.forward(100)
#       t.left(120)
#   t = turtle.Turtle()
#
# העתיקי את השורות למעלה בסדר הנכון.
#
# > רמז: צריך ליצור את הצב לפני שמשתמשים בו.
# > כותרת הלולאה באה לפני גוף הלולאה.
# > שורות גוף הלולאה חייבות להיות עם הזחה (indented)!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
pass  # Delete this and add the correctly ordered lines

# %% [markdown]
# ## {{ORDERING_2_TITLE}}
# {{CONTEXT_ORDERING_2_NARRATIVE}}
#
# צרי ריבוע עבור {{school}}. סדרי את השורות הבאות בסדר הנכון:
#
# SCRAMBLED LINES:
#       t.right(90)
#   t = turtle.Turtle()
#       t.forward(80)
#   for side in range(4):
#
# > רמז: מה בא קודם — ציור או פנייה?
# > קודם מתקדמים קדימה עם `t.forward()`, ואחר כך פונים עם `t.right()`.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{ORDERING_3_TITLE}}
# {{CONTEXT_ORDERING_3_NARRATIVE}}
#
# צייר מסלול עם הודעה עבור {{creature}}. סדרי את השורות הבאות בסדר הנכון:
#
# SCRAMBLED LINES:
#   print("Path complete!")
#   for step in range(5):
#   t = turtle.Turtle()
#       t.forward(20)
#
# > רמז: פקודת `print()` צריכה לבוא אחרי שכל הציור הסתיים.
# > ההודעה מכריזה שהמסלול הושלם.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{ORDERING_4_TITLE}}
# {{CONTEXT_ORDERING_4_NARRATIVE}}
#
# צייר ריבוע צבעוני ב-{{location}}. סדרי את השורות הבאות בסדר הנכון:
#
# SCRAMBLED LINES:
#   for i in range(4):
#       t.forward(60)
#   t.color("blue")
#       t.left(90)
#   t = turtle.Turtle()
#
# > רמז: הגדירי את הצבע לפני שמתחילים לצייר.
# > הצב חייב להיות קיים לפני שאפשר להגדיר את צבעו!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_CODE_ORDERING_INTRO}}")
print("=" * 50)

print("\n=== {{ORDERING_1_TITLE}} ===")
# challenge_a()  # Uncomment when ordered correctly

print("\n=== {{ORDERING_2_TITLE}} ===")
# challenge_b()

print("\n=== {{ORDERING_3_TITLE}} ===")
# challenge_c()

print("\n=== {{ORDERING_4_TITLE}} ===")
# challenge_d()

print("\nReorder each challenge, then uncomment to test!")
print("{{CONTEXT_ROLE_COMPLETE}}")
turtle.done()
