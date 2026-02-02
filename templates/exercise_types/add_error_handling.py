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

# Exercise N: Add Error Handling - [TOPIC]
#
# Each function works for good input but crashes on bad input.
# Add try/except blocks to handle errors gracefully.
#
# Theme: [THEMED CONTEXT USING {{placeholders}}]


# ============================================================
# ERROR HANDLING [LETTER]: [ERROR TYPE]
# ============================================================

def original_X(params):
    """ORIGINAL: Crashes if [DESCRIBE BAD INPUT]"""
    # [CODE THAT CRASHES ON BAD INPUT]
    pass


def safe_X(params):
    """
    [Same description as original]

    Should handle:
    - [Error case 1] → [What to return/do]
    - [Error case 2] → [What to return/do]
    """
    # ✏️ ADD ERROR HANDLING ✏️

    # [STUDENT WRAPS CODE IN TRY/EXCEPT]
    pass


# [REPEAT PATTERN FOR MORE EXERCISES]


def main():
    print("=== Test [LETTER]: [ERROR TYPE] ===")

    # Test happy path
    print(f"Good input: {safe_X(good_input)}")

    # Test error cases
    print(f"Bad input: {safe_X(bad_input)}")

    # [REPEAT FOR EACH EXERCISE]


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
