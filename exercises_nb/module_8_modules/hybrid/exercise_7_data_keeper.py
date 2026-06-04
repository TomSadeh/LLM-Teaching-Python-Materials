# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
#
# This is a multi-part exercise where {{hero}} builds a data persistence
# system for {{school}}. You'll save and load progress using text files,
# understand common errors, and add proper error handling.
#
# Programming concepts: file I/O, context managers, error handling
# Difficulty: 2-3
#
# PART 1: Growth - Save Data to Files
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Learn to save different types of data to text files.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Open file for writing
#         with open(filename, "w") as f:
#
# Step 2: Write each field on its own line:
#         f.write(f"NAME: {name}\n")
#         f.write(f"LEVEL: {level}\n")
#         f.write(f"ABILITIES: {', '.join(abilities)}\n")
#
# Step 3: Print confirmation message

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Open file for writing
#
# Step 2: Loop through scores dict:
#         for name, score in scores.items():
#             f.write(f"{name}: {score}\n")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 2: Growth - Load Data from Files
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Learn to read and parse data from text files.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Initialize profile dict
#
# Step 2: Open and read file:
#         with open(filename, "r") as f:
#             for line in f:
#                 # Parse each line
#
# Step 3: Parse NAME line:
#         if line.startswith("NAME:"):
#             profile["name"] = line.replace("NAME:", "").strip()
#
# Step 4: Parse LEVEL line (convert to int):
#         if line.startswith("LEVEL:"):
#             profile["level"] = int(line.replace("LEVEL:", "").strip())
#
# Step 5: Parse ABILITIES line (split into list):
#         if line.startswith("ABILITIES:"):
#             abilities_str = line.replace("ABILITIES:", "").strip()
#             profile["abilities"] = [a.strip() for a in abilities_str.split(",")]
#
# Step 6: Return the profile dict

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Initialize empty scores dict
#
# Step 2: Open and read file
#
# Step 3: Parse each line:
#         for line in f:
#             if ":" in line:
#                 name, score = line.split(":")
#                 scores[name.strip()] = int(score.strip())
#
# Step 4: Return scores dict

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 3: Investigation - Understanding File Errors
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# What happens when things go wrong?
#
# ERROR MESSAGE 1:
# ----------------
# Traceback (most recent call last):
#   File "load_game.py", line 2, in <module>
#     with open("save_data.txt", "r") as f:
# FileNotFoundError: [Errno 2] No such file or directory: 'save_data.txt'
#
# ERROR MESSAGE 2:
# ----------------
# Traceback (most recent call last):
#   File "parse_score.py", line 5, in <module>
#     score = int(line.strip())
# ValueError: invalid literal for int() with base 10: 'not_a_number'
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Explain FileNotFoundError:
#         print("FileNotFoundError occurs when:")
#         print("  - The file path is wrong")
#         print("  - The file was deleted")
#         print("  - The file was never created")
#
# Step 2: Explain ValueError during parsing:
#         print("\nValueError during int() occurs when:")
#         print("  - The file format is corrupted")
#         print("  - The data isn't what we expected")
#         print("  - Extra whitespace or characters")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 4: Improvement - Safe Loading with Error Handling
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# Add error handling to make the system robust.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Set default if not provided:
#         if default is None:
#             default = {"name": "Unknown", "level": 1, "abilities": []}
#
# Step 2: Try to load:
#         try:
#             profile = load_profile(filename)
#             return profile
#         except FileNotFoundError:
#             print(f"No save file found: {filename}")
#             return default
#         except ValueError as e:
#             print(f"Save file corrupted: {e}")
#             return default

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Handle FileNotFoundError and return {} as default

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: If backup is True, rename old file:
#         import os
#         if os.path.exists(filename) and backup:
#             os.rename(filename, filename + ".backup")
#
# Step 2: Save the new profile
#
# Step 3: Print confirmation

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## MAIN

# %%
print("=" * 60)
print("{{CONTEXT_PROJECT_INTRO}}")
print("Data Persistence for {{school}}")
print("=" * 60)
print()

print(">>> PART 1: Saving Data")
print("-" * 40)
# Uncomment to test:
# save_profile(
#     "hero_save.txt",
#     "{{hero}}",
#     5,
#     ["{{spell1}}", "{{spell2}}"]
# )
# save_high_scores(
#     "scores.txt",
#     {"{{hero}}": 1000, "{{heroine}}": 1200, "{{friend}}": 800}
# )
print()

print(">>> PART 2: Loading Data")
print("-" * 40)
# Uncomment to test:
# profile = load_profile("hero_save.txt")
# print(f"Loaded profile: {profile}")
# scores = load_high_scores("scores.txt")
# print(f"Loaded scores: {scores}")
print()

print(">>> PART 3: Understanding Errors")
print("-" * 40)
explain_file_errors()
print()

print(">>> PART 4: Safe Loading")
print("-" * 40)
# Uncomment to test:
# profile = safe_load_profile("nonexistent.txt")
# print(f"Safe load result: {profile}")
# profile = safe_load_profile("hero_save.txt")
# print(f"Safe load result: {profile}")
print()

print("=" * 60)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
print("=" * 60)
