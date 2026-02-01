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

# Exercise N: Fix the Style - [TOPIC]
#
# This code WORKS but has terrible style! Fix the issues:
# [LIST SPECIFIC ISSUES TO LOOK FOR]
#
# Theme: [THEMED CONTEXT USING {{placeholders}}]


# ============================================================
# STYLE FIX [LETTER]: [TYPE OF ISSUE]
# ============================================================

def original_X():
    """ORIGINAL - [Describe what's wrong]"""
    # [WORKING CODE WITH POOR STYLE]
    pass


def fixed_X():
    # ✏️ FIX THE STYLE ✏️
    # Rewrite the code above with proper style.
    # Changes to make:
    # - [Specific instruction 1]
    # - [Specific instruction 2]
    # - [Etc.]

    # [STUDENT REWRITES CODE HERE]
    pass


# [REPEAT PATTERN FOR MORE EXERCISES]


def main():
    print("=== Original [LETTER] ([issue type]) ===")
    original_X()
    print("\n=== Fixed [LETTER] (your version) ===")
    fixed_X()

    # [REPEAT FOR EACH EXERCISE]


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
