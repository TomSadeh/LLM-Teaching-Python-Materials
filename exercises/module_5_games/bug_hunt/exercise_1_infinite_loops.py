# %% [markdown]
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_MISSION}}
#
# נושא: מציאת באגים של לולאות אינסופיות
# רמת קושי: 1-2
#
# לולאות אינסופיות הן אחד הבאגים הנפוצים ביותר כשלומדים לולאות `while`.
# בתרגיל הזה תמצאי ותתקני לולאות שלא נגמרות.
#
# {{CASE_1_TITLE}}
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# {{hero}} כתבה את הקוד הזה כדי לספור פריטים, אבל הוא רץ לנצח!
#
# התנהגות צפויה:
# הדפסת המספרים 1 עד 5, ואז עצירה
#
# מה שקורה בפועל:
# מדפיסה 1 לנצח, בלי לעצור
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

# %%
count = 1
while count <= 5:
    print(count)

# %% [markdown]
# ## המונה לא משתנה! הלולאה רצה לנצח.
#
# מה מצאתי: ________________________________
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{CASE_2_TITLE}}
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# הספירה לאחור הזו אמורה ללכת מ-5 עד 1, אבל משהו השתבש.
#
# התנהגות צפויה:
# הדפסת 5, 4, 3, 2, 1, `"Done!"`
#
# מה שקורה בפועל:
# סופרת בכיוון הלא נכון ולא מגיעה לעולם ל-0
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}

# %%
num = 5
while num > 0:
    print(num)
    num += 1  # Oops! Going the wrong way!

# %% [markdown]
# מה מצאתי: ________________________________
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{CASE_3_TITLE}}
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# הלולאה הזו אמורה לעבד רשימה, אבל היא לא מסתיימת.
#
# התנהגות צפויה:
# עיבוד כל פריט ועצירה כשהרשימה מתרוקנת
#
# מה שקורה בפועל:
# הרשימה לא מתקצרת אף פעם
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}

# %%
items = ["{{item}}", "{{pet}}", "{{creature}}"]
index = 0
while index < len(items):
    print(f"Processing: {items[index]}")

# %% [markdown]
# ## שכחנו לעבור לפריט הבא!
#
# מה מצאתי: ________________________________
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{CASE_4_TITLE}}
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# המצבר הזה אמור לחבר מספרים, אבל הוא לולא לנצח.
#
# התנהגות צפויה:
# הוספת מספרים עד שהסכום עולה על 20, ואז עצירה
#
# מה שקורה בפועל:
# הסכום לא משתנה, התנאי לא הופך ל-`False` אף פעם
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}

# %%
total = 0
amount = 5
while total < 20:
    print(f"Adding {amount}, total would be {total + amount}")

# %% [markdown]
# ## `total + amount` לא שומר את התוצאה!
#
# מה מצאתי: ________________________________
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_INVESTIGATION_INTRO}}")
print("=" * 50)

print("\n=== {{CASE_1_TITLE}} ===")
print("Buggy version (DON'T RUN - infinite loop):")
print("# buggy_counter()")
print("\nFixed version:")
fix_counter()

print("\n=== {{CASE_2_TITLE}} ===")
print("Buggy version (DON'T RUN - infinite loop):")
print("# buggy_countdown()")
print("\nFixed version:")
fix_countdown()

print("\n=== {{CASE_3_TITLE}} ===")
print("Buggy version (DON'T RUN - infinite loop):")
print("# buggy_list_processor()")
print("\nFixed version:")
fix_list_processor()

print("\n=== {{CASE_4_TITLE}} ===")
print("Buggy version (DON'T RUN - infinite loop):")
print("# buggy_accumulator()")
print("\nFixed version:")
fix_accumulator()

print("\n" + "=" * 50)
print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
