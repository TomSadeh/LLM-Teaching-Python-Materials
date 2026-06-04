# =============================================================================
# Fill in the Blanks: Input
# =============================================================================
# Difficulty: 3-4
# Concepts: input() function, type conversion, int(), str()
# =============================================================================

# %% [markdown]
# {{CONTEXT_FILL_BLANKS_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## {{EXERCISE_1_TITLE}}
# {{CONTEXT_EXERCISE_1_NARRATIVE}}
#
# ✏️ FILL IN THE BLANKS ✏️
#
# Get {{hero}}'s name from the user.
#
# Hint: Use the input() function to get text from the user.
#
# name = ___("What is your name? ")    # Fill in the function name
# print("Hello,", name)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{EXERCISE_2_TITLE}}
# {{CONTEXT_EXERCISE_2_NARRATIVE}}
#
# ✏️ FILL IN THE BLANKS ✏️
#
# Get {{hero}}'s age and store it as a number.
#
# Hint: input() always returns a string. Use int() to convert to a number.
#
# age_text = input("How old are you? ")
# age = ___(age_text)                  # Convert string to integer
# print("Next year you will be", age + 1)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{EXERCISE_3_TITLE}}
# {{CONTEXT_EXERCISE_3_NARRATIVE}}
#
# ✏️ FILL IN THE BLANKS ✏️
#
# Get the price of a {{item}} and calculate the total.
#
# Hint: You can wrap input() directly with int().
#
# price = ___(input("Enter the price: "))    # Convert input directly
# quantity = 3
# total = price ___ quantity                  # Multiply price by quantity
# print("Total:", total)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{EXERCISE_4_TITLE}}
# {{CONTEXT_EXERCISE_4_NARRATIVE}}
#
# ✏️ FILL IN THE BLANKS ✏️
#
# Create a personalized welcome for {{school}}.
#
# Hint: Combine input() with string concatenation.
#
# name = input("Enter your name: ")
# print("Welcome to {{school}}, " ___ name ___ "!")    # Join strings

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_FILL_BLANKS_INTRO}}")
print("=" * 50)

print("\n=== {{EXERCISE_1_TITLE}} ===")
# exercise_a()  # Uncomment when you've filled the blanks

print("\n=== {{EXERCISE_2_TITLE}} ===")
# exercise_b()

print("\n=== {{EXERCISE_3_TITLE}} ===")
# exercise_c()

print("\n=== {{EXERCISE_4_TITLE}} ===")
# exercise_d()

print("\nFill in all the blanks, then uncomment to test!")
print("{{CONTEXT_ROLE_COMPLETE}}")
