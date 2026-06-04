# =============================================================================
# Output Prediction: Simple if Statements
# =============================================================================
# Difficulty: 1
# Concepts: Basic if statement, conditional execution
# =============================================================================

# %% [markdown]
# {{CONTEXT_PREDICTION_INTRO}}
# {{CONTEXT_PREDICTION_PURPOSE}}
#
# ## {{CHALLENGE_1_TITLE}}
# {{CONTEXT_CHALLENGE_1_NARRATIVE}}
# האם הקוד שבתוך בלוק ה-`if` מתבצע?

# %% locked
power_level = 100
if power_level > 50:
    print("{{hero}} is strong enough!")

# %% [markdown]
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# שורה 1: _______________
#
# {{CONTEXT_PREDICTION_GUIDANCE_1}}
# > רמז: האם 100 > 50? אם כן, פקודת ה-`print` מתבצעת.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_2_TITLE}}
# {{CONTEXT_CHALLENGE_2_NARRATIVE}}
# האם יודפס משהו כאשר התנאי הוא `False`?

# %% locked
score = 30
if score > 50:
    print("{{hero}} passed the test!")
print("The test is complete.")

# %% [markdown]
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# שורה 1: _______________
#
# {{CONTEXT_PREDICTION_GUIDANCE_2}}
# > רמז: האם 30 > 50? הקוד שאחרי בלוק ה-`if` תמיד מתבצע.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_3_TITLE}}
# {{CONTEXT_CHALLENGE_3_NARRATIVE}}
# שימי לב מה נמצא בתוך בלוק ה-`if` ומה נמצא מחוצה לו.

# %% locked
points = 75
print(f"{{hero}} earned {points} points")
if points > 60:
    print("That's a good score!")
    print("{{mentor}} is pleased.")
print("Training session ended.")

# %% [markdown]
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# שורה 1: _______________
# שורה 2: _______________
# שורה 3: _______________
# שורה 4: _______________
#
# {{CONTEXT_PREDICTION_GUIDANCE_3}}
# > רמז: ספרי בזהירות — כמה פקודות `print` נמצאות בתוך ה-`if`?

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_4_TITLE}}
# {{CONTEXT_CHALLENGE_4_NARRATIVE}}
# אפשר גם להשוות משתנים אחד לשני.

# %% locked
hero_strength = 45
required_strength = 50
if hero_strength > required_strength:
    print("{{hero}} can enter {{location}}!")
print(f"Strength: {hero_strength}/{required_strength}")

# %% [markdown]
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# שורה 1: _______________
#
# {{CONTEXT_PREDICTION_GUIDANCE_4}}
# > רמז: השווי בין שני המספרים — האם 45 > 50?

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

print("\n" + "=" * 50)
print("{{CONTEXT_VERIFICATION_COMPLETE}}")
