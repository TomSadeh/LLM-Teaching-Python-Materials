# =============================================================================
# Code Tracing: Accumulator Trace
# =============================================================================
# Difficulty: 4
# Concepts: tracking accumulator values, running totals through iterations
# =============================================================================

# %% [markdown]
# {{CONTEXT_CODE_TRACING_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## {{TRACE_1_TITLE}}
# {{CONTEXT_TRACE_1_NARRATIVE}}

# %%
# {{hero}} calculates total energy at {{school}}
total = 0
for i in range(1, 4):
    total = total + i
    print(f"After adding {i}: total = {total}")

# %% [markdown]
# מלאי את טבלת המעקב
#
# עקבי אחרי `i` ו-`total` בכל איטרציה.
#
# | לפני/אחרי    | i | total (לפני) | total (אחרי) | פלט |
# |--------------|---|--------------|--------------|-----|
# | התחלה        | - | 0            | -            | -   |
# | איטרציה 1    |   |              |              |     |
# | איטרציה 2    |   |              |              |     |
# | איטרציה 3    |   |              |              |     |
#
# > רמז: `total` מתחיל ב-0. בכל איטרציה, מוסיפים את `i` ל-`total`.
# > `range(1, 4)` נותן: 1, 2, 3
#
# {{CONTEXT_TRACE_HINT_1}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{TRACE_2_TITLE}}
# {{CONTEXT_TRACE_2_NARRATIVE}}

# %%
# Calculating distances for {{creature}}
distance = 0
for step in range(1, 5):
    move = step * 10
    distance = distance + move
    print(f"Step {step}: moved {move}, total distance = {distance}")

# %% [markdown]
# מלאי את טבלת המעקב
#
# עקבי אחרי `step`, `move` ו-`distance`.
#
# | איטרציה   | step | move (step*10) | distance (לפני) | distance (אחרי) |
# |-----------|------|----------------|-----------------|-----------------|
# | התחלה     | -    | -              | 0               | -               |
# | 1         |      |                |                 |                 |
# | 2         |      |                |                 |                 |
# | 3         |      |                |                 |                 |
# | 4         |      |                |                 |                 |
#
# > רמז: `move` מחושב בכל איטרציה, ו-`distance` מצטבר לאורך כל הלולאה.
#
# {{CONTEXT_TRACE_HINT_2}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{TRACE_3_TITLE}}
# {{CONTEXT_TRACE_3_NARRATIVE}}

# %%
# Tracking angles at {{location}}
total_angle = 0
for side in range(4):
    turn = 90
    total_angle = total_angle + turn
    print(f"After side {side}: turned {total_angle} degrees total")

# %% [markdown]
# מלאי את טבלת המעקב
#
# עקבי אחרי `side` ו-`total_angle`.
#
# | איטרציה   | side | turn | total_angle (לפני) | total_angle (אחרי) |
# |-----------|------|------|--------------------|--------------------|
# | התחלה     | -    | -    | 0                  | -                  |
# | 1         |      | 90   |                    |                    |
# | 2         |      | 90   |                    |                    |
# | 3         |      | 90   |                    |                    |
# | 4         |      | 90   |                    |                    |
#
# > רמז: שימי לב ש-`side` מתחיל ב-0 (מ-`range(4)`: 0, 1, 2, 3).
# > `turn` תמיד שווה ל-90, ו-`total_angle` גדל ב-90 בכל פעם.
#
# {{CONTEXT_TRACE_HINT_3}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{TRACE_4_TITLE}}
# {{CONTEXT_TRACE_4_NARRATIVE}}

# %%
# Building a message for {{hero}} at {{place}}
message = ""
for count in range(1, 4):
    message = message + str(count) + "! "
    print(f"Message so far: '{message}'")

# %% [markdown]
# מלאי את טבלת המעקב
#
# עקבי אחרי `count` ו-`message`.
#
# | איטרציה   | count | message (לפני) | message (אחרי) |
# |-----------|-------|----------------|----------------|
# | התחלה     | -     | `""`           | -              |
# | 1         |       |                |                |
# | 2         |       |                |                |
# | 3         |       |                |                |
#
# > רמז: גם מחרוזות יכולות להצטבר!
# > בכל איטרציה מתווסף: `str(count) + "! "`
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
