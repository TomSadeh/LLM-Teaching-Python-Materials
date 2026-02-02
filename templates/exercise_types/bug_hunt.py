# =============================================================================
# TEMPLATE: Bug Hunt
# =============================================================================
#
# PURPOSE: Students find and fix bugs in themed narrative context.
# SKILL: Debugging, reading code critically, identifying common mistakes
#
# STRUCTURE:
#   - Present a STORY that sets up the problem
#   - Show code that has exactly ONE bug
#   - Describe EXPECTED vs ACTUAL behavior
#   - Student finds and fixes the bug
#
# GUIDELINES:
#   - Each challenge should have exactly ONE bug
#   - The bug should be FINDABLE without running (ideally)
#   - Story should make the expected behavior clear
#   - Include a mix of: obvious bugs, subtle bugs, common pitfalls
#
# BUG TYPES TO INCLUDE:
#   - Off-by-one errors (< vs <=, wrong range bounds)
#   - Logic errors (wrong operator, inverted condition)
#   - Missing operations (forgot to increment, forgot to return)
#   - Wrong variable (typo, using wrong one)
#   - Scope issues (variable in wrong scope)
#   - Mutation issues (forgetting to save result)
#   - Infinite loops (condition never changes)
#   - Mutable default arguments
#   - Comparison vs assignment
#
# DIFFICULTY SCALING:
#   - Easy: Bug is on obvious line, classic mistake
#   - Medium: Bug requires understanding intended behavior
#   - Hard: Bug only triggers in certain conditions, or is a Python gotcha
#
# =============================================================================

# Exercise N: Bug Hunt - [TOPIC]
#
# [VILLAIN/ANTAGONIST] has cursed these [THINGS] with bugs!
# Each function has exactly ONE bug hiding in it.
# Read the story, find the bug, and fix it.
#
# DO NOT run the code first - use your detective skills!


# ============================================================
# BUG HUNT [LETTER]: [BUG TITLE]
# ============================================================
"""
STORY:
[Narrative setup using {{placeholders}}]
[Describe what the code is supposed to do]
[Make it clear what the correct behavior should be]

EXPECTED BEHAVIOR:
[What should happen - be specific with examples]

ACTUAL BEHAVIOR:
[What actually happens - describe the symptom]
"""

def buggy_X():
    # [CODE WITH EXACTLY ONE BUG]
    # The bug should be:
    # - Not immediately obvious (no syntax errors)
    # - Logically incorrect
    # - Discoverable by careful reading
    pass


def fix_X():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    #
    # The fix:

    # [STUDENT WRITES CORRECTED CODE]
    pass


# [REPEAT PATTERN FOR MORE CHALLENGES]


def main():
    print("=== Bug Hunt Challenges ===\n")

    print("[LETTER]: [BUG TITLE]")
    # Show buggy behavior:
    # buggy_X()

    # Show fixed behavior:
    # print("Fixed version:")
    # fix_X()

    # [REPEAT FOR EACH CHALLENGE]


main()


# =============================================================================
# BUG PATTERNS TO USE:
# =============================================================================
#
# OFF-BY-ONE:
#   - range(1, 5) when you need 1-5 inclusive
#   - < vs <= in loop conditions
#   - Indexing [3] when you mean "third element" (should be [2])
#
# LOGIC ERRORS:
#   - > when you meant <
#   - and when you meant or
#   - == when you meant = (or vice versa, in walrus context)
#   - not in wrong place
#
# MISSING OPERATIONS:
#   - Forgot to increment counter (infinite loop)
#   - Forgot to return (returns None)
#   - Forgot to append to result list
#   - Forgot to save method result (string.upper() without assignment)
#
# WRONG VARIABLE:
#   - Typo in variable name (defined vs used)
#   - Using parameter name vs local name
#   - Comparing to wrong variable
#
# SCOPE BUGS:
#   - Variable defined inside if block, used outside
#   - Overwriting loop variable accidentally
#   - Global vs local confusion
#
# COLLECTION BUGS:
#   - Modifying list while iterating
#   - Aliasing (thinking you have a copy)
#   - Wrong method (add vs append, extend vs append)
#
# PYTHON GOTCHAS:
#   - Mutable default argument (def f(x=[]))
#   - Late binding closures in loops
#   - Integer division in Python 2 vs 3 style code
#
# STORYTELLING TIPS:
#   - Use themed language (spells, potions, quests)
#   - Make the expected behavior part of the narrative
#   - The "symptom" should be describable in story terms
#   - Example: "The potion should turn blue, but it stays red"
#
# =============================================================================
