"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn to use the json module to save and load
structured data. JSON is perfect for storing dictionaries and lists -
it's like having a universal language for data.

Topic: JSON module basics (dump, load, dumps, loads)
Difficulty: 3
"""

import json


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}
#
# Learn to save Python data to JSON files.


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Save a dictionary to a JSON file.
    #
    # Step 1: Create a character profile dictionary:
    #         profile = {
    #             "name": "{{hero}}",
    #             "level": 5,
    #             "abilities": ["{{spell1}}", "{{spell2}}"],
    #             "stats": {"health": 100, "energy": 50}
    #         }
    #
    # Step 2: Save to JSON file using json.dump():
    #         with open("profile.json", "w") as f:
    #             json.dump(profile, f)
    #
    # Step 3: Save with pretty formatting (indentation):
    #         with open("profile_pretty.json", "w") as f:
    #             json.dump(profile, f, indent=2)
    #
    # Step 4: Print confirmation message
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Load data from a JSON file.
    #
    # Step 1: Load the profile you saved:
    #         with open("profile.json", "r") as f:
    #             loaded_profile = json.load(f)
    #
    # Step 2: Print the loaded data:
    #         print(f"Loaded profile: {loaded_profile}")
    #         print(f"Name: {loaded_profile['name']}")
    #         print(f"Level: {loaded_profile['level']}")
    #
    # Step 3: Verify it's a real dictionary:
    #         print(f"Type: {type(loaded_profile)}")
    #
    # Note: JSON preserves the structure - dicts stay dicts!
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}
#
# Learn to convert between JSON strings and Python objects.


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Convert Python to JSON string (and back) using dumps/loads.
    #
    # Step 1: Create some data:
    #         data = {
    #             "school": "{{school}}",
    #             "students": ["{{hero}}", "{{heroine}}", "{{friend}}"],
    #             "active": True
    #         }
    #
    # Step 2: Convert to JSON string (not file):
    #         json_string = json.dumps(data)
    #         print(f"JSON string: {json_string}")
    #         print(f"Type: {type(json_string)}")  # It's a str!
    #
    # Step 3: Convert JSON string back to Python:
    #         restored = json.loads(json_string)
    #         print(f"Restored: {restored}")
    #         print(f"Type: {type(restored)}")  # It's a dict again!
    #
    # Note: dumps = dump to string, loads = load from string
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Work with lists in JSON.
    #
    # Step 1: Create a list of records:
    #         records = [
    #             {"name": "{{hero}}", "score": 100},
    #             {"name": "{{heroine}}", "score": 150},
    #             {"name": "{{friend}}", "score": 75}
    #         ]
    #
    # Step 2: Save to JSON:
    #         with open("records.json", "w") as f:
    #             json.dump(records, f, indent=2)
    #
    # Step 3: Load and iterate:
    #         with open("records.json", "r") as f:
    #             loaded_records = json.load(f)
    #
    #         for record in loaded_records:
    #             print(f"{record['name']}: {record['score']}")
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}
#
# Learn JSON limitations and best practices.


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Understand what JSON can and cannot store.
    #
    # Step 1: JSON SUPPORTS these Python types:
    #         supported = {
    #             "string": "hello",
    #             "number": 42,
    #             "float": 3.14,
    #             "boolean": True,
    #             "null": None,
    #             "list": [1, 2, 3],
    #             "dict": {"nested": "value"}
    #         }
    #         Save this to "supported.json" and load it back.
    #
    # Step 2: JSON does NOT support these (directly):
    #         - Sets: {1, 2, 3} becomes [1, 2, 3] (list)
    #         - Tuples: (1, 2, 3) becomes [1, 2, 3] (list)
    #         - Custom objects: Need special handling
    #
    # Step 3: Test with a set:
    #         data = {"items": {"a", "b", "c"}}  # This has a set!
    #         # json.dump(data, f)  # This would ERROR!
    #         # Convert set to list first:
    #         data["items"] = list(data["items"])
    #         # Now it works
    #
    # Step 4: Print what you learned
    pass


def exercise_f():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a complete save/load system for {{school}}.
    #
    # Step 1: Create a game state dictionary:
    #         game_state = {
    #             "player": "{{hero}}",
    #             "level": 1,
    #             "inventory": ["{{item}}", "potion"],
    #             "location": "{{location}}",
    #             "stats": {
    #                 "health": 100,
    #                 "energy": 50,
    #                 "experience": 0
    #             },
    #             "completed_quests": []
    #         }
    #
    # Step 2: Create a save function:
    #         def save_game(state, filename):
    #             with open(filename, "w") as f:
    #                 json.dump(state, f, indent=2)
    #             print(f"Game saved to {filename}")
    #
    # Step 3: Create a load function:
    #         def load_game(filename):
    #             with open(filename, "r") as f:
    #                 return json.load(f)
    #
    # Step 4: Test save and load
    pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)

    print("\n=== {{PHASE_1_TITLE}} ===")
    print("Saving and loading JSON files")
    exercise_a()
    exercise_b()

    print("\n=== {{PHASE_2_TITLE}} ===")
    print("JSON strings: dumps and loads")
    exercise_c()
    exercise_d()

    print("\n=== {{PHASE_3_TITLE}} ===")
    print("JSON best practices")
    exercise_e()
    exercise_f()

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")
    print()
    print("JSON Summary:")
    print("  json.dump(data, file)  # Save to file")
    print("  json.load(file)        # Load from file")
    print("  json.dumps(data)       # Convert to string")
    print("  json.loads(string)     # Parse from string")
    print()
    print("Supports: dict, list, str, int, float, bool, None")
    print("NOT directly: set, tuple, custom objects")


main()
