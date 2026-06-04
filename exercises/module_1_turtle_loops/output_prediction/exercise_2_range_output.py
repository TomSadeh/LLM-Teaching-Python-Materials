# =============================================================================
# Output Prediction: Range Output
# =============================================================================
# Difficulty: 3
# Concepts: range() with 1, 2, and 3 arguments
# =============================================================================

# %% [markdown]
# {{CONTEXT_PREDICTION_INTRO}}
# {{CONTEXT_PREDICTION_PURPOSE}}
#
# ## {{CHALLENGE_1_TITLE}}
# {{CONTEXT_CHALLENGE_1_NARRATIVE}}

# %% locked
# {{hero}} uses range to count steps at {{school}}
for i in range(4):
    print(i)

# %% [markdown]
# `range(4)` מייצרת מספרים שמתחילים מ-0.
# כמה מספרים? מה הם?
#
# שורה 1: ___
# שורה 2: ___
# שורה 3: ___
# שורה 4: ___
#
# > רמז: `range(n)` נותנת לך n מספרים: 0, 1, 2, ..., n-1
# > היא עוצרת לפני שמגיעים ל-n.
#
# {{CONTEXT_PREDICTION_GUIDANCE_1}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_2_TITLE}}
# {{CONTEXT_CHALLENGE_2_NARRATIVE}}

# %% locked
# Counting {{creature}} sightings at {{location}}
for num in range(2, 6):
    print(num)

# %% [markdown]
# ל-`range(2, 6)` יש שני ארגומנטים: התחלה ועצירה.
# באיזה מספר היא מתחילה? לפני איזה מספר היא עוצרת?
#
# שורה 1: ___
# שורה 2: ___
# שורה 3: ___
# שורה 4: ___
#
# > רמז: `range(start, stop)` נותנת מספרים החל מ-start ועד (לא כולל) stop.
#
# {{CONTEXT_PREDICTION_GUIDANCE_2}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_3_TITLE}}
# {{CONTEXT_CHALLENGE_3_NARRATIVE}}

# %% locked
# Levels at {{school}} that {{hero}} can access
for level in range(1, 10, 2):
    print(level)

# %% [markdown]
# ל-`range(1, 10, 2)` יש שלושה ארגומנטים: התחלה, עצירה, וצעד.
# היא מתחילה ב-1, עוצרת לפני 10, ומתקדמת בצעדים של 2.
#
# שורה 1: ___
# שורה 2: ___
# שורה 3: ___
# שורה 4: ___
# שורה 5: ___
#
# > רמז: צעד של 2 אומר לדלג על כל מספר שני.
# > 1, 3, 5, 7, 9... עד שמגיעים ל-10.
#
# {{CONTEXT_PREDICTION_GUIDANCE_3}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_4_TITLE}}
# {{CONTEXT_CHALLENGE_4_NARRATIVE}}

# %% locked
# Countdown for {{hero}}'s {{spell1}}
for count in range(5, 0, -1):
    print(count)

# %% [markdown]
# `range(5, 0, -1)` סופרת אחורה!
# מתחילה ב-5, עוצרת לפני 0, מתקדמת בצעד של 1-.
#
# שורה 1: ___
# שורה 2: ___
# שורה 3: ___
# שורה 4: ___
# שורה 5: ___
#
# > רמז: צעד שלילי הולך אחורה: 5, 4, 3, 2, 1
# > היא עוצרת לפני שמגיעים ל-0.
#
# {{CONTEXT_PREDICTION_GUIDANCE_4}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_5_TITLE}}
# {{CONTEXT_CHALLENGE_5_NARRATIVE}}

# %% locked
# Power levels for {{creature}} at {{place}}
for power in range(10, 31, 10):
    print(power)

# %% [markdown]
# `range(10, 31, 10)` מתחילה ב-10, עוצרת לפני 31, מתקדמת בצעדים של 10.
#
# שורה 1: ___
# שורה 2: ___
# שורה 3: ___
#
# > רמז: 10, 20, 30... אבל עוצרים לפני 31, ולכן מקבלים את שלושתם.
#
# {{CONTEXT_PREDICTION_GUIDANCE_5}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("=== {{CHALLENGE_1_TITLE}} ===")
print("-- Actual Output --")
challenge_a_code()
print("\n-- Your Prediction --")
challenge_a_prediction()

print("\n=== {{CHALLENGE_2_TITLE}} ===")
print("-- Actual Output --")
challenge_b_code()
print("\n-- Your Prediction --")
challenge_b_prediction()

print("\n=== {{CHALLENGE_3_TITLE}} ===")
print("-- Actual Output --")
challenge_c_code()
print("\n-- Your Prediction --")
challenge_c_prediction()

print("\n=== {{CHALLENGE_4_TITLE}} ===")
print("-- Actual Output --")
challenge_d_code()
print("\n-- Your Prediction --")
challenge_d_prediction()

print("\n=== {{CHALLENGE_5_TITLE}} ===")
print("-- Actual Output --")
challenge_e_code()
print("\n-- Your Prediction --")
challenge_e_prediction()

print("\n" + "=" * 50)
print("{{CONTEXT_VERIFICATION_COMPLETE}}")
