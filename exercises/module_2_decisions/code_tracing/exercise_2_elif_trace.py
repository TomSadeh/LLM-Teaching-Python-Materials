# =============================================================================
# Code Tracing: if/elif/else Chains
# =============================================================================
# Difficulty: 3
# Concepts: if/elif/else, first match wins, order matters
# =============================================================================

# %% [markdown]
# {{CONTEXT_CODE_TRACING_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## {{TRACE_1_TITLE}}
# {{CONTEXT_TRACE_1_NARRATIVE}}
# רק ענף אחד מתבצע בשרשרת `if`/`elif`/`else`.

# %%
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"{{hero}}'s grade: {grade}")

# %% [markdown]
# {{CONTEXT_TRACE_HINT_1}}
#
# | תנאי | בדיקה | תוצאה |
# |------|-------|-------|
# | score >= 90 | 85 >= 90 | _____ |
# | score >= 80 | 85 >= 80 | _____ |
# | score >= 70 | (דולג כי ענף קודם התאים) | - |
# | else | (דולג כי ענף קודם התאים) | - |
#
# איזה ענף בוצע? _______________
# מה הערך של `grade`? _______________
# מה מודפס? _______________
#
# > רמז: ברגע שתנאי אחד הוא `True`, כל הענפים הבאים נדלגים!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{TRACE_2_TITLE}}
# {{CONTEXT_TRACE_2_NARRATIVE}}
# סדר התנאים חשוב!

# %%
temperature = 35
if temperature >= 30:
    status = "Hot"
elif temperature >= 20:
    status = "Warm"
elif temperature >= 10:
    status = "Cool"
else:
    status = "Cold"
print(f"Weather at {{location}}: {status}")

# %% [markdown]
# {{CONTEXT_TRACE_HINT_2}}
#
# | תנאי | בדיקה | תוצאה |
# |------|-------|-------|
# | temperature >= 30 | 35 >= 30 | _____ |
# | temperature >= 20 | (נבדק/נדלג?) | _____ |
# | temperature >= 10 | (נבדק/נדלג?) | _____ |
# | else | (נבדק/נדלג?) | _____ |
#
# מה הערך של `status`? _______________
# מה מודפס? _______________
#
# > רמז: 35 הוא גם >= 20 וגם >= 10, אבל אנחנו עוצרות בהתאמה הראשונה!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{TRACE_3_TITLE}}
# {{CONTEXT_TRACE_3_NARRATIVE}}
# עקבי אחרי הקוד כאשר אף `if`/`elif` לא מתאים (ו-`else` מתבצע).

# %%
level = 3
if level == 10:
    rank = "Master"
elif level == 7:
    rank = "Expert"
elif level == 5:
    rank = "Intermediate"
else:
    rank = "Beginner"
print(f"{{hero}}'s rank: {rank}")

# %% [markdown]
# {{CONTEXT_TRACE_HINT_3}}
#
# | תנאי | בדיקה | תוצאה |
# |------|-------|-------|
# | level == 10 | 3 == 10 | _____ |
# | level == 7 | 3 == 7 | _____ |
# | level == 5 | 3 == 5 | _____ |
# | else | (כל התנאים מעל היו False) | מתבצע |
#
# מה הערך של `rank`? _______________
# מה מודפס? _______________
#
# > רמז: `else` מתבצע רק אם כל תנאי ה-`if`/`elif` הם `False`.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{TRACE_4_TITLE}}
# {{CONTEXT_TRACE_4_NARRATIVE}}
# עקבי אחרי הקוד עם משתנים שמשתנים לפני הבדיקה.

# %%
gold = 100
gold = gold + 50  # {{hero}} finds treasure!
if gold >= 200:
    tier = "Rich"
elif gold >= 100:
    tier = "Comfortable"
elif gold >= 50:
    tier = "Modest"
else:
    tier = "Poor"
print(f"{{hero}} with {gold} gold: {tier}")

# %% [markdown]
# {{CONTEXT_TRACE_HINT_4}}
#
# | שלב | gold | פעולה |
# |-----|------|-------|
# | 1   | 100  | אתחול gold |
# | 2   | ___  | הוספת 50 ל-gold |
#
# עכשיו בדקי את התנאים עם gold = ___:
# | תנאי | בדיקה | תוצאה |
# |------|-------|-------|
# | gold >= 200 | ___ >= 200 | _____ |
# | gold >= 100 | ___ >= 100 | _____ |
# | (השאר נדלגים?) | | |
#
# מה הערך של `tier`? _______________
# מה מודפס? _______________

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
