# Exercise 1: Code Tracing - If/Else Flow
#
# Trace through the code step by step, tracking variable values.
# Fill in the tracing table to show how values change.
#
# Theme: {{school}} sorting ceremony


# --- TRACING CHALLENGE A ---
# Simple if/else with comparison

def code_to_trace_a():
    """Study this code - don't run it yet!"""
    score = 75
    if score >= 60:
        result = "pass"
    else:
        result = "fail"
    print(result)


def trace_table_a():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # | Step | score | score >= 60 | result | Output |
    # |------|-------|-------------|--------|--------|
    # | 1    |       |             |        |        |
    # | 2    |       |             |        |        |
    # | 3    |       |             |        |        |
    #
    # Write your completed table as comments below:
    #
    # Step 1: score = ?
    # Step 2: Is score >= 60? (True or False)
    # Step 3: result = ? and print outputs ?

    pass


# --- TRACING CHALLENGE B ---
# Multiple conditions with elif

def code_to_trace_b():
    """Study this code - don't run it yet!"""
    points = 85

    if points >= 90:
        house = "{{house}}"
    elif points >= 70:
        house = "Ravenclaw"
    elif points >= 50:
        house = "Hufflepuff"
    else:
        house = "Slytherin"

    print(f"Sorted into {house}")


def trace_table_b():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # | Step | points | Condition Checked   | Result | house    |
    # |------|--------|---------------------|--------|----------|
    # | 1    |        |                     |        |          |
    # | 2    |        | points >= 90        |        |          |
    # | 3    |        | points >= 70        |        |          |
    # | 4    |        |                     |        | (output) |
    #
    # Write your completed table as comments below:
    #
    # Remember: Only ONE branch executes! Once a condition is True,
    # the rest are skipped.

    pass


# --- TRACING CHALLENGE C ---
# If with and operator

def code_to_trace_c():
    """Study this code - don't run it yet!"""
    age = 15
    has_wand = True

    if age >= 11 and has_wand:
        status = "Ready for {{school}}"
    else:
        status = "Not ready yet"

    print(status)


def trace_table_c():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # | Step | age | has_wand | age >= 11 | Both True? | status |
    # |------|-----|----------|-----------|------------|--------|
    # | 1    |     |          |           |            |        |
    # | 2    |     |          |           |            |        |
    # | 3    |     |          |           |            |        |
    #
    # Hint: "and" requires BOTH conditions to be True

    pass


# --- TRACING CHALLENGE D ---
# If with or operator

def code_to_trace_d():
    """Study this code - don't run it yet!"""
    is_weekend = False
    is_holiday = True

    if is_weekend or is_holiday:
        activity = "Free practice"
    else:
        activity = "Classes"

    print(activity)


def trace_table_d():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # | Step | is_weekend | is_holiday | Either True? | activity |
    # |------|------------|------------|--------------|----------|
    # | 1    |            |            |              |          |
    # | 2    |            |            |              |          |
    # | 3    |            |            |              |          |
    #
    # Hint: "or" requires at least ONE condition to be True

    pass


# --- TRACING CHALLENGE E ---
# Nested if statements

def code_to_trace_e():
    """Study this code - don't run it yet!"""
    skill = "spells"
    level = 3

    if skill == "spells":
        if level >= 5:
            rank = "Master"
        else:
            rank = "Apprentice"
    else:
        rank = "Beginner"

    print(f"Rank: {rank}")


def trace_table_e():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # | Step | skill    | level | skill=="spells" | level>=5 | rank |
    # |------|----------|-------|-----------------|----------|------|
    # | 1    |          |       |                 |          |      |
    # | 2    |          |       |                 |          |      |
    # | 3    |          |       |                 |          |      |
    # | 4    |          |       |                 |          |      |
    #
    # Hint: First check the outer if, then the inner if

    pass


def verify_traces():
    """Run this after completing your traces to check your work"""
    print("=== Trace A - Actual Execution ===")
    code_to_trace_a()
    print()

    print("=== Trace B - Actual Execution ===")
    code_to_trace_b()
    print()

    print("=== Trace C - Actual Execution ===")
    code_to_trace_c()
    print()

    print("=== Trace D - Actual Execution ===")
    code_to_trace_d()
    print()

    print("=== Trace E - Actual Execution ===")
    code_to_trace_e()


def main():
    print("=== Code Tracing: If/Else Flow ===")
    print()
    print("For each challenge:")
    print("1. Study the code in code_to_trace_X()")
    print("2. Fill in the trace table in trace_table_X()")
    print("3. Run verify_traces() to check your answers!")
    print()
    print("="*50)

    # Uncomment this line AFTER completing your traces:
    # verify_traces()


main()
