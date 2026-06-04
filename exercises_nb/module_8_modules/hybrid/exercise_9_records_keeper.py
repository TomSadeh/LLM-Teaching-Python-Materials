# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
#
# This is a multi-part exercise where {{school}} needs to track
# {{creature}} sightings in a spreadsheet-style format using CSV.
#
# Programming concepts: CSV module, data processing, file I/O
# Difficulty: 3-4

# %%
import csv

# %%
from datetime import date

# %% [markdown]
# PART 1: Growth - Write Records to CSV
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Learn to create and write CSV files for record keeping.
#
# ✏️ YOUR CODE HERE ✏️
#
# Return a dict with:
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
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Define fieldnames:
#         fieldnames = ["date", "creature", "location", "observer", "notes"]
#
# Step 2: Open file and create DictWriter:
#         with open(filename, "w", newline="") as f:
#             writer = csv.DictWriter(f, fieldnames=fieldnames)
#
# Step 3: Write header and rows:
#             writer.writeheader()
#             writer.writerows(sightings)
#
# Step 4: Return count

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Check if file exists (for header decision)
#         import os
#         file_exists = os.path.exists(filename)
#
# Step 2: Open in append mode:
#         with open(filename, "a", newline="") as f:
#
# Step 3: Create writer and write:
#         fieldnames = ["date", "creature", "location", "observer", "notes"]
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         if not file_exists:
#             writer.writeheader()
#         writer.writerow(sighting)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 2: Growth - Read and Display CSV Data
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Learn to read and display CSV records.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Try to open and read with DictReader
#
# Step 2: Convert to list:
#         return list(reader)
#
# Step 3: Handle FileNotFoundError, return []

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Print header:
#         print(f"{'Date':<12} {'Creature':<15} {'Location':<15} {'Observer':<10}")
#         print("-" * 55)
#
# Step 2: Print each row:
#         for s in sightings:
#             print(f"{s['date']:<12} {s['creature']:<15} {s['location']:<15} {s['observer']:<10}")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Initialize counts dict
#
# Step 2: Loop through sightings:
#         for s in sightings:
#             creature = s["creature"]
#             counts[creature] = counts.get(creature, 0) + 1
#
# Step 3: Return counts

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 3: Growth - Complete Search and Filter Functions
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Add search and filter capabilities.
#
# ✏️ COMPLETE THIS FUNCTION ✏️
#
# {{CONTEXT_FUNCTION_HINT_3}}
#
# Step 1: Initialize matches list
#
# Step 2: For each sighting, check if search_term is in any field:
#         search_lower = search_term.lower()
#         for s in sightings:
#             for value in s.values():
#                 if search_lower in str(value).lower():
#                     matches.append(s)
#                     break
#
# Step 3: Return matches

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Return sightings where location matches (case-insensitive)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Compare date strings (YYYY-MM-DD format sorts correctly!)
# for s in sightings:
#     if start_date <= s["date"] <= end_date:
#         matches.append(s)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 4: Growth - Generate Reports
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Generate summary reports from the data.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Count total sightings
#
# Step 2: Count by creature type
#
# Step 3: Find unique locations
#
# Step 4: Build report string:
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
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Generate report
#
# Step 2: Write to file

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## MAIN

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
