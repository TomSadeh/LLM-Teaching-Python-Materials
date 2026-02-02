# Exercise 1: Add Error Handling - Function Input
#
# Each function works for good input but crashes on bad input.
# Add try/except blocks to handle errors gracefully.
#
# Theme: Making {{school}}'s helper functions robust


# ============================================================
# ERROR HANDLING A: Type Conversion
# ============================================================

def original_parse_number(text):
    """ORIGINAL: Crashes if text can't be converted"""
    return float(text)  # Crashes on "abc" or None


def safe_parse_number(text, default=0.0):
    """
    Convert text to a number safely.

    Should handle:
    - Non-numeric text → return default
    - None → return default
    - Empty string → return default

    Args:
        text: String to convert
        default: Value to return if conversion fails

    Returns:
        float: The converted number or default
    """
    # ✏️ ADD ERROR HANDLING ✏️
    # Hint: float("abc") raises ValueError
    # Hint: float(None) raises TypeError

    pass


# ============================================================
# ERROR HANDLING B: List Operations
# ============================================================

def original_get_element(items, index):
    """ORIGINAL: Crashes on bad index"""
    return items[index]


def safe_get_element(items, index, default=None):
    """
    Get element from list safely.

    Should handle:
    - Index out of range → return default
    - None list → return default
    - Negative index too large → return default

    Args:
        items: List to get element from
        index: Index of element
        default: Value to return if access fails

    Returns:
        Element at index or default
    """
    # ✏️ ADD ERROR HANDLING ✏️

    pass


# ============================================================
# ERROR HANDLING C: Dictionary Access
# ============================================================

def original_get_nested(data, key1, key2):
    """ORIGINAL: Crashes if keys don't exist"""
    return data[key1][key2]


def safe_get_nested(data, key1, key2, default=None):
    """
    Get value from nested dictionary safely.

    Should handle:
    - First key missing → return default
    - Second key missing → return default
    - None data → return default
    - First value is not a dict → return default

    Args:
        data: Nested dictionary
        key1: First level key
        key2: Second level key
        default: Value to return if access fails

    Returns:
        Value at data[key1][key2] or default
    """
    # ✏️ ADD ERROR HANDLING ✏️
    # Hint: multiple exception types possible!

    pass


# ============================================================
# ERROR HANDLING D: Mathematical Operations
# ============================================================

def original_safe_divide(a, b):
    """ORIGINAL: Crashes on division by zero or incompatible types"""
    return a / b


def safe_divide(a, b, default=None):
    """
    Divide two numbers safely.

    Should handle:
    - Division by zero → return default
    - Non-numeric arguments → return default

    Args:
        a: Dividend
        b: Divisor
        default: Value to return on error

    Returns:
        float: Result of a/b or default
    """
    # ✏️ ADD ERROR HANDLING ✏️
    # Hint: "text" / 2 raises TypeError
    # Hint: 5 / 0 raises ZeroDivisionError

    pass


# ============================================================
# ERROR HANDLING E: String Operations
# ============================================================

def original_extract_word(text, index):
    """ORIGINAL: Crashes if text isn't string or index is bad"""
    words = text.split()
    return words[index]


def safe_extract_word(text, index, default=""):
    """
    Extract a word from text by index.

    Should handle:
    - None text → return default
    - Non-string text → try to convert, or return default
    - Index out of range → return default
    - Empty text → return default

    Args:
        text: String to extract word from
        index: Which word to extract (0-based)
        default: Value to return on error

    Returns:
        str: The word at index or default
    """
    # ✏️ ADD ERROR HANDLING ✏️

    pass


# ============================================================
# ERROR HANDLING F: JSON-like Parsing
# ============================================================

def original_parse_spell_data(spell_string):
    """ORIGINAL: Crashes if format is wrong"""
    # Expected format: "name:power:element"
    parts = spell_string.split(":")
    return {
        "name": parts[0],
        "power": int(parts[1]),
        "element": parts[2]
    }


