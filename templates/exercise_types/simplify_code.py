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
# CONTEXT BLOCKS TO USE:
# =============================================================================
#
# Docstring/Introduction:
#   {{CONTEXT_SIMPLIFY_CODE_INTRO}}  - Main intro for simplification exercises
#   {{CONTEXT_LEARNING_OBJECTIVE}}   - What student will learn
#
# Per-Challenge:
#   {{SIMPLIFY_N_TITLE}}             - Title for simplification N (1, 2, 3...)
#   {{CONTEXT_SIMPLIFY_N_NARRATIVE}} - Story/context for simplification N
#   {{CONTEXT_SIMPLIFY_HINT_N}}      - Hint for simplification N
#
# Closing:
#   {{CONTEXT_IMPROVEMENT_COMPLETE}} - Completion message
#
# Layer 1 entities (use within explanatory text):
#   {{hero}}, {{school}}, {{spell1}}, {{item}}, etc.
#
# =============================================================================

"""
{{CONTEXT_SIMPLIFY_CODE_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# {{SIMPLIFY_1_TITLE}}
# ============================================================
# {{CONTEXT_SIMPLIFY_1_NARRATIVE}}

def original_a(params):
    """ORIGINAL: [Describe the verbosity]"""
    # [WORKING BUT OVERLY VERBOSE CODE]
    pass


def simplified_a(params):
    # ✏️ SIMPLIFY THIS ✏️
    #
    # {{CONTEXT_SIMPLIFY_HINT_1}}

    # [STUDENT REWRITES CODE HERE]
    pass


# ============================================================
# {{SIMPLIFY_2_TITLE}}
# ============================================================
# {{CONTEXT_SIMPLIFY_2_NARRATIVE}}

def original_b(params):
    """ORIGINAL: [Describe the verbosity]"""
    pass


def simplified_b(params):
    # ✏️ SIMPLIFY THIS ✏️
    #
    # {{CONTEXT_SIMPLIFY_HINT_2}}
    pass


# [REPEAT PATTERN FOR MORE EXERCISES]


def main():
    print("{{CONTEXT_SIMPLIFY_CODE_INTRO}}")
    print("=" * 50)

    print("\n=== {{SIMPLIFY_1_TITLE}} ===")
    test_input = ...
    print(f"Original: {original_a(test_input)}")
    print(f"Simplified: {simplified_a(test_input)}")

    print("\n=== {{SIMPLIFY_2_TITLE}} ===")
    # [TEST CALLS]

    print("\n" + "=" * 50)
    print("{{CONTEXT_IMPROVEMENT_COMPLETE}}")


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
