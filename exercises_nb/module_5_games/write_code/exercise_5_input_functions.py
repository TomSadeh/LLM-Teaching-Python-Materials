# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# Topic: Building robust input functions
# Difficulty: 3
#
# Create reusable input functions that validate user input.
# These can be used in any game or interactive program!
#
# {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# Build a function that gets an integer within a specified range.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Start while True loop
# Step 2: Print prompt and get input
# Step 3: Check if numeric using .lstrip('-').isdigit()
#         If not, print "Please enter a number." and continue
# Step 4: Convert to int
# Step 5: Check if in range
#         If not, print f"Must be between {min_val} and {max_val}." and continue
# Step 6: Return valid integer

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# Build a function that gets a choice from a list of options.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Print prompt
# Step 2: Print numbered list of options
# Step 3: Start while True loop
# Step 4: Get input (lowercase for comparison)
# Step 5: Check if input is a valid number (1 to len(options))
#         If so, return options[int(input) - 1]
# Step 6: Check if input matches any option (case insensitive)
#         If so, return the original option
# Step 7: Print "Invalid choice. Try again."

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# Build a function that gets a yes/no answer with custom prompts.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Start while True loop
# Step 2: Print f"{question} ({yes_text}/{no_text}): " and get input
# Step 3: Convert to lowercase and strip
# Step 4: If matches yes_text or its first letter, return True
# Step 5: If matches no_text or its first letter, return False
# Step 6: Print f"Please enter {yes_text} or {no_text}."

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# Build a function that gets a non-empty string with validation.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Start while True loop
# Step 2: Print prompt and get input
# Step 3: If validator_func(input) returns True, return input
# Step 4: Otherwise print error_message

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_5_TITLE}}
# {{CONTEXT_PHASE_5}}
#
# Use your input functions to build a character creator.

# %%
print("=" * 40)
print("   CHARACTER CREATOR")
print("=" * 40)
print()

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Get name using get_validated_string
#         (validator: len >= 2, error: "Name must be at least 2 characters")
# Step 2: Get character class using get_choice_from_list
# Step 3: Get level using get_integer_in_range
# Step 4: Display summary
# Step 5: Confirm with get_yes_no
# Step 6: If confirmed, return dict with name, class, level
# Step 7: If not confirmed, return None

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_PROJECT_INTRO}}")
print("=" * 50)

print("\n=== {{PHASE_1_TITLE}} ===")
print("Testing integer range input:")
# level = get_integer_in_range("Enter level (1-10): ", 1, 10)
# print(f"Level selected: {level}")

print("\n=== {{PHASE_2_TITLE}} ===")
print("Testing choice from list:")
# abilities = ["{{spell1}}", "{{spell2}}", "{{spell3}}"]
# choice = get_choice_from_list("Select ability:", abilities)
# print(f"Selected: {choice}")

print("\n=== {{PHASE_3_TITLE}} ===")
print("Testing yes/no:")
# answer = get_yes_no("Do you want to continue?")
# print(f"Answer: {answer}")

print("\n=== {{PHASE_4_TITLE}} ===")
print("Testing validated string:")
# def is_long_enough(s):
#     return len(s) >= 3
# name = get_validated_string("Enter name (3+ chars): ", is_long_enough, "Too short!")
# print(f"Name: {name}")

print("\n=== {{PHASE_5_TITLE}} ===")
print("Testing character creator:")
# character = create_character()
# if character:
#     print(f"\nCreated: {character}")
# else:
#     print("\nCancelled.")

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
