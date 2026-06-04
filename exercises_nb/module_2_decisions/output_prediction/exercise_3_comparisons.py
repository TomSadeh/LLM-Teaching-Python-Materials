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
# The == operator checks if two values are equal.

# %% locked
hero_level = 5
required_level = 5
if hero_level == required_level:
    print("Level requirement met!")
else:
    print("Level too low!")
print(f"{{hero}} is level {hero_level}")

# %% [markdown]
# ✏️ YOUR PREDICTION HERE ✏️
# Write EXACTLY what you think will be printed above.
#
# Line 1: _______________
# Line 2: _______________
#
# {{CONTEXT_PREDICTION_GUIDANCE_1}}
# Hint: Is 5 == 5? (Yes, they are equal)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_2_TITLE}}
# {{CONTEXT_CHALLENGE_2_NARRATIVE}}
# The != operator checks if two values are NOT equal.

# %% locked
villain = "{{villain}}"
ally = "{{friend}}"
if villain != ally:
    print(f"{{hero}} recognizes {villain} as an enemy!")
else:
    print(f"{{hero}} is confused.")

# %% [markdown]
# ✏️ YOUR PREDICTION HERE ✏️
# Write EXACTLY what you think will be printed above.
#
# Line 1: _______________
#
# {{CONTEXT_PREDICTION_GUIDANCE_2}}
# Hint: Are "{{villain}}" and "{{friend}}" different? (!= means "not equal")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_3_TITLE}}
# {{CONTEXT_CHALLENGE_3_NARRATIVE}}
# Compare < (less than) vs <= (less than OR equal).

# %% locked
health = 50
danger_threshold = 50
print(f"Health: {health}")
if health < danger_threshold:
    print("DANGER: Health critically low!")
if health <= danger_threshold:
    print("WARNING: Health at or below threshold")

# %% [markdown]
# ✏️ YOUR PREDICTION HERE ✏️
# Write EXACTLY what you think will be printed above.
#
# Line 1: _______________
# Line 2: _______________  (maybe?)
# Line 3: _______________  (maybe?)
#
# {{CONTEXT_PREDICTION_GUIDANCE_3}}
# Hint: Is 50 < 50? (No, it's equal, not less)
#       Is 50 <= 50? (Yes, it's equal so it counts)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_4_TITLE}}
# {{CONTEXT_CHALLENGE_4_NARRATIVE}}
# Compare > (greater than) vs >= (greater than OR equal).

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
# ✏️ YOUR PREDICTION HERE ✏️
# Write EXACTLY what you think will be printed above.
#
# Line 1: _______________
# Line 2: _______________  (maybe?)
# Line 3: _______________  (maybe?)
# Line 4: _______________  (maybe?)
#
# {{CONTEXT_PREDICTION_GUIDANCE_4}}
# Hint: Each if is checked independently. How many are True?

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_5_TITLE}}
# {{CONTEXT_CHALLENGE_5_NARRATIVE}}
# Multiple comparisons in sequence.

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
# ✏️ YOUR PREDICTION HERE ✏️
# Write EXACTLY what you think will be printed above.
#
# Line 1: _______________  (maybe?)
# Line 2: _______________  (maybe?)
# Line 3: _______________  (maybe?)
# Line 4: _______________  (maybe?)
#
# {{CONTEXT_PREDICTION_GUIDANCE_5}}
# Hint: These are separate if statements (not if/elif).
#       25 < 0? 25 < 15? 25 < 30? 25 >= 30?

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
