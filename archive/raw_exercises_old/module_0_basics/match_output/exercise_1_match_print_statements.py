# Exercise 1: Match the Output - Print Statements
#
# Match each code snippet with its correct output.
# Don't run the code - use your mental execution skills!
#
# Theme: Messages from {{school}}


# ============================================================
# CODE SNIPPETS - Study these carefully
# ============================================================

def snippet_1():
    name = "{{hero}}"
    print("Hello, " + name)


def snippet_2():
    name = "{{hero}}"
    print("Hello,", name)


def snippet_3():
    name = "{{hero}}"
    print(f"Hello, {name}!")


def snippet_4():
    name = "{{hero}}"
    print("Hello, name")


# ============================================================
# POSSIBLE OUTPUTS - Which goes with which snippet?
# ============================================================

"""
OUTPUT A:
---------
Hello, {{hero}}!

OUTPUT B:
---------
Hello, {{hero}}

OUTPUT C:
---------
Hello, name

OUTPUT D:
---------
Hello,{{hero}}
"""


# ============================================================
# YOUR ANSWERS
# ============================================================

def your_matches():
    # ✏️ MATCH SNIPPETS TO OUTPUTS ✏️
    #
    # Write the letter (A, B, C, or D) that matches each snippet.
    # Think about:
    # - What does + do with strings?
    # - What does print() with commas do?
    # - What do f-strings do?
    # - What happens with quotes around a variable name?

    matches = {
        "snippet_1": "?",  # Hint: + joins strings directly
        "snippet_2": "?",  # Hint: commas add spaces between items
        "snippet_3": "?",  # Hint: f-strings with {} include the variable value
        "snippet_4": "?",  # Hint: quotes around name mean...?
    }

    return matches


def explain_matches():
    # ✏️ OPTIONAL: EXPLAIN YOUR REASONING ✏️

    explanations = {
        "snippet_1": "Because...",
        "snippet_2": "Because...",
        "snippet_3": "Because...",
        "snippet_4": "Because...",
    }

    return explanations


def main():
    print("=== Match the Output: Print Statements ===")
    print()
    print("Match each snippet to its output (A, B, C, or D)")
    print("Fill in your answers in your_matches()")
    print()
    print("="*45)

    print("\n--- Verification (run after making predictions) ---")
    print("\nSnippet 1 output:")
    snippet_1()
    print("\nSnippet 2 output:")
    snippet_2()
    print("\nSnippet 3 output:")
    snippet_3()
    print("\nSnippet 4 output:")
    snippet_4()

    print("\n" + "="*45)
    print("Your matches:", your_matches())


main()
