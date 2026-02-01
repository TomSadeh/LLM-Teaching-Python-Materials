# Exercise 1: Code Tracing - Dictionary Updates
#
# Trace through the code step by step, tracking dictionary contents.
# Fill in the tracing table to show how the dictionary changes.
#
# Theme: Tracking {{hero}}'s inventory and stats


# --- TRACING CHALLENGE A: Basic Updates ---
# Track how dictionary values change with assignments.

def code_to_trace_a():
    """Study this code - don't run it yet!"""
    inventory = {}
    inventory["wand"] = 1
    inventory["potion"] = 3
    inventory["potion"] = inventory["potion"] + 2
    inventory["book"] = 5
    del inventory["potion"]

    print(f"Final inventory: {inventory}")


def trace_table_a():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # Track the dictionary contents after each operation.
    #
    # | Step | Operation                      | inventory                    |
    # |------|--------------------------------|------------------------------|
    # | 0    | inventory = {}                 | {}                           |
    # | 1    | inventory["wand"] = 1          | ?                            |
    # | 2    | inventory["potion"] = 3        | ?                            |
    # | 3    | inventory["potion"] += 2       | ?                            |
    # | 4    | inventory["book"] = 5          | ?                            |
    # | 5    | del inventory["potion"]        | ?                            |
    #
    # Write your completed table below:
    #
    # Final inventory: ?

    pass


# --- TRACING CHALLENGE B: Loop Updates ---
# Track dictionary changes in a loop.

def code_to_trace_b():
    """Study this code - don't run it yet!"""
    counts = {}
    items = ["{{spell1}}", "{{spell2}}", "{{spell1}}", "{{spell1}}", "{{spell2}}"]

    for item in items:
        if item in counts:
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1

    print(f"Final counts: {counts}")


def trace_table_b():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # Track counts dict after processing each item.
    #
    # | Step | item        | item in counts? | counts after this step         |
    # |------|-------------|-----------------|--------------------------------|
    # | 0    | (start)     | -               | {}                             |
    # | 1    | "{{spell1}}"| ?               | ?                              |
    # | 2    | "{{spell2}}"| ?               | ?                              |
    # | 3    | "{{spell1}}"| ?               | ?                              |
    # | 4    | "{{spell1}}"| ?               | ?                              |
    # | 5    | "{{spell2}}"| ?               | ?                              |
    #
    # Write your completed table below:
    #
    # Final counts: ?

    pass


# --- TRACING CHALLENGE C: Nested Dictionary ---
# Track changes to nested dictionary structure.

def code_to_trace_c():
    """Study this code - don't run it yet!"""
    students = {}
    students["{{hero}}"] = {"house": "{{house}}", "year": 1}
    students["{{hero}}"]["year"] = 2
    students["{{heroine}}"] = {"house": "{{house}}", "year": 2}
    students["{{hero}}"]["pet"] = "{{pet}}"

    print(f"Final students: {students}")


def trace_table_c():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # Track the nested structure at each step.
    #
    # | Step | Operation                               | students                                    |
    # |------|-----------------------------------------|---------------------------------------------|
    # | 0    | students = {}                           | {}                                          |
    # | 1    | students["{{hero}}"] = {...}            | ?                                           |
    # | 2    | students["{{hero}}"]["year"] = 2        | ?                                           |
    # | 3    | students["{{heroine}}"] = {...}         | ?                                           |
    # | 4    | students["{{hero}}"]["pet"] = "{{pet}}" | ?                                           |
    #
    # Write your completed table below:

    pass


# --- TRACING CHALLENGE D: Dictionary with .get() ---
# Track how .get() handles missing keys.

def code_to_trace_d():
    """Study this code - don't run it yet!"""
    scores = {"{{hero}}": 85}

    result1 = scores.get("{{hero}}", 0)
    result2 = scores.get("{{friend}}", 0)
    result3 = scores.get("{{heroine}}")

    scores["{{friend}}"] = scores.get("{{friend}}", 0) + 10

    print(f"result1={result1}, result2={result2}, result3={result3}")
    print(f"scores={scores}")


def trace_table_d():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # Remember: .get(key, default) returns value if key exists, else default
    # If no default given, returns None for missing keys
    #
    # | Step | Expression                          | Result | scores after          |
    # |------|-------------------------------------|--------|----------------------|
    # | 0    | scores = {"{{hero}}": 85}           | -      | {"{{hero}}": 85}     |
    # | 1    | scores.get("{{hero}}", 0)           | ?      | (unchanged)          |
    # | 2    | scores.get("{{friend}}", 0)         | ?      | (unchanged)          |
    # | 3    | scores.get("{{heroine}}")           | ?      | (unchanged)          |
    # | 4    | scores["{{friend}}"] = ... + 10     | -      | ?                    |
    #
    # Write your completed table below:

    pass


