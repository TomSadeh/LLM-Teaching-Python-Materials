# =============================================================================
# TEMPLATE: Which is Better?
# =============================================================================
#
# PURPOSE: Students analyze trade-offs between working solutions.
# SKILL: Critical thinking, understanding trade-offs, code judgment
#
# STRUCTURE:
#   - Present 2-3 solutions that ALL work correctly
#   - Student analyzes and explains which is "better" (and why)
#   - Often the answer is "it depends" - explore when each is preferred
#
# GUIDELINES:
#   - ALL versions must produce CORRECT output
#   - Differences should be meaningful (not trivial style)
#   - Include questions that DON'T have a single right answer
#   - Ask students to consider: readability, performance, Pythonic style,
#     beginner-friendliness, maintainability, edge cases
#
# COMPARISON TYPES:
#   - Readable vs concise (loop vs comprehension)
#   - Explicit vs implicit (LBYL vs EAFP)
#   - Simple vs flexible (hardcoded vs configurable)
#   - Safe vs fast (with vs without validation)
#   - Standard vs clever (obvious vs tricky)
#
# DIFFICULTY SCALING:
#   - Easy: Clear winner for beginners, explain why
#   - Medium: Trade-offs depend on context
#   - Hard: Subtle differences, performance vs readability, edge cases
#
# =============================================================================

# Exercise N: Which is Better? - [TOPIC]
#
# For each pair of solutions, both work correctly.
# Your job: Analyze and explain which is better AND WHY.
# Sometimes the answer is "it depends"!
#
# Theme: [THEMED CONTEXT USING {{placeholders}}]


# ============================================================
# COMPARISON [LETTER]: [COMPARISON TYPE]
# ============================================================

def version_X1(params):
    """Version 1: [Describe approach]"""
    # [FIRST IMPLEMENTATION]
    pass


def version_X2(params):
    """Version 2: [Describe approach]"""
    # [SECOND IMPLEMENTATION]
    pass


# Optional: version_X3 for three-way comparisons


def analysis_X():
    # ✏️ YOUR ANALYSIS ✏️
    # Which is better: X1 or X2?
    # Consider: [SPECIFIC FACTORS TO CONSIDER]

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When to use [version 1]:
    -

    When to use [version 2]:
    -
    """
    return analysis


# [REPEAT PATTERN FOR MORE COMPARISONS]


def main():
    print("=== Comparison [LETTER]: [TYPE] ===")

    # Show both versions work
    test_input = ...
    print(f"Version 1: {version_X1(test_input)}")
    print(f"Version 2: {version_X2(test_input)}")

    # Show analysis
    print(f"\nYour analysis:{analysis_X()}")

    # [REPEAT FOR EACH COMPARISON]


main()


# =============================================================================
# COMPARISON IDEAS:
# =============================================================================
#
# LOOP STYLES:
#   - for i in range(len(list)) vs for item in list
#   - while loop vs for loop
#   - enumerate() vs manual counter
#
# DATA ACCESS:
#   - try/except KeyError vs if key in dict vs dict.get()
#   - Checking before acting (LBYL) vs try/except (EAFP)
#
# LIST OPERATIONS:
#   - for loop with append vs list comprehension
#   - filter() with lambda vs list comprehension with if
#   - map() vs list comprehension
#
# STRING BUILDING:
#   - += in loop vs join()
#   - f-string vs .format() vs % formatting
#
# CONDITIONALS:
#   - Multiple if/elif vs dictionary dispatch
#   - Ternary expression vs full if/else
#   - and/or short-circuit vs explicit if
#
# DATA STRUCTURES:
#   - List of tuples vs dictionary
#   - Class vs dictionary
#   - namedtuple vs class vs dict
#
# FUNCTION DESIGN:
#   - Return value vs print directly
#   - Multiple parameters vs single dict/object parameter
#   - Raising exception vs returning None/error code
#
# ANALYSIS PROMPTS:
#   - "Which is more readable to a beginner?"
#   - "Which would be easier to modify later?"
#   - "Which handles edge cases better?"
#   - "Which is more 'Pythonic'?"
#   - "Which would you use in production code?"
#
# =============================================================================
