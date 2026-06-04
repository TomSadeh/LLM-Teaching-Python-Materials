# =============================================================================
# Complete the Function: Slicing Functions
# =============================================================================
# Difficulty: 3-4
# Concepts: Using slicing to extract and manipulate list portions
# =============================================================================

# %% [markdown]
# {{CONTEXT_COMPLETE_FUNCTION_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# {{FUNCTION_1_TITLE}}
# {{CONTEXT_FUNCTION_1_NARRATIVE}}

# %%
# Started for you:
first = items[0]

# COMPLETE THIS FUNCTION
#
# Step 1: Get the last element using negative indexing
# Step 2: Return a new list containing first and last
#
# Hint: Use items[-1] to get the last element

pass  # Replace with implementation

# %% [markdown]
# {{FUNCTION_2_TITLE}}
# {{CONTEXT_FUNCTION_2_NARRATIVE}}

# %%
# Started for you:
length = len(items)
midpoint = (length + 1) // 2  # Rounds up for odd lengths

# COMPLETE THIS FUNCTION
#
# Step 1: Use slicing to get the first half (indices 0 to midpoint)
# Step 2: Use slicing to get the second half (indices midpoint to end)
# Step 3: Return both halves as a tuple
#
# Hint: items[:midpoint] and items[midpoint:]

pass  # Replace with implementation

# %% [markdown]
# {{FUNCTION_3_TITLE}}
# {{CONTEXT_FUNCTION_3_NARRATIVE}}

# %%
# COMPLETE THIS FUNCTION
#
# Use step slicing: items[start:stop:step]
# To get every nth element starting from the first, use items[::n]
#
# Hint: You only need one line using slice notation

pass  # Replace with implementation

# %% [markdown]
# {{FUNCTION_4_TITLE}}
# {{CONTEXT_FUNCTION_4_NARRATIVE}}

# %%
# Started for you:
reversed_list = items[::-1]

# COMPLETE THIS FUNCTION
#
# Step 1: If trim_count is 0, just return the reversed list
# Step 2: Otherwise, slice to remove trim_count from each end
#
# Hint: To remove N from each end, use [N:-N]
# But be careful with trim_count of 0 ([:0] would give empty list)

pass  # Replace with implementation

# %%
print("{{CONTEXT_COMPLETE_FUNCTION_INTRO}}")
print("=" * 50)

print("\n=== Testing {{FUNCTION_1_TITLE}} ===")
result1 = get_first_and_last(["{{hero}}", "{{heroine}}", "{{friend}}"])
print(f"get_first_and_last(['{{hero}}', '{{heroine}}', '{{friend}}']): {result1}")
result2 = get_first_and_last([1, 2, 3, 4, 5])
print(f"get_first_and_last([1, 2, 3, 4, 5]): {result2}")

print("\n=== Testing {{FUNCTION_2_TITLE}} ===")
result3 = split_in_half([1, 2, 3, 4])
print(f"split_in_half([1, 2, 3, 4]): {result3}")
result4 = split_in_half(["A", "B", "C", "D", "E"])
print(f"split_in_half(['A', 'B', 'C', 'D', 'E']): {result4}")

print("\n=== Testing {{FUNCTION_3_TITLE}} ===")
result5 = get_every_nth([1, 2, 3, 4, 5, 6], 2)
print(f"get_every_nth([1, 2, 3, 4, 5, 6], 2): {result5}")
result6 = get_every_nth(["A", "B", "C", "D", "E", "F"], 3)
print(f"get_every_nth(['A', 'B', 'C', 'D', 'E', 'F'], 3): {result6}")

print("\n=== Testing {{FUNCTION_4_TITLE}} ===")
result7 = reverse_and_trim([1, 2, 3, 4, 5], 1)
print(f"reverse_and_trim([1, 2, 3, 4, 5], 1): {result7}")
result8 = reverse_and_trim(["A", "B", "C", "D", "E", "F"], 2)
print(f"reverse_and_trim(['A', 'B', 'C', 'D', 'E', 'F'], 2): {result8}")

print("\n" + "=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
