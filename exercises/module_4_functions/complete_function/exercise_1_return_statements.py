# =============================================================================
# Complete the Function: Return Statements
# =============================================================================
# Difficulty: 2-3
# Concepts: return statement, returning values, using return values
# =============================================================================

# %% [markdown]
# {{CONTEXT_COMPLETE_FUNCTION_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## פונקציה 1: החזרת ערך פשוט
# {{CONTEXT_FUNCTION_1_NARRATIVE}}

# %%
# COMPLETE THIS FUNCTION
#
# Return the string "Welcome to {{school}}!"
#
# Hint: Use the return keyword to send a value back.

pass  # Replace with implementation

# %% [markdown]
# ## פונקציה 2: החזרת ערך עם פרמטר
# {{CONTEXT_FUNCTION_2_NARRATIVE}}

# %%
# Started for you:
title = "Champion"

# COMPLETE THIS FUNCTION
#
# Return the title combined with the name using an f-string.
#
# Hint: return f"{title} {name}"

pass

# %% [markdown]
# ## פונקציה 3: החזרת תוצאת חישוב
# {{CONTEXT_FUNCTION_3_NARRATIVE}}

# %%
# COMPLETE THIS FUNCTION
#
# Calculate the sum of base and bonus, then return it.
#
# Hint: You can calculate and return in one line:
#       return base + bonus

pass

# %% [markdown]
# ## פונקציה 4: החזרת ערך עם תנאי
# {{CONTEXT_FUNCTION_4_NARRATIVE}}

# %%
# COMPLETE THIS FUNCTION
#
# Use if/elif/else to check the level and return the appropriate string.
#
# Hint: Each branch should have a return statement.

pass

# %% [markdown]
# ## פונקציה 5: שימוש בערכים שמוחזרים
# {{CONTEXT_FUNCTION_5_NARRATIVE}}

# %%
# COMPLETE THIS FUNCTION
#
# Return the number multiplied by 2.

pass

# %%
print("{{CONTEXT_COMPLETE_FUNCTION_INTRO}}")
print("=" * 50)

print("\n=== Testing get_greeting ===")
result = get_greeting()
print(f"Result: {result}")
print(f"Expected: Welcome to {{school}}!")

print("\n=== Testing format_name ===")
result1 = format_name("{{hero}}")
result2 = format_name("{{heroine}}")
print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
print("Expected: Champion {{hero}}, Champion {{heroine}}")

print("\n=== Testing calculate_total_points ===")
total1 = calculate_total_points(100, 25)
total2 = calculate_total_points(50, 10)
print(f"100 + 25 = {total1}")
print(f"50 + 10 = {total2}")
print("Expected: 125, 60")

print("\n=== Testing get_status_message ===")
msg1 = get_status_message(5)
msg2 = get_status_message(15)
msg3 = get_status_message(25)
print(f"Level 5: {msg1}")
print(f"Level 15: {msg2}")
print(f"Level 25: {msg3}")
print("Expected: Beginner, Intermediate, Expert")

print("\n=== Testing double_value ===")
d1 = double_value(5)
d2 = double_value(7)
print(f"Double 5: {d1}")
print(f"Double 7: {d2}")
print("Expected: 10, 14")

# Demonstrate using returned values
print("\n=== Using Returned Values ===")
points = calculate_total_points(80, 20)
doubled = double_value(points)
print(f"Points: {points}, Doubled: {doubled}")

print("\n" + "=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
