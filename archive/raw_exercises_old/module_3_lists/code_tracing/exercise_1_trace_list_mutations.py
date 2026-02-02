# Exercise 1: Code Tracing - List Mutations
#
# Trace through the code step by step, tracking how lists change.
# Fill in the tracing table to show the list state at each step.
#
# Theme: {{hero}}'s inventory management


# --- TRACING CHALLENGE A ---
# Basic list operations

def code_to_trace_a():
    """Study this code - don't run it yet!"""
    items = ["wand", "cloak"]
    items.append("map")
    items.append("stone")
    print(items)
    print(len(items))


def trace_table_a():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # | Step | Operation          | items                          | len(items) |
    # |------|--------------------|--------------------------------|------------|
    # | 1    | Create list        |                                |            |
    # | 2    | append("map")      |                                |            |
    # | 3    | append("stone")    |                                |            |
    # | 4    | print items        |                                |            |
    # | 5    | print len(items)   |                                |            |
    #
    # Write your completed table as comments below:

    pass


# --- TRACING CHALLENGE B ---
# List with indexing

def code_to_trace_b():
    """Study this code - don't run it yet!"""
    spells = ["{{spell1}}", "{{spell2}}", "{{spell3}}"]
    print(spells[0])
    print(spells[-1])
    spells[1] = "{{spell4}}"
    print(spells)


def trace_table_b():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # | Step | Operation          | spells                                    | Output |
    # |------|--------------------|-------------------------------------------|--------|
    # | 1    | Create list        |                                           |        |
    # | 2    | print spells[0]    |                                           |        |
    # | 3    | print spells[-1]   |                                           |        |
    # | 4    | spells[1] = ...    |                                           |        |
    # | 5    | print spells       |                                           |        |
    #
    # Hint: [0] is first item, [-1] is last item

    pass


# --- TRACING CHALLENGE C ---
# Loop over list with accumulator

def code_to_trace_c():
    """Study this code - don't run it yet!"""
    prices = [10, 25, 15]
    total = 0
    for price in prices:
        total = total + price
    print(total)


def trace_table_c():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # | Iteration | price | total (before) | total (after) |
    # |-----------|-------|----------------|---------------|
    # | 1         |       |                |               |
    # | 2         |       |                |               |
    # | 3         |       |                |               |
    # | Final     | -     |                | Output: ?     |
    #
    # Hint: Track total before and after adding each price

    pass


# --- TRACING CHALLENGE D ---
# Building a new list in a loop

def code_to_trace_d():
    """Study this code - don't run it yet!"""
    numbers = [1, 2, 3]
    doubled = []
    for n in numbers:
        doubled.append(n * 2)
    print(doubled)


def trace_table_d():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # | Iteration | n | n * 2 | doubled (after append)   |
    # |-----------|---|-------|--------------------------|
    # | Start     | - | -     | []                       |
    # | 1         |   |       |                          |
    # | 2         |   |       |                          |
    # | 3         |   |       |                          |
    # | Final     | - | -     | Output: ?                |
    #
    # Track how doubled grows with each iteration

    pass


# --- TRACING CHALLENGE E ---
# Filtering with conditions

def code_to_trace_e():
    """Study this code - don't run it yet!"""
    scores = [85, 42, 91, 55, 78]
    passing = []
    for score in scores:
        if score >= 60:
            passing.append(score)
    print(passing)
    print(len(passing))


def trace_table_e():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # | Iteration | score | score >= 60 | passing (after)     |
    # |-----------|-------|-------------|---------------------|
    # | Start     | -     | -           | []                  |
    # | 1         |       |             |                     |
    # | 2         |       |             |                     |
    # | 3         |       |             |                     |
    # | 4         |       |             |                     |
    # | 5         |       |             |                     |
    # | Final     | -     | -           | Output: ? (len: ?)  |
    #
    # Only append when condition is True!

    pass


# --- TRACING CHALLENGE F ---
# Using pop() and insert()

def code_to_trace_f():
    """Study this code - don't run it yet!"""
    queue = ["{{hero}}", "{{friend}}", "{{mentor}}"]
    first = queue.pop(0)
    print(f"{first} is served")
    queue.insert(0, "{{villain}}")
    print(queue)


def trace_table_f():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # | Step | Operation        | first | queue                              |
    # |------|------------------|-------|-------------------------------------|
    # | 1    | Create queue     | -     |                                     |
    # | 2    | pop(0)           |       |                                     |
    # | 3    | print first      |       | (output: "? is served")             |
    # | 4    | insert(0, ...)   |       |                                     |
    # | 5    | print queue      |       |                                     |
    #
    # pop(0) removes and returns first item
    # insert(0, x) adds x at the beginning

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
    print()

    print("=== Trace F - Actual Execution ===")
    code_to_trace_f()


def main():
    print("=== Code Tracing: List Mutations ===")
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
