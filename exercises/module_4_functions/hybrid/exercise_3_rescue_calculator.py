# =============================================================================
# Hybrid Exercise: The Rescue - The Broken Calculator
# =============================================================================
# Difficulty: 3
# Arc: Rescue (SETBACK -> INVESTIGATION -> IMPROVEMENT)
# Concepts: Return vs print, debugging, input validation
# =============================================================================

"""
{{CONTEXT_SETBACK_INTRO}}

This is a multi-part exercise. Complete each part in order.

{{mentor}} built a calculator for {{school}}, but it's completely broken!
Students are getting strange results and errors. You need to save the day.
"""


# ============================================================
# PART 1: SETBACK - Understand the Errors
# ============================================================
# {{CONTEXT_SETBACK_INTRO}}
# {{CONTEXT_SETBACK_NARRATIVE}}
#
# The calculator is producing errors. Decode what went wrong.

"""
ERROR MESSAGE 1:
----------------
Traceback (most recent call last):
  File "calculator.py", line 12, in <module>
    final = result * 2
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'

The code that caused this:
    def add(a, b):
        print(a + b)

    result = add(5, 3)
    final = result * 2
"""


def part_1_decode_errors():
    # DECODE THE ERROR
    #
    # Answer these questions:
    #
    # 1. What does "NoneType" mean in Python?
    #    Answer: _______________
    #
    # 2. Why is 'result' equal to None?
    #    Answer: _______________
    #
    # 3. What should the add() function do differently?
    #    Answer: _______________

    # Test your understanding - which function is correct?
    def add_broken(a, b):
        print(a + b)  # This one prints but returns None

    def add_fixed(a, b):
        return a + b  # This one returns the value

    # Run both and see the difference:
    print("Testing broken version:")
    result1 = add_broken(5, 3)
    print(f"Stored result: {result1}")
    print(f"Type: {type(result1)}")

    print("\nTesting fixed version:")
    result2 = add_fixed(5, 3)
    print(f"Stored result: {result2}")
    print(f"Type: {type(result2)}")


# ============================================================
# PART 2: INVESTIGATION - Find and Fix the Bugs
# ============================================================
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# Here's the broken calculator. Find all the bugs!


def buggy_calculator():
    """
    BROKEN CALCULATOR - DO NOT USE!
    This has multiple bugs related to return vs print.
    """
    def add(a, b):
        print(a + b)  # BUG: Should return, not print

    def subtract(a, b):
        result = a - b
        print(result)  # BUG: Should return, not print

    def multiply(a, b):
        a * b  # BUG: Calculates but doesn't return or print!

    def divide(a, b):
        print(a / b)  # BUG: Should return, not print

    # Try to use the calculator
    sum_result = add(10, 5)
    diff_result = subtract(10, 5)
    product = multiply(10, 5)

    # These will all fail because results are None!
    # total = sum_result + diff_result + product


def part_2_fix_the_bugs():
    # FIX THE CALCULATOR
    #
    # Rewrite all four functions to use return instead of print.

    def add(a, b):
        # YOUR FIX HERE
        pass

    def subtract(a, b):
        # YOUR FIX HERE
        pass

    def multiply(a, b):
        # YOUR FIX HERE
        pass

    def divide(a, b):
        # YOUR FIX HERE
        pass

    # Test your fixes
    print("Testing fixed calculator:")
    sum_result = add(10, 5)
    print(f"10 + 5 = {sum_result}")

    diff_result = subtract(10, 5)
    print(f"10 - 5 = {diff_result}")

    product = multiply(10, 5)
    print(f"10 * 5 = {product}")

    quotient = divide(10, 5)
    print(f"10 / 5 = {quotient}")

    # Now we can use the results!
    if sum_result and diff_result and product and quotient:
        total = sum_result + diff_result + product
        print(f"\nSum of results: {total}")


# ============================================================
# PART 3: IMPROVEMENT - Add Input Validation
# ============================================================
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# The calculator works now, but it crashes on bad input.
# Add validation to make it robust.


def part_3_improved_calculator():
    # CREATE AN IMPROVED CALCULATOR
    #
    # Write functions that:
    # 1. Return the calculated value
    # 2. Handle edge cases gracefully

    def safe_add(a, b):
        # YOUR CODE HERE
        #
        # Return a + b
        # This one doesn't need special validation
        pass

    def safe_subtract(a, b):
        # YOUR CODE HERE
        #
        # Return a - b
        pass

    def safe_multiply(a, b):
        # YOUR CODE HERE
        #
        # Return a * b
        pass

    def safe_divide(a, b):
        # YOUR CODE HERE
        #
        # Return a / b if b is not zero
        # If b is zero, return None (can't divide by zero)
        #
        # Hint: Check if b == 0 before dividing
        pass

    # Test normal operations
    print("Testing improved calculator:")
    print(f"15 + 7 = {safe_add(15, 7)}")
    print(f"15 - 7 = {safe_subtract(15, 7)}")
    print(f"15 * 7 = {safe_multiply(15, 7)}")
    print(f"15 / 3 = {safe_divide(15, 3)}")

    # Test edge case: division by zero
    print("\nTesting division by zero:")
    result = safe_divide(10, 0)
    if result is None:
        print("Cannot divide by zero! (Handled gracefully)")
    else:
        print(f"10 / 0 = {result}")


# ============================================================
# FINAL CHALLENGE: Complete Calculator
# ============================================================

def final_calculator():
    # CREATE THE FINAL CALCULATOR
    #
    # Put it all together: a working calculator with proper returns.

    def calculate(operation, a, b):
        """
        Perform a calculation based on the operation.

        Args:
            operation: One of "add", "subtract", "multiply", "divide"
            a: First number
            b: Second number

        Returns:
            The result of the operation, or None if invalid
        """
        # YOUR CODE HERE
        #
        # Use if/elif/else to check the operation and return the result
        # Handle division by zero by returning None
        #
        # Hint:
        # if operation == "add":
        #     return a + b
        # elif operation == "subtract":
        #     ...
        pass

    # Test the complete calculator
    print("\n=== Complete Calculator ===")
    print(f"add(20, 5) = {calculate('add', 20, 5)}")
    print(f"subtract(20, 5) = {calculate('subtract', 20, 5)}")
    print(f"multiply(20, 5) = {calculate('multiply', 20, 5)}")
    print(f"divide(20, 5) = {calculate('divide', 20, 5)}")
    print(f"divide(20, 0) = {calculate('divide', 20, 0)}")


def main():
    print("=" * 60)
    print("THE RESCUE: The Broken Calculator")
    print("=" * 60)
    print("{{CONTEXT_SETBACK_INTRO}}")

    print("\n--- PART 1: SETBACK - Decode the Error ---")
    part_1_decode_errors()

    print("\n--- PART 2: INVESTIGATION - Fix the Bugs ---")
    print("\nBuggy calculator (for reference - don't run):")
    print("def add(a, b): print(a + b)  # Wrong!")
    print("def add(a, b): return a + b  # Correct!")
    print("\nYour fixed calculator:")
    part_2_fix_the_bugs()

    print("\n--- PART 3: IMPROVEMENT - Add Validation ---")
    part_3_improved_calculator()

    print("\n--- FINAL CHALLENGE ---")
    final_calculator()

    print("\n" + "=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print("\nKey Lessons:")
    print("1. Functions should RETURN values, not just PRINT them")
    print("2. return sends data back to your code")
    print("3. print() only displays to humans, returns None")
    print("4. Always validate inputs for edge cases")


main()
