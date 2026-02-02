# Exercise 1: Which is Better? - Many Parameters vs Dictionary
#
# For each pair of solutions, both work correctly.
# Your job: Analyze and explain which is better AND WHY.
# Sometimes the answer is "it depends"!
#
# Theme: Creating character profiles for {{school}}


# ============================================================
# COMPARISON A: Few Parameters
# ============================================================

def version_a1(name, house, year):
    """Version 1: Individual parameters"""
    return f"{name} from {house}, Year {year}"


def version_a2(character_info):
    """Version 2: Dictionary parameter"""
    return f"{character_info['name']} from {character_info['house']}, Year {character_info['year']}"


def analysis_a():
    # ✏️ YOUR ANALYSIS ✏️
    # Which is better: A1 or A2?
    # Consider: simplicity, documentation, when few parameters is enough

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When to use version A1 (individual params):
    -

    When to use version A2 (dictionary):
    -
    """
    return analysis


# ============================================================
# COMPARISON B: Many Parameters
# ============================================================

def version_b1(name, house, year, wand_wood, wand_core, wand_length,
               pet_name, pet_type, favorite_spell, favorite_subject):
    """Version 1: Many individual parameters"""
    return {
        "name": name,
        "house": house,
        "year": year,
        "wand": f"{wand_wood}, {wand_core}, {wand_length} inches",
        "pet": f"{pet_name} the {pet_type}",
        "favorites": f"{favorite_spell}, {favorite_subject}"
    }


def version_b2(character_data):
    """Version 2: Single dictionary parameter"""
    wand = character_data.get("wand", {})
    pet = character_data.get("pet", {})
    return {
        "name": character_data["name"],
        "house": character_data["house"],
        "year": character_data["year"],
        "wand": f"{wand.get('wood')}, {wand.get('core')}, {wand.get('length')} inches",
        "pet": f"{pet.get('name')} the {pet.get('type')}",
        "favorites": f"{character_data.get('favorite_spell')}, {character_data.get('favorite_subject')}"
    }


def analysis_b():
    # ✏️ YOUR ANALYSIS ✏️
    # Which is better: B1 or B2?
    # Consider: code readability, maintainability, caller experience

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When to use version B1 (many params):
    -

    When to use version B2 (dictionary):
    -
    """
    return analysis


# ============================================================
# COMPARISON C: Optional Parameters
# ============================================================

def version_c1(name, house, year=1, pet=None, wand=None):
    """Version 1: Default parameters"""
    result = f"{name}, {house}, Year {year}"
    if pet:
        result += f", Pet: {pet}"
    if wand:
        result += f", Wand: {wand}"
    return result


def version_c2(character_data):
    """Version 2: Dictionary with .get() defaults"""
    name = character_data["name"]  # Required
    house = character_data["house"]  # Required
    year = character_data.get("year", 1)
    pet = character_data.get("pet")
    wand = character_data.get("wand")

    result = f"{name}, {house}, Year {year}"
    if pet:
        result += f", Pet: {pet}"
    if wand:
        result += f", Wand: {wand}"
    return result


def analysis_c():
    # ✏️ YOUR ANALYSIS ✏️
    # Which is better: C1 or C2?
    # Consider: explicit defaults, flexibility, documentation

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When to use version C1 (default params):
    -

    When to use version C2 (dictionary):
    -
    """
    return analysis


# ============================================================
# COMPARISON D: Passing Data Between Functions
# ============================================================

def version_d1_create(name, house, year):
    """Create character data"""
    return (name, house, year)


def version_d1_display(character_tuple):
    """Display character from tuple"""
    name, house, year = character_tuple
    return f"Student: {name} ({house}, Year {year})"


def version_d2_create(name, house, year):
    """Create character data"""
    return {"name": name, "house": house, "year": year}


def version_d2_display(character_dict):
    """Display character from dictionary"""
    return f"Student: {character_dict['name']} ({character_dict['house']}, Year {character_dict['year']})"


def analysis_d():
    # ✏️ YOUR ANALYSIS ✏️
    # Which is better: D1 (tuple) or D2 (dict)?
    # Consider: clarity, accessing fields by name vs position

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When to use version D1 (tuple):
    -

    When to use version D2 (dictionary):
    -
    """
    return analysis


