# Exercise 1: Fix the Style - Function Style
#
# This code WORKS but has terrible function style! Fix the issues:
# - Missing docstrings
# - Confusing parameter names
# - Inconsistent return patterns
# - Functions doing too much
# - Poor spacing and organization
#
# Theme: Helper functions for {{school}} spellcasting


# ============================================================
# STYLE FIX A: Missing Docstrings
# ============================================================

def original_a(x, y, z):
    """ORIGINAL - No documentation, unclear purpose"""
    return x * y + z


def fixed_a(x, y, z):
    # ✏️ FIX THE STYLE ✏️
    # Add a docstring explaining:
    # - What the function does
    # - What each parameter means
    # - What it returns
    # Also rename parameters to be descriptive!

    pass


# ============================================================
# STYLE FIX B: Confusing Parameter Names
# ============================================================

def original_b(a, b, c=True):
    """ORIGINAL - What are a, b, c?"""
    if c:
        return f"*{a}* ({b})"
    else:
        return f"{a} ({b})"


def fixed_b(a, b, c=True):
    # ✏️ FIX THE STYLE ✏️
    # Rename parameters to describe what they represent:
    # - a appears to be some kind of name/text
    # - b appears to be additional info
    # - c appears to control formatting
    # Add a docstring too!

    pass


# ============================================================
# STYLE FIX C: Print vs Return
# ============================================================

def original_c(hero, spell):
    """ORIGINAL - Mixes print and return inconsistently"""
    message = f"{hero} casts {spell}!"
    print(message)  # Side effect
    return message  # Also returns


def calculate_damage_original(power, defense):
    """ORIGINAL - Prints instead of returning"""
    damage = max(0, power - defense)
    print(damage)  # Should this be a return?


def fixed_c(hero, spell):
    # ✏️ FIX THE STYLE ✏️
    # Decide: should the function print OR return?
    # Usually, functions should RETURN values.
    # Let the caller decide whether to print.

    pass


def calculate_damage_fixed(power, defense):
    # ✏️ FIX THE STYLE ✏️
    # This function should return the damage value,
    # not print it. Add a docstring too.

    pass


# ============================================================
# STYLE FIX D: Function Doing Too Much
# ============================================================

def original_d(name, house, year, spell_count, health):
    """ORIGINAL - This function does WAY too much"""
    # Validate name
    if not name:
        name = "Unknown"
    name = name.title()

    # Validate house
    valid_houses = ["{{house}}", "Slytherin", "Ravenclaw", "Hufflepuff"]
    if house not in valid_houses:
        house = "Unknown"

    # Calculate level
    level = year + (spell_count // 10)

    # Create status
    status = "healthy" if health > 50 else "injured"

    # Build report
    report = f"""
    Student: {name}
    House: {house}
    Year: {year}
    Level: {level}
    Status: {status}
    """
    return report


# ✏️ FIX THE STYLE ✏️
# Break this into smaller, focused functions:

def validate_name(name):
    """Validate and format a student name."""
    # Your code here
    pass


def validate_house(house):
    """Validate house name against known houses."""
    # Your code here
    pass


def calculate_level(year, spell_count):
    """Calculate student level from year and spells learned."""
    # Your code here
    pass


def get_health_status(health):
    """Return status string based on health value."""
    # Your code here
    pass


def fixed_d(name, house, year, spell_count, health):
    """Generate a student report using helper functions."""
    # Use the helper functions above to build the report
    # This function should be SHORT and easy to read

    pass


# ============================================================
# STYLE FIX E: Inconsistent Spacing
# ============================================================

def original_e(spell,power,element):
    """ORIGINAL - No spaces, hard to read"""
    if power>50:
        result=f"{spell}: POWERFUL {element}"
    else:
        result=f"{spell}: weak {element}"
    return result


def fixed_e(spell, power, element):
    # ✏️ FIX THE STYLE ✏️
    # Add proper spacing:
    # - Space after commas in parameters
    # - Spaces around operators (>, =)
    # - Consistent formatting

    pass


# ============================================================
# STYLE FIX F: Complete Function Cleanup
# ============================================================

def original_f(l,n):
    """ORIGINAL - Everything wrong at once"""
    r=[]
    for i in l:
        if len(i)>n:
            r.append(i)
    print(r)
    return r


def fixed_f(items, min_length):
    # ✏️ FIX THE STYLE ✏️
    # Fix everything:
    # - Descriptive parameter names (done above)
    # - Proper spacing
    # - Good variable names inside
    # - Docstring
    # - Decide: print or return (not both)

    pass


def main():
    print("=== Original A (no docstring) ===")
    print(f"Result: {original_a(10, 5, 3)}")
    print("\n=== Fixed A (your version) ===")
    print(f"Result: {fixed_a(10, 5, 3)}")

    print("\n=== Original B (confusing params) ===")
    print(original_b("{{spell1}}", "fire"))
    print("\n=== Fixed B (your version) ===")
    # print(fixed_b(...))

    print("\n=== Original C (print vs return) ===")
    original_c("{{hero}}", "{{spell2}}")
    calculate_damage_original(50, 20)
    print("\n=== Fixed C (your version) ===")
    # result = fixed_c("{{hero}}", "{{spell2}}")
    # print(result)  # Caller decides to print

    print("\n=== Original D (doing too much) ===")
    print(original_d("{{hero}}", "{{house}}", 3, 25, 75))
    print("\n=== Fixed D (your version) ===")
    # print(fixed_d("{{hero}}", "{{house}}", 3, 25, 75))

    print("\n=== Original E (no spacing) ===")
    print(original_e("{{spell3}}", 75, "lightning"))
    print("\n=== Fixed E (your version) ===")
    # print(fixed_e("{{spell3}}", 75, "lightning"))

    print("\n=== Original F (everything wrong) ===")
    original_f(["{{hero}}", "{{heroine}}", "{{friend}}", "Al"], 3)
    print("\n=== Fixed F (your version) ===")
    # result = fixed_f(["{{hero}}", "{{heroine}}", "{{friend}}", "Al"], 3)
    # print(result)


main()
