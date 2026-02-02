# Exercise 1: Fix the Style - Naming Conventions
#
# This code WORKS but has terrible style! Fix the issues:
# - Variable names that don't describe what they hold
# - Inconsistent naming style (camelCase vs snake_case)
# - Single-letter variable names
# - Cryptic abbreviations
#
# Theme: Managing {{hero}}'s magical inventory


# ============================================================
# STYLE FIX A: Single-Letter Variables
# ============================================================

def original_a():
    """ORIGINAL - Uses meaningless single-letter names"""
    x = "{{hero}}"
    y = "{{house}}"
    z = 11
    print(f"{x} from {y}, age {z}")


def fixed_a():
    # ✏️ FIX THE STYLE ✏️
    # Rewrite the code above with proper variable names.
    # Changes to make:
    # - Replace x with a name that describes what it holds
    # - Replace y with a name that describes what it holds
    # - Replace z with a name that describes what it holds

    pass  # Delete this and write your fixed code


# ============================================================
# STYLE FIX B: Cryptic Abbreviations
# ============================================================

def original_b():
    """ORIGINAL - Uses abbreviations nobody understands"""
    nm = "{{spell1}}"
    pwr = 50
    dur = 10
    msg = f"{nm}: power {pwr}, lasts {dur} seconds"
    print(msg)


def fixed_b():
    # ✏️ FIX THE STYLE ✏️
    # Rewrite with full, descriptive names.
    # What do nm, pwr, dur really represent?

    pass


# ============================================================
# STYLE FIX C: Inconsistent Naming Style
# ============================================================

def original_c():
    """ORIGINAL - Mixes camelCase and snake_case"""
    heroName = "{{hero}}"
    spell_power = 100
    maxHealth = 200
    current_health = 150
    print(f"{heroName}: {current_health}/{maxHealth} HP, {spell_power} power")


def fixed_c():
    # ✏️ FIX THE STYLE ✏️
    # Python uses snake_case for variables (PEP 8).
    # Convert all variable names to snake_case.

    pass


# ============================================================
# STYLE FIX D: Misleading Names
# ============================================================

def original_d():
    """ORIGINAL - Names don't match what they hold"""
    name = 42  # This is not a name!
    count = "{{spell2}}"  # This is not a count!
    total = ["{{hero}}", "{{friend}}"]  # This is not a total!

    print(f"Age: {name}")
    print(f"Spell: {count}")
    print(f"Team: {total}")


def fixed_d():
    # ✏️ FIX THE STYLE ✏️
    # Rename variables to match what they actually contain:
    # - The number 42 is probably an age
    # - The string is a spell name
    # - The list contains team members

    pass


# ============================================================
# STYLE FIX E: Magic Numbers
# ============================================================

def original_e():
    """ORIGINAL - Uses unexplained numbers"""
    hero = "{{hero}}"
    if 11 <= 17:  # What are these numbers?
        print(f"{hero} can attend {{school}}")
    health = 100 - 25  # What do 100 and 25 mean?
    print(f"Health: {health}")


def fixed_e():
    # ✏️ FIX THE STYLE ✏️
    # Replace magic numbers with named constants.
    # Use UPPERCASE_WITH_UNDERSCORES for constants.
    # Example: MIN_AGE = 11, MAX_AGE = 17

    pass


# ============================================================
# STYLE FIX F: Complete Cleanup
# ============================================================

def original_f():
    """ORIGINAL - Multiple style issues combined"""
    x = "{{hero}}"
    y = "{{heroine}}"
    z = "{{friend}}"
    lst = [x, y, z]
    cnt = 0
    for i in lst:
        cnt = cnt + 1
        msg = f"{cnt}. {i}"
        print(msg)


def fixed_f():
    # ✏️ FIX THE STYLE ✏️
    # Multiple fixes needed:
    # - Better names for x, y, z
    # - Better name for lst (what kind of list?)
    # - Better name for cnt (count of what?)
    # - Better loop variable name than i
    # - Consider if msg variable is even needed

    pass


def main():
    print("=== Original A (single-letter names) ===")
    original_a()
    print("\n=== Fixed A (your version) ===")
    fixed_a()

    print("\n=== Original B (cryptic abbreviations) ===")
    original_b()
    print("\n=== Fixed B (your version) ===")
    fixed_b()

    print("\n=== Original C (inconsistent style) ===")
    original_c()
    print("\n=== Fixed C (your version) ===")
    fixed_c()

    print("\n=== Original D (misleading names) ===")
    original_d()
    print("\n=== Fixed D (your version) ===")
    fixed_d()

    print("\n=== Original E (magic numbers) ===")
    original_e()
    print("\n=== Fixed E (your version) ===")
    fixed_e()

    print("\n=== Original F (complete cleanup) ===")
    original_f()
    print("\n=== Fixed F (your version) ===")
    fixed_f()


main()
