# Exercise 1: Complete the Function - Dictionary Functions
#
# Each function is partially written. Read the docstring and
# the starter code, then complete the implementation.
#
# Theme: Managing {{school}}'s magical records


def safe_lookup(dictionary, key, default="Not found"):
    """
    Safely look up a key in a dictionary with a default value.

    Args:
        dictionary: The dictionary to search
        key: The key to look up
        default: Value to return if key doesn't exist

    Returns:
        The value for the key, or default if not found

    Examples:
        >>> spells = {"{{spell1}}": 10, "{{spell2}}": 20}
        >>> safe_lookup(spells, "{{spell1}}")
        10
        >>> safe_lookup(spells, "{{spell3}}")
        "Not found"
        >>> safe_lookup(spells, "{{spell3}}", 0)
        0
    """
    # ✏️ COMPLETE THIS FUNCTION ✏️
    # Hint: Use the .get() method

    pass  # Replace with implementation


def count_values(items):
    """
    Count occurrences of each item and return as a dictionary.

    Args:
        items: A list of items to count

    Returns:
        A dictionary with items as keys and counts as values

    Examples:
        >>> count_values(["a", "b", "a", "c", "a", "b"])
        {"a": 3, "b": 2, "c": 1}
        >>> count_values([1, 1, 2])
        {1: 2, 2: 1}
    """
    # Started for you:
    counts = {}

    # ✏️ COMPLETE THIS FUNCTION ✏️
    # Hint: For each item, either add it with count 1,
    # or increment its existing count

    for item in items:
        pass  # Your code here

    return counts


def merge_dictionaries(dict1, dict2):
    """
    Merge two dictionaries. If a key exists in both,
    use the value from dict2.

    Args:
        dict1: First dictionary
        dict2: Second dictionary (takes priority)

    Returns:
        A new dictionary with all keys from both

    Examples:
        >>> merge_dictionaries({"a": 1, "b": 2}, {"b": 3, "c": 4})
        {"a": 1, "b": 3, "c": 4}
    """
    # Started for you:
    result = {}

    # ✏️ COMPLETE THIS FUNCTION ✏️
    # Hint: First add all items from dict1, then from dict2

    pass  # Your code here

    return result


def invert_dictionary(original):
    """
    Swap keys and values in a dictionary.

    Args:
        original: A dictionary to invert

    Returns:
        A new dictionary with keys and values swapped

    Examples:
        >>> invert_dictionary({"{{hero}}": "Gryffindor", "{{friend}}": "Hufflepuff"})
        {"Gryffindor": "{{hero}}", "Hufflepuff": "{{friend}}"}
    """
    # Started for you:
    inverted = {}

    # ✏️ COMPLETE THIS FUNCTION ✏️
    # Hint: For each key-value pair, add value as key and key as value

    pass  # Your code here

    return inverted


def filter_by_value(dictionary, threshold):
    """
    Return a new dictionary with only entries where value >= threshold.

    Args:
        dictionary: A dictionary with numeric values
        threshold: Minimum value to include

    Returns:
        A new dictionary with only qualifying entries

    Examples:
        >>> scores = {"{{hero}}": 95, "{{friend}}": 72, "{{villain}}": 45}
        >>> filter_by_value(scores, 70)
        {"{{hero}}": 95, "{{friend}}": 72}
    """
    # Started for you:
    filtered = {}

    # ✏️ COMPLETE THIS FUNCTION ✏️
    # Hint: Loop through items, add to filtered if value >= threshold

    pass  # Your code here

    return filtered


def group_by_first_letter(words):
    """
    Group words by their first letter.

    Args:
        words: A list of words

    Returns:
        A dictionary where keys are first letters and values are lists

    Examples:
        >>> group_by_first_letter(["apple", "ant", "bear", "cat", "cow"])
        {"a": ["apple", "ant"], "b": ["bear"], "c": ["cat", "cow"]}
    """
    # Started for you:
    groups = {}

    # ✏️ COMPLETE THIS FUNCTION ✏️
    # Hint: Get first letter, create list if needed, append word

    for word in words:
        first_letter = word[0].lower()
        pass  # Your code here

    return groups


def main():
    print("=== Complete the Function: Dictionary Functions ===")
    print()

    # Test safe_lookup
    print("Test safe_lookup:")
    spells = {"fireball": 10, "ice": 20}
    print(f"  safe_lookup(spells, 'fireball') = {safe_lookup(spells, 'fireball')}")
    print(f"  Expected: 10")
    print(f"  safe_lookup(spells, 'thunder') = {safe_lookup(spells, 'thunder')}")
    print(f"  Expected: Not found")
    print()

    # Test count_values
    print("Test count_values:")
    result = count_values(["a", "b", "a", "c", "a", "b"])
    print(f"  count_values(['a','b','a','c','a','b']) = {result}")
    print(f"  Expected: {{'a': 3, 'b': 2, 'c': 1}}")
    print()

    # Test merge_dictionaries
    print("Test merge_dictionaries:")
    result = merge_dictionaries({"a": 1, "b": 2}, {"b": 3, "c": 4})
    print(f"  merge_dictionaries({{'a':1,'b':2}}, {{'b':3,'c':4}}) = {result}")
    print(f"  Expected: {{'a': 1, 'b': 3, 'c': 4}}")
    print()

    # Test invert_dictionary
    print("Test invert_dictionary:")
    result = invert_dictionary({"Harry": "Gryffindor", "Luna": "Ravenclaw"})
    print(f"  invert_dictionary(...) = {result}")
    print(f"  Expected: {{'Gryffindor': 'Harry', 'Ravenclaw': 'Luna'}}")
    print()

    # Test filter_by_value
    print("Test filter_by_value:")
    scores = {"Hero": 95, "Friend": 72, "Other": 45}
    result = filter_by_value(scores, 70)
    print(f"  filter_by_value(scores, 70) = {result}")
    print(f"  Expected: {{'Hero': 95, 'Friend': 72}}")
    print()

    # Test group_by_first_letter
    print("Test group_by_first_letter:")
    result = group_by_first_letter(["apple", "ant", "bear", "cat", "cow"])
    print(f"  group_by_first_letter(...) = {result}")
    print(f"  Expected: {{'a': ['apple', 'ant'], 'b': ['bear'], 'c': ['cat', 'cow']}}")


main()
