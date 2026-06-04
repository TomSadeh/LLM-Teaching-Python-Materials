# =============================================================================
# Write Code: First Loop
# =============================================================================
# Difficulty: 2
# Concepts: for loop, range(n), repeating turtle commands
# =============================================================================

# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}

# %%
import turtle

# %% [markdown]
# {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# ✏️ YOUR CODE HERE ✏️
#
# Use a loop to print "Hello, {{school}}!" three times.
#
# Step 1: Write: for i in range(3):
# Step 2: On the next line, INDENTED, write: print("Hello, {{school}}!")
#
# Expected output:
# Hello, {{school}}!
# Hello, {{school}}!
# Hello, {{school}}!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# ✏️ YOUR CODE HERE ✏️
#
# Draw a square for {{hero}} using a loop.
# A square has 4 sides, each with a 90-degree turn.
#
# Step 1: Create a turtle with t = turtle.Turtle()
# Step 2: Write a for loop that repeats 4 times
# Step 3: Inside the loop (indented):
#         - t.forward(100)
#         - t.right(90)
#
# Hint: Each side is: move forward, then turn right.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# ✏️ YOUR CODE HERE ✏️
#
# Draw a triangle for {{creature}} using a loop.
# A triangle has 3 sides with 120-degree turns.
#
# Step 1: Create a turtle
# Step 2: Write a for loop that repeats 3 times
# Step 3: Inside the loop:
#         - Move forward 80 units
#         - Turn left 120 degrees
#
# Hint: The exterior angle of a triangle is 120 degrees.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{PHASE_4_TITLE}}
# {{CONTEXT_PHASE_4}}
#
# ✏️ YOUR CODE HERE ✏️
#
# Create a dashed line at {{location}} by repeating:
# draw, lift pen, move, put pen down.
#
# Step 1: Create a turtle
# Step 2: Use a for loop that repeats 5 times
# Step 3: Inside the loop:
#         - t.forward(20)      # Draw a dash
#         - t.penup()          # Lift the pen
#         - t.forward(10)      # Move without drawing
#         - t.pendown()        # Put pen back down
#
# Expected: A dashed line with 5 dashes and 4 gaps.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_PROJECT_INTRO}}")
print("=" * 50)

print("\n=== {{PHASE_1_TITLE}} ===")
exercise_a()

print("\n=== {{PHASE_2_TITLE}} ===")
exercise_b()

print("\n=== {{PHASE_3_TITLE}} ===")
exercise_c()

print("\n=== {{PHASE_4_TITLE}} ===")
exercise_d()

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
turtle.done()
