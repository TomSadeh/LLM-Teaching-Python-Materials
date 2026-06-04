# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
#
# זוהי תרגילה מרובת-חלקים שבה תבני מערכת לוח זמנים
# עבור {{school}} באמצעות מודול `datetime`. {{mentor}} צריכה עזרה
# בארגון אירועים ותאריכי יעד.
#
# מושגי תכנות: מודול `datetime`, חישובי תאריכים, עיצוב תאריכים
# רמת קושי: 2-3

# %%
from datetime import date, datetime, timedelta

# %% [markdown]
# ## חלק 1: צמיחה - יצירה ועיצוב תאריכים
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# התחילי ללמוד ליצור תאריכים ולעצב אותם בצורה יפה.
#
# 1. צרי תאריך באמצעות: `date(year, month, day)`
# 2. החזירי את התאריך

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. בדקי את הפרמטר `style`
# 2. אם `"long"`, השתמשי ב-`strftime("%B %d, %Y")`
# 3. אם `"short"`, השתמשי ב-`strftime("%m/%d/%y")`
# 4. אם `"iso"`, השתמשי ב-`strftime("%Y-%m-%d")`
# 5. החזירי את המחרוזת המעוצבת

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# השתמשי ב-`strftime("%A")` כדי לקבל את שם היום המלא

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: צמיחה - חישוב תאריכי יעד והפרשים
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# למדי לחשב תאריכים עתידיים והפרשי זמן.
#
# 1. צרי `timedelta`: `delta = timedelta(days=days_from_now)`
# 2. הוסיפי ל-`start_date`: `deadline = start_date + delta`
# 3. החזירי את תאריך היעד

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. חסרי תאריכים: `difference = date2 - date1`
# 2. קבלי את הימים: `difference.days`
# 3. השתמשי ב-`abs()` לקבלת ערך מוחלט (במקרה ש-`date1 > date2`)
# 4. החזירי את התוצאה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. קבלי את היום הנוכחי: `today = date.today()`
# 2. חשבי: `(target_date - today).days`
# 3. החזירי את התוצאה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: צמיחה - בניית מתזמן אירועים
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# שלבי את הכל למערכת תזמון שלמה.
#
# 1. צרי מילון עם:
#    - `"name"`: name
#    - `"date"`: event_date
#    - `"description"`: description
#    - `"day_of_week"`: `get_day_of_week(event_date)`
#    - `"formatted_date"`: `format_event_date(event_date, "long")`
#    - `"days_away"`: `days_until(event_date)`
#
# 2. החזירי את המילון

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# הדפיסי את האירוע בפורמט יפה:
# `"[name]"`
# `"  Date: [formatted_date] ([day_of_week])"`
# `"  [days_away] days away"`
# `"  Description: [description]"` (רק אם לא ריק)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# השתמשי ב-`sorted()` עם פונקציית מפתח:
# `sorted(events, key=lambda e: e["date"])`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## ראשי

# %%
print("=" * 60)
print("{{CONTEXT_PROJECT_INTRO}}")
print("Event Scheduler for {{school}}")
print("=" * 60)
print()

print(">>> PART 1: Creating and Formatting Dates")
print("-" * 40)
# Uncomment to test:
# test_date = create_event_date(2024, 12, 25)
# print(f"Long format: {format_event_date(test_date, 'long')}")
# print(f"Short format: {format_event_date(test_date, 'short')}")
# print(f"ISO format: {format_event_date(test_date, 'iso')}")
# print(f"Day of week: {get_day_of_week(test_date)}")
print()

print(">>> PART 2: Calculating Deadlines")
print("-" * 40)
# Uncomment to test:
# today = date.today()
# deadline = calculate_deadline(today, 30)
# print(f"Today: {today}")
# print(f"30-day deadline: {deadline}")
# print(f"Days between: {days_between(today, deadline)}")
# end_of_year = date(today.year, 12, 31)
# print(f"Days until end of year: {days_until(end_of_year)}")
print()

print(">>> PART 3: Event Scheduler")
print("-" * 40)
# Uncomment to test:
# events = [
#     create_event("Midterm Exam", date(2024, 10, 15), "Study hard!"),
#     create_event("Project Due", date(2024, 10, 1)),
#     create_event("Final Exam", date(2024, 12, 15), "Cumulative"),
# ]
# print("Upcoming Events:")
# for event in sort_events_by_date(events):
#     display_event(event)
#     print()
print()

print("=" * 60)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
print("=" * 60)
