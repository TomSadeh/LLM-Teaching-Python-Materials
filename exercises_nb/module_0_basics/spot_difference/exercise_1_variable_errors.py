# =============================================================================
# Spot the Difference: Variable Errors
# =============================================================================
# Difficulty: 2
# Concepts: variable assignment vs comparison, variable naming, typos
# =============================================================================

# %% [markdown]
# {{CONTEXT_SPOT_DIFFERENCE_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# {{COMPARISON_1_TITLE}}
# {{CONTEXT_COMPARISON_1_NARRATIVE}}

# %%
hero_name = "{{hero}}"
print(hero_name)

# %%
hero_name = "{{hero}}"
print(hero_Name)

# %% [markdown]
# ✏️ EXPLAIN THE DIFFERENCE ✏️
#
# Look closely at both versions. What's different?
# Hint: Python cares about uppercase and lowercase letters.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
explanation = """
The difference is:
-

Version 1 behavior:
-

Version 2 behavior:
-

Why this matters:
-
"""
return explanation

# %% [markdown]
# {{COMPARISON_2_TITLE}}
# {{CONTEXT_COMPARISON_2_NARRATIVE}}

# %%
points = 50
print("Score:", points)

# %%
points = 50
print("Score:", "points")

# %% [markdown]
# ✏️ EXPLAIN THE DIFFERENCE ✏️
#
# One version prints the value, one prints the word.
# Hint: Quotes make a difference!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
explanation = """
The difference is:
-

Version 1 output:
-

Version 2 output:
-

Why this matters:
-
"""
return explanation

# %% [markdown]
# {{COMPARISON_3_TITLE}}
# {{CONTEXT_COMPARISON_3_NARRATIVE}}

# %%
item_count = 5
print("{{hero}} has", item_count, "{{item}}s")

# %%
itemcount = 5
print("{{hero}} has", item_count, "{{item}}s")

# %% [markdown]
# ✏️ EXPLAIN THE DIFFERENCE ✏️
#
# The variable is created with one name but used with another.
# Hint: Underscores matter in variable names.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
explanation = """
The difference is:
-

Version 1 behavior:
-

Version 2 behavior:
-

Why this matters:
-
"""
return explanation

# %%
print("{{CONTEXT_SPOT_DIFFERENCE_INTRO}}")
print("=" * 50)

print("\n=== {{COMPARISON_1_TITLE}} ===")
print("Version 1:")
snippet_a1()
print("\nVersion 2:")
# snippet_a2()  # This would cause an error!
print("(This version has a bug - can you find it?)")
print(f"\nYour explanation:{explain_difference_a()}")

print("\n=== {{COMPARISON_2_TITLE}} ===")
print("Version 1:")
snippet_b1()
print("\nVersion 2:")
snippet_b2()
print(f"\nYour explanation:{explain_difference_b()}")

print("\n=== {{COMPARISON_3_TITLE}} ===")
print("Version 1:")
snippet_c1()
print("\nVersion 2:")
# snippet_c2()  # This would cause an error!
print("(This version has a bug - can you find it?)")
print(f"\nYour explanation:{explain_difference_c()}")

print("=" * 50)
print("{{CONTEXT_ROLE_COMPLETE}}")
