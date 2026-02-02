# =============================================================================
# TEMPLATE: Fix the Style
# =============================================================================
#
# PURPOSE: Students improve working but poorly-styled code.
# SKILL: Code readability, PEP 8, Python conventions
#
# STRUCTURE:
#   - Provide working code with intentional style issues
#   - Student rewrites with proper style
#   - Both versions should produce identical output
#
# GUIDELINES:
#   - Code must WORK (this is about style, not bugs)
#   - Include multiple style issues per exercise
#   - Focus on teachable conventions, not personal preference
#   - Show "before" clearly, give space for "after"
#
# STYLE ISSUES TO INCLUDE:
#   - Naming: x, y, temp1 instead of descriptive names
#   - Spacing: missing spaces around operators, after commas
#   - Formatting: inconsistent indentation, line length
#   - Structure: overly complex expressions, no separation
#   - Comments: missing where needed, present where obvious
#   - String formatting: mixing %, .format(), f-strings, concatenation
#
# DIFFICULTY SCALING:
#   - Easy: Obvious naming issues, basic spacing
#   - Medium: Mixed formatting styles, structure improvements
#   - Hard: Subtle issues, adding documentation, refactoring logic
#
# =============================================================================
# CONTEXT BLOCKS TO USE:
# =============================================================================
#
# Docstring/Introduction:
#   {{CONTEXT_FIX_STYLE_INTRO}}      - Main intro for style exercises
#   {{CONTEXT_LEARNING_OBJECTIVE}}   - What student will learn
#
# Per-Style Issue:
#   {{STYLE_N_TITLE}}                - Title for style issue N (1, 2, 3...)
#   {{CONTEXT_STYLE_N_NARRATIVE}}    - Story/context for style issue N
#   {{CONTEXT_STYLE_FIX_N}}          - What specifically to fix
#
# Closing:
#   {{CONTEXT_IMPROVEMENT_COMPLETE}} - Completion message
#
# Layer 1 entities (use within explanatory text):
#   {{hero}}, {{school}}, {{spell1}}, {{item}}, etc.
#
# =============================================================================

"""
{{CONTEXT_FIX_STYLE_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# {{STYLE_1_TITLE}}
# ============================================================
# {{CONTEXT_STYLE_1_NARRATIVE}}

def original_a():
    """ORIGINAL - This code works but has style issues"""
    # [WORKING CODE WITH POOR STYLE]
    pass


def fixed_a():
    # ✏️ FIX THE STYLE ✏️
    #
    # {{CONTEXT_STYLE_FIX_1}}
    #
    # Rewrite the code above with proper style.
    # Changes to make:
    # - [Specific instruction 1]
    # - [Specific instruction 2]
    # - [Etc.]

    # [STUDENT REWRITES CODE HERE]
    pass


# ============================================================
# {{STYLE_2_TITLE}}
# ============================================================
# {{CONTEXT_STYLE_2_NARRATIVE}}

def original_b():
    """ORIGINAL - This code works but has style issues"""
    pass


def fixed_b():
    # ✏️ FIX THE STYLE ✏️
    #
    # {{CONTEXT_STYLE_FIX_2}}
    pass


# [REPEAT PATTERN FOR MORE EXERCISES]


def main():
    print("{{CONTEXT_FIX_STYLE_INTRO}}")
    print("=" * 50)

    print("\n=== {{STYLE_1_TITLE}} ===")
    print("Original (poor style):")
    original_a()
    print("\nFixed (your version):")
    fixed_a()

    print("\n=== {{STYLE_2_TITLE}} ===")
    print("Original (poor style):")
    original_b()
    print("\nFixed (your version):")
    fixed_b()

    print("\n" + "=" * 50)
    print("{{CONTEXT_IMPROVEMENT_COMPLETE}}")


main()


# =============================================================================
# STYLE ISSUES TO TEACH:
# =============================================================================
#
# NAMING (PEP 8):
#   - Variables: lowercase_with_underscores
#   - Constants: UPPERCASE_WITH_UNDERSCORES
#   - Classes: CapitalizedWords
#   - Meaningful names over abbreviations
#
# SPACING (PEP 8):
#   - Spaces around binary operators: x = 1 + 2
#   - No space before colon in slices: list[1:3]
#   - Space after comma: func(a, b, c)
#   - Two blank lines between top-level definitions
#
# STRING FORMATTING:
#   - Prefer f-strings for readability
#   - Avoid: "Hello " + name + "!"
#   - Avoid: "Hello %s" % name
#   - Avoid: "Hello {}".format(name)
#   - Use: f"Hello {name}!"
#
# COMPLEXITY:
#   - Break long lines (79 char limit)
#   - Extract complex expressions into named variables
#   - One statement per line
#
# COMMENTS:
#   - Explain WHY, not WHAT
#   - Remove obvious comments
#   - Use docstrings for functions
#
# =============================================================================
