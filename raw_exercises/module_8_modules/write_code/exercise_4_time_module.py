# Exercise 4: The Time Module (Delays, Timers, and More!)

import time


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Use time.sleep() to create a dramatic pause!
    # Print "3..."
    # Wait 1 second
    # Print "2..."
    # Wait 1 second
    # Print "1..."
    # Wait 1 second
    # Print "{{spell3}}!"
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Create a typing effect!
    # Print a message one character at a time with a small delay
    # Hint: for char in message: print(char, end="", flush=True); time.sleep(0.05)
    message = "{{greeting}}"
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Measure how long something takes!
    # start = time.time()
    # ... do something ...
    # end = time.time()
    # elapsed = end - start
    #
    # Calculate how long it takes to count to 1 million
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # Reaction time game!
    # 1. Print "Get ready..."
    # 2. Wait a random amount of time (2-5 seconds)
    # 3. Print "GO!"
    # 4. Measure how fast they press Enter
    # 5. Print their reaction time
    #
    # Hint: You'll need 'import random' too!
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # Create a simple timer!
    # Ask user how many seconds to wait
    # Show countdown (update every second)
    # Print "Time's up!" at the end
    pass


def exercise_f():
    # ✏️ YOUR CODE HERE ✏️
    # Speed typing challenge!
    # 1. Show a phrase to type: "The quick {{creature}} jumped over {{location}}"
    # 2. Start timer when they press Enter
    # 3. Time how long it takes them to type it
    # 4. Check if they typed it correctly
    # 5. Calculate words per minute (WPM)
    # WPM = (number of characters / 5) / (time in minutes)
    pass


def dramatic_story():
    # ✏️ YOUR CODE HERE ✏️
    # Tell a short story with dramatic pauses!
    # Use time.sleep() for tension
    # Use the typing effect for dialogue
    #
    # Example:
    # "{{hero}} walked into {{location}}..."
    # (pause)
    # "Suddenly, a {{creature}} appeared!"
    # (longer pause)
    # "{{hero}}: '{{spell2}}!'"
    pass


def main():
    print("=== Exercise A: Countdown ===")
    exercise_a()

    print("\n=== Exercise B: Typing Effect ===")
    exercise_b()

    print("\n=== Exercise C: Timing Code ===")
    exercise_c()

    print("\n=== Exercise D: Reaction Game ===")
    exercise_d()

    print("\n=== Exercise E: Timer ===")
    exercise_e()

    print("\n=== Exercise F: Speed Typing ===")
    exercise_f()

    print("\n=== Dramatic Story ===")
    dramatic_story()


main()
