# =============================================================================
# Code Tracing: Loop Variables
# =============================================================================
# Difficulty: 3
# Concepts: loop variable changes, tracking iterations
# =============================================================================

# %% [markdown]
# {{CONTEXT_CODE_TRACING_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## {{TRACE_1_TITLE}}
# {{CONTEXT_TRACE_1_NARRATIVE}}

# %%
# {{hero}} tracks steps taken at {{school}}
for step in range(4):
    print(f"Step {step}")

# %% [markdown]
# עקבי אחרי הערך של `step` בכל איטרציה.
#
# | Iteration | step | Output |
# |-----------|------|--------|
# | 1         |      |        |
# | 2         |      |        |
# | 3         |      |        |
# | 4         |      |        |
#
# > רמז: `range(4)` מייצר את הערכים 0, 1, 2, 3.
# > בכל איטרציה, `step` מקבל את הערך הבא.
#
# {{CONTEXT_TRACE_HINT_1}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{TRACE_2_TITLE}}
# {{CONTEXT_TRACE_2_NARRATIVE}}

# %%
# Counting down for {{creature}} at {{location}}
for num in range(3, 0, -1):
    print(f"T-minus {num}")
print("Launch!")

# %% [markdown]
# עקבי אחרי הערך של `num` בכל איטרציה.
#
# | Iteration | num | Output |
# |-----------|-----|--------|
# | 1         |     |        |
# | 2         |     |        |
# | 3         |     |        |
# | After loop |  - | ????   |
#
# > רמז: `range(3, 0, -1)` סופר לאחור: 3, 2, 1.
# > אחרי שהלולאה מסתיימת, ה-`print()` האחרון רץ.
#
# {{CONTEXT_TRACE_HINT_2}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{TRACE_3_TITLE}}
# {{CONTEXT_TRACE_3_NARRATIVE}}

# %%
# Drawing segments for {{hero}}'s path
for i in range(1, 4):
    length = i * 10
    print(f"Segment {i}: {length} units")

# %% [markdown]
# עקבי אחרי שני הערכים `i` וגם `length` בכל איטרציה.
#
# | Iteration | i | length (i * 10) | Output |
# |-----------|---|-----------------|--------|
# | 1         |   |                 |        |
# | 2         |   |                 |        |
# | 3         |   |                 |        |
#
# > רמז: `length` מחושב בתוך הלולאה, כך שהוא משתנה
# > בהתאם לערך הנוכחי של `i`.
#
# {{CONTEXT_TRACE_HINT_3}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{TRACE_4_TITLE}}
# {{CONTEXT_TRACE_4_NARRATIVE}}

# %%
# Calculating angles for shapes at {{place}}
for sides in range(3, 6):
    angle = 360 // sides
    print(f"{sides} sides: turn {angle} degrees")

# %% [markdown]
# עקבי אחרי `sides` ו-`angle` בכל איטרציה.
# זכרי: `//` הוא חילוק שלם (ללא עשרונות).
#
# | Iteration | sides | angle (360 // sides) | Output |
# |-----------|-------|----------------------|--------|
# | 1         |       |                      |        |
# | 2         |       |                      |        |
# | 3         |       |                      |        |
#
# > רמז: `360 // 3 = 120`, `360 // 4 = 90`, `360 // 5 = 72`
#
# {{CONTEXT_TRACE_HINT_4}}

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
