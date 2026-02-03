"""
{{CONTEXT_DISCOVERY_INTRO}}

This is a multi-part exercise where you'll master all import variations
by building a stat calculator for {{school}}.

Programming concepts: import syntax, dot notation, from import, aliases
Difficulty: 1-2
"""


# ============================================================
# PART 1: Guidance - Basic Import with Dot Notation
# ============================================================
# {{CONTEXT_GUIDANCE_NARRATIVE}}
#
# Start by using the basic import syntax. This is the most
# explicit way to use modules - you always see where things come from.


def exercise_part1():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Use basic import syntax to access math functions.
    #
    # Step 1: Import the math module using: import math
    #
    # Step 2: Create a character stat dictionary:
    #         stats = {
    #             "name": "{{hero}}",
    #             "base_power": 100,
    #             "multiplier": 1.5
    #         }
    #
    # Step 3: Calculate using dot notation:
    #         - power_root = math.sqrt(stats["base_power"])
    #         - rounded_mult = math.floor(stats["multiplier"])
    #
    # Step 4: Print the results:
    #         "[name]'s power root: [power_root]"
    #         "Rounded multiplier: [rounded_mult]"
    #
    # Note: With 'import math', always use math.function_name
    pass


# ============================================================
# PART 2: Growth - Refactor with from import
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Now refactor to use direct imports. This makes code cleaner
# when you use the same functions many times.


def exercise_part2():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Refactor to use from...import syntax.
    #
    # Step 1: Import specific functions:
    #         from math import sqrt, floor, ceil, pow
    #
    # Step 2: Create stats for multiple characters:
    #         hero_power = 144
    #         ally_power = 81
    #         mentor_power = 225
    #
    # Step 3: Calculate power levels (no math. prefix needed!):
    #         hero_level = sqrt(hero_power)
    #         ally_level = sqrt(ally_power)
    #         mentor_level = sqrt(mentor_power)
    #
    # Step 4: Calculate boosted power using pow():
    #         boosted = pow(hero_level, 2)
    #
    # Step 5: Print all results:
    #         "{{hero}} level: [value]"
    #         "{{friend}} level: [value]"
    #         "{{mentor}} level: [value]"
    #         "Boosted power: [value]"
    #
    # Notice: Code is cleaner without math. prefix everywhere
    pass


# ============================================================
# PART 3: Growth - Adding Aliases
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Learn when aliases are useful: avoiding name conflicts or
# shortening long module names.


def exercise_part3():
    # ✏️ YOUR CODE HERE ✏️
    #
    # Use aliases for cleaner, conflict-free code.
    #
    # Step 1: What if we have our own sqrt function?
    #         First, import math with an alias:
    #         import math as m
    #
    # Step 2: Create a local function that uses the module:
    #         def calculate_stat(value):
    #             """Calculate a derived stat."""
    #             return m.floor(m.sqrt(value))
    #
    # Step 3: Test with several values:
    #         values = [100, 144, 200, 256]
    #         for value in values:
    #             result = calculate_stat(value)
    #             print(f"Stat from {value}: {result}")
    #
    # Step 4: Also try aliasing a specific function:
    #         from math import factorial as fact
    #         Print: "5! = [fact(5)]"
    #         Print: "7! = [fact(7)]"
    #
    # Note: Common aliases: import numpy as np, import pandas as pd
    pass


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("{{CONTEXT_DISCOVERY_INTRO}}")
    print("=" * 60)
    print()

    print(">>> PART 1: Basic Import with Dot Notation")
    print("(Using import math and math.function())")
    print()
    exercise_part1()

    print()
    print(">>> PART 2: Refactoring with from...import")
    print("(Using from math import function)")
    print()
    exercise_part2()

    print()
    print(">>> PART 3: Using Aliases")
    print("(Using import math as m)")
    print()
    exercise_part3()

    print()
    print("=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print()
    print("Import Syntax Summary:")
    print("  import math          -> math.sqrt()")
    print("  from math import sqrt -> sqrt()")
    print("  import math as m     -> m.sqrt()")
    print("=" * 60)


if __name__ == "__main__":
    main()
