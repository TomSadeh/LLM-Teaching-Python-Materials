# =============================================================================
# Output Prediction: Print Basics
# =============================================================================
# Difficulty: 1
# Concepts: print() function, string literals, commas in print
# =============================================================================

# %% [markdown]
# {{CONTEXT_PREDICTION_INTRO}}
# {{CONTEXT_PREDICTION_PURPOSE}}
#
# ## {{CHALLENGE_1_TITLE}}
# {{CONTEXT_CHALLENGE_1_NARRATIVE}}

# %% locked
print("Hello, world!")
print("Welcome to {{school}}")

# %% [markdown]
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# שורה 1: _______________
# שורה 2: _______________
#
# {{CONTEXT_PREDICTION_GUIDANCE_1}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_2_TITLE}}
# {{CONTEXT_CHALLENGE_2_NARRATIVE}}

# %% locked
print("{{hero}}", "is learning")
print("Python" + " programming")

# %% [markdown]
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# שורה 1: _______________
# שורה 2: _______________
#
# > רמז: שימי לב להבדל בין פסיק (,) לבין פלוס (+).
# > פסיק מוסיף רווח בין הפריטים, ואילו פלוס מחבר אותם ישירות.
#
# {{CONTEXT_PREDICTION_GUIDANCE_2}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_3_TITLE}}
# {{CONTEXT_CHALLENGE_3_NARRATIVE}}

# %% locked
message = "{{greeting}}"
print(message)
print("message")

# %% [markdown]
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# שורה 1: _______________
# שורה 2: _______________
#
# > רמז: שימי לב להבדל בין שם משתנה (ללא מרכאות) לבין מחרוזת טקסט (עם מרכאות).
#
# {{CONTEXT_PREDICTION_GUIDANCE_3}}

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

print("\n" + "=" * 50)
print("{{CONTEXT_VERIFICATION_COMPLETE}}")
