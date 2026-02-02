# =============================================================================
# TEMPLATE: Simplify This
# =============================================================================
#
# PURPOSE: Students rewrite verbose code more elegantly.
# SKILL: Pythonic idioms, recognizing patterns, conciseness
#
# STRUCTURE:
#   - Provide working but overly-complex code
#   - Student rewrites to be simpler while keeping same behavior
#   - Tests verify both versions produce identical results
#
# GUIDELINES:
#   - Original code must be CORRECT (just verbose)
#   - The simplification should be SUBSTANTIAL (not trivial)
#   - There should be a clearly "better" Pythonic way
#   - Explain what kind of simplification to look for
#
# SIMPLIFICATION PATTERNS:
#   - Manual loops → list comprehensions
#   - if x == True → if x
#   - Manual counting → len() or .count()
#   - Manual string building → .join()
#   - Manual max/min finding → max()/min()
#   - Repeated code → loop or function
#   - Complex conditionals → dictionary lookup
#   - Manual enumerate → enumerate()
#
# DIFFICULTY SCALING:
#   - Easy: One obvious simplification
#   - Medium: Multiple simplifications possible
#   - Hard: Requires knowing less-common Python features
#
# =============================================================================

# Exercise N: Simplify This - [TOPIC]
#
# Each piece of code works but is more complex than needed.
# Rewrite each one to be simpler while keeping the same behavior.
#
# Theme: [THEMED CONTEXT USING {{placeholders}}]


# ============================================================
# SIMPLIFY [LETTER]: [PATTERN NAME]
# ============================================================

def original_X(params):
    """ORIGINAL: [Describe the verbosity]"""
    # [WORKING BUT OVERLY VERBOSE CODE]
    pass


def simplified_X(params):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: [WHAT PYTHON FEATURE TO USE]

    # [STUDENT REWRITES CODE HERE]
    pass


# [REPEAT PATTERN FOR MORE EXERCISES]


def main():
    print("=== Test [LETTER]: [PATTERN NAME] ===")
    test_input = ...
    print(f"Original: {original_X(test_input)}")
    print(f"Simplified: {simplified_X(test_input)}")
    # Verify outputs match

    # [REPEAT FOR EACH EXERCISE]


main()


# =============================================================================
# SIMPLIFICATION PATTERNS TO TEACH:
# =============================================================================
#
# BOOLEAN SIMPLIFICATION:
#   # Verbose:
#   if condition:
#       return True
#   else:
#       return False
#   # Simple:
#   return condition
#
# CONDITIONAL ASSIGNMENT:
#   # Verbose:
#   if condition:
#       x = value1
#   else:
#       x = value2
#   # Simple:
#   x = value1 if condition else value2
#
# LIST BUILDING:
#   # Verbose:
#   result = []
#   for item in items:
#       result.append(transform(item))
#   # Simple:
#   result = [transform(item) for item in items]
#
# FILTERING:
#   # Verbose:
#   result = []
#   for item in items:
#       if condition(item):
#           result.append(item)
#   # Simple:
#   result = [item for item in items if condition(item)]
#
# STRING JOINING:
#   # Verbose:
#   result = ""
#   for item in items:
#       result = result + item + ", "
#   result = result[:-2]
#   # Simple:
#   result = ", ".join(items)
#
# COUNTING:
#   # Verbose:
#   count = 0
#   for item in items:
#       if item == target:
#           count += 1
#   # Simple:
#   count = items.count(target)
#
# DICTIONARY FROM PAIRS:
#   # Verbose:
#   d = {}
#   for key, value in pairs:
#       d[key] = value
#   # Simple:
#   d = dict(pairs)
#
# SUM/MAX/MIN:
#   # Verbose:
#   total = 0
#   for num in numbers:
#       total += num
#   # Simple:
#   total = sum(numbers)
#
# =============================================================================
