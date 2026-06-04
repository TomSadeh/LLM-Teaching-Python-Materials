# =============================================================================
# Fix the Style: Naming Conventions
# =============================================================================
# Difficulty: 5
# Concepts: PEP 8 naming, readable code, meaningful variable names
# =============================================================================

# %% [markdown]
# {{CONTEXT_FIX_STYLE_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# {{STYLE_1_TITLE}}
# {{CONTEXT_STYLE_1_NARRATIVE}}

# %%
x = "{{hero}}"
y = "{{school}}"
z = 100
print(x, "studies at", y, "with", z, "points")

# %% [markdown]
# ✏️ FIX THE STYLE ✏️
#
# {{CONTEXT_STYLE_FIX_1}}
#
# Rewrite the code above with proper style.
# Changes to make:
# - Rename x to something meaningful (like hero_name)
# - Rename y to something meaningful (like school_name)
# - Rename z to something meaningful (like points)
#
# The output should be exactly the same!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{STYLE_2_TITLE}}
# {{CONTEXT_STYLE_2_NARRATIVE}}

# %%
a=10
b=5
c=a+b
d=a*b
print("Sum:",c,"Product:",d)

# %% [markdown]
# ✏️ FIX THE STYLE ✏️
#
# {{CONTEXT_STYLE_FIX_2}}
#
# Changes to make:
# - Add spaces around = signs
# - Add spaces around + and * operators
# - Add spaces after colons in the print statement
# - Use meaningful variable names

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{STYLE_3_TITLE}}
# {{CONTEXT_STYLE_3_NARRATIVE}}

# %%
n = "{{hero}}"
l = 5
h = 100
g = 50
print(n)
print("Level:" + str(l))
print("HP:" + str(h))
print("Gold:" + str(g))

# %% [markdown]
# ✏️ FIX THE STYLE ✏️
#
# {{CONTEXT_STYLE_FIX_3}}
#
# Changes to make:
# - Use meaningful variable names (name, level, health, gold)
# - Use f-strings instead of concatenation
# - Add spaces after colons in output

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_FIX_STYLE_INTRO}}")
print("=" * 50)

print("\n=== {{STYLE_1_TITLE}} ===")
print("Original (poor style):")
original_a()
print("\nFixed (your version):")
fixed_a()

print("\n=== {{STYLE_2_TITLE}} ===")
print("Original (poor style):")
original_b()
print("\nFixed (your version):")
fixed_b()

print("\n=== {{STYLE_3_TITLE}} ===")
print("Original (poor style):")
original_c()
print("\nFixed (your version):")
fixed_c()

print("\n" + "=" * 50)
print("{{CONTEXT_IMPROVEMENT_COMPLETE}}")
