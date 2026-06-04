# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
#
# This is a multi-part exercise where you build a scheduling system
# for {{school}} using the datetime module. {{mentor}} needs help
# organizing events and deadlines.
#
# Programming concepts: datetime module, date arithmetic, formatting
# Difficulty: 2-3

# %%
from datetime import date, datetime, timedelta

# %% [markdown]
# PART 1: Growth - Create and Format Dates
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Start by learning to create dates and format them nicely.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Create a date using: date(year, month, day)
# Step 2: Return the date

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Check the style parameter
# Step 2: If "long", use strftime("%B %d, %Y")
# Step 3: If "short", use strftime("%m/%d/%y")
# Step 4: If "iso", use strftime("%Y-%m-%d")
# Step 5: Return the formatted string

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Use strftime("%A") to get the full day name

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 2: Growth - Calculate Deadlines and Differences
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Learn to calculate future dates and time differences.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Create a timedelta: delta = timedelta(days=days_from_now)
# Step 2: Add to start_date: deadline = start_date + delta
# Step 3: Return the deadline

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Subtract dates: difference = date2 - date1
# Step 2: Get the days: difference.days
# Step 3: Use abs() to get absolute value (in case date1 > date2)
# Step 4: Return the result

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Get today: today = date.today()
# Step 2: Calculate: (target_date - today).days
# Step 3: Return the result

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# PART 3: Growth - Build Event Scheduler
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Combine everything into a complete scheduling system.
#
# ✏️ YOUR CODE HERE ✏️
#
# Step 1: Create a dictionary with:
#         - "name": name
#         - "date": event_date
#         - "description": description
#         - "day_of_week": get_day_of_week(event_date)
#         - "formatted_date": format_event_date(event_date, "long")
#         - "days_away": days_until(event_date)
#
# Step 2: Return the dictionary

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Print the event in a nice format:
# "[name]"
# "  Date: [formatted_date] ([day_of_week])"
# "  [days_away] days away"
# "  Description: [description]" (if not empty)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ✏️ YOUR CODE HERE ✏️
#
# Use sorted() with a key function:
# sorted(events, key=lambda e: e["date"])

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## MAIN

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
