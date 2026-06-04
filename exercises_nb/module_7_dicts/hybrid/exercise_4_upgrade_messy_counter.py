# %% [markdown]
# {{CONTEXT_EVALUATION_INTRO}}
#
# This is a multi-part exercise where you upgrade messy counting code
# to use elegant dictionary patterns.
#
# Programming concepts: counting pattern, .get(), dict iteration
#
# PART 1: Evaluation - Assess the Messy Code
# {{CONTEXT_EVALUATION_NARRATIVE}}
#
# This counting code works but is messy. Analyze what's wrong.

# %%
counts = []  # List of [item, count] pairs

for item in items:
    # Search for existing item in counts
    found = False
    index = 0
    while index < len(counts):
        if counts[index][0] == item:
            counts[index][1] = counts[index][1] + 1
            found = True
            break
        index = index + 1

    # If not found, add new entry
    if found == False:
        counts.append([item, 1])

return counts

# %% [markdown]
# ✏️ YOUR ANALYSIS ✏️
#
# Identify problems with the messy code:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
analysis = """
PROBLEMS WITH MESSY COUNTER:

1. Data structure choice:
   - Uses ___ instead of ___
   - Why is this problematic?

2. Search efficiency:
   - How does it find existing items?
   - What if there are 1000 different items?

3. Code complexity:
   - How many lines for the counting logic?
   - Is it easy to understand at a glance?

4. Specific issues:
   - Line "if found == False" should be:
   - The while loop could be replaced with:
"""
return analysis

# %% [markdown]
# PART 2: Discovery - Trace the Messy Code
# {{CONTEXT_DISCOVERY_INTRO}}
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# Trace through the messy code to understand exactly what it does.

# %%
items = ["a", "b", "a"]
counts = []

for item in items:
    found = False
    index = 0
    while index < len(counts):
        if counts[index][0] == item:
            counts[index][1] = counts[index][1] + 1
            found = True
            break
        index = index + 1
    if found == False:
        counts.append([item, 1])

print(counts)

# %% [markdown]
# ✏️ FILL IN THE TRACING TABLE ✏️
#
# items = ["a", "b", "a"]
#
# | Outer | item | counts before      | found | counts after       |
# |-------|------|--------------------|-------|--------------------|
# | 1     | "a"  | []                 |       |                    |
# | 2     | "b"  |                    |       |                    |
# | 3     | "a"  |                    |       |                    |
#
# Final result:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 3: Improvement - Simplify with Dictionary
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Rewrite the counter using a dictionary.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Create an empty dictionary: counts = {}
#
# Step 2: For each item in items:
#         counts[item] = counts.get(item, 0) + 1
#
# Step 3: Return counts
#
# This should be about 4 lines of code!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Use simple_counter to get counts dict
#
# Step 2: Print each item and count using .items()
#
# Step 3: Find and print the most common item
#         Hint: Track max_count and max_item while iterating
#
# Step 4: Print the total (sum of all counts)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Count all items
# Step 2: Filter to those above threshold
# Step 3: Return the list of items (not counts)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## PART 4: Comparison - Before and After
#
# ✏️ COMPARE THE APPROACHES ✏️

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
comparison_text = """
BEFORE (messy_counter):
- Lines of code: ~15
- Data structure: list of lists
- Lookup method: linear search with while loop
- Easy to read: No

AFTER (simple_counter):
- Lines of code: ~4
- Data structure: dictionary
- Lookup method: direct key access
- Easy to read: Yes

KEY INSIGHT:
The dictionary .get(key, default) pattern is perfect for counting
because it handles both "first occurrence" and "subsequent occurrence"
in a single line of code.

WHAT I LEARNED:
-
"""
return comparison_text

# %% [markdown]
# ## MAIN

# %%
print("=" * 60)
print("{{CONTEXT_EVALUATION_INTRO}}")
print("=" * 60)
print()

test_items = [
    "{{item}}", "{{spell1}}", "{{item}}",
    "{{spell2}}", "{{item}}", "{{spell1}}"
]

print(">>> PART 1: Analyze the messy code...")
print()
print(f"Messy counter result: {messy_counter(test_items)}")
print()
print("Your analysis:")
print(analysis_part_1())

print()
print(">>> PART 2: Trace the messy code...")
print("(Complete trace_messy_counter())")
# Uncomment to verify:
# code_to_trace()

print()
print(">>> PART 3: Implement the simple version...")
print("(Implement simple_counter, count_and_report, count_above_threshold)")
print()
# Uncomment after implementing:
# print(f"Simple counter: {simple_counter(test_items)}")
# print()
# count_and_report(test_items)
# print()
# print(f"Items appearing 2+ times: {count_above_threshold(test_items, 1)}")

print()
print(">>> PART 4: Compare approaches...")
print()
print(comparison())

print()
print("=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print("=" * 60)
