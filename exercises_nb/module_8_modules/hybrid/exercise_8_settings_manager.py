# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
#
# This is a multi-part exercise where you build a configuration system
# for {{school}} that persists settings between sessions using JSON.
#
# Programming concepts: JSON, file I/O, error handling, defaults
# Difficulty: 3-4

# %%
import json

# %% [markdown]
# PART 1: Growth - Save Settings to JSON
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Learn to save configuration settings to a JSON file.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Open file for writing
#         with open(filename, "w") as f:
#
# Step 2: Save with pretty formatting:
#             json.dump(settings, f, indent=2)
#
# Step 3: Return True

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Return a dict with these defaults:
# {
#     "player_name": "{{hero}}",
#     "difficulty": "normal",
#     "music_enabled": True,
#     "volume": 80,
#     "language": "en",
#     "theme": "default",
#     "last_save": None,
#     "high_score": 0
# }

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 2: Growth - Load Settings with Defaults
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Load settings and fill in any missing values with defaults.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Get defaults if not provided:
#         if defaults is None:
#             defaults = create_default_settings()
#
# Step 2: Start with copy of defaults:
#         settings = defaults.copy()
#
# Step 3: Try to load file and update settings:
#         try:
#             with open(filename, "r") as f:
#                 loaded = json.load(f)
#                 settings.update(loaded)
#         except FileNotFoundError:
#             pass  # Use defaults
#         except json.JSONDecodeError:
#             print("Settings file corrupt, using defaults")
#
# Step 4: Return settings

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Use dict.get() method

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 3: Investigation - Handling Corrupt Files
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# What happens when the settings file is corrupted?
#
# ERROR MESSAGE:
# --------------
# Traceback (most recent call last):
#   File "load_config.py", line 3, in <module>
#     settings = json.load(f)
# json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
#
# This happens when:
# 1. File is empty
# 2. File contains invalid JSON
# 3. File was corrupted during write
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Try to open file
#         If FileNotFoundError: return ("missing", "File not found")
#
# Step 2: Read content
#         If empty: return ("empty", "File is empty")
#
# Step 3: Try to parse JSON
#         If JSONDecodeError: return ("corrupt", "Invalid JSON")
#
# Step 4: Return ("ok", "Settings file is valid")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 4: Growth - Complete Settings Manager
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Build a complete settings manager with all features.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Create storage dict:
#         manager = {
#             "filename": filename,
#             "settings": load_settings(filename),
#             "dirty": False  # Track unsaved changes
#         }
#
# Step 2: Create helper functions (nested in this function):
#
#         def get(key, default=None):
#             return manager["settings"].get(key, default)
#
#         def set_value(key, value):
#             manager["settings"][key] = value
#             manager["dirty"] = True
#
#         def save():
#             save_settings(manager["filename"], manager["settings"])
#             manager["dirty"] = False
#
#         def has_unsaved():
#             return manager["dirty"]
#
#         def reset_to_defaults():
#             manager["settings"] = create_default_settings()
#             manager["dirty"] = True
#
# Step 3: Add functions to manager:
#         manager["get"] = get
#         manager["set"] = set_value
#         manager["save"] = save
#         manager["has_unsaved"] = has_unsaved
#         manager["reset"] = reset_to_defaults
#
# Step 4: Return manager

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Print each setting nicely:
# print("Current Settings:")
# print("-" * 30)
# for key, value in settings.items():
#     print(f"  {key}: {value}")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## MAIN

# %%
print("=" * 60)
print("{{CONTEXT_PROJECT_INTRO}}")
print("Settings Manager for {{school}}")
print("=" * 60)
print()

print(">>> PART 1: Saving Settings")
print("-" * 40)
# Uncomment to test:
# defaults = create_default_settings()
# print("Default settings:")
# display_settings(defaults)
# save_settings("test_settings.json", defaults)
# print("\nSaved to test_settings.json")
print()

print(">>> PART 2: Loading Settings")
print("-" * 40)
# Uncomment to test:
# settings = load_settings("test_settings.json")
# print("Loaded settings:")
# display_settings(settings)
# print()
# # Test with missing file
# settings = load_settings("nonexistent.json")
# print("From missing file (defaults):")
# display_settings(settings)
print()

print(">>> PART 3: Diagnosing Files")
print("-" * 40)
# Uncomment to test:
# status, message = diagnose_settings_file("test_settings.json")
# print(f"test_settings.json: {status} - {message}")
# status, message = diagnose_settings_file("nonexistent.json")
# print(f"nonexistent.json: {status} - {message}")
print()

print(">>> PART 4: Settings Manager")
print("-" * 40)
# Uncomment to test:
# manager = create_settings_manager("game_settings.json")
# print(f"Current difficulty: {manager['get']('difficulty')}")
# print(f"Current volume: {manager['get']('volume')}")
# manager['set']('difficulty', 'hard')
# manager['set']('volume', 100)
# print(f"Has unsaved changes: {manager['has_unsaved']()}")
# manager['save']()
# print("Settings saved!")
print()

print("=" * 60)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
print("=" * 60)
