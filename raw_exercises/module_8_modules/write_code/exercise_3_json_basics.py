# Exercise 3: Saving and Loading Data with JSON

import json


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Convert a dictionary to a JSON string using json.dumps()
    character = {
        "name": "{{hero}}",
        "house": "{{house}}",
        "level": 5
    }
    # json_string = json.dumps(character)
    # Print the JSON string
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # Convert a JSON string BACK to a dictionary using json.loads()
    json_string = '{"name": "{{heroine}}", "skill": "{{spell1}}", "books_read": 100}'
    # character = json.loads(json_string)
    # Print the character's name from the dictionary
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Make JSON pretty with indent!
    # Use json.dumps(data, indent=2) for readable output
    game_data = {
        "player": {"name": "{{hero}}", "health": 100},
        "inventory": ["{{item}}", "potion", "map"],
        "location": "{{school}}"
    }
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # SAVE a dictionary to a file!
    # Use: with open("filename.json", "w") as file:
    #          json.dump(data, file)
    save_data = {
        "player_name": "{{hero}}",
        "level": 10,
        "gold": 500,
        "completed_quests": ["Find the {{item}}", "Defeat {{villain}}"]
    }
    # Save to "game_save.json"
    # Print "Game saved!"
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # LOAD a dictionary from a file!
    # Use: with open("filename.json", "r") as file:
    #          data = json.load(file)
    # Load from "game_save.json" (from exercise_d)
    # Print the loaded data
    pass


def exercise_f():
    # ✏️ YOUR CODE HERE ✏️
    # Save and load a high scores list!
    # Create a list of high scores as dictionaries:
    # [{"name": "{{hero}}", "score": 1000}, ...]
    # Save to file, then load and display
    pass


def save_game_demo():
    # ✏️ YOUR CODE HERE ✏️
    # Complete game save/load system!
    # 1. Ask for player name and create initial stats
    # 2. Let them "play" (add gold, level up, etc.)
    # 3. Save their progress to a JSON file
    # 4. Offer to load a previous save or start new
    pass


def main():
    print("=== Exercise A: Dict to JSON String ===")
    exercise_a()

    print("\n=== Exercise B: JSON String to Dict ===")
    exercise_b()

    print("\n=== Exercise C: Pretty JSON ===")
    exercise_c()

    print("\n=== Exercise D: Save to File ===")
    exercise_d()

    print("\n=== Exercise E: Load from File ===")
    exercise_e()

    print("\n=== Exercise F: High Scores ===")
    exercise_f()

    print("\n=== Save Game Demo ===")
    save_game_demo()


main()
