# Exercise 2: Character Stats Tracker


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Create a hero dictionary:
    hero = {
        "name": "{{hero}}",
        "health": 100,
        "strength": 15,
        "defense": 10
    }
    # The hero takes 20 damage! Update health by subtracting 20
    # Print: "[name] now has [health] health!"
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Create a hero with health = 50
    # Use an if statement to check:
    # - If health > 75: print "[name] is feeling great!"
    # - If health > 25: print "[name] is hurt but fighting!"
    # - Otherwise: print "[name] is in danger!"
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Create two characters as dictionaries:
    # hero: name="{{hero}}", power=25
    # villain: name="{{villain}}", power=30
    # Compare their power levels and print who is stronger
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # Create a character dictionary
    # Ask the user "How much damage?" using input()
    # Subtract that from health (don't forget int()!)
    # Print the new health
    # Bonus: Make sure health doesn't go below 0!
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # Level up system!
    # Create a character with: name, level=1, xp=0
    # Add 150 XP to the character
    # If XP >= 100: increase level by 1 and subtract 100 from XP
    # Print: "[name] is now level [level]!"
    pass


def main():
    print("=== Exercise A: Taking Damage ===")
    exercise_a()

    print("\n=== Exercise B: Health Check ===")
    exercise_b()

    print("\n=== Exercise C: Power Comparison ===")
    exercise_c()

    print("\n=== Exercise D: Combat Damage ===")
    exercise_d()

    print("\n=== Exercise E: Level Up! ===")
    exercise_e()


main()
