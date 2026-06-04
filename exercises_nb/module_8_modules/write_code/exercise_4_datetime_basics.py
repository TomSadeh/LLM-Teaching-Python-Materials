# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי לעבוד עם תאריכים ושעות באמצעות
# המודול `datetime` של Python. זה שימושי מאוד לתזמון, לוגים,
# וכל דבר שקשור לזמן.
#
# Topic: datetime module basics
# Difficulty: 2

# %%
from datetime import date, datetime, timedelta

# %% [markdown]
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# למדי ליצור תאריכים ולהדפיס אותם.
#
# 1. קבלי את תאריך היום: `today = date.today()`
# 2. צרי תאריך ספציפי:
#    `special_date = date(2024, 12, 25)`
#    זה יוצר את ה-25 בדצמבר 2024
# 3. הדפיסי את התאריכים:
#    `"Today is: [today]"`
#    `"Special date: [special_date]"`
# 4. גשי לחלקים הנפרדים של התאריך:
#    `print(f"Year: {today.year}")`
#    `print(f"Month: {today.month}")`
#    `print(f"Day: {today.day}")`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# למדי לעצב תאריכים בדרכים שונות.
#
# 1. קבלי את תאריך היום
# 2. עצבי באמצעות `strftime()`:
#    - `format1 = today.strftime("%Y-%m-%d")`    # 2024-01-15
#    - `format2 = today.strftime("%d/%m/%Y")`    # 15/01/2024
#    - `format3 = today.strftime("%B %d, %Y")`   # January 15, 2024
#    - `format4 = today.strftime("%A")`          # Monday
# 3. הדפיסי כל פורמט עם תווית:
#    `"ISO format: [format1]"`
#    `"EU format: [format2]"`
#    `"Long format: [format3]"`
#    `"Day name: [format4]"`
#
# > רמז: קודי עיצוב נפוצים:
# > `%Y` = שנה ב-4 ספרות, `%m` = חודש, `%d` = יום
# > `%B` = שם החודש המלא, `%A` = שם היום המלא
# > `%H` = שעה, `%M` = דקה, `%S` = שנייה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# למדי חשבון תאריכים לצורך תזמון ב-{{school}}.
#
# 1. קבלי את תאריך היום
# 2. צרי מרווחי זמן (משכים):
#    `one_week = timedelta(days=7)`
#    `one_month = timedelta(days=30)`
# 3. חשבי תאריכים עתידיים:
#    `next_week = today + one_week`
#    `next_month = today + one_month`
# 4. חשבי תאריכים שעברו:
#    `last_week = today - one_week`
# 5. חשבי כמה ימים בין שני תאריכים:
#    `end_of_year = date(today.year, 12, 31)`
#    `days_left = end_of_year - today`
#    `print(f"Days until end of year: {days_left.days}")`
# 6. הדפיסי את כל התאריכים שחישבת

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

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
