# =============================================================================
# Code Ordering: Function Structure
# =============================================================================
# Difficulty: 2
# Concepts: Function definition order, calling functions, parameters
# =============================================================================

"""
{{CONTEXT_CODE_ORDERING_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# Challenge A: Basic Function Order
# ============================================================
# {{CONTEXT_ORDERING_1_NARRATIVE}}
#
# Arrange these lines to create and call a function.
#
# SCRAMBLED LINES:
#   greet_visitor()
#   print("Welcome to {{school}}!")
#   def greet_visitor():

def challenge_a():
    # REORDER THE LINES
    #
    # Copy the lines above in the CORRECT order.
    #
    # Hint: A function must be defined before it can be called.
    #       The function body must be indented.

    pass  # Delete this and add the correctly ordered lines


# ============================================================
# Challenge B: Function with Parameter
# ============================================================
# {{CONTEXT_ORDERING_2_NARRATIVE}}
#
# Arrange these lines to create a function with a parameter.
#
# SCRAMBLED LINES:
#   print(f"Hello, {name}!")
#   greet("{{hero}}")
#   def greet(name):
#   print(f"{name} has arrived.")

def challenge_b():
    # REORDER THE LINES
    #
    # Hint: Function definition comes first.
    #       Both print statements are inside the function.
    #       The function call is last.

    pass


# ============================================================
# Challenge C: Multiple Functions
# ============================================================
# {{CONTEXT_ORDERING_3_NARRATIVE}}
#
# Arrange these lines to define two functions and call them.
#
# SCRAMBLED LINES:
#   show_header()
#   def show_header():
#   def show_footer():
#   print("=== End ===")
#   show_footer()
#   print("=== {{school}} ===")

def challenge_c():
    # REORDER THE LINES
    #
    # Hint: Both functions must be defined before they are called.
    #       Each function has one print statement as its body.

    pass


# ============================================================
# Challenge D: Function with Setup
# ============================================================
# {{CONTEXT_ORDERING_4_NARRATIVE}}
#
# Arrange these lines for a function that uses a variable.
#
# SCRAMBLED LINES:
#   print(f"Status: {status}")
#   display_status()
#   status = "Active"
#   def display_status():
#   print(f"Location: {{location}}")

def challenge_d():
    # REORDER THE LINES
    #
    # Hint: Inside the function, create the variable before using it.
    #       Variables defined inside a function are local to it.

    pass


# ============================================================
# Challenge E: Function Call with Arguments
# ============================================================
# {{CONTEXT_ORDERING_5_NARRATIVE}}
#
# Arrange these lines to create and call a function with two parameters.
#
# SCRAMBLED LINES:
#   introduce("{{hero}}", "{{school}}")
#   def introduce(person, place):
#   print(f"{person} attends {place}.")
#   print(f"Welcome, {person}!")

def challenge_e():
    # REORDER THE LINES
    #
    # Hint: Both print statements belong inside the function.
    #       Order them so the welcome comes before the attendance info.

    pass


def main():
    print("{{CONTEXT_CODE_ORDERING_INTRO}}")
    print("=" * 50)

    print("\n=== Challenge A: Basic Function Order ===")
    # challenge_a()  # Uncomment when ordered correctly

    print("\n=== Challenge B: Function with Parameter ===")
    # challenge_b()

    print("\n=== Challenge C: Multiple Functions ===")
    # challenge_c()

    print("\n=== Challenge D: Function with Setup ===")
    # challenge_d()

    print("\n=== Challenge E: Function Call with Arguments ===")
    # challenge_e()

    print("\nReorder each challenge, then uncomment to test!")
    print("{{CONTEXT_ROLE_COMPLETE}}")


main()
