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
# {{MATCH_SET_1_TITLE}}
# {{CONTEXT_MATCH_SET_1_NARRATIVE}}
#
# ## CODE SNIPPETS

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
# ## POSSIBLE OUTPUTS
#
# OUTPUT A:
# ---------
# Hello {{hero}}
#
# OUTPUT B:
# ---------
# Hello{{hero}}
#
# OUTPUT C:
# ---------
# Hello  {{hero}}
#
# ## YOUR ANSWERS
#
# ✏️ MATCH SNIPPETS TO OUTPUTS ✏️
#
# Write the letter (A, B, or C) that matches each snippet.
#
# Hint: The + operator joins strings exactly as they are.
# The comma in print() adds a space between items.

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
# {{MATCH_SET_2_TITLE}}
# {{CONTEXT_MATCH_SET_2_NARRATIVE}}
#
# ## CODE SNIPPETS

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
# ## POSSIBLE OUTPUTS
#
# OUTPUT D:
# ---------
# {{item}}5
#
# OUTPUT E:
# ---------
# {{item}} 5
#
# OUTPUT F:
# ---------
# {{item}}  5
#
# ## YOUR ANSWERS
#
# ✏️ MATCH SNIPPETS TO OUTPUTS ✏️
#
# Hint: When using + with strings and numbers, you must convert
# the number to a string first using str().

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
