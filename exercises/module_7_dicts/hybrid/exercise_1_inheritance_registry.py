"""
{{CONTEXT_DISCOVERY_INTRO}}

This is a multi-part exercise where you inherit a registry system,
understand how it works, extend it, and fix issues.

Programming concepts: dictionaries, key-value pairs, KeyError, .get()
"""


# ============================================================
# PART 1: Discovery - Understanding the Inherited Registry
# ============================================================
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# {{mentor}} left behind this registry system. Before you can use it,
# you need to understand how it works.
#
# Study the code below and trace through its execution.


def code_to_trace():
    """The inherited registry - study this carefully!"""
    registry = {
        "{{spell1}}": {"power": 10, "type": "basic"},
        "{{spell2}}": {"power": 25, "type": "intermediate"}
    }

    ability_name = "{{spell1}}"
    ability_data = registry[ability_name]
    power = ability_data["power"]
    print(f"{ability_name}: power {power}")


def trace_the_registry():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # Track the variables at each step.
    #
    # | Step | ability_name | ability_data                  | power | Output |
    # |------|--------------|-------------------------------|-------|--------|
    # | 0    | -            | -                             | -     |        |
    # | 1    | "{{spell1}}" | -                             | -     |        |
    # | 2    |              |                               | -     |        |
    # | 3    |              |                               |       |        |
    # | 4    |              |                               |       |        |
    #
    # Write your completed table as comments below:
    #

    pass


# ============================================================
# PART 2: Ownership - Extending the Registry
# ============================================================
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# Now make the registry your own by adding new entries and
# a function to look up abilities.


def create_extended_registry():
    """
    Create an extended version of the registry.

    Returns:
        dict: A registry with at least 4 abilities, each containing
              'power' (int) and 'type' (str) keys.
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Create a dictionary with the original 2 abilities:
    #         - "{{spell1}}": power 10, type "basic"
    #         - "{{spell2}}": power 25, type "intermediate"
    #
    # Step 2: Add 2 more abilities of your design:
    #         - "{{spell3}}": power 50, type "advanced"
    #         - "{{spell4}}": power 15, type "utility"
    #
    # Step 3: Return the registry

    pass


def lookup_ability(registry, ability_name):
    """
    Look up an ability in the registry and display its info.

    Args:
        registry: The ability registry dictionary
        ability_name: Name of the ability to look up

    Prints the ability's power and type, or "not found" message.
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Check if ability_name exists in the registry
    #         Hint: Use `if ability_name in registry:`
    #
    # Step 2: If it exists, print: "[name]: power [X], type [Y]"
    #
    # Step 3: If not found, print: "[name] not found in registry"

    pass


# ============================================================
# PART 3: Investigation - Debugging the Registry
# ============================================================
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# Someone reported bugs in this registry code. Find and fix them!

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "registry.py", line 12, in <module>
    total_power = total_power + registry[name]["power"]
KeyError: '{{creature}}'
"""


def buggy_power_calculator(registry):
    """BUGGY: Calculate total power of requested abilities."""
    requested = ["{{spell1}}", "{{spell2}}", "{{creature}}"]
    total_power = 0

    for name in requested:
        # BUG: Doesn't check if name exists in registry!
        total_power = total_power + registry[name]["power"]

    return total_power


def fixed_power_calculator(registry):
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # Fix the code so it:
    # 1. Only adds power for abilities that exist in the registry
    # 2. Prints a warning for abilities not found
    # 3. Returns the total power of found abilities
    #
    # Hint: Check if each name exists before accessing it

    pass


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("{{CONTEXT_DISCOVERY_INTRO}}")
    print("=" * 60)
    print()

    print(">>> PART 1: Understanding the inherited registry...")
    print("(Study code_to_trace() and complete trace_the_registry())")
    print()
    # Uncomment to verify your trace:
    # code_to_trace()

    print()
    print(">>> PART 2: Extending the registry...")
    print("(Implement create_extended_registry() and lookup_ability())")
    print()
    # Uncomment to test:
    # registry = create_extended_registry()
    # print(f"Registry has {len(registry)} abilities")
    # lookup_ability(registry, "{{spell1}}")
    # lookup_ability(registry, "{{spell3}}")
    # lookup_ability(registry, "unknown")

    print()
    print(">>> PART 3: Fixing the bugs...")
    print("(Implement fixed_power_calculator())")
    print()
    # Uncomment to test:
    # registry = create_extended_registry()
    # total = fixed_power_calculator(registry)
    # print(f"Total power of found abilities: {total}")

    print()
    print("=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print("=" * 60)


if __name__ == "__main__":
    main()
