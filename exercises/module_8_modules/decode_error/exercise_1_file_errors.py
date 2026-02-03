"""
{{CONTEXT_DECODE_ERROR_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

In this exercise, you'll learn to understand and fix common file-related
errors: FileNotFoundError, PermissionError, and more.

Topic: File I/O error interpretation
Difficulty: 2-3
"""


# ============================================================
# {{ERROR_1_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_1_NARRATIVE}}
#
# The most common file error: trying to read a file that doesn't exist.

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "read_data.py", line 3, in <module>
    with open("nonexistent_file.txt", "r") as f:
FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent_file.txt'
"""


def buggy_code_a():
    """The code that caused the error."""
    # Trying to read a file that doesn't exist
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
    print(content)


def fix_code_a():
    # ✏️ FIX THE CODE ✏️
    #
    # First, explain what caused the error:
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_1}}
    #
    # Fix option 1: Check if file exists before opening
    #   import os
    #   if os.path.exists("data.txt"):
    #       with open("data.txt", "r") as f:
    #           content = f.read()
    #
    # Fix option 2: Use try/except to handle the error
    #   try:
    #       with open("data.txt", "r") as f:
    #           content = f.read()
    #   except FileNotFoundError:
    #       content = "File not found, using default"
    #
    # Choose one approach and write the fixed code:

    pass


# ============================================================
# {{ERROR_2_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_2_NARRATIVE}}
#
# Forgetting to handle the case where a directory doesn't exist.

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "save_data.py", line 2, in <module>
    with open("data/output.txt", "w") as f:
FileNotFoundError: [Errno 2] No such file or directory: 'data/output.txt'
"""


def buggy_code_b():
    """The code that caused the error."""
    # Trying to write to a file in a directory that doesn't exist
    with open("data/output.txt", "w") as f:
        f.write("Some data")


def fix_code_b():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_2}}
    #
    # The directory "data" doesn't exist! Python won't create
    # directories automatically when writing files.
    #
    # Fix: Create the directory first (if needed)
    #   import os
    #   os.makedirs("data", exist_ok=True)  # exist_ok prevents error if exists
    #   with open("data/output.txt", "w") as f:
    #       f.write("Some data")

    pass


# ============================================================
# {{ERROR_3_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_3_NARRATIVE}}
#
# Opening a file in the wrong mode.

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "update_data.py", line 3, in <module>
    f.write("New line\n")
io.UnsupportedOperation: not writable
"""


def buggy_code_c():
    """The code that caused the error."""
    # Opened file for reading but trying to write
    with open("data.txt", "r") as f:  # "r" = read mode!
        f.write("New line\n")


def fix_code_c():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_3}}
    #
    # The file was opened in read mode ("r") but we tried to write.
    #
    # Fix: Use the correct mode
    #   "w" - write (overwrites file)
    #   "a" - append (adds to end)
    #   "r+" - read and write
    #
    # If you want to append to the file:
    #   with open("data.txt", "a") as f:
    #       f.write("New line\n")

    pass


# ============================================================
# {{ERROR_4_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_4_NARRATIVE}}
#
# Using a file object after the 'with' block has closed it.

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "read_later.py", line 5, in <module>
    content = f.read()
ValueError: I/O operation on closed file.
"""


def buggy_code_d():
    """The code that caused the error."""
    with open("data.txt", "r") as f:
        first_line = f.readline()
    # File is closed here!
    content = f.read()  # Error: file is closed
    print(content)


def fix_code_d():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_4}}
    #
    # When the 'with' block ends, the file is automatically closed.
    # Any file operations must happen INSIDE the 'with' block.
    #
    # Fix: Do all file operations inside the 'with' block
    #   with open("data.txt", "r") as f:
    #       first_line = f.readline()
    #       content = f.read()  # Still inside the block!
    #   print(content)  # Can print outside, just can't read more

    pass


# ============================================================
# {{ERROR_5_TITLE}}
# ============================================================
# {{CONTEXT_ERROR_5_NARRATIVE}}
#
# Forgetting to use the correct encoding.

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "read_unicode.py", line 2, in <module>
    content = f.read()
UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 123: character maps to <undefined>
"""


def buggy_code_e():
    """The code that caused the error (on Windows)."""
    # File contains UTF-8 text but default encoding is different
    with open("unicode_file.txt", "r") as f:
        content = f.read()


def fix_code_e():
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # {{CONTEXT_ERROR_HINT_5}}
    #
    # The file contains special characters (like emojis or accented
    # letters) encoded in UTF-8, but Python tried to read it with
    # a different encoding.
    #
    # Fix: Specify UTF-8 encoding explicitly
    #   with open("unicode_file.txt", "r", encoding="utf-8") as f:
    #       content = f.read()
    #
    # Best practice: Always specify encoding="utf-8" for text files

    pass


def main():
    print("{{CONTEXT_DECODE_ERROR_INTRO}}")
    print("=" * 50)
    print()
    print("For each exercise:")
    print("1. Read the error message carefully")
    print("2. Identify what caused the error")
    print("3. Fix the code in the fix_code_X function")
    print()

    print("=== {{ERROR_1_TITLE}} ===")
    print("FileNotFoundError - file doesn't exist")
    # Uncomment to test after fixing:
    # fix_code_a()

    print("\n=== {{ERROR_2_TITLE}} ===")
    print("FileNotFoundError - directory doesn't exist")
    # fix_code_b()

    print("\n=== {{ERROR_3_TITLE}} ===")
    print("UnsupportedOperation - wrong file mode")
    # fix_code_c()

    print("\n=== {{ERROR_4_TITLE}} ===")
    print("ValueError - file already closed")
    # fix_code_d()

    print("\n=== {{ERROR_5_TITLE}} ===")
    print("UnicodeDecodeError - encoding mismatch")
    # fix_code_e()

    print("\n" + "=" * 50)
    print("{{CONTEXT_INVESTIGATION_COMPLETE}}")
    print()
    print("Key takeaways:")
    print("  1. Always handle FileNotFoundError for reads")
    print("  2. Create directories before writing to them")
    print("  3. Use correct mode: 'r', 'w', 'a', 'r+'")
    print("  4. Do all I/O inside the 'with' block")
    print("  5. Use encoding='utf-8' for text files")


main()
