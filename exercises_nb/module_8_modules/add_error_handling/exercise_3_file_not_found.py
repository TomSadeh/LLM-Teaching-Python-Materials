# %% [markdown]
# {{CONTEXT_ERROR_HANDLING_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# Topic: Handling FileNotFoundError gracefully
# Difficulty: 3
#
# Files may not exist when you try to read them. Learn to handle this
# gracefully by providing defaults, creating the file, or informing the user.
#
# {{HANDLING_1_TITLE}}
# {{CONTEXT_HANDLING_1_NARRATIVE}}
#
# This function crashes if the file doesn't exist.

# %%
with open("config.txt", "r") as f:
    return f.read()

# %% [markdown]
# ✏️ ADD ERROR HANDLING ✏️
#
# {{CONTEXT_HANDLING_HINT_1}}
#
# Step 1: Try to open and read the file
#
# Step 2: If FileNotFoundError, return default_content
#
# Pattern:
#   try:
#       with open(filename, "r") as f:
#           return f.read()
#   except FileNotFoundError:
#       return default_content

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{HANDLING_2_TITLE}}
# {{CONTEXT_HANDLING_2_NARRATIVE}}
#
# This function doesn't handle missing files.

# %%
with open("items.txt", "r") as f:
    return [line.strip() for line in f]

# %% [markdown]
# ✏️ ADD ERROR HANDLING ✏️
#
# {{CONTEXT_HANDLING_HINT_2}}
#
# Step 1: Handle None default (use empty list)
#         if default_list is None:
#             default_list = []
#
# Step 2: Try to load the file
#
# Step 3: Handle FileNotFoundError

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{HANDLING_3_TITLE}}
# {{CONTEXT_HANDLING_3_NARRATIVE}}
#
# Create file with defaults if it doesn't exist.

# %%
with open("settings.txt", "r") as f:
    return f.read()

# %% [markdown]
# ✏️ ADD ERROR HANDLING ✏️
#
# {{CONTEXT_HANDLING_HINT_3}}
#
# Step 1: Try to read existing file
#
# Step 2: If FileNotFoundError:
#         - Create file with default_config
#         - Print message about creating new file
#         - Return default_config
#
# Pattern:
#   try:
#       with open(filename, "r") as f:
#           return f.read()
#   except FileNotFoundError:
#       with open(filename, "w") as f:
#           f.write(default_config)
#       print(f"Created new config: {filename}")
#       return default_config

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{HANDLING_4_TITLE}}
# {{CONTEXT_HANDLING_4_NARRATIVE}}
#
# Handle multiple file operations safely.

# %%
with open("source.txt", "r") as src:
    content = src.read()
with open("dest.txt", "w") as dst:
    dst.write(content)

# %% [markdown]
# ✏️ ADD ERROR HANDLING ✏️
#
# {{CONTEXT_HANDLING_HINT_4}}
#
# Step 1: Try to read source file
#
# Step 2: Try to write destination file
#
# Step 3: Handle FileNotFoundError for source
#
# Step 4: Handle PermissionError for destination
#
# Step 5: Return True on success, False on failure

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{HANDLING_5_TITLE}}
# {{CONTEXT_HANDLING_5_NARRATIVE}}
#
# Build a robust file loader for {{school}}.
#
# ✏️ ADD ERROR HANDLING ✏️
#
# {{CONTEXT_HANDLING_HINT_5}}
#
# Step 1: Loop through filenames
#
# Step 2: Try to read each file
#
# Step 3: If successful, return content immediately
#
# Step 4: If FileNotFoundError, continue to next
#
# Step 5: After loop (all failed), return default
#
# Pattern:
#   for filename in filenames:
#       try:
#           with open(filename, "r") as f:
#               return f.read()
#       except FileNotFoundError:
#           continue
#   return default

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_ERROR_HANDLING_INTRO}}")
print("=" * 50)

print("\n=== {{HANDLING_1_TITLE}} ===")
print("Reading with default:")
# content = safe_read_config("nonexistent.txt", "default value")
# print(f"  Result: {content}")

print("\n=== {{HANDLING_2_TITLE}} ===")
print("Loading list with default:")
# items = safe_load_list("nonexistent.txt", ["default1", "default2"])
# print(f"  Items: {items}")

print("\n=== {{HANDLING_3_TITLE}} ===")
print("Ensuring config exists:")
# config = ensure_config_exists("test_config.txt", "setting=value")
# print(f"  Config: {config}")

print("\n=== {{HANDLING_4_TITLE}} ===")
print("Safe file copy:")
# success = safe_copy_file("source.txt", "dest.txt")
# print(f"  Copy successful: {success}")

print("\n=== {{HANDLING_5_TITLE}} ===")
print("Loading with fallbacks:")
# content = load_with_fallbacks(["primary.txt", "backup.txt"], "default")
# print(f"  Content: {content}")

print("\n" + "=" * 50)
print("{{CONTEXT_ROBUSTNESS_COMPLETE}}")
