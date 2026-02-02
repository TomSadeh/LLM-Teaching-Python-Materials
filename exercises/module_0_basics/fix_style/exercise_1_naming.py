# =============================================================================
# Fix the Style: Naming Conventions
# =============================================================================
# Difficulty: 5
# Concepts: PEP 8 naming, readable code, meaningful variable names
# =============================================================================

"""
{{CONTEXT_FIX_STYLE_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# {{STYLE_1_TITLE}}
# ============================================================
# {{CONTEXT_STYLE_1_NARRATIVE}}


def original_a():
    """ORIGINAL - This code works but has style issues"""
    x = "{{hero}}"
    y = "{{school}}"
    z = 100
    print(x, "studies at", y, "with", z, "points")


def fixed_a():
    # ✏️ FIX THE STYLE ✏️
    #
    # {{CONTEXT_STYLE_FIX_1}}
    #
    # Rewrite the code above with proper style.
    # Changes to make:
    # - Rename x to something meaningful (like hero_name)
    # - Rename y to something meaningful (like school_name)
    # - Rename z to something meaningful (like points)
    #
    # The output should be exactly the same!

    pass


# ============================================================
# {{STYLE_2_TITLE}}
# ============================================================
# {{CONTEXT_STYLE_2_NARRATIVE}}


def original_b():
    """ORIGINAL - This code works but has style issues"""
    a=10
    b=5
    c=a+b
    d=a*b
    print("Sum:",c,"Product:",d)


def fixed_b():
    # ✏️ FIX THE STYLE ✏️
    #
    # {{CONTEXT_STYLE_FIX_2}}
    #
    # Changes to make:
    # - Add spaces around = signs
    # - Add spaces around + and * operators
    # - Add spaces after colons in the print statement
    # - Use meaningful variable names

    pass


# ============================================================
# {{STYLE_3_TITLE}}
# ============================================================
# {{CONTEXT_STYLE_3_NARRATIVE}}


def original_c():
    """ORIGINAL - This code works but has style issues"""
    n = "{{hero}}"
    l = 5
    h = 100
    g = 50
    print(n)
    print("Level:" + str(l))
    print("HP:" + str(h))
    print("Gold:" + str(g))


def fixed_c():
    # ✏️ FIX THE STYLE ✏️
    #
    # {{CONTEXT_STYLE_FIX_3}}
    #
    # Changes to make:
    # - Use meaningful variable names (name, level, health, gold)
    # - Use f-strings instead of concatenation
    # - Add spaces after colons in output

    pass


def main():
    print("{{CONTEXT_FIX_STYLE_INTRO}}")
    print("=" * 50)

    print("\n=== {{STYLE_1_TITLE}} ===")
    print("Original (poor style):")
    original_a()
    print("\nFixed (your version):")
    fixed_a()

    print("\n=== {{STYLE_2_TITLE}} ===")
    print("Original (poor style):")
    original_b()
    print("\nFixed (your version):")
    fixed_b()

    print("\n=== {{STYLE_3_TITLE}} ===")
    print("Original (poor style):")
    original_c()
    print("\nFixed (your version):")
    fixed_c()

    print("\n" + "=" * 50)
    print("{{CONTEXT_IMPROVEMENT_COMPLETE}}")


main()
