# %% [markdown]
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_MISSION}}
#
# Topic: Finding bugs with break and continue
# Difficulty: 2-3
#
# break and continue are powerful but can cause subtle bugs
# when placed incorrectly or when the logic is inverted.
#
# {{CASE_1_TITLE}}
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# This search function should find an item and return its index.
#
# EXPECTED BEHAVIOR:
# Return the index where target is found, or -1 if not found
#
# ACTUAL BEHAVIOR:
# Always returns -1, even when the item exists
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

# %%
index = 0
while index < len(items):
    if items[index] == target:
        break  # Found it!
    index += 1
return -1  # BUG: Always returns -1, never returns the found index

# %% [markdown]
# ✏️ FIX THE BUG ✏️
#
# What I found: ________________________________
#
# The fix:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{CASE_2_TITLE}}
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# This function should skip negative numbers and sum the positives.
#
# EXPECTED BEHAVIOR:
# Sum only the positive numbers, skip negatives
#
# ACTUAL BEHAVIOR:
# Returns 0 because it breaks on the first negative
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}

# %%
total = 0
for num in numbers:
    if num < 0:
        break  # BUG: Should be continue, not break!
    total += num
return total

# %% [markdown]
# ✏️ FIX THE BUG ✏️
#
# What I found: ________________________________
#
# The fix:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{CASE_3_TITLE}}
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# This collector should stop when the user enters 'quit'.
#
# EXPECTED BEHAVIOR:
# Collect items until user types 'quit', then return the list
#
# ACTUAL BEHAVIOR:
# Never stops, keeps asking forever
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}

# %%
items = []
while True:
    user_input = input("Enter item (or 'quit'): ")
    if user_input == "quit":
        continue  # BUG: Should be break, not continue!
    items.append(user_input)
return items

# %% [markdown]
# ✏️ FIX THE BUG ✏️
#
# What I found: ________________________________
#
# The fix:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{CASE_4_TITLE}}
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# This validator should stop validating after finding one error.
#
# EXPECTED BEHAVIOR:
# Check items until finding an invalid one, then stop
#
# ACTUAL BEHAVIOR:
# The break is inside the else, so it breaks on VALID items
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}

# %%
valid_items = []
for item in items:
    if item == "" or item is None:
        print(f"Invalid item found!")
    else:
        valid_items.append(item)
        break  # BUG: Break is in wrong branch!
return valid_items

# %% [markdown]
# ✏️ FIX THE BUG ✏️
#
# What I found: ________________________________
#
# The fix:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{CASE_5_TITLE}}
# {{CONTEXT_CASE_5_NARRATIVE}}
#
# This function should find the first item that matches a condition.
#
# EXPECTED BEHAVIOR:
# Return the first item longer than 5 characters
#
# ACTUAL BEHAVIOR:
# Skips items that match! Returns wrong result.
#
# {{CONTEXT_INVESTIGATION_PROMPT_5}}

# %%
for item in items:
    if len(item) > 5:
        continue  # BUG: Should return item, not continue!
    # Falls through without returning the match
return None

# %% [markdown]
# ✏️ FIX THE BUG ✏️
#
# What I found: ________________________________
#
# The fix:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_INVESTIGATION_INTRO}}")
print("=" * 50)

print("\n=== {{CASE_1_TITLE}} ===")
print("Testing search:")
items = ["{{item}}", "{{pet}}", "{{creature}}"]
buggy_result = buggy_search(items, "{{pet}}")
print(f"Buggy result: {buggy_result} (should be 1)")
# fixed_result = fix_search(items, "{{pet}}")
# print(f"Fixed result: {fixed_result}")

print("\n=== {{CASE_2_TITLE}} ===")
print("Testing sum positives:")
numbers = [5, -3, 10, -1, 7]
buggy_result = buggy_sum_positives(numbers)
print(f"Buggy result: {buggy_result} (should be 22)")
# fixed_result = fix_sum_positives(numbers)
# print(f"Fixed result: {fixed_result}")

print("\n=== {{CASE_3_TITLE}} ===")
print("Testing collector:")
print("(Buggy version would loop forever - don't run!)")
# fixed_items = fix_collector()
# print(f"Collected: {fixed_items}")

print("\n=== {{CASE_4_TITLE}} ===")
print("Testing validator:")
test_items = ["{{hero}}", "{{villain}}", "", "{{friend}}"]
buggy_result = buggy_validator(test_items.copy())
print(f"Buggy result: {buggy_result} (should be ['{{{{hero}}}}', '{{{{villain}}}}'])")
# fixed_result = fix_validator(test_items)
# print(f"Fixed result: {fixed_result}")

print("\n=== {{CASE_5_TITLE}} ===")
print("Testing find long item:")
words = ["cat", "elephant", "dog", "hippopotamus"]
buggy_result = buggy_find_long_item(words)
print(f"Buggy result: {buggy_result} (should be 'elephant')")
# fixed_result = fix_find_long_item(words)
# print(f"Fixed result: {fixed_result}")

print("\n" + "=" * 50)
print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
