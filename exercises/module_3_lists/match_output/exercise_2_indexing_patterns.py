# =============================================================================
# Match the Output: Indexing Patterns
# =============================================================================
# Difficulty: 2
# Concepts: Positive indexing, accessing list elements
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
    abilities = ["{{spell1}}", "{{spell2}}", "{{spell3}}"]
    print(abilities[0])


def snippet_2():
    abilities = ["{{spell1}}", "{{spell2}}", "{{spell3}}"]
    print(abilities[1])


def snippet_3():
    abilities = ["{{spell1}}", "{{spell2}}", "{{spell3}}"]
    print(abilities[2])


# --- POSSIBLE OUTPUTS ---
"""
OUTPUT A:
---------
{{spell2}}

OUTPUT B:
---------
{{spell1}}

OUTPUT C:
---------
{{spell3}}
"""


# --- YOUR ANSWERS ---


def your_matches_set_1():
    # YOUR MATCHES HERE
    #
    # Write the letter (A, B, or C) that matches each snippet.
    # Remember: Index 0 is the FIRST element.
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
    team = ["{{hero}}", "{{heroine}}", "{{friend}}", "{{mentor}}"]
    print(f"Leader: {team[0]}")


def snippet_5():
    team = ["{{hero}}", "{{heroine}}", "{{friend}}", "{{mentor}}"]
    print(f"Count: {len(team)}")


def snippet_6():
    team = ["{{hero}}", "{{heroine}}", "{{friend}}", "{{mentor}}"]
    print(f"Last index: {len(team) - 1}")


# --- POSSIBLE OUTPUTS ---
"""
OUTPUT D:
---------
Leader: {{hero}}

OUTPUT E:
---------
Last index: 3

OUTPUT F:
---------
Count: 4
"""


# --- YOUR ANSWERS ---


def your_matches_set_2():
    # YOUR MATCHES HERE
    #
    # Write the letter (D, E, or F) that matches each snippet.
    # Notice: len() returns the count, but the last INDEX is len()-1.
    #
    # {{CONTEXT_MATCH_HINT_2}}

    matches = {
        "snippet_4": "?",
        "snippet_5": "?",
        "snippet_6": "?",
    }

    return matches


# ============================================================
# {{MATCH_SET_3_TITLE}}
# ============================================================
# {{CONTEXT_MATCH_SET_3_NARRATIVE}}

# --- CODE SNIPPETS ---


def snippet_7():
    items = ["{{item}}", "potion"]
    print(items[0], items[1])


def snippet_8():
    items = ["{{item}}", "potion"]
    print(items[1], items[0])


def snippet_9():
    items = ["{{item}}", "potion"]
    first = items[0]
    items[0] = items[1]
    items[1] = first
    print(items)


# --- POSSIBLE OUTPUTS ---
"""
OUTPUT G:
---------
{{item}} potion

OUTPUT H:
---------
potion {{item}}

OUTPUT I:
---------
['potion', '{{item}}']
"""


# --- YOUR ANSWERS ---


def your_matches_set_3():
    # YOUR MATCHES HERE
    #
    # Write the letter (G, H, or I) that matches each snippet.
    # Watch the order of access carefully!
    #
    # {{CONTEXT_MATCH_HINT_3}}

    matches = {
        "snippet_7": "?",
        "snippet_8": "?",
        "snippet_9": "?",
    }

    return matches


def explain_matches():
    # OPTIONAL: EXPLAIN YOUR REASONING
    #
    # Understanding indexing is key to working with lists.

    explanations = {
        "snippet_1": "abilities[0] gets...",
        "snippet_6": "len(team)-1 gives...",
        "snippet_9": "Swapping elements means...",
    }

    return explanations


def main():
    print("{{CONTEXT_MATCH_OUTPUT_INTRO}}")
    print("=" * 50)

    print("\n=== {{MATCH_SET_1_TITLE}} ===")
    print("\nYour matches:", your_matches_set_1())

    print("\n=== {{MATCH_SET_2_TITLE}} ===")
    print("\nYour matches:", your_matches_set_2())

    print("\n=== {{MATCH_SET_3_TITLE}} ===")
    print("\nYour matches:", your_matches_set_3())

    print("\nYour explanations:", explain_matches())

    print("\n" + "=" * 50)
    print("{{CONTEXT_VERIFICATION_COMPLETE}}")


main()
