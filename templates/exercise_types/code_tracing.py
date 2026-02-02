# =============================================================================
# TEMPLATE: Code Tracing
# =============================================================================
#
# PURPOSE: Students step through code manually, tracking variable values.
# SKILL: Debugging mindset, understanding state changes
#
# STRUCTURE:
#   - Provide code to trace
#   - Provide blank table template for student to fill
#   - Student tracks variable values at each step
#   - Verification section to run and compare
#
# GUIDELINES:
#   - Keep code SHORT (under 15 lines ideally)
#   - Choose code where state CHANGES meaningfully each iteration
#   - Table columns should match variables in the code
#   - Include output column if code prints anything
#
# WHAT MAKES GOOD TRACING EXERCISES:
#   - Loops with accumulators (sum, count, etc.)
#   - Conditionals that sometimes trigger, sometimes don't
#   - Variables that depend on other variables
#   - Swapping, incrementing, or reassigning values
#
# DIFFICULTY SCALING:
#   - Easy: Single loop, 2-3 variables, no conditions
#   - Medium: Loop with condition, 3-4 variables
#   - Hard: Nested loops, multiple conditions, list mutations
#
# =============================================================================
# CONTEXT BLOCKS TO USE:
# =============================================================================
#
# Docstring/Introduction:
#   {{CONTEXT_CODE_TRACING_INTRO}}   - Main intro for tracing exercises
#   {{CONTEXT_LEARNING_OBJECTIVE}}   - What student will learn
#
# Per-Challenge:
#   {{TRACE_N_TITLE}}                - Title for trace N (1, 2, 3...)
#   {{CONTEXT_TRACE_N_NARRATIVE}}    - Story/context for trace N
#   {{CONTEXT_TRACE_HINT_N}}         - Hint for trace N
#
# Closing:
#   {{CONTEXT_VERIFICATION_COMPLETE}} - Completion message
#
# Layer 1 entities (use within explanatory text):
#   {{hero}}, {{school}}, {{spell1}}, {{item}}, etc.
#
# =============================================================================

"""
{{CONTEXT_CODE_TRACING_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# --- {{TRACE_1_TITLE}} ---
# {{CONTEXT_TRACE_1_NARRATIVE}}

def code_to_trace_a():
    """Study this code - don't run it yet!"""
    # [CODE TO TRACE]
    # - Should have clear steps that modify state
    # - Each line should be traceable
    pass


def trace_table_a():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # {{CONTEXT_TRACE_HINT_1}}
    #
    # Complete this table showing variable values at each step.
    # Use None or - for variables that don't exist yet.
    #
    # | Step | [VAR1] | [VAR2] | [VAR3] | Output (if any) |
    # |------|--------|--------|--------|-----------------|
    # | 0    |        |        |        |                 |
    # | 1    |        |        |        |                 |
    # | 2    |        |        |        |                 |
    # | ...  |        |        |        |                 |
    #
    # Write your completed table as comments below:
    #
    # [STUDENT WRITES TABLE HERE]

    pass


# --- {{TRACE_2_TITLE}} ---
# {{CONTEXT_TRACE_2_NARRATIVE}}

def code_to_trace_b():
    """Study this code - don't run it yet!"""
    pass


def trace_table_b():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # {{CONTEXT_TRACE_HINT_2}}
    pass


# [REPEAT PATTERN FOR MORE CHALLENGES]


def verify_traces():
    """Run this after completing your traces to check your work"""
    print("=== {{TRACE_1_TITLE}} - Actual Execution ===")
    code_to_trace_a()

    print("\n=== {{TRACE_2_TITLE}} - Actual Execution ===")
    code_to_trace_b()


def main():
    print("{{CONTEXT_CODE_TRACING_INTRO}}")
    print("=" * 50)
    print()
    print("Complete the tracing tables in trace_table_X functions first!")
    print("Then uncomment the line below to verify your answers.")
    print()

    # Uncomment this line AFTER completing your traces:
    # verify_traces()

    print("{{CONTEXT_VERIFICATION_COMPLETE}}")


main()


# =============================================================================
# TABLE DESIGN TIPS:
# =============================================================================
#
# COLUMNS TO CONSIDER:
#   - Step/iteration number
#   - Each variable that changes
#   - Loop counter (i, index, etc.)
#   - Condition result (True/False)
#   - Output/printed value
#   - Return value (for functions)
#
# GOOD PATTERNS TO TRACE:
#   - Running totals: total = total + x
#   - Counters: count += 1
#   - Max/min finding: if x > best: best = x
#   - List building: result.append(x)
#   - String building: message = message + char
#   - Flag variables: found = True
#
# =============================================================================
