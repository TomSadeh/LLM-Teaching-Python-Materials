# =============================================================================
# TEMPLATE: Write Code
# =============================================================================
#
# PURPOSE: Students write code following instructions to solve tasks.
# SKILL: Core programming, applying concepts, problem-solving
#
# STRUCTURE:
#   - Clear task description with context
#   - Step-by-step instructions in comments
#   - Hints when helpful
#   - Pass placeholder for student code
#
# GUIDELINES:
#   - Each function should focus on ONE concept/task
#   - Use {{placeholders}} for themed content (REQUIRED - at least one per file)
#   - Progressive difficulty within the file
#   - Instructions should be unambiguous
#   - Include hints for non-obvious steps
#
# DIFFICULTY SCALING:
#   - Easy: Single concept, explicit instructions
#   - Medium: Combine 2-3 concepts, some inference required
#   - Hard: Integration, problem decomposition, minimal guidance
#
# =============================================================================
# CONTEXT BLOCKS TO USE:
# =============================================================================
#
# Docstring/Introduction:
#   {{CONTEXT_PROJECT_INTRO}}        - Sets up the overall project/task
#   {{CONTEXT_LEARNING_OBJECTIVE}}   - What student will learn
#
# Per-Phase/Exercise:
#   {{PHASE_N_TITLE}}                - Title for phase N (1, 2, 3...)
#   {{CONTEXT_PHASE_N}}              - Narrative context for phase N
#   {{CONTEXT_STUDENT_TASK}}         - What the student needs to do
#   {{CONTEXT_IMPLEMENTATION_GUIDANCE}} - Tips for writing code
#
# Closing:
#   {{CONTEXT_FINAL_ASSEMBLY}}       - Completion message
#
# Layer 1 entities (use within explanatory text):
#   {{hero}}, {{school}}, {{spell1}}, {{item}}, etc.
#
# =============================================================================

"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""

# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # Step 1: [First action to take]
    # Step 2: [Second action to take]
    #
    # Hint: {{CONTEXT_IMPLEMENTATION_GUIDANCE}}
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # [Instructions...]
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # [Instructions...]
    pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)

    print("\n=== {{PHASE_1_TITLE}} ===")
    exercise_a()

    print("\n=== {{PHASE_2_TITLE}} ===")
    exercise_b()

    print("\n=== {{PHASE_3_TITLE}} ===")
    exercise_c()

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()


# =============================================================================
# PLACEHOLDER EXAMPLES:
# =============================================================================
#
# Characters:
#   hero = "{{hero}}"
#   print(f"{{heroine}} casts {{spell1}}!")
#   villain_name = "{{villain}}"
#
# Places:
#   location = "{{school}}"
#   print(f"Welcome to {{place}}!")
#
# Objects:
#   inventory = ["{{item}}", "{{pet}}"]
#   transport = "{{transport}}"
#
# Phrases:
#   print("{{exclamation}}")
#   secret = "{{password}}"
#
# REMEMBER: Every exercise file must have at least ONE placeholder!
#
# =============================================================================
# INSTRUCTION PATTERNS:
# =============================================================================
#
# For variables:
#   "Create a variable called 'x' with the value ___"
#
# For printing:
#   "Print: [exact output format]"
#   "Display the result using an f-string"
#
# For input:
#   "Ask the user for their ___"
#   "Store the input in a variable called ___"
#
# For loops:
#   "Use a for loop to iterate over ___"
#   "Repeat N times using a loop"
#
# For conditions:
#   "If ___ is true, then ___"
#   "Check whether ___ and respond accordingly"
#
# For functions:
#   "Create a function called ___ that takes ___"
#   "Return the result instead of printing it"
#
# =============================================================================
