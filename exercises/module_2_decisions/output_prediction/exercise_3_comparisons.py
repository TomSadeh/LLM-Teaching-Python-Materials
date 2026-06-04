# =============================================================================
# Output Prediction: Comparison Operators
# =============================================================================
# Difficulty: 2-3
# Concepts: ==, !=, <, >, <=, >= operators
# =============================================================================

# %% [markdown]
# {{CONTEXT_PREDICTION_INTRO}}
# {{CONTEXT_PREDICTION_PURPOSE}}
#
# ## {{CHALLENGE_1_TITLE}}
# {{CONTEXT_CHALLENGE_1_NARRATIVE}}
# האופרטור `==` בודק אם שני ערכים שווים זה לזה.

# %% locked
hero_level = 5
required_level = 5
if hero_level == required_level:
    print("Level requirement met!")
else:
    print("Level too low!")
print(f"{{hero}} is level {hero_level}")

# %% [markdown]
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# שורה 1: _______________
# שורה 2: _______________
#
# {{CONTEXT_PREDICTION_GUIDANCE_1}}
# > רמז: האם 5 `==` 5? (כן, הם שווים)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_2_TITLE}}
# {{CONTEXT_CHALLENGE_2_NARRATIVE}}
# האופרטור `!=` בודק אם שני ערכים אינם שווים זה לזה.

# %% locked
villain = "{{villain}}"
ally = "{{friend}}"
if villain != ally:
    print(f"{{hero}} recognizes {villain} as an enemy!")
else:
    print(f"{{hero}} is confused.")

# %% [markdown]
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# שורה 1: _______________
#
# {{CONTEXT_PREDICTION_GUIDANCE_2}}
# > רמז: האם `"{{villain}}"` ו-`"{{friend}}"` שונים זה מזה? (`!=` פירושו "לא שווה")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_3_TITLE}}
# {{CONTEXT_CHALLENGE_3_NARRATIVE}}
# נשווה בין `<` (קטן מ-) לבין `<=` (קטן מ- או שווה ל-).

# %% locked
health = 50
danger_threshold = 50
print(f"Health: {health}")
if health < danger_threshold:
    print("DANGER: Health critically low!")
if health <= danger_threshold:
    print("WARNING: Health at or below threshold")

# %% [markdown]
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# שורה 1: _______________
# שורה 2: _______________  (אולי?)
# שורה 3: _______________  (אולי?)
#
# {{CONTEXT_PREDICTION_GUIDANCE_3}}
# > רמז: האם 50 `<` 50? (לא, הם שווים, לא קטן)
# >       האם 50 `<=` 50? (כן, הם שווים אז זה נחשב)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_4_TITLE}}
# {{CONTEXT_CHALLENGE_4_NARRATIVE}}
# נשווה בין `>` (גדול מ-) לבין `>=` (גדול מ- או שווה ל-).

# %% locked
score = 70
passing = 70
print(f"Score: {score}, Passing: {passing}")
if score > passing:
    print("Above passing!")
if score >= passing:
    print("Passed!")
if score == passing:
    print("Exactly at the threshold")

# %% [markdown]
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# שורה 1: _______________
# שורה 2: _______________  (אולי?)
# שורה 3: _______________  (אולי?)
# שורה 4: _______________  (אולי?)
#
# {{CONTEXT_PREDICTION_GUIDANCE_4}}
# > רמז: כל `if` נבדק בנפרד. כמה מהם נכונים?

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_5_TITLE}}
# {{CONTEXT_CHALLENGE_5_NARRATIVE}}
# מספר השוואות ברצף.

# %% locked
temperature = 25
if temperature < 0:
    print("Freezing!")
if temperature < 15:
    print("Cold")
if temperature < 30:
    print("Comfortable")
if temperature >= 30:
    print("Hot!")

# %% [markdown]
# כתבי בדיוק מה לדעתך יודפס למעלה.
#
# שורה 1: _______________  (אולי?)
# שורה 2: _______________  (אולי?)
# שורה 3: _______________  (אולי?)
# שורה 4: _______________  (אולי?)
#
# {{CONTEXT_PREDICTION_GUIDANCE_5}}
# > רמז: אלו משפטי `if` נפרדים (לא `if/elif`).
# >       25 `<` 0? 25 `<` 15? 25 `<` 30? 25 `>=` 30?

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
