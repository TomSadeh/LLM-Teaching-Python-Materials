# =============================================================================
# Spot the Difference: Indexing Errors
# =============================================================================
# Difficulty: 2-3
# Concepts: Off-by-one errors, common indexing mistakes
# =============================================================================

# %% [markdown]
# {{CONTEXT_SPOT_DIFFERENCE_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## {{COMPARISON_1_TITLE}}
# {{CONTEXT_COMPARISON_1_NARRATIVE}}
# גרסה אחת מגיעה לאיבר האחרון בהצלחה, והשנייה גורמת לשגיאה.

# %%
items = ["{{item}}", "potion", "key"]
last_index = len(items) - 1
print(f"Last item: {items[last_index]}")

# %%
items = ["{{item}}", "potion", "key"]
last_index = len(items)
print(f"Last item: {items[last_index]}")

# %%
# EXPLAIN THE DIFFERENCE
#
# Hint: What does len() return vs what is the last valid index?

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
# ## {{COMPARISON_2_TITLE}}
# {{CONTEXT_COMPARISON_2_NARRATIVE}}
# גרסה אחת ניגשת לאיברים בצורה בטוחה בלולאה, והשנייה הולכת רחוק מדי.

# %%
team = ["{{hero}}", "{{heroine}}", "{{friend}}"]
for i in range(len(team)):
    print(f"Member {i}: {team[i]}")

# %%
team = ["{{hero}}", "{{heroine}}", "{{friend}}"]
for i in range(len(team) + 1):
    print(f"Member {i}: {team[i]}")

# %%
# EXPLAIN THE DIFFERENCE
#
# Hint: What values does each range() produce?

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
# ## {{COMPARISON_3_TITLE}}
# {{CONTEXT_COMPARISON_3_NARRATIVE}}
# שתי הגרסאות ניגשות לאיבר, אבל אחת משנה את הרשימה והשנייה לא.

# %%
scores = [85, 92, 78]
bonus = scores[0] + 10
print(f"Bonus: {bonus}")
print(f"Scores: {scores}")

# %%
scores = [85, 92, 78]
scores[0] = scores[0] + 10
print(f"Bonus: {scores[0]}")
print(f"Scores: {scores}")

# %%
# EXPLAIN THE DIFFERENCE
#
# Hint: What happens to the original list in each version?

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
# ## {{COMPARISON_4_TITLE}}
# {{CONTEXT_COMPARISON_4_NARRATIVE}}
# שתי דרכים להגיע לאיבר האחרון — איזו מהן בטוחה יותר?

# %%
inventory = ["{{item}}", "potion"]
last = inventory[-1]
print(f"Last: {last}")

# %%
inventory = ["{{item}}", "potion"]
last = inventory[1]
print(f"Last: {last}")

# %%
# EXPLAIN THE DIFFERENCE
#
# Hint: What if the list length changes?

explanation = """
The difference is:
-

Version 1 behavior:
-

Version 2 behavior:
-

Why -1 is often better:
-
"""
return explanation

# %%
print("{{CONTEXT_SPOT_DIFFERENCE_INTRO}}")
print("=" * 50)

print("\n=== {{COMPARISON_1_TITLE}} ===")
print("Version 1:")
snippet_a1()
# print("\nVersion 2:")
# snippet_a2()  # Uncomment to see the error
print(f"\nExplanation:{explain_difference_a()}")

print("\n=== {{COMPARISON_2_TITLE}} ===")
print("Version 1:")
snippet_b1()
# print("\nVersion 2:")
# snippet_b2()  # Uncomment to see the error
print(f"\nExplanation:{explain_difference_b()}")

print("\n=== {{COMPARISON_3_TITLE}} ===")
print("Version 1:")
snippet_c1()
print("\nVersion 2:")
snippet_c2()
print(f"\nExplanation:{explain_difference_c()}")

print("\n=== {{COMPARISON_4_TITLE}} ===")
print("Version 1:")
snippet_d1()
print("\nVersion 2:")
snippet_d2()
print(f"\nExplanation:{explain_difference_d()}")

print("=" * 50)
print("{{CONTEXT_ROLE_COMPLETE}}")
