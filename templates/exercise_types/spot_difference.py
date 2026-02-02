# =============================================================================
# TEMPLATE: Spot the Difference
# =============================================================================
#
# PURPOSE: Students identify subtle differences between similar code.
# SKILL: Attention to detail, understanding how small changes affect behavior
#
# STRUCTURE:
#   - Present two nearly-identical code snippets
#   - One small difference causes different behavior
#   - Student identifies the difference and explains the impact
#
# GUIDELINES:
#   - Code should look VERY similar at first glance
#   - The difference should be SUBTLE but SIGNIFICANT
#   - Both versions should RUN (no syntax errors)
#   - Difference should teach an important concept
#
# GOOD DIFFERENCES TO HIGHLIGHT:
#   - = vs == (assignment vs comparison)
#   - / vs // (float vs integer division)
#   - list vs list[:] (alias vs copy)
#   - append vs extend
#   - print vs return
#   - is vs ==
#   - and vs or
#   - default parameter mutation
#   - string method without reassignment
#
# DIFFICULTY SCALING:
#   - Easy: Visual difference is obvious once pointed out
#   - Medium: Difference requires understanding behavior
#   - Hard: Difference only manifests in certain conditions
#
# =============================================================================
# CONTEXT BLOCKS TO USE:
# =============================================================================
#
# Docstring/Introduction:
#   {{CONTEXT_SPOT_DIFFERENCE_INTRO}} - Main intro for spot-difference exercises
#   {{CONTEXT_LEARNING_OBJECTIVE}}    - What student will learn
#
# Per-Comparison:
#   {{COMPARISON_N_TITLE}}            - Title for comparison N (1, 2, 3...)
#   {{CONTEXT_COMPARISON_N_NARRATIVE}} - Story/context for comparison N
#   {{CONTEXT_SPOT_DIFFERENCE_HINT_N}} - Hint for comparison N
#
# Closing:
#   {{CONTEXT_ROLE_COMPLETE}}         - Completion message
#
# Layer 1 entities (use within explanatory text):
#   {{hero}}, {{school}}, {{spell1}}, {{item}}, etc.
#
# =============================================================================

"""
{{CONTEXT_SPOT_DIFFERENCE_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# {{COMPARISON_1_TITLE}}
# ============================================================
# {{CONTEXT_COMPARISON_1_NARRATIVE}}

def snippet_a1():
    """Snippet 1"""
    # [CODE VERSION 1]
    pass


def snippet_a2():
    """Snippet 2 - spot the difference!"""
    # [CODE VERSION 2 - NEARLY IDENTICAL, ONE SUBTLE CHANGE]
    pass


def explain_difference_a():
    # ✏️ EXPLAIN THE DIFFERENCE ✏️
    #
    # {{CONTEXT_SPOT_DIFFERENCE_HINT_1}}

    explanation = """
    The difference is:
    -

    Version 1 behavior:
    -

    Version 2 behavior:
    -

    Why this matters:
    -
    """
    return explanation


# ============================================================
# {{COMPARISON_2_TITLE}}
# ============================================================
# {{CONTEXT_COMPARISON_2_NARRATIVE}}

def snippet_b1():
    """Snippet 1"""
    pass


def snippet_b2():
    """Snippet 2 - spot the difference!"""
    pass


def explain_difference_b():
    # ✏️ EXPLAIN THE DIFFERENCE ✏️
    #
    # {{CONTEXT_SPOT_DIFFERENCE_HINT_2}}

    explanation = """
    The difference is:
    -

    Why this matters:
    -
    """
    return explanation


# [REPEAT PATTERN FOR MORE COMPARISONS]


def main():
    print("{{CONTEXT_SPOT_DIFFERENCE_INTRO}}")
    print("=" * 50)

    print("\n=== {{COMPARISON_1_TITLE}} ===")
    print("Version 1:")
    snippet_a1()
    print("\nVersion 2:")
    snippet_a2()
    print(f"\nExplanation:{explain_difference_a()}")

    print("\n=== {{COMPARISON_2_TITLE}} ===")
    print("Version 1:")
    snippet_b1()
    print("\nVersion 2:")
    snippet_b2()
    print(f"\nExplanation:{explain_difference_b()}")

    print("=" * 50)
    print("{{CONTEXT_ROLE_COMPLETE}}")


main()


# =============================================================================
# DIFFERENCE IDEAS:
# =============================================================================
#
# OPERATORS:
#   - x = 5 vs x == 5 (assignment vs comparison)
#   - a / b vs a // b (true vs floor division)
#   - a % b vs a // b (modulo vs division)
#   - i += 1 vs i =+ 1 (increment vs assign positive)
#
# COMPARISONS:
#   - x == y vs x is y (value vs identity)
#   - x and y vs x or y (different short-circuit)
#   - not x == y vs x != y (subtle precedence)
#
# LISTS:
#   - copy = original vs copy = original[:] (alias vs copy)
#   - list.append(x) vs list.extend(x) (item vs iterable)
#   - list.sort() vs sorted(list) (in-place vs new)
#   - list[0] vs list[:1] (element vs sublist)
#
# STRINGS:
#   - s.upper() vs s = s.upper() (ignored vs saved)
#   - s.split() vs s.split(" ") (any whitespace vs space only)
#
# FUNCTIONS:
#   - print(x) vs return x (side effect vs value)
#   - def f(x=[]) vs def f(x=None) (mutable default trap)
#
# SCOPE:
#   - global x vs x as parameter
#   - Variable defined in/out of loop
#
# LOOPS:
#   - range(5) vs range(1, 5) (start from 0 vs 1)
#   - for i in range(len(x)) vs for item in x (index vs item)
#   - while x: vs while x > 0: (truthy vs explicit)
#
# =============================================================================
