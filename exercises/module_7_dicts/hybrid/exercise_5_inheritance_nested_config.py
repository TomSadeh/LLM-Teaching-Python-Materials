"""
{{CONTEXT_DISCOVERY_INTRO}}

This is a multi-part exercise where you inherit a nested configuration
system, understand its structure, extend it, and debug issues.

Programming concepts: nested dictionaries, safe access, multi-level data
"""


# ============================================================
# PART 1: Discovery - Understanding the Nested Config
# ============================================================
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# {{mentor}} left behind this configuration system.
# Study the nested structure before making changes.

CONFIG = {
    "player": {
        "name": "{{hero}}",
        "stats": {
            "health": 100,
            "mana": 50,
            "strength": 10
        },
        "preferences": {
            "difficulty": "normal",
            "hints_enabled": True
        }
    },
    "display": {
        "resolution": "1920x1080",
        "fullscreen": False,
        "colors": {
            "background": "dark",
            "text": "light"
        }
    },
    "audio": {
        "master_volume": 80,
        "music_volume": 60,
        "effects_volume": 100
    }
}


def code_to_trace():
    """Trace through accessing nested config values."""
    player_name = CONFIG["player"]["name"]
    player_health = CONFIG["player"]["stats"]["health"]
    bg_color = CONFIG["display"]["colors"]["background"]
    music_vol = CONFIG["audio"]["music_volume"]

    print(f"Player: {player_name}")
    print(f"Health: {player_health}")
    print(f"Background: {bg_color}")
    print(f"Music: {music_vol}")


def trace_nested_access():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # For each line, trace the path through the nested dictionaries.
    #
    # | Variable      | Path                           | Value        |
    # |---------------|--------------------------------|--------------|
    # | player_name   | CONFIG["player"]["name"]       | "{{hero}}"   |
    # | player_health | CONFIG["player"]["stats"][?]   |              |
    # | bg_color      | CONFIG[?][?][?]                |              |
    # | music_vol     | CONFIG[?][?]                   |              |
    #
    # How many levels deep is each access?
    # - player_name: 2 levels
    # - player_health: ? levels
    # - bg_color: ? levels
    # - music_vol: ? levels

    pass


# ============================================================
# PART 2: Ownership - Extending the Config
# ============================================================
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# Add new configuration sections and functions to access them safely.


def get_config_value(config, *keys):
    """
    Safely get a nested config value.

    Args:
        config: The configuration dictionary
        *keys: Variable number of keys forming the path

    Returns:
        The value at the path, or None if any key is missing.

    Examples:
        >>> get_config_value(CONFIG, "player", "name")
        '{{hero}}'
        >>> get_config_value(CONFIG, "player", "stats", "health")
        100
        >>> get_config_value(CONFIG, "nonexistent", "key")
        None
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Start with the config
    # Step 2: For each key in keys:
    #         - If current is a dict and has the key, go deeper
    #         - Otherwise, return None
    # Step 3: Return the final value
    #
    # Hint: Use a loop through keys, checking each step

    pass


def set_config_value(config, value, *keys):
    """
    Set a nested config value, creating intermediate dicts if needed.

    Args:
        config: The configuration dictionary
        value: The value to set
        *keys: Variable number of keys forming the path

    Examples:
        >>> cfg = {}
        >>> set_config_value(cfg, "test", "a", "b", "c")
        >>> cfg
        {'a': {'b': {'c': 'test'}}}
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Step 1: Navigate through all keys EXCEPT the last one
    #         - If a key doesn't exist, create an empty dict
    #         - Move into the nested dict
    # Step 2: Use the last key to set the value
    #
    # This is tricky! Work through it step by step.

    pass


def add_controls_config(config):
    """
    Add a new "controls" section to the config.

    Args:
        config: The configuration dictionary (modified in place)

    Add these settings:
        controls:
            keybindings:
                jump: "space"
                attack: "left_click"
                use_item: "e"
            mouse_sensitivity: 5
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Add the nested structure to config["controls"]

    pass


# ============================================================
# PART 3: Investigation - Debugging Nested Access
# ============================================================
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# Find and fix bugs in this nested config code.

"""
ERROR MESSAGE:
--------------
Traceback (most recent call last):
  File "config.py", line 5, in <module>
    sensitivity = config["controls"]["mouse"]["sensitivity"]
KeyError: 'controls'
"""


def buggy_get_sensitivity(config):
    """BUGGY: Get mouse sensitivity from config."""
    sensitivity = config["controls"]["mouse"]["sensitivity"]
    return sensitivity


def fixed_get_sensitivity(config):
    # ✏️ FIX THE CODE ✏️
    #
    # The error occurred because: _______________
    #
    # Use get_config_value or manual checking to safely access
    # the sensitivity, returning a default value if not found.

    pass


def buggy_update_stats(config, stat_name, new_value):
    """BUGGY: Update a player stat."""
    config["player"]["stats"][stat_name] = new_value


def fixed_update_stats(config, stat_name, new_value):
    # ✏️ FIX THE CODE ✏️
    #
    # What if config["player"] doesn't exist?
    # What if config["player"]["stats"] doesn't exist?
    #
    # Create a version that ensures the path exists before updating.

    pass


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("{{CONTEXT_DISCOVERY_INTRO}}")
    print("=" * 60)
    print()

    print(">>> PART 1: Understanding the nested config...")
    print()
    print("CONFIG structure:")
    for section in CONFIG:
        print(f"  {section}: {list(CONFIG[section].keys())}")
    print()
    print("(Study code_to_trace() and complete trace_nested_access())")
    # Uncomment to verify:
    # code_to_trace()

    print()
    print(">>> PART 2: Extending the config...")
    print("(Implement get_config_value, set_config_value, add_controls_config)")
    print()
    # Uncomment after implementing:
    # print(f"Safe get player name: {get_config_value(CONFIG, 'player', 'name')}")
    # print(f"Safe get missing: {get_config_value(CONFIG, 'missing', 'key')}")
    # test_cfg = {}
    # set_config_value(test_cfg, "test_value", "a", "b", "c")
    # print(f"After set_config_value: {test_cfg}")
    # add_controls_config(CONFIG)
    # print(f"Controls added: {'controls' in CONFIG}")

    print()
    print(">>> PART 3: Debugging nested access...")
    print("(Implement fixed_get_sensitivity, fixed_update_stats)")
    print()
    # Uncomment after implementing:
    # empty_config = {}
    # print(f"Sensitivity from empty config: {fixed_get_sensitivity(empty_config)}")
    # fixed_update_stats(empty_config, "health", 200)
    # print(f"After update: {empty_config}")

    print()
    print("=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print("=" * 60)


if __name__ == "__main__":
    main()
