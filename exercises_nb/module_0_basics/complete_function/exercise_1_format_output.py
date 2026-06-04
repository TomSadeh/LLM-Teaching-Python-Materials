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
# ## {{FUNCTION_1_TITLE}}
# {{CONTEXT_FUNCTION_1_NARRATIVE}}
#
# השתמשי ב-f-string כדי ליצור את ברכת ההצגה.
# f-strings מאפשרות לך לשים משתנים בתוך סוגריים מסולסלים: `f"Hello, {name}!"`
#
# > רמז: האות `f` באה לפני גרש הפתיחה.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
pass  # Replace with: return f"..."

# %% [markdown]
# ## {{FUNCTION_2_TITLE}}
# {{CONTEXT_FUNCTION_2_NARRATIVE}}
#
# השתמשי ב-f-string עם כמה משתנים.
# אפשר לשים כל משתנה בתוך `{סוגריים מסולסלים}`.
#
# > רמז: מספרים עובדים בתוך f-strings בדיוק כמו טקסט!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{FUNCTION_3_TITLE}}
# {{CONTEXT_FUNCTION_3_NARRATIVE}}
#
# אפשר לעשות חישובים ישירות בתוך הסוגריים המסולסלים של ה-f-string!
# לדוגמה: `f"{a} + {b} = {a + b}"`
#
# > רמז: החישוב מתבצע ברגע שה-f-string נוצרת.

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
