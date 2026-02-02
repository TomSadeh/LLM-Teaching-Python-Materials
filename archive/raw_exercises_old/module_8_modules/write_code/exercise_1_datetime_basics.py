# Exercise 1: Working with Dates and Times

import datetime


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Get today's date using datetime.date.today()
    # Print: "Today is [date]"
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Get the current time using datetime.datetime.now()
    # Print just the hour and minute
    # Hint: now.hour and now.minute
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Create a specific date: September 1, 1991 (when {{hero}} started at {{school}}!)
    # Use datetime.date(year, month, day)
    # Print: "{{hero}} started school on [date]"
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # Calculate how many days until your next birthday!
    # 1. Create your birthday as a date this year
    # 2. Get today's date
    # 3. Subtract to get the difference
    # Hint: (birthday - today).days gives you the number of days
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # Create a countdown timer for a {{school}} event!
    # Pick a future date (like a tournament or festival)
    # Calculate days remaining
    # Print: "Only [days] days until the event!"
    pass


def exercise_f():
    # ✏️ YOUR CODE HERE ✏️
    # Day of the week checker!
    # Ask user for a year, month, and day
    # Create that date and print what day of the week it was
    # Hint: date.strftime("%A") gives the day name
    pass


def exercise_g():
    # ✏️ YOUR CODE HERE ✏️
    # Age calculator!
    # Ask for the user's birth year, month, and day
    # Calculate their exact age in years
    # Print: "You are [age] years old!"
    pass


def main():
    print("=== Exercise A: Today's Date ===")
    exercise_a()

    print("\n=== Exercise B: Current Time ===")
    exercise_b()

    print("\n=== Exercise C: Create a Date ===")
    exercise_c()

    print("\n=== Exercise D: Birthday Countdown ===")
    exercise_d()

    print("\n=== Exercise E: Event Countdown ===")
    exercise_e()

    print("\n=== Exercise F: Day of Week ===")
    exercise_f()

    print("\n=== Exercise G: Age Calculator ===")
    exercise_g()


main()
