# =============================================================================
# TEMPLATE: Fill in the Blanks
# =============================================================================
#
# PURPOSE: Students complete code by filling strategic gaps.
# SKILL: Syntax recall, understanding code structure
#
# STRUCTURE:
#   - Provide mostly-complete code with ___ blanks
#   - Each blank should have ONE correct answer (or limited valid options)
#   - Include hints to guide toward the answer
#   - Code should work when blanks are filled correctly
#
# GUIDELINES:
#   - Use ___ (triple underscore) for blanks
#   - Each blank = ONE concept (keyword, operator, method name, etc.)
#   - Don't blank out too much - context should make answer guessable
#   - Include hint comment near each blank
#   - Blanks should test RECALL, not problem-solving
#
# WHAT TO BLANK OUT:
#   - Keywords: def, return, if, else, for, while, in, and, or, not
#   - Operators: ==, !=, >, <, >=, <=, +, -, *, /, //, %
#   - Method names: .append(), .split(), .join(), .get(), etc.
#   - Built-in functions: len(), range(), print(), int(), str()
#   - String prefixes: f for f-strings
#   - Special values: True, False, None
#
# DIFFICULTY SCALING:
#   - Easy: Common keywords, single blanks, strong context
#   - Medium: Method names, multiple blanks per exercise
#   - Hard: Subtle operators, less context, chained operations
#
# =============================================================================
# CONTEXT BLOCKS TO USE:
# =============================================================================
#
# Docstring/Introduction:
#   {{CONTEXT_FILL_BLANKS_INTRO}}    - Main intro for fill-blanks exercises
#   {{CONTEXT_LEARNING_OBJECTIVE}}   - What student will learn
#
# Per-Exercise:
#   {{EXERCISE_N_TITLE}}             - Title for exercise N (1, 2, 3...)
#   {{CONTEXT_EXERCISE_N_NARRATIVE}} - Story/context for exercise N
#   {{CONTEXT_FILL_BLANKS_HINT_N}}   - Hint for exercise N
#
# Closing:
#   {{CONTEXT_ROLE_COMPLETE}}        - Completion message
#
# Layer 1 entities (use within explanatory text):
#   {{hero}}, {{school}}, {{spell1}}, {{item}}, etc.
#
# =============================================================================

"""
{{CONTEXT_FILL_BLANKS_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# --- {{EXERCISE_1_TITLE}} ---
# {{CONTEXT_EXERCISE_1_NARRATIVE}}

def exercise_a():
    # ✏️ FILL IN THE BLANKS ✏️

    # [LINE OF CODE WITH ___]  # Hint: {{CONTEXT_FILL_BLANKS_HINT_1}}
    # [MORE LINES AS NEEDED]
    pass


# --- {{EXERCISE_2_TITLE}} ---
# {{CONTEXT_EXERCISE_2_NARRATIVE}}

def exercise_b():
    # ✏️ FILL IN THE BLANKS ✏️

    # [LINE OF CODE WITH ___]  # Hint: {{CONTEXT_FILL_BLANKS_HINT_2}}
    pass


# [REPEAT PATTERN FOR MORE EXERCISES]


def main():
    print("{{CONTEXT_FILL_BLANKS_INTRO}}")
    print("=" * 50)

    print("\n=== {{EXERCISE_1_TITLE}} ===")
    # exercise_a()  # Uncomment when you've filled the blanks

    print("\n=== {{EXERCISE_2_TITLE}} ===")
    # exercise_b()

    print("\nFill in all the blanks, then uncomment to test!")
    print("{{CONTEXT_ROLE_COMPLETE}}")


main()


# =============================================================================
# BLANK PATTERNS BY CONCEPT:
# =============================================================================
#
# LOOPS:
#   ___ i in range(10):          # for
#   for item ___ collection:     # in
#   ___(1, 10):                  # range
#
# CONDITIONALS:
#   ___ condition:               # if
#   ___:                         # else (after if block)
#   ___ other_condition:         # elif
#
# FUNCTIONS:
#   ___ function_name():         # def
#   ___ result                   # return
#
# OPERATORS:
#   if x ___ y:                  # ==, >, <, etc.
#   total = total ___ item       # +, -, etc.
#
# COLLECTIONS:
#   my_list.___(item)            # append
#   len = ___(my_list)           # len
#   value = my_dict.___(key, default)  # get
#
# STRINGS:
#   ___"Hello, {name}"           # f (f-string prefix)
#   text.___()                   # upper, lower, strip, split
#
# =============================================================================
