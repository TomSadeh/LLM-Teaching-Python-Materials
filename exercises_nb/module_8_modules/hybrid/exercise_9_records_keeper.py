# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
#
# בתרגיל הזה ב-{{school}} צריך לעקוב אחרי
# תיעוד ראיות של {{creature}} בפורמט גיליון אלקטרוני באמצעות CSV.
#
# מושגי תכנות: מודול `csv`, עיבוד נתונים, קלט/פלט לקובץ
# רמת קושי: 3-4

# %%
import csv

# %%
from datetime import date

# %% [markdown]
# ## חלק 1: צמיחה - כתיבת רשומות לקובץ CSV
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# למדי ליצור ולכתוב קבצי CSV לשמירת רשומות.
#
# החזירי מילון עם השדות הבאים:
# {
#     "date": str(date.today()),  # Current date as string
#     "creature": creature_name,
#     "location": location,
#     "observer": observer,
#     "notes": notes
# }

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#
# 1. הגדירי את שמות השדות:
#         fieldnames = ["date", "creature", "location", "observer", "notes"]
#
# 2. פתחי קובץ וצרי `DictWriter`:
#         with open(filename, "w", newline="") as f:
#             writer = csv.DictWriter(f, fieldnames=fieldnames)
#
# 3. כתבי כותרת ושורות:
#             writer.writeheader()
#             writer.writerows(sightings)
#
# 4. החזירי את הספירה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#
# 1. בדקי אם הקובץ קיים (כדי להחליט אם לכתוב כותרת):
#         import os
#         file_exists = os.path.exists(filename)
#
# 2. פתחי במצב הוספה:
#         with open(filename, "a", newline="") as f:
#
# 3. צרי writer וכתבי:
#         fieldnames = ["date", "creature", "location", "observer", "notes"]
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         if not file_exists:
#             writer.writeheader()
#         writer.writerow(sighting)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: צמיחה - קריאה והצגת נתוני CSV
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# למדי לקרוא ולהציג רשומות CSV.
#
# 1. נסי לפתוח ולקרוא עם `DictReader`
#
# 2. המירי לרשימה:
#         return list(reader)
#
# 3. טפלי ב-`FileNotFoundError`, החזירי `[]`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#
# 1. הדפיסי כותרת:
#         print(f"{'Date':<12} {'Creature':<15} {'Location':<15} {'Observer':<10}")
#         print("-" * 55)
#
# 2. הדפיסי כל שורה:
#         for s in sightings:
#             print(f"{s['date']:<12} {s['creature']:<15} {s['location']:<15} {s['observer']:<10}")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#
# 1. אתחלי מילון ספירות
#
# 2. עברי על הראיות בלולאה:
#         for s in sightings:
#             creature = s["creature"]
#             counts[creature] = counts.get(creature, 0) + 1
#
# 3. החזירי את הספירות

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: צמיחה - פונקציות חיפוש וסינון
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# הוסיפי יכולות חיפוש וסינון.
#
# {{CONTEXT_FUNCTION_HINT_3}}
#
# 1. אתחלי רשימת התאמות
#
# 2. לכל ראיה, בדקי אם מונח החיפוש מופיע באחד השדות:
#         search_lower = search_term.lower()
#         for s in sightings:
#             for value in s.values():
#                 if search_lower in str(value).lower():
#                     matches.append(s)
#                     break
#
# 3. החזירי את ההתאמות

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#
# החזירי ראיות שבהן המיקום תואם (ללא תלות בגודל אות)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#
# השוואת מחרוזות תאריך (פורמט `YYYY-MM-DD` ממוין נכון!)
# for s in sightings:
#     if start_date <= s["date"] <= end_date:
#         matches.append(s)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 4: צמיחה - יצירת דוחות
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# צרי דוחות סיכום מהנתונים.
#
# 1. ספרי את סך הראיות
#
# 2. ספרי לפי סוג יצור
#
# 3. מצאי מיקומים ייחודיים
#
# 4. בני מחרוזת דוח:
#         report = []
#         report.append("=" * 40)
#         report.append("SIGHTING SUMMARY REPORT")
#         report.append("=" * 40)
#         report.append(f"Total Sightings: {total}")
#         report.append("")
#         report.append("By Creature:")
#         for creature, count in counts.items():
#             report.append(f"  {creature}: {count}")
#         ...
#         return "\n".join(report)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#
# 1. צרי דוח
#
# 2. כתבי לקובץ

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## ראשי

# %%
print("=" * 60)
print("{{CONTEXT_PROJECT_INTRO}}")
print("{{creature}} Sighting Records for {{school}}")
print("=" * 60)
print()

# Sample data for testing
sample_sightings = [
    create_sighting_record("{{creature}}", "{{location}}", "{{hero}}", "Very rare!"),
    create_sighting_record("phoenix", "tower", "{{heroine}}", ""),
    create_sighting_record("{{creature}}", "forest", "{{friend}}", "Spotted at dawn"),
    create_sighting_record("unicorn", "lake", "{{hero}}", "Drinking water"),
    create_sighting_record("phoenix", "{{location}}", "{{mentor}}", "Teaching flight"),
] if all([create_sighting_record]) else []

print(">>> PART 1: Writing Records")
print("-" * 40)
# Uncomment to test:
# count = save_sightings("sightings.csv", sample_sightings)
# print(f"Saved {count} sightings to CSV")
# new_sighting = create_sighting_record("dragon", "mountain", "{{hero}}")
# append_sighting("sightings.csv", new_sighting)
# print("Appended new sighting")
print()

print(">>> PART 2: Reading and Displaying")
print("-" * 40)
# Uncomment to test:
# sightings = load_sightings("sightings.csv")
# print(f"Loaded {len(sightings)} sightings")
# display_sightings(sightings)
# print()
# counts = count_by_creature(sightings)
# print(f"Counts by creature: {counts}")
print()

print(">>> PART 3: Search and Filter")
print("-" * 40)
# Uncomment to test:
# matches = search_sightings(sightings, "{{hero}}")
# print(f"Sightings by {{hero}}: {len(matches)}")
# by_location = filter_by_location(sightings, "{{location}}")
# print(f"Sightings at {{location}}: {len(by_location)}")
print()

print(">>> PART 4: Reports")
print("-" * 40)
# Uncomment to test:
# report = generate_summary_report(sightings)
# print(report)
# export_summary_to_file(sightings, "sighting_report.txt")
print()

print("=" * 60)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
print("=" * 60)
