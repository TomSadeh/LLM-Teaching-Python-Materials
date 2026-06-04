# =============================================================================
# Fill in the Blanks: Accumulator Pattern
# =============================================================================
# Difficulty: 4
# Concepts: accumulator variables, running totals, loop-based calculations
# =============================================================================

# %% [markdown]
# {{CONTEXT_FILL_BLANKS_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# ## {{EXERCISE_1_TITLE}}
# {{CONTEXT_EXERCISE_1_NARRATIVE}}
#
# חשבי את סכום המספרים 1 עד 5 עבור {{hero}}.
#
# > רמז: אתחלי את המצבר לערך 0 לפני הלולאה.
#
# ```python
# total = ___                         # התחילי מאפס
# for num in range(1, 6):
#     total = total ___ num           # הוסיפי כל מספר
# print("Sum:", total)                # צריך להדפיס 15
# ```

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{EXERCISE_2_TITLE}}
# {{CONTEXT_EXERCISE_2_NARRATIVE}}
#
# ספרי אחורה ועקבי אחר המרחק הכולל ב-{{school}}.
#
# > רמז: כל צעד מתווסף אל `total_distance`.
#
# ```python
# total_distance = 0
# for step in range(1, 5):
#     distance = step * 10
#     total_distance = ___ + distance  # הוסיפי למצבר
# print("Total distance:", ___)        # הדפיסי את התוצאה
# ```

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{EXERCISE_3_TITLE}}
# {{CONTEXT_EXERCISE_3_NARRATIVE}}
#
# בני משפט על ידי הוספת מילים עבור {{creature}}.
#
# > רמז: גם מחרוזות אפשר לצבור! התחילי עם מחרוזת ריקה `""`.
#
# ```python
# message = ___                        # התחילי עם מחרוזת ריקה
# for i in range(3):
#     message = message ___ "Go! "     # הוסיפי "Go! " בכל פעם
# print(message)                       # צריך להדפיס "Go! Go! Go! "
# ```

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{EXERCISE_4_TITLE}}
# {{CONTEXT_EXERCISE_4_NARRATIVE}}
#
# חשבי את סך הפניות לצייר ב-{{location}}.
# כשמציירים צורה, עקבי אחר סך המעלות שפנית.
#
# ```python
# total_turns = ___                    # אתחלי את המצבר
# for side in range(4):
#     turn_amount = 90
#     total_turns = total_turns + ___  # הוסיפי את כמות הפנייה
# print("Total turned:", total_turns, "degrees")  # צריך להיות 360
# ```

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{EXERCISE_5_TITLE}}
# {{CONTEXT_EXERCISE_5_NARRATIVE}}
#
# חשבי את אורך הקו הכולל במסלול של {{hero}}.
# הקווים גדלים: 10, 20, 30, 40, 50 יחידות.
#
# ```python
# total_length = 0
# ___ i in range(1, 6):               # מלאי את מילת המפתח של הלולאה
#     line_length = i ___ 10          # חשבי: i כפול 10
#     total_length = total_length + line_length
# print("Total length:", ___)         # הדפיסי את המצבר
# ```

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_FILL_BLANKS_INTRO}}")
print("=" * 50)

print("\n=== {{EXERCISE_1_TITLE}} ===")
# exercise_a()  # Uncomment when you've filled the blanks

print("\n=== {{EXERCISE_2_TITLE}} ===")
# exercise_b()

print("\n=== {{EXERCISE_3_TITLE}} ===")
# exercise_c()

print("\n=== {{EXERCISE_4_TITLE}} ===")
# exercise_d()

print("\n=== {{EXERCISE_5_TITLE}} ===")
# exercise_e()

print("\nFill in all the blanks, then uncomment to test!")
print("{{CONTEXT_ROLE_COMPLETE}}")
