# =============================================================================
# TEMPLATE: Code Ordering
# =============================================================================
#
# PURPOSE: Students arrange scrambled lines into working code.
# SKILL: Understanding program flow, dependencies, structure
#
# STRUCTURE:
#   - Present scrambled lines of code (as comments or strings)
#   - Student copies lines in correct order into function body
#   - Code should run correctly when properly ordered
#
# GUIDELINES:
#   - Lines should be COMPLETE (don't split expressions across lines)
#   - Include INDENTATION in the scrambled lines where relevant
#   - Each challenge should have ONE clear correct order
#   - Don't scramble too many lines (4-8 is ideal)
#   - Choose code where ORDER MATTERS (not just independent statements)
#
# GOOD ORDERING CHALLENGES:
#   - Variable used before defined (must define first)
#   - Loop body must be inside loop
#   - Return must come after computation
#   - Accumulator must be initialized before loop
#   - Close resources after using them
#
# DIFFICULTY SCALING:
#   - Easy: 4-5 lines, obvious dependencies
#   - Medium: 6-8 lines, some lines could go multiple places
#   - Hard: 8+ lines, nested structures, subtle ordering requirements
#
# =============================================================================
# CONTEXT BLOCKS TO USE:
# =============================================================================
#
# Docstring/Introduction:
#   {{CONTEXT_CODE_ORDERING_INTRO}}  - Main intro for ordering exercises
#   {{CONTEXT_LEARNING_OBJECTIVE}}   - What student will learn
#
# Per-Challenge:
#   {{ORDERING_N_TITLE}}             - Title for challenge N (1, 2, 3...)
#   {{CONTEXT_ORDERING_N_NARRATIVE}} - Story/context for challenge N
#   {{CONTEXT_ORDERING_HINT_N}}      - Hint for challenge N
#
# Closing:
#   {{CONTEXT_ROLE_COMPLETE}}        - Completion message
#
# Layer 1 entities (use within explanatory text):
#   {{hero}}, {{school}}, {{spell1}}, {{item}}, etc.
#
# =============================================================================

"""
{{CONTEXT_CODE_ORDERING_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# {{ORDERING_1_TITLE}}
# ============================================================
# {{CONTEXT_ORDERING_1_NARRATIVE}}
#
# SCRAMBLED LINES:
#   [LINE 1 - with proper indentation shown]
#   [LINE 2]
#   [LINE 3]
#   [LINE 4]
#   [ETC.]

def challenge_a():
    # ✏️ REORDER THE LINES ✏️
    # Copy the lines above in the CORRECT order.
    #
    # {{CONTEXT_ORDERING_HINT_1}}

    pass  # Delete this and add the correctly ordered lines


# ============================================================
# {{ORDERING_2_TITLE}}
# ============================================================
# {{CONTEXT_ORDERING_2_NARRATIVE}}
#
# SCRAMBLED LINES:
#   [LINE 1]
#   [LINE 2]
#   [LINE 3]
#   [LINE 4]

def challenge_b():
    # ✏️ REORDER THE LINES ✏️
    #
    # {{CONTEXT_ORDERING_HINT_2}}

    pass


# [REPEAT PATTERN FOR MORE CHALLENGES]


def main():
    print("{{CONTEXT_CODE_ORDERING_INTRO}}")
    print("=" * 50)

    print("\n=== {{ORDERING_1_TITLE}} ===")
    # challenge_a()  # Uncomment when ordered correctly

    print("\n=== {{ORDERING_2_TITLE}} ===")
    # challenge_b()

    print("\nReorder each challenge, then uncomment to test!")
    print("{{CONTEXT_ROLE_COMPLETE}}")


main()


# =============================================================================
# ORDERING CHALLENGE PATTERNS:
# =============================================================================
#
# SETUP -> USE -> CLEANUP:
#   - Open file, read, close
#   - Create list, fill list, process list
#   - Get input, validate, use
#
# INITIALIZE -> LOOP -> RESULT:
#   - total = 0, for loop adding, print total
#   - result = [], for loop appending, return result
#
# DEFINE -> CALL:
#   - def function, then call function
#   - Import, then use imported item
#
# CALCULATE DEPENDENCIES:
#   - Calculate A, calculate B using A, use B
#   - Get user input, convert type, use value
#
# NESTED STRUCTURES:
#   - Outer loop, inner loop (with indentation)
#   - if block, else block (clearly show indentation)
#
# TIPS FOR WRITING CHALLENGES:
#   - Write the working code first, then scramble
#   - Include indentation markers if ambiguous
#   - Test that there's only ONE valid ordering
#   - Avoid red herrings (lines that could go anywhere)
#
# =============================================================================
