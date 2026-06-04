# =============================================================================
# Fill in the Blanks: Parameters
# =============================================================================
# Difficulty: 2
# Concepts: Parameters, arguments, passing values to functions
# =============================================================================

# %% [markdown]
# {{CONTEXT_FILL_BLANKS_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## תרגיל א: פרמטר אחד
# {{CONTEXT_EXERCISE_1_NARRATIVE}}
#
# פרמטרים מאפשרים לפונקציות לקבל ערכים מבחוץ.

# %%
# FILL IN THE BLANKS
#
# Complete the function to accept and use a parameter.

# def greet(___):                         # Hint: What name for the parameter?
#     print(f"Hello, {name}!")

# greet("{{hero}}")                       # Passing an argument

pass

# %% [markdown]
# ## תרגיל ב: שימוש בפרמטר
# {{CONTEXT_EXERCISE_2_NARRATIVE}}
#
# הפרמטר מתנהג כמו משתנה בתוך הפונקציה.

# %%
# FILL IN THE BLANKS
#
# Complete the function that uses a parameter in multiple places.

# def describe_location(place):
#     print(f"Welcome to {___}!")         # Hint: Use the parameter name
#     print(f"{___} is beautiful.")       # Hint: Same parameter

# describe_location("{{location}}")

pass

# %% [markdown]
# ## תרגיל ג: פרמטרים מרובים
# {{CONTEXT_EXERCISE_3_NARRATIVE}}
#
# פונקציות יכולות לקבל פרמטרים מרובים, מופרדים בפסיקים.

# %%
# FILL IN THE BLANKS
#
# Complete the function with two parameters.

# def introduce(___, ___):                # Hint: Two parameter names
#     print(f"{name} is from {place}.")

# introduce("{{hero}}", "{{school}}")     # Two arguments

pass

# %% [markdown]
# ## תרגיל ד: שימוש בפרמטרים מרובים
# {{CONTEXT_EXERCISE_4_NARRATIVE}}
#
# כל פרמטר יכול לשמש באופן עצמאי בגוף הפונקציה.

# %%
# FILL IN THE BLANKS
#
# Complete the function that uses all its parameters.

# def show_team(leader, member1, member2):
#     print(f"Team Leader: {___}")        # Hint: First parameter
#     print(f"Member 1: {___}")           # Hint: Second parameter
#     print(f"Member 2: {___}")           # Hint: Third parameter

# show_team("{{hero}}", "{{heroine}}", "{{friend}}")

pass

# %% [markdown]
# ## תרגיל ה: הסדר חשוב
# {{CONTEXT_EXERCISE_5_NARRATIVE}}
#
# ארגומנטים מותאמים לפרמטרים לפי מיקומם.

# %%
# FILL IN THE BLANKS
#
# Fill in the arguments in the correct order.

# def format_message(subject, action, object_name):
#     print(f"{subject} will {action} the {object_name}.")

# Call the function to print: "{{hero}} will find the {{item}}."
# format_message(___, ___, ___)          # Hint: subject, action, object_name

pass

# %%
print("{{CONTEXT_FILL_BLANKS_INTRO}}")
print("=" * 50)

print("\n=== Exercise A: Single Parameter ===")
# exercise_a()  # Uncomment when you've filled the blanks

print("\n=== Exercise B: Using the Parameter ===")
# exercise_b()

print("\n=== Exercise C: Multiple Parameters ===")
# exercise_c()

print("\n=== Exercise D: Using Multiple Parameters ===")
# exercise_d()

print("\n=== Exercise E: Order Matters ===")
# exercise_e()

print("\nFill in all the blanks, then uncomment to test!")
print("{{CONTEXT_ROLE_COMPLETE}}")
