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

# Exercise N: Code Tracing - [TOPIC]
#
# Trace through the code step by step, tracking variable values.
# Fill in the tracing table to show how values change.
#
# Theme: [THEMED CONTEXT USING {{placeholders}}]


# --- TRACING CHALLENGE [LETTER] ---
# [Description of what pattern this practices]

def code_to_trace_X():
    """Study this code - don't run it yet!"""
    # [CODE TO TRACE]
    # - Should have clear steps that modify state
    # - Each line should be traceable
    pass


def trace_table_X():
    # ✏️ FILL IN THE TRACING TABLE ✏️
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


# [REPEAT PATTERN FOR CHALLENGES B, C, ETC.]


def verify_traces():
    """Run this after completing your traces to check your work"""
    print("=== Trace [LETTER] - Actual Execution ===")
    code_to_trace_X()
    # [REPEAT FOR EACH]


def main():
    print("Complete the tracing tables in trace_table_X functions first!")
    print("Then uncomment the line below to verify your answers.")
    print()

    # Uncomment this line AFTER completing your traces:
    # verify_traces()


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
