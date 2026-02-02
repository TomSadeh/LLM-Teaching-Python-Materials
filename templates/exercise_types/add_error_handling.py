# =============================================================================
# TEMPLATE: Add Error Handling
# =============================================================================
#
# PURPOSE: Students add try/except to code that only handles happy path.
# SKILL: Defensive programming, exception handling, robustness
#
# STRUCTURE:
#   - Provide code that works for good input but crashes on bad input
#   - List specific error cases to handle
#   - Student adds appropriate try/except blocks
#   - Tests verify both happy path and error handling
#
# GUIDELINES:
#   - Original code should CRASH on bad input (to show the problem)
#   - Specify WHICH exceptions to catch (don't use bare except)
#   - Specify WHAT to return/do for each error case
#   - Include realistic error scenarios
#
# COMMON ERROR SCENARIOS:
#   - Division by zero (ZeroDivisionError)
#   - Invalid type conversion (ValueError)
#   - Missing dictionary key (KeyError)
#   - List index out of range (IndexError)
#   - File not found (FileNotFoundError)
#   - Invalid attribute (AttributeError)
#   - None value operations (TypeError)
#
# DIFFICULTY SCALING:
#   - Easy: One exception type, simple handling
#   - Medium: Multiple exception types, different responses
#   - Hard: Nested operations, cleanup required, multiple failure points
#
# =============================================================================
# CONTEXT BLOCKS TO USE:
# =============================================================================
#
# Docstring/Introduction:
#   {{CONTEXT_ERROR_HANDLING_INTRO}} - Main intro for error handling exercises
#   {{CONTEXT_LEARNING_OBJECTIVE}}   - What student will learn
#
# Per-Challenge:
#   {{HANDLING_N_TITLE}}             - Title for handling N (1, 2, 3...)
#   {{CONTEXT_HANDLING_N_NARRATIVE}} - Story/context for handling N
#   {{CONTEXT_HANDLING_HINT_N}}      - Hint for handling N
#
# Closing:
#   {{CONTEXT_ROBUSTNESS_COMPLETE}}  - Completion message
#
# Layer 1 entities (use within explanatory text):
#   {{hero}}, {{school}}, {{spell1}}, {{item}}, etc.
#
# =============================================================================

"""
{{CONTEXT_ERROR_HANDLING_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# {{HANDLING_1_TITLE}}
# ============================================================
# {{CONTEXT_HANDLING_1_NARRATIVE}}

def original_a(params):
    """ORIGINAL: Crashes if [DESCRIBE BAD INPUT]"""
    # [CODE THAT CRASHES ON BAD INPUT]
    pass


def safe_a(params):
    """
    [Same description as original]

    Should handle:
    - [Error case 1] → [What to return/do]
    - [Error case 2] → [What to return/do]
    """
    # ✏️ ADD ERROR HANDLING ✏️
    #
    # {{CONTEXT_HANDLING_HINT_1}}

    # [STUDENT WRAPS CODE IN TRY/EXCEPT]
    pass


# ============================================================
# {{HANDLING_2_TITLE}}
# ============================================================
# {{CONTEXT_HANDLING_2_NARRATIVE}}

def original_b(params):
    """ORIGINAL: Crashes if [DESCRIBE BAD INPUT]"""
    pass


def safe_b(params):
    # ✏️ ADD ERROR HANDLING ✏️
    #
    # {{CONTEXT_HANDLING_HINT_2}}
    pass


# [REPEAT PATTERN FOR MORE EXERCISES]


def main():
    print("{{CONTEXT_ERROR_HANDLING_INTRO}}")
    print("=" * 50)

    print("\n=== {{HANDLING_1_TITLE}} ===")
    # Test happy path
    print(f"Good input: {safe_a(good_input)}")
    # Test error cases
    print(f"Bad input: {safe_a(bad_input)}")

    print("\n=== {{HANDLING_2_TITLE}} ===")
    # [TEST CALLS]

    print("\n" + "=" * 50)
    print("{{CONTEXT_ROBUSTNESS_COMPLETE}}")


main()


# =============================================================================
# ERROR HANDLING PATTERNS:
# =============================================================================
#
# BASIC TRY/EXCEPT:
#   try:
#       risky_operation()
#   except SpecificError:
#       handle_error()
#
# MULTIPLE EXCEPTIONS:
#   try:
#       risky_operation()
#   except ValueError:
#       handle_value_error()
#   except KeyError:
#       handle_key_error()
#
# CATCH MULTIPLE IN ONE:
#   try:
#       risky_operation()
#   except (ValueError, TypeError):
#       handle_type_errors()
#
# WITH ERROR MESSAGE:
#   try:
#       risky_operation()
#   except ValueError as e:
#       print(f"Error: {e}")
#
# WITH FINALLY:
#   try:
#       file = open(path)
#       process(file)
#   except FileNotFoundError:
#       handle_missing()
#   finally:
#       file.close()  # Always runs
#
# WITH ELSE:
#   try:
#       result = risky_operation()
#   except SomeError:
#       handle_error()
#   else:
#       use_result(result)  # Only if no exception
#
# =============================================================================
#
# COMMON EXCEPTIONS TO TEACH:
#   - ValueError: int("abc")
#   - TypeError: "text" + 5
#   - KeyError: dict["missing_key"]
#   - IndexError: list[999]
#   - ZeroDivisionError: 1 / 0
#   - FileNotFoundError: open("missing.txt")
#   - AttributeError: None.method()
#
# =============================================================================
