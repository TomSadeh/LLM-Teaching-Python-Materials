# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# Topic: Using continue to skip iterations
# Difficulty: 2-3
#
# The 'continue' statement skips the rest of the current iteration
# and moves to the next one. Use it to skip unwanted items.
#
# {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# Use continue to skip items that don't match criteria.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Loop through each number in numbers
# Step 2: If number is less than or equal to 0, continue
# Step 3: Print the number

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# Use continue to filter during processing.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Create an empty result list
# Step 2: Loop through each item
# Step 3: If item is an empty string "", continue
# Step 4: Convert to uppercase and add to result
# Step 5: Return result

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# Use continue with index-based loops.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Create an empty result list
# Step 2: Loop with index: for i in range(len(values))
# Step 3: If i is odd (i % 2 != 0), continue
# Step 4: Add values[i] to result
# Step 5: Return result

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# Combine continue with while loops.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Set total = 0
# Step 2: While True:
#         - Get input
#         - If input is 'done', break
#         - If input.isdigit() or (input.startswith('-') and input[1:].isdigit()):
#           Add int(input) to total
#         - Else: print "Invalid number, skipping." and continue
# Step 3: Return total
#
# Note: Use .lstrip('-').isdigit() to check for negative numbers

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_5_TITLE}}
# {{CONTEXT_PHASE_5}}
#
# Use continue with complex skip conditions.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Create an empty result list
# Step 2: Loop through each item
# Step 3: If item is in blocked_list:
#         - Print f"Blocked: {item}"
#         - Continue
# Step 4: Process item (convert to lowercase) and add to result
#         - Print f"Approved: {item}"
# Step 5: Return result

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_PROJECT_INTRO}}")
print("=" * 50)

print("\n=== {{PHASE_1_TITLE}} ===")
numbers = [5, -3, 0, 8, -1, 12, 0, -7]
print(f"Numbers: {numbers}")
print("Positive only:")
print_positive_only(numbers)

print("\n=== {{PHASE_2_TITLE}} ===")
items = ["{{hero}}", "", "{{villain}}", "", "{{friend}}"]
result = filter_and_transform(items)
print(f"Filtered and transformed: {result}")

print("\n=== {{PHASE_3_TITLE}} ===")
values = ["A", "B", "C", "D", "E", "F"]
result = process_every_other(values)
print(f"Every other item: {result}")

print("\n=== {{PHASE_4_TITLE}} ===")
print("Sum numbers (type 'done' to finish):")
# Uncomment to test:
# total = sum_valid_inputs()
# print(f"Sum: {total}")

print("\n=== {{PHASE_5_TITLE}} ===")
all_items = ["{{hero}}", "{{villain}}", "{{friend}}", "{{mentor}}"]
blocked = ["{{villain}}"]
result = process_approved_items(all_items, blocked)
print(f"Approved items: {result}")

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
