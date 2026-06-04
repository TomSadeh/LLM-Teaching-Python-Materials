# =============================================================================
# Bug Hunt: Basics Bugs
# =============================================================================
# Difficulty: 5
# Concepts: All Module 0 concepts - integration debugging
# =============================================================================

# %% [markdown]
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_MISSION}}
#
# {{CASE_1_TITLE}}
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Should print "{{hero}} has 75 gold" (100 - 25 = 75)
#
# ACTUAL BEHAVIOR:
# Prints "{{hero}} has 10025 gold" (concatenated as strings!)
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

# %%
gold = "100"
spent = 25
remaining = gold - spent
print("{{hero}} has", remaining, "gold")

# %% [markdown]
# ✏️ FIX THE BUG ✏️
#
# What I found: ________________________________
#
# Hint: Look at how gold is defined. Is it a number or a string?
#
# The fix:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{CASE_2_TITLE}}
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Should print the hero's name stored in the variable
#
# ACTUAL BEHAVIOR:
# Prints the word "hero_name" instead of the actual name
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}

# %%
hero_name = "{{hero}}"
print("Welcome,", "hero_name")

# %% [markdown]
# ✏️ FIX THE BUG ✏️
#
# What I found: ________________________________
#
# Hint: When do you use quotes around a variable name?
#
# The fix:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{CASE_3_TITLE}}
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Should calculate double the score: 50 * 2 = 100
#
# ACTUAL BEHAVIOR:
# The doubled variable is never used!
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}

# %%
score = 50
doubled = score * 2
print("Double score:", score)

# %% [markdown]
# ✏️ FIX THE BUG ✏️
#
# What I found: ________________________________
#
# Hint: Check which variable is being printed.
#
# The fix:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{CASE_4_TITLE}}
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# Should greet {{hero}} at {{school}} on one line
#
# ACTUAL BEHAVIOR:
# Error: can only concatenate str (not "int") to str
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}

# %%
name = "{{hero}}"
level = 5
message = name + " is level " + level + " at {{school}}"
print(message)

# %% [markdown]
# ✏️ FIX THE BUG ✏️
#
# What I found: ________________________________
#
# Hint: You can't use + to join a string with a number directly.
# Either convert the number to a string, or use a different approach.
#
# The fix:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_INVESTIGATION_INTRO}}")
print("=" * 50)

print("\n=== {{CASE_1_TITLE}} ===")
print("Buggy version:")
# buggy_a()  # This would cause an error!
print("(Error: can't subtract from string)")
print("\nFixed version:")
fix_a()

print("\n=== {{CASE_2_TITLE}} ===")
print("Buggy version:")
buggy_b()
print("\nFixed version:")
fix_b()

print("\n=== {{CASE_3_TITLE}} ===")
print("Buggy version:")
buggy_c()
print("\nFixed version:")
fix_c()

print("\n=== {{CASE_4_TITLE}} ===")
print("Buggy version:")
# buggy_d()  # This would cause an error!
print("(Error: can't concatenate str and int)")
print("\nFixed version:")
fix_d()

print("\n" + "=" * 50)
print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
