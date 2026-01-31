# Exercise 7: Working with Files and Folders (os and pathlib)

import os


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    # Find out your current working directory!
    # Use os.getcwd()
    # Print: "You are in: [directory]"
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    # List all files in the current directory!
    # Use os.listdir()
    # Print each file on its own line
    pass


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    # Check if a file exists!
    # Use os.path.exists("filename")
    # Check if "game_save.json" exists (from earlier exercises)
    # Print whether it exists or not
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    # Create a folder for saving games!
    # Use os.makedirs("folder_name", exist_ok=True)
    # Create a folder called "{{school}}_saves"
    # The exist_ok=True means it won't error if folder exists
    pass


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    # Build a file path safely!
    # Use os.path.join() to combine folder and filename
    # Example: os.path.join("saves", "game1.json")
    # This works on any operating system!
    pass


def exercise_f():
    # ✏️ YOUR CODE HERE ✏️
    # Get file information!
    # Use os.path.getsize("filename") to get size in bytes
    # Create a file, then check its size
    pass


def file_explorer():
    # ✏️ YOUR CODE HERE ✏️
    # Simple file explorer!
    # 1. Show current directory
    # 2. List all files and folders
    # 3. Mark folders with [DIR] and files with their size
    # Hint: os.path.isdir(path) checks if something is a folder
    pass


def organize_saves():
    # ✏️ YOUR CODE HERE ✏️
    # Game save organizer!
    # 1. Create a "saves" folder if it doesn't exist
    # 2. List any .json files in it
    # 3. Let user pick one to "load" (just print its name)
    # 4. Or create a new save file
    pass


def main():
    print("=== Exercise A: Current Directory ===")
    exercise_a()

    print("\n=== Exercise B: List Files ===")
    exercise_b()

    print("\n=== Exercise C: Check File Exists ===")
    exercise_c()

    print("\n=== Exercise D: Create Folder ===")
    exercise_d()

    print("\n=== Exercise E: Build Path ===")
    exercise_e()

    print("\n=== Exercise F: File Size ===")
    exercise_f()

    print("\n=== File Explorer ===")
    file_explorer()

    print("\n=== Save Organizer ===")
    organize_saves()


main()
