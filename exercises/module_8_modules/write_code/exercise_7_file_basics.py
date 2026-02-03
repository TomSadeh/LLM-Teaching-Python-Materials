"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn to read from and write to files using
Python's built-in file handling. This is essential for saving data,
loading configuration, and working with external data.

Topic: File I/O basics with context managers
Difficulty: 2-3
"""


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}
#
# Learn the 'with' statement (context manager) for safe file handling.


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Write text to a file using a context manager.
    #
    # Step 1: Use 'with open()' to open a file for writing:
    #         with open("greeting.txt", "w") as f:
    #             # file operations go here
    #
    # Step 2: Write a greeting message:
    #         f.write("Welcome to {{school}}!\n")
    #         f.write("Greetings, {{hero}}.\n")
    #
    # Step 3: The file is automatically closed when the 'with' block ends!
    #
    # Step 4: Print: "File 'greeting.txt' created successfully!"
    #
    # File modes:
    #   "w" = write (creates new or overwrites existing)
    #   "r" = read (default)
    #   "a" = append (add to end)
    pass


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Read text from the file you just created.
    #
    # Step 1: Open the file for reading:
    #         with open("greeting.txt", "r") as f:
    #
    # Step 2: Read all content at once:
    #         content = f.read()
    #
    # Step 3: Print the content:
    #         print("File content:")
    #         print(content)
    #
    # Note: After the 'with' block, the file is closed automatically
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}
#
# Learn different ways to read files.


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # First, create a file with multiple lines.
    #
    # Step 1: Create a file with numbered lines:
    #         with open("lines.txt", "w") as f:
    #             for i in range(1, 6):
    #                 f.write(f"Line {i}: {{spell1}}\n")
    #
    # Step 2: Read and print using readlines():
    #         with open("lines.txt", "r") as f:
    #             lines = f.readlines()  # Returns a list of lines
    #
    # Step 3: Print each line with its index:
    #         for i, line in enumerate(lines):
    #             print(f"{i}: {line.strip()}")  # strip() removes \n
    #
    # Note: readlines() includes the newline character \n
    pass


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Read a file line by line (more memory efficient for large files).
    #
    # Step 1: Open the file
    #         with open("lines.txt", "r") as f:
    #
    # Step 2: Iterate directly over the file object:
    #             for line in f:
    #                 print(line.strip())
    #
    # This is the most Pythonic way to read files line by line.
    # It doesn't load the entire file into memory at once.
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}
#
# Learn to append to files and work with file paths.


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Append to an existing file.
    #
    # Step 1: Open in append mode "a":
    #         with open("greeting.txt", "a") as f:
    #             f.write("\nNew message added!\n")
    #             f.write("From {{heroine}}.\n")
    #
    # Step 2: Read the file to verify:
    #         with open("greeting.txt", "r") as f:
    #             print(f.read())
    #
    # Note: "a" mode adds to the end, "w" mode overwrites!
    pass


def exercise_f():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Create a function to save a list to a file.
    #
    # Step 1: Create a list of items:
    #         inventory = ["{{item}}", "potion", "scroll", "gem", "key"]
    #
    # Step 2: Write each item to a file (one per line):
    #         with open("inventory.txt", "w") as f:
    #             for item in inventory:
    #                 f.write(item + "\n")
    #
    # Step 3: Read the file back into a list:
    #         with open("inventory.txt", "r") as f:
    #             loaded = []
    #             for line in f:
    #                 loaded.append(line.strip())
    #
    # Step 4: Print both lists to verify they match:
    #         print(f"Original: {inventory}")
    #         print(f"Loaded: {loaded}")
    pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)

    print("\n=== {{PHASE_1_TITLE}} ===")
    print("Writing and reading files with 'with' statement")
    exercise_a()
    exercise_b()

    print("\n=== {{PHASE_2_TITLE}} ===")
    print("Different ways to read files")
    exercise_c()
    exercise_d()

    print("\n=== {{PHASE_3_TITLE}} ===")
    print("Appending and saving lists")
    exercise_e()
    exercise_f()

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")
    print()
    print("File I/O Summary:")
    print("  with open(file, 'w') as f:  # Write (overwrite)")
    print("  with open(file, 'r') as f:  # Read")
    print("  with open(file, 'a') as f:  # Append")
    print("  f.read()       # Read all content")
    print("  f.readlines()  # Read as list of lines")
    print("  f.write(text)  # Write text")


main()
