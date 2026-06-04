# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# Topic: Using break to exit loops early
# Difficulty: 2-3
#
# The 'break' statement immediately exits the current loop.
# Use it when you've found what you're looking for or need to stop early.
#
# {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# Use break to exit a loop when a condition is met.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Set result = None
# Step 2: Loop through each number in numbers
# Step 3: If the number is negative:
#         - Set result to that number
#         - Break out of the loop
# Step 4: Return result

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# Use break with user input to create exit conditions.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Create an empty list for names
# Step 2: Start an infinite loop (while True)
# Step 3: Ask for input
# Step 4: If input is 'done', break
# Step 5: Otherwise, add the name to the list
# Step 6: After the loop, return the list

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# Use break in a search to stop once you find the target.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Loop through inventory with index (use range(len(...)))
# Step 2: Print f"Checking: {item}"
# Step 3: If item equals target:
#         - Print f"Found {target}!"
#         - Return the index (using break or direct return)
# Step 4: After the loop, print f"{target} not found."
# Step 5: Return -1

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# Use break with a counter limit to prevent infinite loops.

# %%
secret = "{{password}}"
max_attempts = 5

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Set attempts = 0
# Step 2: While attempts < max_attempts:
#         - Increase attempts
#         - Ask for a guess
#         - If guess equals secret, print success and return True
# Step 3: After the loop, print failure message
# Step 4: Return False

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_5_TITLE}}
# {{CONTEXT_PHASE_5}}
#
# Combine break with complex conditions.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Create an empty list for results
# Step 2: Loop through each item in data
# Step 3: If item is "ERROR", "", or None:
#         - Print f"Error encountered! Stopping."
#         - Break
# Step 4: Process the item (convert to uppercase) and add to results
#         - Print f"Processed: {processed_item}"
# Step 5: Return results

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_PROJECT_INTRO}}")
print("=" * 50)

print("\n=== {{PHASE_1_TITLE}} ===")
numbers = [5, 12, 8, -3, 7, -1]
result = find_first_negative(numbers)
print(f"First negative in {numbers}: {result}")

print("\n=== {{PHASE_2_TITLE}} ===")
print("Collecting names (type 'done' to finish):")
# Uncomment to test:
# names = collect_names_until_done()
# print(f"Collected: {names}")

print("\n=== {{PHASE_3_TITLE}} ===")
inventory = ["{{item}}", "{{pet}}", "{{creature}}", "{{transport}}"]
index = search_inventory(inventory, "{{creature}}")
print(f"Found at index: {index}")

print("\n=== {{PHASE_4_TITLE}} ===")
print("Guess the secret word:")
# Uncomment to test:
# success = safe_guess_loop()
# print(f"Result: {'Success!' if success else 'Failed'}")

print("\n=== {{PHASE_5_TITLE}} ===")
test_data = ["{{hero}}", "{{heroine}}", "ERROR", "{{friend}}"]
processed = process_until_error(test_data)
print(f"Processed items: {processed}")

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
