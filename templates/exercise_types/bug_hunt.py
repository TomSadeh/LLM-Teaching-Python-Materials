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
# CONTEXT BLOCKS TO USE:
# =============================================================================
#
# Docstring/Introduction:
#   {{CONTEXT_INVESTIGATION_INTRO}}   - Main intro for bug hunt exercises
#   {{CONTEXT_INVESTIGATION_MISSION}} - What student is investigating
#
# Per-Bug:
#   {{CASE_N_TITLE}}                  - Title for case N (1, 2, 3...)
#   {{CONTEXT_CASE_N_NARRATIVE}}      - Story/context for case N
#   {{CONTEXT_INVESTIGATION_PROMPT_N}} - What to look for in case N
#
# Closing:
#   {{CONTEXT_INVESTIGATION_COMPLETE}} - Completion message
#
# Layer 1 entities (use within explanatory text):
#   {{hero}}, {{villain}}, {{school}}, {{spell1}}, {{item}}, etc.
#
# =============================================================================

"""
{{CONTEXT_INVESTIGATION_INTRO}}
{{CONTEXT_INVESTIGATION_MISSION}}
"""


# ============================================================
# {{CASE_1_TITLE}}
# ============================================================
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# [What should happen - be specific with examples]
#
# ACTUAL BEHAVIOR:
# [What actually happens - describe the symptom]
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

def buggy_a():
    """This code has exactly ONE bug. Find it!"""
    # [CODE WITH EXACTLY ONE BUG]
    # The bug should be:
    # - Not immediately obvious (no syntax errors)
    # - Logically incorrect
    # - Discoverable by careful reading
    pass


def fix_a():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    #
    # The fix:

    # [STUDENT WRITES CORRECTED CODE]
    pass


# ============================================================
# {{CASE_2_TITLE}}
# ============================================================
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# EXPECTED BEHAVIOR:
# [What should happen]
#
# ACTUAL BEHAVIOR:
# [What actually happens]
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}

def buggy_b():
    """This code has exactly ONE bug. Find it!"""
    pass


def fix_b():
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    pass


# [REPEAT PATTERN FOR MORE CASES]


def main():
    print("{{CONTEXT_INVESTIGATION_INTRO}}")
    print("=" * 50)

    print("\n=== {{CASE_1_TITLE}} ===")
    print("Buggy version:")
    # buggy_a()
    print("\nFixed version:")
    # fix_a()

    print("\n=== {{CASE_2_TITLE}} ===")
    print("Buggy version:")
    # buggy_b()
    print("\nFixed version:")
    # fix_b()

    print("\n" + "=" * 50)
    print("{{CONTEXT_INVESTIGATION_COMPLETE}}")


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
# =============================================================================
