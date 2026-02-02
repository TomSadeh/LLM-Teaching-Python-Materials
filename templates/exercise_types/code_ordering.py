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

# Exercise N: Code Ordering - [TOPIC]
#
# The lines of code are scrambled! Put them in the correct order
# to make the program work properly.
#
# Theme: [THEMED CONTEXT USING {{placeholders}}]


# ============================================================
# ORDERING CHALLENGE [LETTER]: [DESCRIPTION]
# ============================================================
#
# [Explain what the code should do when correctly ordered]
#
# SCRAMBLED LINES:
#   [LINE 1 - with proper indentation shown]
#   [LINE 2]
#   [LINE 3]
#   [LINE 4]
#   [ETC.]

def challenge_X():
    # ✏️ REORDER THE LINES ✏️
    # Copy the lines above in the CORRECT order:
    # Remember: [SPECIFIC HINT ABOUT DEPENDENCIES]

    pass  # Delete this and add the correctly ordered lines


# [REPEAT PATTERN FOR MORE CHALLENGES]


def main():
    print("=== Challenge [LETTER]: [DESCRIPTION] ===")
    # challenge_X()  # Uncomment when ordered correctly

    # [REPEAT FOR EACH CHALLENGE]

    print("\nReorder each challenge, then uncomment to test!")


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
