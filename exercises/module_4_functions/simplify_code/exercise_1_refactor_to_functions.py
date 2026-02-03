# =============================================================================
# Simplify Code: Refactor to Functions
# =============================================================================
# Difficulty: 3-4
# Concepts: Refactoring, code reuse, identifying repeated patterns
# =============================================================================

"""
{{CONTEXT_SIMPLIFY_CODE_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""


# ============================================================
# Simplify 1: Repeated Calculations
# ============================================================
# {{CONTEXT_SIMPLIFY_1_NARRATIVE}}

def original_a():
    """ORIGINAL: Same calculation repeated multiple times"""
    # Calculate score for hero
    hero_base = 100
    hero_bonus = 25
    hero_score = (hero_base + hero_bonus) * 2
    print(f"{{hero}} score: {hero_score}")

    # Calculate score for heroine
    heroine_base = 150
    heroine_bonus = 30
    heroine_score = (heroine_base + heroine_bonus) * 2
    print(f"{{heroine}} score: {heroine_score}")

    # Calculate score for friend
    friend_base = 80
    friend_bonus = 20
    friend_score = (friend_base + friend_bonus) * 2
    print(f"{{friend}} score: {friend_score}")


def simplified_a():
    # SIMPLIFY THIS
    #
    # Create a function to perform the calculation once,
    # then call it three times.
    #
    # Hint: def calculate_score(base, bonus):
    #           return (base + bonus) * 2

    # YOUR CODE HERE
    pass


# ============================================================
# Simplify 2: Repeated Formatting
# ============================================================
# {{CONTEXT_SIMPLIFY_2_NARRATIVE}}

def original_b():
    """ORIGINAL: Same formatting pattern repeated"""
    # Format item 1
    item1 = "{{item}}"
    formatted1 = "[" + item1.upper() + "]"
    print(formatted1)

    # Format item 2
    item2 = "book"
    formatted2 = "[" + item2.upper() + "]"
    print(formatted2)

    # Format item 3
    item3 = "key"
    formatted3 = "[" + item3.upper() + "]"
    print(formatted3)

    # Format item 4
    item4 = "map"
    formatted4 = "[" + item4.upper() + "]"
    print(formatted4)


def simplified_b():
    # SIMPLIFY THIS
    #
    # Create a function that formats an item, then use it four times.
    #
    # Hint: def format_item(item):
    #           return "[" + item.upper() + "]"

    # YOUR CODE HERE
    pass


# ============================================================
# Simplify 3: Repeated Validation
# ============================================================
# {{CONTEXT_SIMPLIFY_3_NARRATIVE}}

def original_c():
    """ORIGINAL: Same validation logic repeated"""
    # Check hero level
    hero_level = 15
    if hero_level < 10:
        hero_status = "Novice"
    elif hero_level < 20:
        hero_status = "Intermediate"
    else:
        hero_status = "Expert"
    print(f"{{hero}}: {hero_status}")

    # Check heroine level
    heroine_level = 25
    if heroine_level < 10:
        heroine_status = "Novice"
    elif heroine_level < 20:
        heroine_status = "Intermediate"
    else:
        heroine_status = "Expert"
    print(f"{{heroine}}: {heroine_status}")

    # Check friend level
    friend_level = 5
    if friend_level < 10:
        friend_status = "Novice"
    elif friend_level < 20:
        friend_status = "Intermediate"
    else:
        friend_status = "Expert"
    print(f"{{friend}}: {friend_status}")


def simplified_c():
    # SIMPLIFY THIS
    #
    # Create a function that returns the status based on level.
    #
    # Hint: def get_status(level):
    #           if level < 10:
    #               return "Novice"
    #           ...

    # YOUR CODE HERE
    pass


# ============================================================
# Simplify 4: Repeated Report Sections
# ============================================================
# {{CONTEXT_SIMPLIFY_4_NARRATIVE}}

def original_d():
    """ORIGINAL: Same section format repeated"""
    # Section 1
    print("-" * 30)
    print("TEAM MEMBERS")
    print("-" * 30)

    # Section 2
    print("-" * 30)
    print("ACHIEVEMENTS")
    print("-" * 30)

    # Section 3
    print("-" * 30)
    print("GOALS")
    print("-" * 30)

    # Section 4
    print("-" * 30)
    print("NOTES")
    print("-" * 30)


def simplified_d():
    # SIMPLIFY THIS
    #
    # Create a function that prints a section header.
    #
    # Hint: def print_section(title):
    #           print("-" * 30)
    #           print(title)
    #           print("-" * 30)

    # YOUR CODE HERE
    pass


# ============================================================
# Simplify 5: Complex Refactoring
# ============================================================
# {{CONTEXT_SIMPLIFY_5_NARRATIVE}}

def original_e():
    """ORIGINAL: Multiple patterns that can be simplified"""
    # Process data for location 1
    loc1_name = "{{location}}"
    loc1_visitors = 100
    loc1_rating = 4.5
    print("=" * 40)
    print(f"Location: {loc1_name}")
    print("=" * 40)
    print(f"  Visitors: {loc1_visitors}")
    print(f"  Rating: {loc1_rating}/5.0")
    if loc1_rating >= 4.0:
        print("  Status: Highly Recommended")
    else:
        print("  Status: Good")
    print()

    # Process data for location 2
    loc2_name = "{{school}}"
    loc2_visitors = 250
    loc2_rating = 4.8
    print("=" * 40)
    print(f"Location: {loc2_name}")
    print("=" * 40)
    print(f"  Visitors: {loc2_visitors}")
    print(f"  Rating: {loc2_rating}/5.0")
    if loc2_rating >= 4.0:
        print("  Status: Highly Recommended")
    else:
        print("  Status: Good")
    print()

    # Process data for location 3
    loc3_name = "{{place}}"
    loc3_visitors = 50
    loc3_rating = 3.5
    print("=" * 40)
    print(f"Location: {loc3_name}")
    print("=" * 40)
    print(f"  Visitors: {loc3_visitors}")
    print(f"  Rating: {loc3_rating}/5.0")
    if loc3_rating >= 4.0:
        print("  Status: Highly Recommended")
    else:
        print("  Status: Good")
    print()


def simplified_e():
    # SIMPLIFY THIS
    #
    # Create functions to handle the repeated logic:
    # 1. A function to determine status based on rating
    # 2. A function to display a location's information
    #
    # Hint: Break it into two functions:
    #   - get_recommendation(rating) -> returns status string
    #   - display_location(name, visitors, rating) -> prints everything

    # YOUR CODE HERE
    pass


def main():
    print("{{CONTEXT_SIMPLIFY_CODE_INTRO}}")
    print("=" * 50)

    print("\n=== Simplify 1: Repeated Calculations ===")
    print("Original:")
    original_a()
    print("\nSimplified:")
    simplified_a()

    print("\n=== Simplify 2: Repeated Formatting ===")
    print("Original:")
    original_b()
    print("\nSimplified:")
    simplified_b()

    print("\n=== Simplify 3: Repeated Validation ===")
    print("Original:")
    original_c()
    print("\nSimplified:")
    simplified_c()

    print("\n=== Simplify 4: Repeated Report Sections ===")
    print("Original:")
    original_d()
    print("\nSimplified:")
    simplified_d()

    print("\n=== Simplify 5: Complex Refactoring ===")
    print("Original:")
    original_e()
    print("\nSimplified:")
    simplified_e()

    print("\n" + "=" * 50)
    print("{{CONTEXT_IMPROVEMENT_COMPLETE}}")


main()
