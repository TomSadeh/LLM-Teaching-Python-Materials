"""
{{CONTEXT_CODE_TRACING_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

Trace through dictionary mutations to understand how
dictionaries change over multiple operations.
"""


# --- {{TRACE_1_TITLE}} ---
# {{CONTEXT_TRACE_1_NARRATIVE}}


def code_to_trace_a():
    """Study this code - don't run it yet!"""
    inventory = {"{{item}}": 2}
    inventory["{{item}}"] = inventory["{{item}}"] + 3
    inventory["{{spell1}}"] = 1
    del inventory["{{item}}"]
    print(inventory)


def trace_table_a():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # {{CONTEXT_TRACE_HINT_1}}
    #
    # Track the dictionary contents at each step.
    #
    # | Step | inventory contents             | Output (if any) |
    # |------|--------------------------------|-----------------|
    # | 0    | {"{{item}}": 2}                |                 |
    # | 1    |                                |                 |
    # | 2    |                                |                 |
    # | 3    |                                |                 |
    # | 4    |                                |                 |
    #
    # Write your completed table as comments below:
    #

    pass


# --- {{TRACE_2_TITLE}} ---
# {{CONTEXT_TRACE_2_NARRATIVE}}


def code_to_trace_b():
    """Study this code - don't run it yet!"""
    scores = {}
    players = ["{{hero}}", "{{heroine}}", "{{hero}}"]
    for player in players:
        scores[player] = scores.get(player, 0) + 10
    print(scores)


def trace_table_b():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # {{CONTEXT_TRACE_HINT_2}}
    #
    # Track the dictionary and loop variable at each iteration.
    #
    # | Iter | player        | scores.get(player, 0) | scores after update      |
    # |------|---------------|-----------------------|--------------------------|
    # | 0    | -             | -                     | {}                       |
    # | 1    | "{{hero}}"    | 0                     |                          |
    # | 2    | "{{heroine}}" |                       |                          |
    # | 3    | "{{hero}}"    |                       |                          |
    #
    # What is the final output?
    #

    pass


# --- {{TRACE_3_TITLE}} ---
# {{CONTEXT_TRACE_3_NARRATIVE}}


def code_to_trace_c():
    """Study this code - don't run it yet!"""
    data = {"a": 1, "b": 2, "c": 3}
    total = 0
    for key in data:
        if data[key] > 1:
            total = total + data[key]
    print(f"Total: {total}")


def trace_table_c():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # {{CONTEXT_TRACE_HINT_3}}
    #
    # Track the loop variable, condition, and running total.
    #
    # | Iter | key | data[key] | data[key] > 1 | total after |
    # |------|-----|-----------|---------------|-------------|
    # | 0    | -   | -         | -             | 0           |
    # | 1    | "a" | 1         | False         |             |
    # | 2    | "b" |           |               |             |
    # | 3    | "c" |           |               |             |
    #
    # What is the final output?
    #

    pass


# --- {{TRACE_4_TITLE}} ---
# {{CONTEXT_TRACE_4_NARRATIVE}}


def code_to_trace_d():
    """Study this code - don't run it yet!"""
    profiles = {
        "{{hero}}": {"level": 5},
        "{{heroine}}": {"level": 7}
    }
    for name in profiles:
        profiles[name]["level"] = profiles[name]["level"] + 1
    print(profiles["{{hero}}"]["level"])
    print(profiles["{{heroine}}"]["level"])


def trace_table_d():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # {{CONTEXT_TRACE_HINT_4}}
    #
    # Track the nested dictionary mutations.
    #
    # | Iter | name          | before update            | after update             |
    # |------|---------------|--------------------------|--------------------------|
    # | 0    | -             | {"{{hero}}": {"level": 5}, "{{heroine}}": {"level": 7}} | - |
    # | 1    | "{{hero}}"    |                          |                          |
    # | 2    | "{{heroine}}" |                          |                          |
    #
    # What are the two printed values?
    #

    pass


def verify_traces():
    """Run this after completing your traces to check your work."""
    print("=== {{TRACE_1_TITLE}} - Actual Execution ===")
    code_to_trace_a()

    print("\n=== {{TRACE_2_TITLE}} - Actual Execution ===")
    code_to_trace_b()

    print("\n=== {{TRACE_3_TITLE}} - Actual Execution ===")
    code_to_trace_c()

    print("\n=== {{TRACE_4_TITLE}} - Actual Execution ===")
    code_to_trace_d()


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
