# =============================================================================
# Complete the Function: Default Parameters
# =============================================================================
# Difficulty: 3
# Concepts: Default parameter values, optional arguments, parameter ordering
# =============================================================================

# %% [markdown]
# {{CONTEXT_COMPLETE_FUNCTION_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## פונקציה 1: פרמטר ברירת מחדל בודד
# {{CONTEXT_FUNCTION_1_NARRATIVE}}

# %%
# COMPLETE THIS FUNCTION
#
# Return a formatted string: "{greeting}, {name}!"
#
# Hint: The greeting parameter already has a default value.
#       If the caller doesn't provide it, "Hello" is used.

pass  # Replace with implementation

# %% [markdown]
# ## פונקציה 2: מספר פרמטרים עם ברירת מחדל
# {{CONTEXT_FUNCTION_2_NARRATIVE}}

# %%
# COMPLETE THIS FUNCTION
#
# Return: "{name} - {title} (Level {level})"
#
# Hint: All the parameters are available, just format them.

pass

# %% [markdown]
# ## פונקציה 3: פרמטרים חובה לפני אופציונליים
# {{CONTEXT_FUNCTION_3_NARRATIVE}}

# %%
# COMPLETE THIS FUNCTION
#
# Calculate and return: (base + bonus) * multiplier
#
# Hint: Do the addition first, then multiply.

pass

# %% [markdown]
# ## פונקציה 4: ברירת מחדל עם תנאי
# {{CONTEXT_FUNCTION_4_NARRATIVE}}

# %%
# COMPLETE THIS FUNCTION
#
# If is_new is True, return: "Welcome to {{school}}, {name}!"
# If is_new is False, return: "Welcome back, {name}!"
#
# Hint: Use an if/else statement.

pass

# %% [markdown]
# ## פונקציה 5: עיצוב גמיש
# {{CONTEXT_FUNCTION_5_NARRATIVE}}

# %%
# COMPLETE THIS FUNCTION
#
# Create a header with:
# - A line of {char} repeated {width} times
# - The text
# - Another line of {char} repeated {width} times
#
# Hint: Use char * width to create the border line.
#       Use \n to join the parts, or return them combined.

pass

# %%
print("{{CONTEXT_COMPLETE_FUNCTION_INTRO}}")
print("=" * 50)

print("\n=== Testing greet ===")
print(greet("{{hero}}"))
print(greet("{{heroine}}", "Welcome"))
print(greet("{{friend}}", "Greetings"))

print("\n=== Testing format_profile ===")
print(format_profile("{{hero}}"))
print(format_profile("{{heroine}}", "Leader"))
print(format_profile("{{mentor}}", "Advisor", 10))

print("\n=== Testing calculate_score ===")
print(f"Base only: {calculate_score(100)}")
print(f"With bonus: {calculate_score(100, 20)}")
print(f"With multiplier: {calculate_score(100, 20, 2)}")

print("\n=== Testing get_message ===")
print(get_message("{{hero}}"))
print(get_message("{{heroine}}", False))
print(get_message("{{friend}}", True))

print("\n=== Testing create_header ===")
header1 = create_header("{{school}} News")
print(header1)
print()
header2 = create_header("Alert", 30, "-")
print(header2)

print("\n" + "=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
