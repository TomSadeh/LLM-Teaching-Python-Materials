# =============================================================================
# Code Tracing: Boolean Operators (and/or/not)
# =============================================================================
# Difficulty: 4
# Concepts: and, or, not, compound conditions, operator precedence
# =============================================================================

# %% [markdown]
# {{CONTEXT_CODE_TRACING_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## {{TRACE_1_TITLE}}
# {{CONTEXT_TRACE_1_NARRATIVE}}
# The 'and' operator: BOTH conditions must be True.

# %%
level = 10
gold = 150
if level >= 5 and gold >= 100:
    print("{{hero}} can enter {{danger_location}}!")
else:
    print("{{hero}} cannot enter yet.")

# %% [markdown]
# ✏️ FILL IN THE TRACING TABLE ✏️
#
# {{CONTEXT_TRACE_HINT_1}}
#
# | Condition | Check | Result |
# |-----------|-------|--------|
# | level >= 5 | 10 >= 5 | _____ |
# | gold >= 100 | 150 >= 100 | _____ |
# | Combined (and) | _____ and _____ | _____ |
#
# Which branch executes? _______________
# What gets printed? _______________
#
# Remember: 'and' means BOTH must be True!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{TRACE_2_TITLE}}
# {{CONTEXT_TRACE_2_NARRATIVE}}
# The 'or' operator: AT LEAST ONE condition must be True.

# %%
has_key = False
has_password = True
if has_key or has_password:
    print("{{hero}} opens the door to {{location}}!")
else:
    print("The door remains locked.")

# %% [markdown]
# ✏️ FILL IN THE TRACING TABLE ✏️
#
# {{CONTEXT_TRACE_HINT_2}}
#
# | Condition | Value | Result |
# |-----------|-------|--------|
# | has_key | False | False |
# | has_password | True | True |
# | Combined (or) | False or True | _____ |
#
# Which branch executes? _______________
# What gets printed? _______________
#
# Remember: 'or' means AT LEAST ONE must be True!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{TRACE_3_TITLE}}
# {{CONTEXT_TRACE_3_NARRATIVE}}
# The 'not' operator: Flips True to False and False to True.

# %%
is_raining = False
if not is_raining:
    print("{{hero}} goes outside to train.")
else:
    print("{{hero}} stays inside.")

# %% [markdown]
# ✏️ FILL IN THE TRACING TABLE ✏️
#
# {{CONTEXT_TRACE_HINT_3}}
#
# | Variable | Value |
# |----------|-------|
# | is_raining | False |
# | not is_raining | _____ |
#
# Which branch executes? _______________
# What gets printed? _______________
#
# Remember: 'not' flips the boolean value!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{TRACE_4_TITLE}}
# {{CONTEXT_TRACE_4_NARRATIVE}}
# Combining multiple operators.

# %%
health = 80
has_item = True
enemy_nearby = True

if health < 50 and has_item:
    print("{{hero}} uses an {{item}}!")
elif health >= 50 or not enemy_nearby:
    print("{{hero}} continues exploring.")
else:
    print("{{hero}} must {{retreat_action}}!")

# %% [markdown]
# ✏️ FILL IN THE TRACING TABLE ✏️
#
# {{CONTEXT_TRACE_HINT_4}}
#
# Check 1: health < 50 and has_item
# | Condition | Check | Result |
# |-----------|-------|--------|
# | health < 50 | 80 < 50 | _____ |
# | has_item | True | True |
# | Combined (and) | _____ and True | _____ |
#
# First branch executes? _____
#
# Check 2: health >= 50 or not enemy_nearby
# | Condition | Check | Result |
# |-----------|-------|--------|
# | health >= 50 | 80 >= 50 | _____ |
# | enemy_nearby | True | True |
# | not enemy_nearby | not True | _____ |
# | Combined (or) | _____ or _____ | _____ |
#
# Second branch executes? _____
#
# What gets printed? _______________

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{TRACE_5_TITLE}}
# {{CONTEXT_TRACE_5_NARRATIVE}}
# 'and' has higher precedence than 'or'.

# %%
a = True
b = False
c = True
# Without parentheses, 'and' is evaluated first
result = a or b and c
print(f"Result: {result}")

# %% [markdown]
# Same as: a or (b and c)
# NOT: (a or b) and c
#
# ✏️ FILL IN THE TRACING TABLE ✏️
#
# {{CONTEXT_TRACE_HINT_5}}
#
# The expression: a or b and c
# Values: True or False and True
#
# Step 1: Evaluate 'and' first (higher precedence)
# b and c = False and True = _____
#
# Step 2: Then evaluate 'or'
# a or (result from step 1) = True or _____ = _____
#
# Final result: _____
# What gets printed? _______________
#
# If it were (a or b) and c instead:
# (True or False) and True = _____ and True = _____

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("=== {{TRACE_1_TITLE}} - Actual Execution ===")
code_to_trace_a()

print("\n=== {{TRACE_2_TITLE}} - Actual Execution ===")
code_to_trace_b()

print("\n=== {{TRACE_3_TITLE}} - Actual Execution ===")
code_to_trace_c()

print("\n=== {{TRACE_4_TITLE}} - Actual Execution ===")
code_to_trace_d()

print("\n=== {{TRACE_5_TITLE}} - Actual Execution ===")
code_to_trace_e()

# %%
print("{{CONTEXT_CODE_TRACING_INTRO}}")
print("=" * 50)
print()
print("Complete the tracing tables in trace_table_X functions first!")
print("Then uncomment the line below to verify your answers.")
print()

# Uncomment this line AFTER completing your traces:
# verify_traces()

print("{{CONTEXT_VERIFICATION_COMPLETE}}")
