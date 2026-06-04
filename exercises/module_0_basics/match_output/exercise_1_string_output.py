# =============================================================================
# Match the Output: String Operations
# =============================================================================
# Difficulty: 3
# Concepts: string concatenation, print with commas vs plus
# =============================================================================

# %% [markdown]
# {{CONTEXT_MATCH_OUTPUT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## {{MATCH_SET_1_TITLE}}
# {{CONTEXT_MATCH_SET_1_NARRATIVE}}
#
# ## קטעי קוד

# %%
name = "{{hero}}"
print("Hello " + name)

# %%
name = "{{hero}}"
print("Hello", name)

# %%
name = "{{hero}}"
print("Hello" + name)

# %% [markdown]
# ## פלטים אפשריים
#
# פלט A:
# ---------
# Hello {{hero}}
#
# פלט B:
# ---------
# Hello{{hero}}
#
# פלט C:
# ---------
# Hello  {{hero}}
#
# ## התשובות שלך
#
# כתבי את האות (A, B, או C) שמתאימה לכל קטע קוד.
#
# > רמז: האופרטור `+` מחבר מחרוזות בדיוק כפי שהן.
# > הפסיק בתוך `print()` מוסיף רווח בין הפריטים.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
matches = {
    "snippet_1": "?",
    "snippet_2": "?",
    "snippet_3": "?",
}

return matches

# %% [markdown]
# ## {{MATCH_SET_2_TITLE}}
# {{CONTEXT_MATCH_SET_2_NARRATIVE}}
#
# ## קטעי קוד

# %%
item = "{{item}}"
count = 5
print(item, count)

# %%
item = "{{item}}"
count = 5
print(item + str(count))

# %%
item = "{{item}}"
count = 5
print(item + " " + str(count))

# %% [markdown]
# ## פלטים אפשריים
#
# פלט D:
# ---------
# {{item}}5
#
# פלט E:
# ---------
# {{item}} 5
#
# פלט F:
# ---------
# {{item}}  5
#
# ## התשובות שלך
#
# כתבי את האות (D, E, או F) שמתאימה לכל קטע קוד.
#
# > רמז: כשמשתמשים ב-`+` עם מחרוזות ומספרים, צריך להמיר
# > את המספר למחרוזת תחילה באמצעות `str()`.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
matches = {
    "snippet_4": "?",
    "snippet_5": "?",
    "snippet_6": "?",
}

return matches

# %%
print("{{CONTEXT_MATCH_OUTPUT_INTRO}}")
print("=" * 50)

print("\n=== {{MATCH_SET_1_TITLE}} ===")
print("\nSnippet 1 output:")
snippet_1()
print("\nSnippet 2 output:")
snippet_2()
print("\nSnippet 3 output:")
snippet_3()
print("\nYour matches:", your_matches_set1())

print("\n=== {{MATCH_SET_2_TITLE}} ===")
print("\nSnippet 4 output:")
snippet_4()
print("\nSnippet 5 output:")
snippet_5()
print("\nSnippet 6 output:")
snippet_6()
print("\nYour matches:", your_matches_set2())

print("\n" + "=" * 50)
print("{{CONTEXT_VERIFICATION_COMPLETE}}")
