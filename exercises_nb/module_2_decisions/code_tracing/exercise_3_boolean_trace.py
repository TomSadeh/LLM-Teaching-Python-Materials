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
# האופרטור `and`: שני התנאים חייבים להיות `True`.

# %%
level = 10
gold = 150
if level >= 5 and gold >= 100:
    print("{{hero}} can enter {{danger_location}}!")
else:
    print("{{hero}} cannot enter yet.")

# %% [markdown]
# {{CONTEXT_TRACE_HINT_1}}
#
# | תנאי | בדיקה | תוצאה |
# |-----------|-------|--------|
# | `level >= 5` | `10 >= 5` | _____ |
# | `gold >= 100` | `150 >= 100` | _____ |
# | שילוב (`and`) | _____ `and` _____ | _____ |
#
# איזה ענף מתבצע? _______________
# מה מודפס? _______________
#
# זכרי: `and` אומר שהשניים חייבים להיות `True`!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{TRACE_2_TITLE}}
# {{CONTEXT_TRACE_2_NARRATIVE}}
# האופרטור `or`: לפחות אחד מהתנאים חייב להיות `True`.

# %%
has_key = False
has_password = True
if has_key or has_password:
    print("{{hero}} opens the door to {{location}}!")
else:
    print("The door remains locked.")

# %% [markdown]
# {{CONTEXT_TRACE_HINT_2}}
#
# | תנאי | ערך | תוצאה |
# |-----------|-------|--------|
# | `has_key` | `False` | `False` |
# | `has_password` | `True` | `True` |
# | שילוב (`or`) | `False or True` | _____ |
#
# איזה ענף מתבצע? _______________
# מה מודפס? _______________
#
# זכרי: `or` אומר שלפחות אחד חייב להיות `True`!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{TRACE_3_TITLE}}
# {{CONTEXT_TRACE_3_NARRATIVE}}
# האופרטור `not`: הופך `True` ל-`False` ו-`False` ל-`True`.

# %%
is_raining = False
if not is_raining:
    print("{{hero}} goes outside to train.")
else:
    print("{{hero}} stays inside.")

# %% [markdown]
# {{CONTEXT_TRACE_HINT_3}}
#
# | משתנה | ערך |
# |----------|-------|
# | `is_raining` | `False` |
# | `not is_raining` | _____ |
#
# איזה ענף מתבצע? _______________
# מה מודפס? _______________
#
# זכרי: `not` הופך את הערך הבוליאני!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{TRACE_4_TITLE}}
# {{CONTEXT_TRACE_4_NARRATIVE}}
# שילוב של מספר אופרטורים יחד.

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
# {{CONTEXT_TRACE_HINT_4}}
#
# בדיקה 1: `health < 50 and has_item`
# | תנאי | בדיקה | תוצאה |
# |-----------|-------|--------|
# | `health < 50` | `80 < 50` | _____ |
# | `has_item` | `True` | `True` |
# | שילוב (`and`) | _____ `and True` | _____ |
#
# הענף הראשון מתבצע? _____
#
# בדיקה 2: `health >= 50 or not enemy_nearby`
# | תנאי | בדיקה | תוצאה |
# |-----------|-------|--------|
# | `health >= 50` | `80 >= 50` | _____ |
# | `enemy_nearby` | `True` | `True` |
# | `not enemy_nearby` | `not True` | _____ |
# | שילוב (`or`) | _____ `or` _____ | _____ |
#
# הענף השני מתבצע? _____
#
# מה מודפס? _______________

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{TRACE_5_TITLE}}
# {{CONTEXT_TRACE_5_NARRATIVE}}
# ל-`and` יש עדיפות גבוהה יותר מ-`or`.

# %%
a = True
b = False
c = True
# Without parentheses, 'and' is evaluated first
result = a or b and c
print(f"Result: {result}")

# %% [markdown]
# זה שווה ל: `a or (b and c)`
# ולא ל: `(a or b) and c`
#
# {{CONTEXT_TRACE_HINT_5}}
#
# הביטוי: `a or b and c`
# ערכים: `True or False and True`
#
# 1. מחשבים את `and` קודם (עדיפות גבוהה יותר):
# `b and c` = `False and True` = _____
#
# 2. אחר כך מחשבים את `or`:
# `a or (תוצאה משלב 1)` = `True or` _____ = _____
#
# תוצאה סופית: _____
# מה מודפס? _______________
#
# אם היה כתוב `(a or b) and c`:
# `(True or False) and True` = _____ `and True` = _____

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
