# Exercise 4: Nested Dictionaries (Dictionaries inside Dictionaries!)


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Create a character with nested stats:
    character = {
        "name": "{{hero}}",
        "stats": {
            "health": 100,
            "mana": 50,
            "strength": 15
        },
        "house": "{{house}}"
    }
    # Print the character's health (it's inside "stats"!)
    # Hint: character["stats"]["health"]
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Create a school dictionary with different houses and their points:
    school = {
        "{{house}}": {"points": 472, "members": 40},
        "{{house}}": {"points": 450, "members": 38}
    }
    # Add 10 points to {{house}}
    # Print: "{{house}} now has [points] points!"
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Create a dictionary of spells, each with name, power, and type:
    spells = {
        "light": {"name": "{{spell1}}", "power": 10, "type": "utility"},
        "defense": {"name": "{{spell2}}", "power": 25, "type": "combat"},
        "guardian": {"name": "{{spell3}}", "power": 50, "type": "advanced"}
    }
    # Loop through and print only combat-type spells
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # Team roster! Create a dictionary where each member has:
    # - name, role, and skill_level
    team = {
        "leader": {"name": "{{hero}}", "role": "seeker", "skill": 9},
        "friend": {"name": "{{friend}}", "role": "keeper", "skill": 7}
    }
    # Add a new member with position "chaser"
    # Print the whole team
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # Create a simple game save with player data:
    save_data = {
        "player": {
            "name": "???",  # Ask user for name
            "level": 1,
            "location": "{{school}}"
        },
        "inventory": {
            "{{item}}": 1,
            "gold": 0  # Ask user how much gold
        }
    }
    # Fill in the ??? with user input and print the save data
    pass


def main():
    print("=== Exercise A: Access Nested Data ===")
    exercise_a()

    print("\n=== Exercise B: Modify Nested Data ===")
    exercise_b()

    print("\n=== Exercise C: Filter Nested Data ===")
    exercise_c()

    print("\n=== Exercise D: Team Roster ===")
    exercise_d()

    print("\n=== Exercise E: Game Save ===")
    exercise_e()


main()
