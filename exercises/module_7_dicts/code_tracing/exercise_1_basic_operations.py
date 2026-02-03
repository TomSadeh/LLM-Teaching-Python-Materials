"""
{{CONTEXT_CODE_TRACING_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

Trace through dictionary operations to understand how
dictionaries store and retrieve data.
"""


# --- {{TRACE_1_TITLE}} ---
# {{CONTEXT_TRACE_1_NARRATIVE}}


def code_to_trace_a():
    """Study this code - don't run it yet!"""
    profile = {}
    profile["name"] = "{{hero}}"
    profile["level"] = 1
    profile["level"] = profile["level"] + 1
    print(profile["name"])
    print(profile["level"])


def trace_table_a():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # {{CONTEXT_TRACE_HINT_1}}
    #
    # Track the dictionary contents at each step.
    # Use {} to show an empty dictionary.
    #
    # | Step | profile (dict contents)        | Output (if any) |
    # |------|--------------------------------|-----------------|
    # | 0    | {}                             |                 |
    # | 1    | {"name": "{{hero}}"}           |                 |
    # | 2    |                                |                 |
    # | 3    |                                |                 |
    # | 4    |                                |                 |
    # | 5    |                                |                 |
    #
    # Write your completed table as comments below:
    #

    pass


# --- {{TRACE_2_TITLE}} ---
# {{CONTEXT_TRACE_2_NARRATIVE}}


def code_to_trace_b():
    """Study this code - don't run it yet!"""
    inventory = {"{{item}}": 3, "{{spell1}}": 1}
    inventory["{{spell1}}"] = inventory["{{spell1}}"] + 2
    inventory["{{spell2}}"] = 1
    total = inventory["{{item}}"] + inventory["{{spell1}}"]
    print(f"Total: {total}")


def trace_table_b():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # {{CONTEXT_TRACE_HINT_2}}
    #
    # Track both the dictionary and the total variable.
    #
    # | Step | inventory (dict contents)                | total | Output |
    # |------|------------------------------------------|-------|--------|
    # | 0    | {"{{item}}": 3, "{{spell1}}": 1}         | -     |        |
    # | 1    |                                          | -     |        |
    # | 2    |                                          | -     |        |
    # | 3    |                                          |       |        |
    # | 4    |                                          |       |        |
    #
    # Write your completed table as comments below:
    #

    pass


# --- {{TRACE_3_TITLE}} ---
# {{CONTEXT_TRACE_3_NARRATIVE}}


def code_to_trace_c():
    """Study this code - don't run it yet!"""
    scores = {"{{hero}}": 10, "{{heroine}}": 20}
    winner = ""
    if scores["{{hero}}"] > scores["{{heroine}}"]:
        winner = "{{hero}}"
    else:
        winner = "{{heroine}}"
    scores[winner] = scores[winner] + 5
    print(f"Winner: {winner}")
    print(f"New score: {scores[winner]}")


def trace_table_c():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # {{CONTEXT_TRACE_HINT_3}}
    #
    # Track scores dict, winner variable, and condition results.
    #
    # | Step | scores                              | winner | condition | Output |
    # |------|-------------------------------------|--------|-----------|--------|
    # | 0    | {"{{hero}}": 10, "{{heroine}}": 20} | ""     | -         |        |
    # | 1    |                                     |        | T/F?      |        |
    # | 2    |                                     |        |           |        |
    # | 3    |                                     |        |           |        |
    # | 4    |                                     |        |           |        |
    # | 5    |                                     |        |           |        |
    #
    # Write your completed table as comments below:
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
