# =============================================================================
# Output Prediction: Arithmetic
# =============================================================================
# Difficulty: 2-3
# Concepts: arithmetic operators, order of operations, integer vs float division
# =============================================================================

# %% [markdown]
# {{CONTEXT_PREDICTION_INTRO}}
# {{CONTEXT_PREDICTION_PURPOSE}}
#
# ## {{CHALLENGE_1_TITLE}}
# {{CONTEXT_CHALLENGE_1_NARRATIVE}}

# %% locked
gold = 100
spent = 25
remaining = gold - spent
print(remaining)

# %% [markdown]
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# פלט: _______________
#
# > רמז: חיסור עובד בדיוק כמו במתמטיקה.
#
# {{CONTEXT_PREDICTION_GUIDANCE_1}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_2_TITLE}}
# {{CONTEXT_CHALLENGE_2_NARRATIVE}}

# %% locked
items = 3
price = 10
total = items * price
print("Total cost:", total)

# %% [markdown]
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# פלט: _______________
#
# > רמז: הסימן `*` אומר כפל.
#
# {{CONTEXT_PREDICTION_GUIDANCE_2}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_3_TITLE}}
# {{CONTEXT_CHALLENGE_3_NARRATIVE}}

# %% locked
cookies = 10
people = 3
each_gets = cookies // people
leftover = cookies % people
print("Each person gets:", each_gets)
print("Leftover:", leftover)

# %% [markdown]
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# שורה 1: _______________
# שורה 2: _______________
#
# > רמז: `//` נותן את החלק השלם של החלוקה.
# > `%` נותן את השארית אחרי החלוקה.
#
# {{CONTEXT_PREDICTION_GUIDANCE_3}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_4_TITLE}}
# {{CONTEXT_CHALLENGE_4_NARRATIVE}}

# %% locked
base = 2
power = base ** 3
print(power)

# %% [markdown]
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# פלט: _______________
#
# > רמז: `**` אומר חזקה (העלאה בחזקה).
# > `2 ** 3` פירושו `2 * 2 * 2`
#
# {{CONTEXT_PREDICTION_GUIDANCE_4}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_5_TITLE}}
# {{CONTEXT_CHALLENGE_5_NARRATIVE}}

# %% locked
result = 2 + 3 * 4
print(result)

# %% [markdown]
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# פלט: _______________
#
# > רמז: Python פועל לפי סדר הפעולות המתמטי.
# > כפל מתבצע לפני חיבור.
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