def safe_parse_spell_data(spell_string):
    """
    Parse spell data from string format "name:power:element".

    Should handle:
    - None input → return None with message "No spell data provided"
    - Wrong number of parts → return None with message "Invalid format"
    - Power not a number → return None with message "Power must be a number"

    Args:
        spell_string: String in format "name:power:element"

    Returns:
        dict or None: Parsed spell data or None if invalid
    """
    # ✏️ ADD ERROR HANDLING ✏️
    # This one needs multiple checks!

    pass


# ============================================================
# ERROR HANDLING G: Chained Operations
# ============================================================

def original_process_scores(scores_text):
    """ORIGINAL: Multiple failure points"""
    # Expected: "10,20,30,40"
    numbers = [int(x) for x in scores_text.split(",")]
    total = sum(numbers)
    average = total / len(numbers)
    return {"total": total, "average": average, "count": len(numbers)}


def safe_process_scores(scores_text):
    """
    Process comma-separated scores into statistics.

    Should handle:
    - None input → return default stats
    - Empty string → return default stats
    - Non-numeric values → skip them, process the rest
    - No valid numbers → return default stats

    Default stats: {"total": 0, "average": 0, "count": 0}

    Args:
        scores_text: Comma-separated numbers like "10,20,30"

    Returns:
        dict: Statistics about the scores
    """
    # ✏️ ADD ERROR HANDLING ✏️
    # Handle errors at multiple stages

    pass


def main():
    print("=== Test A: Type Conversion ===")
    print(f"parse '42.5': {safe_parse_number('42.5')}")
    print(f"parse 'abc': {safe_parse_number('abc')}")
    print(f"parse None: {safe_parse_number(None)}")
    print(f"parse '' with default 100: {safe_parse_number('', 100)}")

    print("\n=== Test B: List Operations ===")
    items = ["{{hero}}", "{{heroine}}", "{{friend}}"]
    print(f"items[1]: {safe_get_element(items, 1)}")
    print(f"items[99]: {safe_get_element(items, 99)}")
    print(f"items[99] default='N/A': {safe_get_element(items, 99, 'N/A')}")
    print(f"None[0]: {safe_get_element(None, 0)}")

    print("\n=== Test C: Dictionary Access ===")
    data = {"{{house}}": {"points": 500, "wins": 3}}
    print(f"data['{{house}}']['points']: {safe_get_nested(data, '{{house}}', 'points')}")
    print(f"data['missing']['x']: {safe_get_nested(data, 'missing', 'x')}")
    print(f"data['{{house}}']['missing']: {safe_get_nested(data, '{{house}}', 'missing')}")

    print("\n=== Test D: Mathematical Operations ===")
    print(f"10 / 2: {safe_divide(10, 2)}")
    print(f"10 / 0: {safe_divide(10, 0)}")
    print(f"'text' / 2: {safe_divide('text', 2)}")

    print("\n=== Test E: String Operations ===")
    text = "{{hero}} casts {{spell1}}"
    print(f"word 0: {safe_extract_word(text, 0)}")
    print(f"word 2: {safe_extract_word(text, 2)}")
    print(f"word 99: {safe_extract_word(text, 99)}")
    print(f"None word 0: {safe_extract_word(None, 0)}")

    print("\n=== Test F: Spell Parsing ===")
    print(f"Valid: {safe_parse_spell_data('{{spell1}}:50:fire')}")
    print(f"Invalid: {safe_parse_spell_data('bad data')}")
    print(f"Bad power: {safe_parse_spell_data('spell:abc:water')}")
    print(f"None: {safe_parse_spell_data(None)}")

    print("\n=== Test G: Score Processing ===")
    print(f"Valid: {safe_process_scores('10,20,30,40')}")
    print(f"With invalid: {safe_process_scores('10,abc,30')}")
    print(f"Empty: {safe_process_scores('')}")
    print(f"None: {safe_process_scores(None)}")


main()