# ============================================================
# COMPARISON E: Configuration Objects
# ============================================================

def version_e1_game(difficulty, max_lives, time_limit, sound_on, hints_enabled):
    """Version 1: All config as parameters"""
    print(f"Starting game: difficulty={difficulty}, lives={max_lives}")
    print(f"Time: {time_limit}s, Sound: {sound_on}, Hints: {hints_enabled}")


def version_e2_game(config):
    """Version 2: Config dictionary"""
    print(f"Starting game: difficulty={config['difficulty']}, lives={config['max_lives']}")
    print(f"Time: {config['time_limit']}s, Sound: {config['sound_on']}, Hints: {config['hints_enabled']}")


def analysis_e():
    # ✏️ YOUR ANALYSIS ✏️
    # Which is better: E1 or E2?
    # Consider: adding new options, saving/loading config, testing

    analysis = """
    Better version: ??? (or "it depends")

    Reasons:
    1.
    2.

    When to use version E1 (parameters):
    -

    When to use version E2 (config dict):
    -
    """
    return analysis


def main():
    print("=== Comparison A: Few Parameters ===")
    print(f"Version 1: {version_a1('{{hero}}', '{{house}}', 3)}")
    print(f"Version 2: {version_a2({'name': '{{hero}}', 'house': '{{house}}', 'year': 3})}")
    print(f"\nAnalysis:{analysis_a()}")

    print("\n=== Comparison B: Many Parameters ===")
    print("Version 1:")
    result1 = version_b1("{{hero}}", "{{house}}", 3, "Holly", "Phoenix", 11,
                         "{{pet}}", "Owl", "{{spell1}}", "Defense")
    print(result1)

    print("\nVersion 2:")
    character = {
        "name": "{{hero}}",
        "house": "{{house}}",
        "year": 3,
        "wand": {"wood": "Holly", "core": "Phoenix", "length": 11},
        "pet": {"name": "{{pet}}", "type": "Owl"},
        "favorite_spell": "{{spell1}}",
        "favorite_subject": "Defense"
    }
    result2 = version_b2(character)
    print(result2)
    print(f"\nAnalysis:{analysis_b()}")

    print("\n=== Comparison C: Optional Parameters ===")
    print(f"Version 1: {version_c1('{{hero}}', '{{house}}')}")
    print(f"Version 1: {version_c1('{{hero}}', '{{house}}', 3, '{{pet}}')}")
    print(f"Version 2: {version_c2({'name': '{{hero}}', 'house': '{{house}}'})}")
    print(f"Version 2: {version_c2({'name': '{{hero}}', 'house': '{{house}}', 'year': 3, 'pet': '{{pet}}'})}")
    print(f"\nAnalysis:{analysis_c()}")

    print("\n=== Comparison D: Passing Data Between Functions ===")
    char1 = version_d1_create("{{hero}}", "{{house}}", 3)
    print(f"Version 1: {version_d1_display(char1)}")
    char2 = version_d2_create("{{hero}}", "{{house}}", 3)
    print(f"Version 2: {version_d2_display(char2)}")
    print(f"\nAnalysis:{analysis_d()}")

    print("\n=== Comparison E: Configuration Objects ===")
    print("Version 1:")
    version_e1_game("hard", 3, 60, True, False)
    print("\nVersion 2:")
    config = {"difficulty": "hard", "max_lives": 3, "time_limit": 60,
              "sound_on": True, "hints_enabled": False}
    version_e2_game(config)
    print(f"\nAnalysis:{analysis_e()}")


main()
