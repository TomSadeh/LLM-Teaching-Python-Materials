# %% [markdown]
# {{CONTEXT_CODE_TRACING_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# עקבי אחרי שינויים במילוניות כדי להבין כיצד
# מילוניות משתנות לאורך מספר פעולות.
#
# ## {{TRACE_1_TITLE}}
# {{CONTEXT_TRACE_1_NARRATIVE}}

# %%
inventory = {"{{item}}": 2}
inventory["{{item}}"] = inventory["{{item}}"] + 3
inventory["{{spell1}}"] = 1
del inventory["{{item}}"]
print(inventory)

# %% [markdown]
# {{CONTEXT_TRACE_HINT_1}}
#
# עקבי אחרי תוכן המילונית בכל שלב.
#
# | שלב | תוכן inventory                 | פלט (אם יש)     |
# |-----|--------------------------------|-----------------|
# | 0   | {"{{item}}": 2}                |                 |
# | 1   |                                |                 |
# | 2   |                                |                 |
# | 3   |                                |                 |
# | 4   |                                |                 |
#
# כתבי את הטבלה המלאה כהערות למטה:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{TRACE_2_TITLE}}
# {{CONTEXT_TRACE_2_NARRATIVE}}

# %%
scores = {}
players = ["{{hero}}", "{{heroine}}", "{{hero}}"]
for player in players:
    scores[player] = scores.get(player, 0) + 10
print(scores)

# %% [markdown]
# {{CONTEXT_TRACE_HINT_2}}
#
# עקבי אחרי המילונית ומשתנה הלולאה בכל איטרציה.
#
# | איטרציה | player        | scores.get(player, 0) | scores אחרי העדכון       |
# |---------|---------------|-----------------------|--------------------------|
# | 0       | -             | -                     | {}                       |
# | 1       | "{{hero}}"    | 0                     |                          |
# | 2       | "{{heroine}}" |                       |                          |
# | 3       | "{{hero}}"    |                       |                          |
#
# מה הפלט הסופי?

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{TRACE_3_TITLE}}
# {{CONTEXT_TRACE_3_NARRATIVE}}

# %%
data = {"a": 1, "b": 2, "c": 3}
total = 0
for key in data:
    if data[key] > 1:
        total = total + data[key]
print(f"Total: {total}")

# %% [markdown]
# {{CONTEXT_TRACE_HINT_3}}
#
# עקבי אחרי משתנה הלולאה, התנאי והסכום המצטבר.
#
# | איטרציה | key | data[key] | data[key] > 1 | total אחרי |
# |---------|-----|-----------|---------------|------------|
# | 0       | -   | -         | -             | 0          |
# | 1       | "a" | 1         | False         |            |
# | 2       | "b" |           |               |            |
# | 3       | "c" |           |               |            |
#
# מה הפלט הסופי?

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{TRACE_4_TITLE}}
# {{CONTEXT_TRACE_4_NARRATIVE}}

# %%
profiles = {
    "{{hero}}": {"level": 5},
    "{{heroine}}": {"level": 7}
}
for name in profiles:
    profiles[name]["level"] = profiles[name]["level"] + 1
print(profiles["{{hero}}"]["level"])
print(profiles["{{heroine}}"]["level"])

# %% [markdown]
# {{CONTEXT_TRACE_HINT_4}}
#
# עקבי אחרי השינויים במילוניות המקוננת.
#
# | איטרציה | name          | לפני העדכון              | אחרי העדכון              |
# |---------|---------------|--------------------------|--------------------------|
# | 0       | -             | {"{{hero}}": {"level": 5}, "{{heroine}}": {"level": 7}} | - |
# | 1       | "{{hero}}"    |                          |                          |
# | 2       | "{{heroine}}" |                          |                          |
#
# מה שני הערכים שמודפסים?

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
