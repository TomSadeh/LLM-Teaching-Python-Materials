# =============================================================================
# Which is Better: Return vs Print
# =============================================================================
# Difficulty: 3
# Concepts: When to use return, when to use print, function design
# =============================================================================

# %% [markdown]
# {{CONTEXT_COMPARISON_INTRO}}
# {{CONTEXT_COMPARISON_DECISION}}
#
# ## תרחיש 1: פונקציה לחישוב
# את צריכה פונקציה שמחשבת ניקוד.
# את רוצה להשתמש בתוצאה בחישובים נוספים.

# %%
result = base + bonus
print(f"Score: {result}")

# %%
result = base + bonus
return result

# %%
# YOUR ANALYSIS
#
# Consider: Which version lets you use the score in more calculations?

analysis = """
Better version: Version 2 (return)

Reasons:
1. Returns the value so it can be stored and reused
2. Can be used in further calculations
3. More flexible - caller decides whether to print

When to use Version 1 (print):
- When you ONLY need to display the value once
- In debugging, to see intermediate values

When to use Version 2 (return):
- When you need to use the value in calculations
- When building reusable functions
- Almost always the better choice for functions
"""
return analysis

# %% [markdown]
# ## תרחיש 2: פונקציית ברכה
# את צריכה פונקציה שמציגה ברכה למשתמש.

# %%
print(f"Hello, {name}!")
print(f"Welcome to {{school}}!")

# %%
return f"Hello, {name}!\nWelcome to {{school}}!"

# %%
# YOUR ANALYSIS
#
# Consider: What if you want to modify the greeting before showing it?

analysis = """
Better version: ??? (it depends!)

Reasons:
1.
2.

When to use Version 1 (print):
-

When to use Version 2 (return):
-
"""
return analysis

# %% [markdown]
# ## תרחיש 3: פונקציית בדיקת סטטוס
# את צריכה לבדוק אם משתמש מוסמך.

# %%
if level >= 10:
    print("Qualified!")
else:
    print("Not yet qualified")

# %%
return level >= 10

# %%
# YOUR ANALYSIS
#
# Consider: What if you need to make a decision based on the status?

analysis = """
Better version: ???

Reasons:
1.
2.

When to use Version 1:
-

When to use Version 2:
-
"""
return analysis

# %% [markdown]
# ## תרחיש 4: מחולל דוחות
# את צריכה ליצור דוח מעוצב.

# %%
print("=" * 40)
print(title)
print("=" * 40)
print(content)
print("=" * 40)

# %%
lines = [
    "=" * 40,
    title,
    "=" * 40,
    content,
    "=" * 40
]
return "\n".join(lines)

# %%
# YOUR ANALYSIS
#
# Consider: What if you want to save the report to a file?

analysis = """
Better version: ???

Reasons:
1.
2.

When to use Version 1:
-

When to use Version 2:
-
"""
return analysis

# %% [markdown]
# ## תרחיש 5: גישה משולבת
# לפעמים את רוצה את שניהם: גם לחשב וגם להציג.

# %%
result = base + bonus
return result

# %%
print(f"Final Score: {score}")
print("=" * 20)

# %%
# YOUR ANALYSIS
#
# Consider: How does separating concerns help?

analysis = """
The combined approach:
- One function calculates (returns value)
- Another function displays (prints formatted output)

Benefits:
1.
2.
3.

This is called "separation of concerns" - each function has
one clear job.
"""
return analysis

# %%
print("{{CONTEXT_COMPARISON_INTRO}}")
print("=" * 50)

print("\n=== Scenario 1: Calculation ===")
print("\nVersion 1 (prints):")
calculate_score_v1(100, 25)
print("Can we use this value? Let's try:")
result1 = calculate_score_v1(100, 25)
print(f"Stored value: {result1}")

print("\nVersion 2 (returns):")
result2 = calculate_score_v2(100, 25)
print(f"Stored value: {result2}")
doubled = result2 * 2
print(f"Doubled: {doubled}")
print(f"\nYour analysis:{analysis_scenario_1()}")

print("\n=== Scenario 2: Greeting ===")
print("\nVersion 1 (prints):")
greet_user_v1("{{hero}}")
print("\nVersion 2 (returns):")
greeting = greet_user_v2("{{hero}}")
print(greeting)
print(f"\nYour analysis:{analysis_scenario_2()}")

print("\n=== Scenario 3: Status Check ===")
print("\nVersion 1 (prints):")
check_status_v1(15)
print("\nVersion 2 (returns):")
is_qualified = check_status_v2(15)
print(f"Qualified? {is_qualified}")
if is_qualified:
    print("Access granted!")
print(f"\nYour analysis:{analysis_scenario_3()}")

print("\n=== Scenario 4: Report ===")
print("\nVersion 1 (prints directly):")
create_report_v1("{{school}} Report", "Status: Active")
print("\nVersion 2 (returns string):")
report = create_report_v2("{{school}} Report", "Status: Active")
print(report)
print(f"\nYour analysis:{analysis_scenario_4()}")

print("\n=== Scenario 5: Combined Approach ===")
score = process_score_combined(100, 50)
display_score(score)
# Can also use score in calculations
bonus_score = score * 1.5
display_score(int(bonus_score))
print(f"\nYour analysis:{analysis_scenario_5()}")

print("\n" + "=" * 50)
print("{{CONTEXT_EVALUATION_COMPLETE}}")