# --- TRACING CHALLENGE E: Dictionary Comprehension Equivalent ---
# Trace building a dictionary from another dictionary.

def code_to_trace_e():
    """Study this code - don't run it yet!"""
    original = {"a": 1, "b": 2, "c": 3}
    doubled = {}

    for key, value in original.items():
        doubled[key] = value * 2

    print(f"doubled: {doubled}")


def trace_table_e():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # Track doubled dict as we iterate through original.items()
    #
    # | Step | key | value | doubled after this iteration |
    # |------|-----|-------|------------------------------|
    # | 0    | -   | -     | {}                           |
    # | 1    | "a" | 1     | ?                            |
    # | 2    | "b" | 2     | ?                            |
    # | 3    | "c" | 3     | ?                            |
    #
    # Write your completed table below:

    pass


# --- TRACING CHALLENGE F: setdefault Pattern ---
# Track how setdefault initializes missing keys.

def code_to_trace_f():
    """Study this code - don't run it yet!"""
    groups = {}
    items = [("{{house}}", "{{hero}}"), ("Ravenclaw", "{{friend}}"), ("{{house}}", "{{heroine}}")]

    for house, name in items:
        groups.setdefault(house, []).append(name)

    print(f"groups: {groups}")


def trace_table_f():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # setdefault(key, default) returns existing value if key exists,
    # otherwise sets key to default and returns default.
    # Here it returns a list that we then append to.
    #
    # | Step | house       | name         | setdefault returns | groups after        |
    # |------|-------------|--------------|-------------------|---------------------|
    # | 0    | -           | -            | -                 | {}                  |
    # | 1    | "{{house}}" | "{{hero}}"   | ? (new or existing?)| ?                 |
    # | 2    | "Ravenclaw" | "{{friend}}" | ?                 | ?                   |
    # | 3    | "{{house}}" | "{{heroine}}"| ?                 | ?                   |
    #
    # Write your completed table below:

    pass


def verify_traces():
    """Run this after completing your traces to check your work"""

    print("=== Trace A - Basic Updates ===")
    inventory = {}
    inventory["wand"] = 1
    inventory["potion"] = 3
    inventory["potion"] = inventory["potion"] + 2
    inventory["book"] = 5
    del inventory["potion"]
    print(f"Actual: {inventory}")

    print("\n=== Trace B - Loop Updates ===")
    counts = {}
    items = ["{{spell1}}", "{{spell2}}", "{{spell1}}", "{{spell1}}", "{{spell2}}"]
    for item in items:
        if item in counts:
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1
    print(f"Actual: {counts}")

    print("\n=== Trace C - Nested Dictionary ===")
    students = {}
    students["{{hero}}"] = {"house": "{{house}}", "year": 1}
    students["{{hero}}"]["year"] = 2
    students["{{heroine}}"] = {"house": "{{house}}", "year": 2}
    students["{{hero}}"]["pet"] = "{{pet}}"
    print(f"Actual: {students}")

    print("\n=== Trace D - Dictionary with .get() ===")
    scores = {"{{hero}}": 85}
    result1 = scores.get("{{hero}}", 0)
    result2 = scores.get("{{friend}}", 0)
    result3 = scores.get("{{heroine}}")
    scores["{{friend}}"] = scores.get("{{friend}}", 0) + 10
    print(f"result1={result1}, result2={result2}, result3={result3}")
    print(f"scores={scores}")

    print("\n=== Trace E - Building Dictionary ===")
    original = {"a": 1, "b": 2, "c": 3}
    doubled = {}
    for key, value in original.items():
        doubled[key] = value * 2
    print(f"Actual: {doubled}")

    print("\n=== Trace F - setdefault Pattern ===")
    groups = {}
    items = [("{{house}}", "{{hero}}"), ("Ravenclaw", "{{friend}}"), ("{{house}}", "{{heroine}}")]
    for house, name in items:
        groups.setdefault(house, []).append(name)
    print(f"Actual: {groups}")


def main():
    print("Complete the tracing tables in trace_table_X functions first!")
    print("Then uncomment the line below to verify your answers.")
    print()
    print("Remember:")
    print("- dict[key] = value adds or updates a key")
    print("- del dict[key] removes a key")
    print("- dict.get(key, default) returns value or default")
    print("- dict.setdefault(key, default) returns existing or sets default")
    print()

    # Uncomment this line AFTER completing your traces:
    # verify_traces()


main()
