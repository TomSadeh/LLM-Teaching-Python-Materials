"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn to work with dates and times using
Python's datetime module. This is essential for scheduling, logging,
and any time-based features.

Topic: datetime module basics
Difficulty: 2
"""

from datetime import date, datetime, timedelta


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Learn to create and format dates.
    #
    # Step 1: Get today's date using: today = date.today()
    #
    # Step 2: Create a specific date:
    #         special_date = date(2024, 12, 25)
    #         This creates December 25, 2024
    #
    # Step 3: Print the dates:
    #         "Today is: [today]"
    #         "Special date: [special_date]"
    #
    # Step 4: Access individual parts:
    #         print(f"Year: {today.year}")
    #         print(f"Month: {today.month}")
    #         print(f"Day: {today.day}")
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Learn to format dates in different ways.
    #
    # Step 1: Get today's date
    #
    # Step 2: Format using strftime():
    #         - format1 = today.strftime("%Y-%m-%d")    # 2024-01-15
    #         - format2 = today.strftime("%d/%m/%Y")    # 15/01/2024
    #         - format3 = today.strftime("%B %d, %Y")   # January 15, 2024
    #         - format4 = today.strftime("%A")          # Monday
    #
    # Step 3: Print each format with a label:
    #         "ISO format: [format1]"
    #         "EU format: [format2]"
    #         "Long format: [format3]"
    #         "Day name: [format4]"
    #
    # Common format codes:
    #   %Y = 4-digit year, %m = month, %d = day
    #   %B = full month name, %A = full day name
    #   %H = hour, %M = minute, %S = second
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Learn date arithmetic for {{school}} scheduling.
    #
    # Step 1: Get today's date
    #
    # Step 2: Create time deltas (durations):
    #         one_week = timedelta(days=7)
    #         one_month = timedelta(days=30)
    #
    # Step 3: Calculate future dates:
    #         next_week = today + one_week
    #         next_month = today + one_month
    #
    # Step 4: Calculate past dates:
    #         last_week = today - one_week
    #
    # Step 5: Calculate days between two dates:
    #         end_of_year = date(today.year, 12, 31)
    #         days_left = end_of_year - today
    #         print(f"Days until end of year: {days_left.days}")
    #
    # Step 6: Print all your calculated dates
    pass


def main():
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


main()
