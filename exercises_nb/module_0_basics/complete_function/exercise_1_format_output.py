# =============================================================================
# Complete the Function: Format Output
# =============================================================================
# Difficulty: 4
# Concepts: f-strings, string formatting, return values
# =============================================================================

# %% [markdown]
# {{CONTEXT_COMPLETE_FUNCTION_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# {{FUNCTION_1_TITLE}}
# {{CONTEXT_FUNCTION_1_NARRATIVE}}
#
# ✏️ COMPLETE THIS FUNCTION ✏️
#
# Use an f-string to create the greeting.
# f-strings let you put variables inside curly braces: f"Hello, {name}!"
#
# Hint: The f goes BEFORE the opening quote.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
pass  # Replace with: return f"..."

# %% [markdown]
# {{FUNCTION_2_TITLE}}
# {{CONTEXT_FUNCTION_2_NARRATIVE}}
#
# ✏️ COMPLETE THIS FUNCTION ✏️
#
# Use an f-string with multiple variables.
# You can put any variable inside {braces}.
#
# Hint: Numbers work inside f-strings too!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{FUNCTION_3_TITLE}}
# {{CONTEXT_FUNCTION_3_NARRATIVE}}
#
# ✏️ COMPLETE THIS FUNCTION ✏️
#
# You can do math INSIDE the f-string braces!
# Example: f"{a} + {b} = {a + b}"
#
# Hint: The calculation happens when the f-string is created.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_COMPLETE_FUNCTION_INTRO}}")
print("=" * 50)

print("\n=== Testing {{FUNCTION_1_TITLE}} ===")
result1 = format_greeting("{{hero}}", "{{school}}")
print("Result:", result1)
print("Expected: Hello, {{hero}}! Welcome to {{school}}.")

print("\n=== Testing {{FUNCTION_2_TITLE}} ===")
result2 = format_stats("{{hero}}", 100, 50)
print("Result:", result2)
print("Expected: {{hero}} - HP: 100 | Gold: 50")

print("\n=== Testing {{FUNCTION_3_TITLE}} ===")
result3 = format_calculation(10, 5)
print("Result:", result3)
print("Expected: 10 + 5 = 15")

print("\n" + "=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
