# =============================================================================
# Hybrid Exercise: The Apprentice - Return Value Mastery
# =============================================================================
# Difficulty: 2-3
# Arc: Apprentice (DISCOVERY -> GUIDANCE -> GROWTH)
# Concepts: Return values, using returned data, return vs print
# =============================================================================

# %% [markdown]
# {{CONTEXT_DISCOVERY_INTRO}}
#
# This is a multi-part exercise. Complete each part in order.
#
# PART 1: DISCOVERY - Observe Return vs Print
# {{CONTEXT_DISCOVERY_INTRO}}
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# Study these two functions carefully. They look similar but behave
# differently.

# %%
print(f"Hello, {name}!")

# %%
return f"Hello, {name}!"

# %%
print("--- Testing function_with_print ---")
result1 = function_with_print("{{hero}}")
print(f"Stored result: {result1}")
print(f"Type of result: {type(result1)}")

print("\n--- Testing function_with_return ---")
result2 = function_with_return("{{hero}}")
print(f"Stored result: {result2}")
print(f"Type of result: {type(result2)}")

# %% [markdown]
# YOUR OBSERVATIONS
#
# Answer these questions after running the code:
#
# 1. What does function_with_print return? _______________
# 2. What does function_with_return return? _______________
# 3. Which one can you use in other calculations? _______________
#
#
# PART 2: GUIDANCE - Practice with Return Statements
# {{CONTEXT_GUIDANCE_INTRO}}
# {{CONTEXT_GUIDANCE_NARRATIVE}}
#
# Complete these functions by adding the correct return statements.

# %%
# Started for you:
message = f"Welcome, {name}!"

# COMPLETE THIS FUNCTION
#
# Return the message variable.
#
# Hint: Use the return keyword.

pass  # Replace with implementation

# %%
# COMPLETE THIS FUNCTION
#
# Calculate the result and return it.
#
# Hint: You can calculate and return in one line.

pass

# %%
# COMPLETE THIS FUNCTION
#
# Use if/elif/else with return statements.

pass

# %% [markdown]
# PART 3: GROWTH - Create Returning Functions
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Now create your own functions that return values.

# %%
# YOUR CODE HERE
#
# Create a function that returns a formatted string.
#
# Step 1: Define a function called format_title that takes one parameter:
#         text and returns f"=== {text} ==="
# Step 2: Call format_title("{{school}} News") and store in header
# Step 3: Print header
# Step 4: Call format_title("End of Report") and store in footer
# Step 5: Print footer
#
# Expected output:
#   === {{school}} News ===
#   === End of Report ===
pass

# %%
# YOUR CODE HERE
#
# Create functions that return calculated values.
#
# Step 1: Define add(a, b) that returns a + b
# Step 2: Define subtract(a, b) that returns a - b
# Step 3: Store add(50, 30) in sum_result
# Step 4: Store subtract(sum_result, 20) in final_result
# Step 5: Print f"50 + 30 = {sum_result}"
# Step 6: Print f"{sum_result} - 20 = {final_result}"
#
# Expected output:
#   50 + 30 = 80
#   80 - 20 = 60
pass

# %%
# YOUR CODE HERE
#
# Use returned values directly in print statements.
#
# Step 1: Define make_label(item) that returns f"[{item}]"
# Step 2: Print f"Item: {make_label('{{item}}')}"
#         (Call make_label directly inside the f-string)
# Step 3: Print f"Location: {make_label('{{location}}')}"
#
# Hint: You can call functions inside f-strings!
#
# Expected output:
#   Item: [{{item}}]
#   Location: [{{location}}]
pass

# %%
# YOUR CODE HERE
#
# Chain multiple function calls.
#
# Step 1: Define get_base() that returns 100
# Step 2: Define add_bonus(score) that returns score + 25
# Step 3: Define double(number) that returns number * 2
# Step 4: Store get_base() in base
# Step 5: Store add_bonus(base) in with_bonus
# Step 6: Store double(with_bonus) in final
# Step 7: Print f"Base: {base}"
# Step 8: Print f"With bonus: {with_bonus}"
# Step 9: Print f"Doubled: {final}"
#
# Expected output:
#   Base: 100
#   With bonus: 125
#   Doubled: 250
pass

# %%
print("=" * 60)
print("THE APPRENTICE: Return Value Mastery")
print("=" * 60)

print("\n--- PART 1: DISCOVERY - Observe Differences ---")
print("{{CONTEXT_DISCOVERY_INTRO}}")
part_1_observe_differences()

print("\n--- PART 2: GUIDANCE - Practice Returns ---")
print("{{CONTEXT_GUIDANCE_INTRO}}")

print("\nTesting get_greeting:")
greeting = get_greeting("{{hero}}")
print(f"Result: {greeting}")

print("\nTesting calculate_power:")
power1 = calculate_power(10, 3)
power2 = calculate_power(25, 4)
print(f"10 * 3 = {power1}")
print(f"25 * 4 = {power2}")

print("\nTesting get_status:")
status1 = get_status(5)
status2 = get_status(20)
status3 = get_status(30)
print(f"Level 5: {status1}")
print(f"Level 20: {status2}")
print(f"Level 30: {status3}")

print("\n--- PART 3: GROWTH - Your Turn ---")
print("{{CONTEXT_GROWTH_INTRO}}")

print("\nSimple return:")
exercise_simple_return()

print("\nCalculation return:")
exercise_calculation_return()

print("\nUse in print:")
exercise_use_in_print()

print("\nChain returns:")
exercise_chain_returns()

print("\n" + "=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
