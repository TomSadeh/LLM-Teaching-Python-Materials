# Exercise 1: Match the Output - List Operations
#
# Match each code snippet with its correct output.
# Don't run the code - use your mental execution skills!
#
# Theme: {{hero}}'s collection of {{item}}s


# ============================================================
# CODE SNIPPETS - Study these carefully
# ============================================================

def snippet_1():
    items = ["wand", "cloak", "stone"]
    items.append("book")
    print(items)


def snippet_2():
    items = ["wand", "cloak", "stone"]
    items.extend(["book"])
    print(items)


def snippet_3():
    items = ["wand", "cloak", "stone"]
    items.append(["book", "potion"])
    print(items)


def snippet_4():
    items = ["wand", "cloak", "stone"]
    items.extend(["book", "potion"])
    print(items)


# ============================================================
# POSSIBLE OUTPUTS - Which goes with which snippet?
# ============================================================

"""
OUTPUT A:
---------
['wand', 'cloak', 'stone', 'book', 'potion']

OUTPUT B:
---------
['wand', 'cloak', 'stone', 'book']

OUTPUT C:
---------
['wand', 'cloak', 'stone', ['book', 'potion']]

OUTPUT D:
---------
['wand', 'cloak', 'stone', 'book']
"""


# ============================================================
# YOUR ANSWERS
# ============================================================

def your_matches():
    # ✏️ MATCH SNIPPETS TO OUTPUTS ✏️
    #
    # Write the letter (A, B, C, or D) that matches each snippet.
    # Think about:
    # - What does append() do? (adds ONE item)
    # - What does extend() do? (adds EACH item from another list)
    # - What happens when you append a list vs extend with a list?

    matches = {
        "snippet_1": "?",  # Hint: append() adds "book" as one item
        "snippet_2": "?",  # Hint: extend() with one-item list
        "snippet_3": "?",  # Hint: append() adds the entire list as one item
        "snippet_4": "?",  # Hint: extend() adds each item from the list
    }

    return matches


def explain_matches():
    # ✏️ OPTIONAL: EXPLAIN YOUR REASONING ✏️
    #
    # Explain the difference between append() and extend()

    explanations = {
        "snippet_1": "Because append...",
        "snippet_2": "Because extend...",
        "snippet_3": "Because appending a list...",
        "snippet_4": "Because extending with a list...",
    }

    return explanations


# ============================================================
# BONUS CHALLENGE
# ============================================================

def bonus_snippet_5():
    items = ["wand", "cloak", "stone"]
    print(items[0])
    print(items[-1])
    print(items[1:3])


"""
BONUS OUTPUT:
What does snippet_5 print? (3 separate lines)
"""


def bonus_prediction():
    # ✏️ BONUS: PREDICT THE OUTPUT ✏️
    # What three things are printed?
    #
    # Hint:
    # - items[0] gets the first item
    # - items[-1] gets the last item
    # - items[1:3] gets items from index 1 up to (not including) 3

    predictions = {
        "line_1": "?",
        "line_2": "?",
        "line_3": "?",
    }

    return predictions


def main():
    print("=== Match the Output: List Operations ===")
    print()
    print("Match each snippet to its output (A, B, C, or D)")
    print("Fill in your answers in your_matches()")
    print()
    print("KEY CONCEPT:")
    print("  append(x)  -> adds x as ONE item")
    print("  extend(x)  -> adds EACH item from x")
    print()
    print("="*50)

    print("\n--- Verification (run after making predictions) ---")
    print("\nSnippet 1 output:")
    snippet_1()
    print("\nSnippet 2 output:")
    snippet_2()
    print("\nSnippet 3 output:")
    snippet_3()
    print("\nSnippet 4 output:")
    snippet_4()

    print("\n--- Bonus ---")
    print("Snippet 5 output:")
    bonus_snippet_5()

    print("\n" + "="*50)
    print("Your matches:", your_matches())


main()
