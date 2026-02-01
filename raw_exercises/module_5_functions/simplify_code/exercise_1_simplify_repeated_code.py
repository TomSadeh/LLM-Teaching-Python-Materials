# Exercise 1: Simplify This - Repeated Code
#
# Each piece of code works but contains unnecessary repetition.
# Rewrite using functions, loops, or better patterns.
#
# Theme: Streamlining {{school}}'s magical systems


# ============================================================
# SIMPLIFY A: Repeated Print Statements
# ============================================================

def original_a():
    """ORIGINAL: Same pattern repeated multiple times"""
    print("=" * 30)
    print("{{hero}}")
    print("=" * 30)

    print("=" * 30)
    print("{{heroine}}")
    print("=" * 30)

    print("=" * 30)
    print("{{friend}}")
    print("=" * 30)


def print_boxed(text):
    # ✏️ CREATE A HELPER FUNCTION ✏️
    # This function should print text surrounded by lines
    pass


def simplified_a():
    # ✏️ SIMPLIFY THIS ✏️
    # Use the helper function to eliminate repetition

    pass


# ============================================================
# SIMPLIFY B: Repeated Validation
# ============================================================

def original_b(name, spell, house):
    """ORIGINAL: Same validation pattern three times"""
    # Validate name
    if name is None:
        name = "Unknown"
    if not isinstance(name, str):
        name = str(name)
    name = name.strip()

    # Validate spell
    if spell is None:
        spell = "Unknown"
    if not isinstance(spell, str):
        spell = str(spell)
    spell = spell.strip()

    # Validate house
    if house is None:
        house = "Unknown"
    if not isinstance(house, str):
        house = str(house)
    house = house.strip()

    return f"{name} from {house} casts {spell}"


def validate_string(value, default="Unknown"):
    # ✏️ CREATE A HELPER FUNCTION ✏️
    # Handle None, non-string, and whitespace

    pass


def simplified_b(name, spell, house):
    # ✏️ SIMPLIFY THIS ✏️
    # Use the helper function

    pass


# ============================================================
# SIMPLIFY C: Repeated Calculations
# ============================================================

def original_c(items):
    """ORIGINAL: Same calculation pattern repeated"""
    potion_price = 10
    potion_tax = potion_price * 0.1
    potion_total = potion_price + potion_tax

    wand_price = 50
    wand_tax = wand_price * 0.1
    wand_total = wand_price + wand_tax

    book_price = 25
    book_tax = book_price * 0.1
    book_total = book_price + book_tax

    return potion_total + wand_total + book_total


def calculate_with_tax(price, tax_rate=0.1):
    # ✏️ CREATE A HELPER FUNCTION ✏️

    pass


def simplified_c(items):
    # ✏️ SIMPLIFY THIS ✏️
    # Use the helper function and perhaps a loop

    # items would be: [("potion", 10), ("wand", 50), ("book", 25)]
    pass


# ============================================================
# SIMPLIFY D: Boolean Return Pattern
# ============================================================

def original_d(value, minimum, maximum):
    """ORIGINAL: Overly complex boolean logic"""
    if value >= minimum:
        if value <= maximum:
            return True
        else:
            return False
    else:
        return False


def simplified_d(value, minimum, maximum):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: A comparison IS a boolean - you can return it directly
    # Also: Python supports chained comparisons!

    pass


# ============================================================
# SIMPLIFY E: Conditional Assignment
# ============================================================

def original_e(score):
    """ORIGINAL: Verbose conditional assignment"""
    if score >= 90:
        grade = "Outstanding"
    else:
        if score >= 80:
            grade = "Exceeds Expectations"
        else:
            if score >= 70:
                grade = "Acceptable"
            else:
                if score >= 60:
                    grade = "Poor"
                else:
                    grade = "Troll"
    return grade


def simplified_e(score):
    # ✏️ SIMPLIFY THIS ✏️
    # Use elif instead of nested if/else
    # Or consider a different approach entirely!

    pass


# ============================================================
# SIMPLIFY F: Building String with Loop
# ============================================================

def original_f(names):
    """ORIGINAL: Building string with concatenation"""
    result = ""
    for i in range(len(names)):
        if i > 0:
            result = result + ", "
        result = result + names[i]
    return result


def simplified_f(names):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: str.join() is perfect for this!

    pass


# ============================================================
# SIMPLIFY G: Dictionary from Two Lists
# ============================================================

def original_g(keys, values):
    """ORIGINAL: Manual dictionary building"""
    result = {}
    for i in range(len(keys)):
        key = keys[i]
        value = values[i]
        result[key] = value
    return result


def simplified_g(keys, values):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: zip() and dict() are your friends

    pass


# ============================================================
# SIMPLIFY H: Finding Maximum
# ============================================================

def original_h(numbers):
    """ORIGINAL: Manual max finding"""
    if len(numbers) == 0:
        return None
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def simplified_h(numbers):
    # ✏️ SIMPLIFY THIS ✏️
    # Hint: Python has a built-in for this!

    pass


def main():
    print("=== Test A: Repeated Print ===")
    print("Original:")
    original_a()
    print("\nSimplified:")
    simplified_a()

    print("\n=== Test B: Repeated Validation ===")
    print(f"Original: {original_b('  {{hero}}  ', None, '{{house}}')}")
    print(f"Simplified: {simplified_b('  {{hero}}  ', None, '{{house}}')}")

    print("\n=== Test C: Repeated Calculations ===")
    items = [("potion", 10), ("wand", 50), ("book", 25)]
    print(f"Original: {original_c(items)}")
    print(f"Simplified: {simplified_c(items)}")

    print("\n=== Test D: Boolean Return ===")
    print(f"Original (50 in 1-100): {original_d(50, 1, 100)}")
    print(f"Simplified (50 in 1-100): {simplified_d(50, 1, 100)}")

    print("\n=== Test E: Conditional Assignment ===")
    for score in [95, 85, 75, 65, 55]:
        print(f"Score {score}: Original={original_e(score)}, Simplified={simplified_e(score)}")

    print("\n=== Test F: Building String ===")
    names = ["{{hero}}", "{{heroine}}", "{{friend}}"]
    print(f"Original: {original_f(names)}")
    print(f"Simplified: {simplified_f(names)}")

    print("\n=== Test G: Dictionary from Lists ===")
    keys = ["hero", "spell", "house"]
    values = ["{{hero}}", "{{spell1}}", "{{house}}"]
    print(f"Original: {original_g(keys, values)}")
    print(f"Simplified: {simplified_g(keys, values)}")

    print("\n=== Test H: Finding Maximum ===")
    numbers = [10, 45, 23, 67, 34]
    print(f"Original: {original_h(numbers)}")
    print(f"Simplified: {simplified_h(numbers)}")


main()
