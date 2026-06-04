# %% [markdown]
# {{CONTEXT_ERROR_HANDLING_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# Topic: Handling AttributeError from imports
# Difficulty: 3
#
# Even when a module imports successfully, trying to use a function
# or attribute that doesn't exist causes AttributeError. Learn to
# handle this gracefully.
#
# {{HANDLING_1_TITLE}}
# {{CONTEXT_HANDLING_1_NARRATIVE}}
#
# This function crashes if the function doesn't exist in the module.

# %%
import math
return math.fake_function(42)  # AttributeError!

# %% [markdown]
# ✏️ ADD ERROR HANDLING ✏️
#
# {{CONTEXT_HANDLING_HINT_1}}
#
# Step 1: Try to import the module
#
# Step 2: Get the function using getattr(module, function_name)
#
# Step 3: Call the function with *args
#
# Step 4: Handle ModuleNotFoundError and AttributeError
#
# Example:
#   try:
#       module = __import__(module_name)
#       func = getattr(module, function_name)
#       return func(*args)
#   except ModuleNotFoundError:
#       print(f"Module '{module_name}' not found")
#       return None
#   except AttributeError:
#       print(f"Function '{function_name}' not found in {module_name}")
#       return None

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{HANDLING_2_TITLE}}
# {{CONTEXT_HANDLING_2_NARRATIVE}}
#
# Check if a function exists before using it.

# %%
import math
return math.nonexistent()  # Crashes!

# %% [markdown]
# ✏️ ADD ERROR HANDLING ✏️
#
# {{CONTEXT_HANDLING_HINT_2}}
#
# Option 1: Use hasattr()
#   return hasattr(module, function_name)
#
# Option 2: Use try/except with getattr()
#   try:
#       getattr(module, function_name)
#       return True
#   except AttributeError:
#       return False

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ ADD ERROR HANDLING ✏️
#
# {{CONTEXT_HANDLING_HINT_2}}
#
# Step 1: Try to import the module
#
# Step 2: Try to get the attribute with getattr(module, constant_name, default)
#         The third argument to getattr is a default value!
#
# Step 3: Handle ModuleNotFoundError
#
# Example:
#   try:
#       module = __import__(module_name)
#       return getattr(module, constant_name, default)
#   except ModuleNotFoundError:
#       return default

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{HANDLING_3_TITLE}}
# {{CONTEXT_HANDLING_3_NARRATIVE}}
#
# Build a flexible function caller for {{school}}.

# %%
import math
func = getattr(math, operation)
return func(value)

# %% [markdown]
# ✏️ ADD ERROR HANDLING ✏️
#
# {{CONTEXT_HANDLING_HINT_3}}
#
# Step 1: Import math
#
# Step 2: Try to get and call the function
#
# Step 3: Handle multiple exception types:
#         except AttributeError:
#             print(f"Unknown operation: {operation}")
#         except ValueError as e:
#             print(f"Invalid value: {e}")
#         except TypeError as e:
#             print(f"Wrong type: {e}")
#
# Step 4: Return default for any error

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{HANDLING_4_TITLE}}
# {{CONTEXT_HANDLING_4_NARRATIVE}}
#
# Create a module explorer that safely lists available functions.
#
# ✏️ ADD ERROR HANDLING ✏️
#
# {{CONTEXT_HANDLING_HINT_4}}
#
# Step 1: Try to import the module
#
# Step 2: Get all names with dir(module)
#
# Step 3: Filter to only callable items:
#         functions = []
#         for name in dir(module):
#             if not name.startswith('_'):  # Skip private
#                 attr = getattr(module, name)
#                 if callable(attr):
#                     functions.append(name)
#
# Step 4: Return the list
#
# Step 5: Handle ModuleNotFoundError, return empty list

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_ERROR_HANDLING_INTRO}}")
print("=" * 50)

print("\n=== {{HANDLING_1_TITLE}} ===")
print("Testing safe function call:")
# Uncomment to test:
# result = safe_use_module_function("math", "sqrt", 16)
# print(f"  math.sqrt(16) = {result}")
# result = safe_use_module_function("math", "fake_func", 16)
# print(f"  math.fake_func(16) = {result}")
# result = safe_use_module_function("fake_module", "sqrt", 16)
# print(f"  fake_module.sqrt(16) = {result}")

print("\n=== {{HANDLING_2_TITLE}} ===")
print("Testing function existence check:")
# Uncomment to test:
# import math
# print(f"  math has sqrt: {has_function(math, 'sqrt')}")
# print(f"  math has fake: {has_function(math, 'fake')}")
# print(f"  Pi value: {safe_get_constant('math', 'pi', 3.14)}")
# print(f"  Fake constant: {safe_get_constant('math', 'fake', 'N/A')}")

print("\n=== {{HANDLING_3_TITLE}} ===")
print("Testing safe math operations:")
# Uncomment to test:
# print(f"  sqrt(16): {safe_math_operation('sqrt', 16)}")
# print(f"  floor(3.7): {safe_math_operation('floor', 3.7)}")
# print(f"  fake(16): {safe_math_operation('fake', 16, 'N/A')}")
# print(f"  sqrt(-1): {safe_math_operation('sqrt', -1, 'N/A')}")

print("\n=== {{HANDLING_4_TITLE}} ===")
print("Listing module functions:")
# Uncomment to test:
# functions = list_module_functions("math")
# print(f"  math has {len(functions)} functions")
# print(f"  First 5: {functions[:5]}")
# functions = list_module_functions("fake_module")
# print(f"  fake_module: {functions}")

print("\n" + "=" * 50)
print("{{CONTEXT_ROBUSTNESS_COMPLETE}}")
