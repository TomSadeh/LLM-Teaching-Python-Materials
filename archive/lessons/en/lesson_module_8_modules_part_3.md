# Lesson: Using Modules - Part 3: The Datetime Module

> **Module**: module_8_modules
> **Part**: 3 of 6
> **Difficulty**: 3
> **Duration**: 5-6 minutes

---

## Learning Objective

By the end of this part, the student will be able to:

- Use the datetime module to work with dates and times

---

## Key Concepts

| Concept | One-sentence explanation |
|---------|--------------------------|
| `datetime.datetime.now()` | Returns the current date and time |
| `datetime.date.today()` | Returns just today's date (simpler than datetime) |
| `.strftime()` | Formats a datetime object into a readable string |
| `timedelta` | Represents a duration (difference between two dates/times) |

---

## Lesson Content

### Building on Part 2

We've practiced with random - now let's learn a completely new module. The datetime module helps us work with dates and times.

### Getting the Current Date and Time

```python
import datetime

# Current date and time
now = datetime.datetime.now()
print(now)  # 2024-01-15 14:30:45.123456

# Just today's date (simpler)
today = datetime.date.today()
print(today)  # 2024-01-15
```

### Formatting Dates

Use `.strftime()` to create nice-looking date strings:

```python
import datetime

now = datetime.datetime.now()

# Common format codes:
# %Y = year (2024)
# %m = month (01-12)
# %d = day (01-31)
# %H = hour (00-23)
# %M = minute (00-59)

formatted = now.strftime("%Y-%m-%d")  # "2024-01-15"
nice = now.strftime("%B %d, %Y")      # "January 15, 2024"
```

### Calculating Time Differences

```python
import datetime

today = datetime.date.today()
birthday = datetime.date(2024, 12, 25)  # Year, Month, Day

days_until = birthday - today
print(f"Days until birthday: {days_until.days}")
```

### Watch For

- The double datetime: `datetime.datetime` (module name is same as class name)
- Alternative: `from datetime import datetime` then just use `datetime.now()`

---

## Practice Exercises

| Exercise | Notes |
|----------|-------|
| exercise_1_datetime | Practical date handling - getting and formatting current time |
| exercise_7_time_calculator | Calculate time differences between dates |

---

## Checkpoint

Ask: "How do you get the current date and time?"
Expected: `datetime.datetime.now()` or `from datetime import datetime` then `datetime.now()`

---

## If the Student Struggles

- **If datetime.datetime is confusing**: Use `from datetime import datetime` to simplify, or start with `datetime.date.today()` for date-only operations
- **If strftime codes are overwhelming**: Start with just `%Y-%m-%d` - they can look up others as needed
