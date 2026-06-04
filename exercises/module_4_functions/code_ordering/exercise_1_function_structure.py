# =============================================================================
# Code Ordering: Function Structure
# =============================================================================
# Difficulty: 2
# Concepts: Function definition order, calling functions, parameters
# =============================================================================

# %% [markdown]
# {{CONTEXT_CODE_ORDERING_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## אתגר א': סדר בסיסי של פונקציה
# {{CONTEXT_ORDERING_1_NARRATIVE}}
#
# סדרי את השורות כדי ליצור ולקרוא לפונקציה.
#
# השורות המפוזרות:
#   greet_visitor()
#   print("Welcome to {{school}}!")
#   def greet_visitor():

# %%
# REORDER THE LINES
#
# Copy the lines above in the CORRECT order.
#
# Hint: A function must be defined before it can be called.
#       The function body must be indented.

pass  # Delete this and add the correctly ordered lines

# %% [markdown]
# ## אתגר ב': פונקציה עם פרמטר
# {{CONTEXT_ORDERING_2_NARRATIVE}}
#
# סדרי את השורות כדי ליצור פונקציה עם פרמטר.
#
# השורות המפוזרות:
#   print(f"Hello, {name}!")
#   greet("{{hero}}")
#   def greet(name):
#   print(f"{name} has arrived.")

# %%
# REORDER THE LINES
#
# Hint: Function definition comes first.
#       Both print statements are inside the function.
#       The function call is last.

pass

# %% [markdown]
# ## אתגר ג': מספר פונקציות
# {{CONTEXT_ORDERING_3_NARRATIVE}}
#
# סדרי את השורות כדי להגדיר שתי פונקציות ולקרוא להן.
#
# השורות המפוזרות:
#   show_header()
#   def show_header():
#   def show_footer():
#   print("=== End ===")
#   show_footer()
#   print("=== {{school}} ===")

# %%
# REORDER THE LINES
#
# Hint: Both functions must be defined before they are called.
#       Each function has one print statement as its body.

pass

# %% [markdown]
# ## אתגר ד': פונקציה עם הגדרת משתנה
# {{CONTEXT_ORDERING_4_NARRATIVE}}
#
# סדרי את השורות לפונקציה שמשתמשת במשתנה.
#
# השורות המפוזרות:
#   print(f"Status: {status}")
#   display_status()
#   status = "Active"
#   def display_status():
#   print(f"Location: {{location}}")

# %%
# REORDER THE LINES
#
# Hint: Inside the function, create the variable before using it.
#       Variables defined inside a function are local to it.

pass

# %% [markdown]
# ## אתגר ה': קריאה לפונקציה עם ארגומנטים
# {{CONTEXT_ORDERING_5_NARRATIVE}}
#
# סדרי את השורות כדי ליצור ולקרוא לפונקציה עם שני פרמטרים.
#
# השורות המפוזרות:
#   introduce("{{hero}}", "{{school}}")
#   def introduce(person, place):
#   print(f"{person} attends {place}.")
#   print(f"Welcome, {person}!")

# %%
# REORDER THE LINES
#
# Hint: Both print statements belong inside the function.
#       Order them so the welcome comes before the attendance info.

pass

# %%
print("{{CONTEXT_CODE_ORDERING_INTRO}}")
print("=" * 50)

print("\n=== Challenge A: Basic Function Order ===")
# challenge_a()  # Uncomment when ordered correctly

print("\n=== Challenge B: Function with Parameter ===")
# challenge_b()

print("\n=== Challenge C: Multiple Functions ===")
# challenge_c()

print("\n=== Challenge D: Function with Setup ===")
# challenge_d()

print("\n=== Challenge E: Function Call with Arguments ===")
# challenge_e()

print("\nReorder each challenge, then uncomment to test!")
print("{{CONTEXT_ROLE_COMPLETE}}")
