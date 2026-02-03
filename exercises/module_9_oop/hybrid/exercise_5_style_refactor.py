"""
{{CONTEXT_FIX_STYLE_INTRO}}

This is a multi-part exercise where you identify style problems,
fix them, and then reorganize code into a proper class structure.

Programming concepts: OOP conventions, refactoring, code organization
"""


# ============================================================
# PART 1: Evaluation - Identify What's Wrong
# ============================================================
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# Legacy code from {{school}}'s old system. It works, but has problems.


class data:
    def __init__(s, N, v1, v2, v3):
        s.N = N
        s.v1 = v1
        s.v2 = v2
        s.v3 = v3

    def ProcessData(s, x):
        s.v1 = s.v1 + x
        if s.v1 > 100:
            s.v1 = 100

    def DoOther(s, y):
        if s.v2 >= y:
            s.v2 = s.v2 - y
            s.v3 = s.v3 + 1
            return True
        return False

    def Info(s):
        return s.N + ": " + str(s.v1) + "/" + str(s.v2) + "/" + str(s.v3)


def part1_identify_problems():
    # ✏️ IDENTIFY THE STYLE ISSUES ✏️
    #
    # List all the problems with the code above:
    #
    # Class name issues:
    # 1.
    #
    # Parameter naming issues:
    # 2.
    # 3.
    #
    # Attribute naming issues:
    # 4.
    # 5.
    #
    # Method naming issues:
    # 6.
    # 7.
    #
    # Other issues:
    # 8. (hint: look at the 'self' parameter)
    # 9. (hint: string formatting)
    #
    # What do you think this class actually represents?
    # (The attributes seem to be: name, some value capped at 100,
    #  some resource that gets consumed, and a counter)
    #
    # Your guess: _______________

    pass


# ============================================================
# PART 2: Improvement - Fix the Naming
# ============================================================
# {{CONTEXT_STYLE_FIX_1}}
#
# Apply proper naming conventions to the code.


def part2_fix_naming():
    # ✏️ FIX THE NAMING ✏️
    #
    # Rewrite the class with proper conventions:
    #
    # Assuming this is a character with:
    # - name (N)
    # - health (v1) capped at 100
    # - energy (v2) consumed by actions
    # - actions_completed counter (v3)
    #
    # Apply these fixes:
    # - Class name: PascalCase, meaningful (ActionTracker? Character?)
    # - self, not s
    # - Descriptive parameter and attribute names
    # - snake_case method names
    # - Meaningful method names (heal instead of ProcessData, etc.)
    # - f-strings for formatting
    #
    # Write your fixed version:

    pass


# ============================================================
# PART 3: Growth - Reorganize Into Proper Structure
# ============================================================
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# Now refactor into a well-organized class with clear responsibilities.


def part3_reorganize():
    # ✏️ REORGANIZE THE CODE ✏️
    #
    # Create a properly structured class:
    #
    # class Character:
    #     """A character that can perform actions at {{school}}.
    #
    #     Attributes:
    #         name: The character's name
    #         health: Current health (0-100)
    #         max_health: Maximum health (default 100)
    #         energy: Current energy for actions
    #         actions_completed: Count of successful actions
    #     """
    #
    #     def __init__(self, name, health, energy):
    #         """Initialize a new character."""
    #         # Your code here
    #         pass
    #
    #     def heal(self, amount):
    #         """Restore health, capped at max_health.
    #
    #         Args:
    #             amount: Health points to restore
    #
    #         Returns:
    #             The new health value
    #         """
    #         # Your code here
    #         pass
    #
    #     def perform_action(self, energy_cost):
    #         """Attempt to perform an action that costs energy.
    #
    #         Args:
    #             energy_cost: Energy required for the action
    #
    #         Returns:
    #             True if action was performed, False if not enough energy
    #         """
    #         # Your code here
    #         pass
    #
    #     def get_status(self):
    #         """Get a formatted status string."""
    #         # Your code here
    #         pass
    #
    #     def __str__(self):
    #         """Return string representation."""
    #         # Your code here
    #         pass
    #
    # Test your reorganized class:
    #     char = Character("{{hero}}", 50, 30)
    #     print(char)
    #
    #     char.heal(30)
    #     print(f"After healing: {char.get_status()}")
    #
    #     char.perform_action(10)
    #     char.perform_action(10)
    #     print(f"After 2 actions: {char}")

    pass


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("{{CONTEXT_FIX_STYLE_INTRO}}")
    print("Legacy Code Refactoring")
    print("=" * 60)
    print()

    print(">>> PART 1: Identify What's Wrong")
    print()
    print("Original code:")
    d = data("{{hero}}", 50, 30, 0)
    d.ProcessData(30)
    d.DoOther(10)
    print(d.Info())
    print()
    print("(List the style problems you found)")
    part1_identify_problems()
    print()

    print(">>> PART 2: Fix the Naming")
    print("(Rewrite with proper conventions)")
    part2_fix_naming()
    print()

    print(">>> PART 3: Reorganize Into Proper Structure")
    print("(Create a well-documented, properly structured class)")
    part3_reorganize()

    print()
    print("=" * 60)
    print("{{CONTEXT_IMPROVEMENT_COMPLETE}}")
    print("=" * 60)


if __name__ == "__main__":
    main()
