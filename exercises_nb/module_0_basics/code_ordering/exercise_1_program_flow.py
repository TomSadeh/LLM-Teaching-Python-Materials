# =============================================================================
# Code Ordering: Program Flow
# =============================================================================
# Difficulty: 2-3
# Concepts: variable creation before use, order of operations, program sequence
# =============================================================================

# %% [markdown]
# {{CONTEXT_CODE_ORDERING_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## {{ORDERING_1_TITLE}}
# {{CONTEXT_ORDERING_1_NARRATIVE}}
#
# שורות מבולגנות:
#   `print("Final score:", score)`
#   `score = base + bonus`
#   `bonus = 50`
#   `base = 100`
#
# סדרי מחדש את השורות בסדר הנכון.
#
# > רמז: חייבים ליצור משתנה לפני שמשתמשים בו.
# > אילו ערכים את צריכה לפני שאפשר לחשב את `score`?

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
pass  # Delete this and add the correctly ordered lines

# %% [markdown]
# ## {{ORDERING_2_TITLE}}
# {{CONTEXT_ORDERING_2_NARRATIVE}}
#
# שורות מבולגנות:
#   `total = price * quantity`
#   `print("{{hero}} pays:", total)`
#   `quantity = 4`
#   `price = 25`
#
# סדרי מחדש את השורות בסדר הנכון.
#
# > רמז: חשבי איזה ערכים החישוב של `total` צריך.
# > `price` ו-`quantity` חייבים להתקיים לפני שאפשר להכפיל אותם.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{ORDERING_3_TITLE}}
# {{CONTEXT_ORDERING_3_NARRATIVE}}
#
# שורות מבולגנות:
#   `print("{{hero}} has", leftover, "remaining")`
#   `leftover = total - spent`
#   `spent = 30`
#   `print("{{hero}} starts with", total)`
#   `total = 100`
#
# סדרי מחדש את השורות בסדר הנכון.
#
# > רמז: יש פה שתי פקודות `print`. שימי לב מתי כל אחת צריכה להופיע
# > כדי לספר את הסיפור בסדר: קודם הסכום ההתחלתי, ואז התוצאה.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{ORDERING_4_TITLE}}
# {{CONTEXT_ORDERING_4_NARRATIVE}}
#
# שורות מבולגנות:
#   `final = doubled ** 2`
#   `print("Result:", final)`
#   `start = 3`
#   `doubled = start * 2`
#
# סדרי מחדש את השורות בסדר הנכון.
#
# > רמז: כל חישוב תלוי בזה שלפניו.
# > `start` ← `doubled` ← `final` ← `print`

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
