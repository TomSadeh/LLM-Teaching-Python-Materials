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
# ✏️ YOUR PREDICTION HERE ✏️
# range(4) generates numbers starting from 0.
# How many numbers? What are they?
#
# Line 1: ___
# Line 2: ___
# Line 3: ___
# Line 4: ___
#
# Hint: range(n) gives you n numbers: 0, 1, 2, ..., n-1
# It STOPS before reaching n.
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
# ✏️ YOUR PREDICTION HERE ✏️
# range(2, 6) has TWO arguments: start and stop.
# What number does it start at? What number does it stop before?
#
# Line 1: ___
# Line 2: ___
# Line 3: ___
# Line 4: ___
#
# Hint: range(start, stop) gives numbers from start up to (but not including) stop.
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
# ✏️ YOUR PREDICTION HERE ✏️
# range(1, 10, 2) has THREE arguments: start, stop, step.
# It starts at 1, stops before 10, and steps by 2.
#
# Line 1: ___
# Line 2: ___
# Line 3: ___
# Line 4: ___
# Line 5: ___
#
# Hint: Step of 2 means skip every other number.
# 1, 3, 5, 7, 9... until you reach 10.
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
# ✏️ YOUR PREDICTION HERE ✏️
# range(5, 0, -1) counts BACKWARDS!
# Start at 5, stop before 0, step by -1.
#
# Line 1: ___
# Line 2: ___
# Line 3: ___
# Line 4: ___
# Line 5: ___
#
# Hint: A negative step goes backwards: 5, 4, 3, 2, 1
# It stops BEFORE reaching 0.
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
# ✏️ YOUR PREDICTION HERE ✏️
# range(10, 31, 10) starts at 10, stops before 31, steps by 10.
#
# Line 1: ___
# Line 2: ___
# Line 3: ___
#
# Hint: 10, 20, 30... but stop before 31, so we get all three.
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
