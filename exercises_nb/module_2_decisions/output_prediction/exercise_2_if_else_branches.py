# =============================================================================
# Output Prediction: if/else Branches
# =============================================================================
# Difficulty: 2
# Concepts: if/else, two-branch decisions, mutual exclusion
# =============================================================================

# %% [markdown]
# {{CONTEXT_PREDICTION_INTRO}}
# {{CONTEXT_PREDICTION_PURPOSE}}
#
# ## {{CHALLENGE_1_TITLE}}
# {{CONTEXT_CHALLENGE_1_NARRATIVE}}
# עם `if/else`, בדיוק ענף אחד מתבצע.

# %% locked
age = 15
if age >= 18:
    print("{{hero}} is an adult")
else:
    print("{{hero}} is still training")

# %% [markdown]
# ## ניחוש הפלט
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# שורה 1: _______________
#
# {{CONTEXT_PREDICTION_GUIDANCE_1}}
# > רמז: האם 15 >= 18? אם לא, הענף של `else` מתבצע במקום.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_2_TITLE}}
# {{CONTEXT_CHALLENGE_2_NARRATIVE}}
# שימי לב למה קורה לפני ואחרי ה-`if/else`.

# %% locked
score = 85
print("Checking score...")
if score >= 70:
    print("{{hero}} passed!")
    print("{{mentor}} is proud.")
else:
    print("{{hero}} needs more practice.")
print("Result recorded.")

# %% [markdown]
# ## ניחוש הפלט
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# שורה 1: _______________
# שורה 2: _______________
# שורה 3: _______________
# שורה 4: _______________
#
# {{CONTEXT_PREDICTION_GUIDANCE_2}}
# > רמז: קוד שנמצא לפני ה-`if` ואחרי ה-`else` תמיד מתבצע. רק ענף אחד מתבצע.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_3_TITLE}}
# {{CONTEXT_CHALLENGE_3_NARRATIVE}}
# התנאי משתמש ב-`==` כדי לבדוק שוויון.

# %% locked
password = "{{password}}"
entered = "wrong"
if password == entered:
    print("Access granted to {{location}}")
else:
    print("Access denied!")

# %% [markdown]
# ## ניחוש הפלט
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# שורה 1: _______________
#
# {{CONTEXT_PREDICTION_GUIDANCE_3}}
# > רמז: האם `"{{password}}"` ו-`"wrong"` הן אותה מחרוזת?

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_4_TITLE}}
# {{CONTEXT_CHALLENGE_4_NARRATIVE}}
# המשתנים מושווים בזמן שה-`if` מתבצע.

# %% locked
gold = 100
price = 75
if gold >= price:
    print(f"{{hero}} buys the {{item}} for {price} gold")
    gold = gold - price
else:
    print("Not enough gold!")
print(f"Gold remaining: {gold}")

# %% [markdown]
# ## ניחוש הפלט
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# שורה 1: _______________
# שורה 2: _______________
#
# {{CONTEXT_PREDICTION_GUIDANCE_4}}
# > רמז: האם 100 >= 75? כמה זה 100 - 75?

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
