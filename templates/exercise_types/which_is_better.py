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
# CONTEXT BLOCKS TO USE:
# =============================================================================
#
# Docstring/Introduction:
#   {{CONTEXT_COMPARISON_INTRO}}     - Main intro for comparison exercises
#   {{CONTEXT_COMPARISON_DECISION}}  - Framing the decision to make
#
# Per-Comparison:
#   {{APPROACH_N_NAME}}              - Name for approach N (1, 2, 3...)
#   {{CONTEXT_APPROACH_N_NARRATIVE}} - Story/context for approach N
#   {{CONTEXT_ANALYSIS_PROMPT}}      - Prompt for analysis
#   {{CONTEXT_DECISION_GUIDANCE}}    - Criteria for decisions
#
# Closing:
#   {{CONTEXT_EVALUATION_COMPLETE}}  - Completion message
#
# Layer 1 entities (use within explanatory text):
#   {{hero}}, {{school}}, {{spell1}}, {{item}}, etc.
#
# =============================================================================

"""
{{CONTEXT_COMPARISON_INTRO}}
{{CONTEXT_COMPARISON_DECISION}}
"""


# ============================================================
# {{APPROACH_1_NAME}}
# ============================================================
# {{CONTEXT_APPROACH_1_NARRATIVE}}

def version_a1(params):
    """Version 1: [Describe approach]"""
    # [FIRST IMPLEMENTATION]
    pass


# ============================================================
# {{APPROACH_2_NAME}}
# ============================================================
# {{CONTEXT_APPROACH_2_NARRATIVE}}

def version_a2(params):
    """Version 2: [Describe approach]"""
    # [SECOND IMPLEMENTATION]
    pass


# Optional: version_a3 for three-way comparisons


def analysis_a():
    # ✏️ YOUR ANALYSIS ✏️
    #
    # {{CONTEXT_ANALYSIS_PROMPT}}
    # Consider: {{CONTEXT_DECISION_GUIDANCE}}

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When to use version 1:
    -

    When to use version 2:
    -
    """
    return analysis


# [REPEAT PATTERN FOR MORE COMPARISONS]


def main():
    print("{{CONTEXT_COMPARISON_INTRO}}")
    print("=" * 50)

    print("\n=== {{APPROACH_1_NAME}} vs {{APPROACH_2_NAME}} ===")

    # Show both versions work
    test_input = ...
    print(f"Version 1: {version_a1(test_input)}")
    print(f"Version 2: {version_a2(test_input)}")

    # Show analysis
    print(f"\nYour analysis:{analysis_a()}")

    print("\n" + "=" * 50)
    print("{{CONTEXT_EVALUATION_COMPLETE}}")


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
