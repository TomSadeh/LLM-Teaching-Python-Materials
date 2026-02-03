# =============================================================================
# Fix the Style: Function Naming Conventions
# =============================================================================
# Difficulty: 3
# Concepts: PEP 8 naming, descriptive names, parameter names
# =============================================================================

"""
{{CONTEXT_FIX_STYLE_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# Style Issue 1: Poor Function Names
# ============================================================
# {{CONTEXT_STYLE_1_NARRATIVE}}

def original_a():
    """ORIGINAL - This code works but has style issues"""
    def f(x):
        return x * 2

    def g(a, b):
        return a + b

    result1 = f(10)
    result2 = g(5, 3)
    print(f"Results: {result1}, {result2}")


def fixed_a():
    # FIX THE STYLE
    #
    # Rewrite with descriptive function names.
    # Changes to make:
    # - Rename 'f' to describe what it does (doubles a number)
    # - Rename 'g' to describe what it does (adds two numbers)
    # - Keep the same functionality

    # YOUR FIX HERE
    pass


# ============================================================
# Style Issue 2: Poor Parameter Names
# ============================================================
# {{CONTEXT_STYLE_2_NARRATIVE}}

def original_b():
    """ORIGINAL - This code works but has style issues"""
    def greet(x):
        return f"Hello, {x}!"

    def calculate(a, b, c):
        return (a + b) * c

    print(greet("{{hero}}"))
    print(calculate(10, 5, 2))


def fixed_b():
    # FIX THE STYLE
    #
    # Rewrite with descriptive parameter names.
    # Changes to make:
    # - In greet: rename 'x' to something meaningful
    # - In calculate: rename 'a', 'b', 'c' to meaningful names
    #   (hint: a and b are added, c is the multiplier)

    # YOUR FIX HERE
    pass


# ============================================================
# Style Issue 3: Inconsistent Naming Style
# ============================================================
# {{CONTEXT_STYLE_3_NARRATIVE}}

def original_c():
    """ORIGINAL - This code works but has style issues"""
    def GetUserName():  # Wrong: CamelCase
        return "{{hero}}"

    def Calculate_Total(baseValue, BonusAmount):  # Mixed styles
        return baseValue + BonusAmount

    name = GetUserName()
    total = Calculate_Total(100, 25)
    print(f"{name}: {total}")


def fixed_c():
    # FIX THE STYLE
    #
    # Use consistent snake_case naming (Python convention).
    # Changes to make:
    # - GetUserName -> get_user_name
    # - Calculate_Total -> calculate_total
    # - baseValue -> base_value
    # - BonusAmount -> bonus_amount

    # YOUR FIX HERE
    pass


# ============================================================
# Style Issue 4: Unclear Purpose
# ============================================================
# {{CONTEXT_STYLE_4_NARRATIVE}}

def original_d():
    """ORIGINAL - This code works but has style issues"""
    def do_stuff(thing):
        return thing.upper()

    def process(data):
        return len(data)

    def handle(items):
        return items[0]

    text = "{{hero}}"
    result1 = do_stuff(text)
    result2 = process(text)
    result3 = handle([1, 2, 3])
    print(f"{result1}, {result2}, {result3}")


def fixed_d():
    # FIX THE STYLE
    #
    # Rename functions to describe what they actually do.
    # Changes to make:
    # - do_stuff -> something that describes converting to uppercase
    # - process -> something that describes getting length
    # - handle -> something that describes getting first item

    # YOUR FIX HERE
    pass


# ============================================================
# Style Issue 5: Complete Makeover
# ============================================================
# {{CONTEXT_STYLE_5_NARRATIVE}}

def original_e():
    """ORIGINAL - This code works but has style issues"""
    def f1(n, m="{{school}}"):
        return f"{n} from {m}"

    def f2(x, y, z=1):
        return (x + y) * z

    def Thing(A):
        if A > 10:
            return "high"
        return "low"

    print(f1("{{hero}}"))
    print(f2(5, 3, 2))
    print(Thing(15))


def fixed_e():
    # FIX THE STYLE
    #
    # Complete style makeover:
    # - Rename f1 to describe creating an introduction
    # - Rename f2 to describe calculating with multiplier
    # - Rename Thing to describe getting a level description
    # - Fix all parameter names to be descriptive
    # - Use consistent snake_case

    # YOUR FIX HERE
    pass


def main():
    print("{{CONTEXT_FIX_STYLE_INTRO}}")
    print("=" * 50)

    print("\n=== Style Issue 1: Poor Function Names ===")
    print("Original (poor style):")
    original_a()
    print("\nFixed (your version):")
    fixed_a()

    print("\n=== Style Issue 2: Poor Parameter Names ===")
    print("Original (poor style):")
    original_b()
    print("\nFixed (your version):")
    fixed_b()

    print("\n=== Style Issue 3: Inconsistent Naming ===")
    print("Original (poor style):")
    original_c()
    print("\nFixed (your version):")
    fixed_c()

    print("\n=== Style Issue 4: Unclear Purpose ===")
    print("Original (poor style):")
    original_d()
    print("\nFixed (your version):")
    fixed_d()

    print("\n=== Style Issue 5: Complete Makeover ===")
    print("Original (poor style):")
    original_e()
    print("\nFixed (your version):")
    fixed_e()

    print("\n" + "=" * 50)
    print("PEP 8 Naming Conventions:")
    print("- Functions: lowercase_with_underscores")
    print("- Parameters: lowercase_with_underscores")
    print("- Be descriptive: calculate_total > f1")
    print("{{CONTEXT_IMPROVEMENT_COMPLETE}}")


main()
