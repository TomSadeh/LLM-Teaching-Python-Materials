# =============================================================================
# Match the Output: List Basics
# =============================================================================
# Difficulty: 1
# Concepts: List creation, printing lists, list length
# =============================================================================

"""
{{CONTEXT_MATCH_OUTPUT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# {{MATCH_SET_1_TITLE}}
# ============================================================
# {{CONTEXT_MATCH_SET_1_NARRATIVE}}

# --- CODE SNIPPETS ---


def snippet_1():
    inventory = ["{{item}}", "potion", "key"]
    print(inventory)


def snippet_2():
    inventory = ["{{item}}", "potion", "key"]
    print(len(inventory))


def snippet_3():
    inventory = []
    print(inventory)


# --- POSSIBLE OUTPUTS ---
"""
OUTPUT A:
---------
[]

OUTPUT B:
---------
['{{item}}', 'potion', 'key']

OUTPUT C:
---------
3
"""


# --- YOUR ANSWERS ---


def your_matches_set_1():
    # YOUR MATCHES HERE
    #
    # Write the letter (A, B, or C) that matches each snippet.
    # Study how printing a list and len() work.
    #
    # {{CONTEXT_MATCH_HINT_1}}

    matches = {
        "snippet_1": "?",
        "snippet_2": "?",
        "snippet_3": "?",
    }

    return matches


# ============================================================
# {{MATCH_SET_2_TITLE}}
# ============================================================
# {{CONTEXT_MATCH_SET_2_NARRATIVE}}

# --- CODE SNIPPETS ---


def snippet_4():
    party = ["{{hero}}", "{{heroine}}"]
    print(f"Party: {party}")


def snippet_5():
    party = ["{{hero}}", "{{heroine}}"]
    print(f"Size: {len(party)}")


def snippet_6():
    party = ["{{hero}}", "{{heroine}}"]
    party = party + ["{{friend}}"]
    print(party)


# --- POSSIBLE OUTPUTS ---
"""
OUTPUT D:
---------
Party: ['{{hero}}', '{{heroine}}']

OUTPUT E:
---------
['{{hero}}', '{{heroine}}', '{{friend}}']

OUTPUT F:
---------
Size: 2
"""


# --- YOUR ANSWERS ---


def your_matches_set_2():
    # YOUR MATCHES HERE
    #
    # Write the letter (D, E, or F) that matches each snippet.
    # Notice how list concatenation (+) creates a new list.
    #
    # {{CONTEXT_MATCH_HINT_2}}

    matches = {
        "snippet_4": "?",
        "snippet_5": "?",
        "snippet_6": "?",
    }

    return matches


def explain_matches():
    # OPTIONAL: EXPLAIN YOUR REASONING
    #
    # Understanding list basics helps with all future list operations.

    explanations = {
        "snippet_1": "Printing a list shows...",
        "snippet_2": "len() returns...",
        "snippet_3": "An empty list shows as...",
        "snippet_6": "Using + with lists...",
    }

    return explanations


def main():
    print("{{CONTEXT_MATCH_OUTPUT_INTRO}}")
    print("=" * 50)

    print("\n=== {{MATCH_SET_1_TITLE}} ===")
    print("\nYour matches:", your_matches_set_1())

    print("\n=== {{MATCH_SET_2_TITLE}} ===")
    print("\nYour matches:", your_matches_set_2())

    print("\nYour explanations:", explain_matches())

    print("\n" + "=" * 50)
    print("{{CONTEXT_VERIFICATION_COMPLETE}}")


main()
