# =============================================================================
# TEMPLATE: Match the Output
# =============================================================================
#
# PURPOSE: Students match code snippets to their outputs.
# SKILL: Pattern recognition, quick code reading
#
# STRUCTURE:
#   - Present N code snippets (labeled snippet_1, snippet_2, etc.)
#   - Present N possible outputs (labeled OUTPUT A, B, C, etc.)
#   - Student matches each snippet to its output
#   - Optional: explain reasoning
#
# GUIDELINES:
#   - Keep snippets SHORT (3-8 lines each)
#   - Snippets should look SIMILAR but behave DIFFERENTLY
#   - Outputs should be distinct enough to match unambiguously
#   - Good for testing: operator differences, method behaviors,
#     loop variations, indexing differences
#
# DIFFICULTY SCALING:
#   - Easy: Obviously different code, clearly different outputs
#   - Medium: Similar-looking code, subtle output differences
#   - Hard: Nearly identical code, requires deep understanding
#
# =============================================================================
# CONTEXT BLOCKS TO USE:
# =============================================================================
#
# Docstring/Introduction:
#   {{CONTEXT_MATCH_OUTPUT_INTRO}}   - Main intro for matching exercises
#   {{CONTEXT_LEARNING_OBJECTIVE}}   - What student will learn
#
# Per-Challenge Set:
#   {{MATCH_SET_N_TITLE}}            - Title for set N (1, 2, 3...)
#   {{CONTEXT_MATCH_SET_N_NARRATIVE}} - Story/context for set N
#   {{CONTEXT_MATCH_HINT_N}}         - Hint for set N
#
# Closing:
#   {{CONTEXT_VERIFICATION_COMPLETE}} - Completion message
#
# Layer 1 entities (use within explanatory text):
#   {{hero}}, {{school}}, {{spell1}}, {{item}}, etc.
#
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
    # [SHORT CODE THAT PRODUCES OUTPUT]
    pass


def snippet_2():
    # [SIMILAR BUT DIFFERENT CODE]
    pass


def snippet_3():
    # [ANOTHER VARIATION]
    pass


# --- POSSIBLE OUTPUTS ---
"""
OUTPUT A:
---------
[What one snippet would print]

OUTPUT B:
---------
[What another snippet would print]

OUTPUT C:
---------
[What another snippet would print]
"""


# --- YOUR ANSWERS ---

def your_matches():
    # ✏️ MATCH SNIPPETS TO OUTPUTS ✏️
    #
    # Write the letter (A, B, C, etc.) that matches each snippet.
    #
    # {{CONTEXT_MATCH_HINT_1}}

    matches = {
        "snippet_1": "?",
        "snippet_2": "?",
        "snippet_3": "?",
    }

    return matches


def explain_matches():
    # ✏️ OPTIONAL: EXPLAIN YOUR REASONING ✏️

    explanations = {
        "snippet_1": "Because...",
        "snippet_2": "Because...",
        "snippet_3": "Because...",
    }

    return explanations


# [REPEAT PATTERN FOR MORE MATCH SETS]


def main():
    print("{{CONTEXT_MATCH_OUTPUT_INTRO}}")
    print("=" * 50)

    print("\n=== {{MATCH_SET_1_TITLE}} ===")
    print("\nYour matches:", your_matches())
    print("\nYour explanations:", explain_matches())

    print("\n" + "=" * 50)
    print("{{CONTEXT_VERIFICATION_COMPLETE}}")


main()


# =============================================================================
# GOOD CONCEPTS FOR MATCHING EXERCISES:
# =============================================================================
#
# OPERATORS:
#   - / vs //
#   - + with strings vs numbers
#   - == vs = (in context)
#   - and vs or behavior
#
# STRING METHODS:
#   - split() vs split(" ")
#   - strip() vs replace()
#   - upper() vs capitalize()
#
# LIST OPERATIONS:
#   - append() vs extend()
#   - [0] vs [:1]
#   - pop() vs remove()
#
# LOOP VARIATIONS:
#   - range(5) vs range(1, 5) vs range(0, 5, 2)
#   - for x in list vs for i, x in enumerate(list)
#
# =============================================================================
