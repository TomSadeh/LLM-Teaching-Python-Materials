"""
{{CONTEXT_DISCOVERY_INTRO}}

This is the capstone project for Module 7. You'll study a model system,
design your own structure, implement operations, and add a custom feature.

Programming concepts: All dictionary concepts from Module 7
"""


# ============================================================
# PART 1: Discovery - Study the Model System
# ============================================================
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# Study this achievement system to understand how it works.


MODEL_ACHIEVEMENTS = {
    "achievements": {
        "first_steps": {
            "name": "First Steps",
            "description": "Complete the tutorial",
            "points": 10,
            "category": "progress"
        },
        "collector": {
            "name": "Collector",
            "description": "Collect 100 items",
            "points": 25,
            "category": "collection"
        },
        "master": {
            "name": "Master",
            "description": "Reach level 50",
            "points": 100,
            "category": "progress"
        }
    },
    "players": {
        "{{hero}}": {
            "unlocked": ["first_steps"],
            "total_points": 10
        },
        "{{heroine}}": {
            "unlocked": ["first_steps", "collector"],
            "total_points": 35
        }
    }
}


def study_model():
    """Study how the model system works."""
    system = MODEL_ACHIEVEMENTS

    # Get all achievement IDs
    achievement_ids = list(system["achievements"].keys())

    # Get a specific achievement's details
    collector_details = system["achievements"]["collector"]

    # Check what {{hero}} has unlocked
    hero_unlocked = system["players"]["{{hero}}"]["unlocked"]

    # Get {{hero}}'s points
    hero_points = system["players"]["{{hero}}"]["total_points"]

    print(f"All achievements: {achievement_ids}")
    print(f"Collector details: {collector_details}")
    print(f"{{{{hero}}}} unlocked: {hero_unlocked}")
    print(f"{{{{hero}}}} points: {hero_points}")


def trace_model_access():
    # ✏️ FILL IN THE TRACING TABLE ✏️
    #
    # Trace the path to access each piece of data:
    #
    # | Data                  | Access Path                                    |
    # |-----------------------|------------------------------------------------|
    # | "Master" name         | MODEL_ACHIEVEMENTS["achievements"]["master"]["name"] |
    # | Collector points      | MODEL_ACHIEVEMENTS[?][?][?]                   |
    # | {{heroine}}'s points  | MODEL_ACHIEVEMENTS[?][?][?]                   |
    # | Is {{hero}} a master? | "master" in MODEL_ACHIEVEMENTS[?][?][?]       |
    #
    # How many levels deep is the deepest access?
    #

    pass


# ============================================================
# PART 2: Growth - Design Your Own Structure
# ============================================================
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Design and create your own data system using dictionaries.


def create_quest_system():
    """
    Create a quest tracking system.

    Returns:
        dict: A quest system with 'quests' and 'players' sections.

    Structure:
        {
            "quests": {
                "quest_id": {
                    "name": str,
                    "description": str,
                    "reward": int,
                    "difficulty": str ("easy", "medium", "hard")
                },
                ...
            },
            "players": {
                "player_name": {
                    "active_quests": [list of quest_ids],
                    "completed_quests": [list of quest_ids],
                    "total_rewards": int
                },
                ...
            }
        }

    Create at least 3 quests and 2 players.
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Design your own quests! Be creative with names and descriptions.
    # Use {{placeholders}} for thematic content.

    pass


# ============================================================
# PART 3: Growth - Implement Core Operations
# ============================================================
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# Implement CRUD operations for your quest system.


def add_quest(system, quest_id, name, description, reward, difficulty):
    """
    Add a new quest to the system.

    Args:
        system: The quest system dictionary
        quest_id: Unique identifier for the quest
        name: Display name of the quest
        description: Quest description
        reward: Points awarded on completion
        difficulty: "easy", "medium", or "hard"

    Returns:
        bool: True if added, False if quest_id already exists
    """
    # ✏️ YOUR CODE HERE ✏️

    pass


def add_player(system, player_name):
    """
    Add a new player to the system.

    Args:
        system: The quest system dictionary
        player_name: Name of the new player

    Returns:
        bool: True if added, False if player already exists

    New players start with empty quest lists and 0 rewards.
    """
    # ✏️ YOUR CODE HERE ✏️

    pass


def start_quest(system, player_name, quest_id):
    """
    Start a quest for a player.

    Args:
        system: The quest system dictionary
        player_name: Player starting the quest
        quest_id: Quest to start

    Returns:
        bool: True if started, False if:
              - Player doesn't exist
              - Quest doesn't exist
              - Quest already active or completed
    """
    # ✏️ YOUR CODE HERE ✏️

    pass


def complete_quest(system, player_name, quest_id):
    """
    Complete an active quest for a player.

    Args:
        system: The quest system dictionary
        player_name: Player completing the quest
        quest_id: Quest to complete

    Returns:
        int: Reward points earned, or 0 if:
             - Player doesn't exist
             - Quest not in player's active quests

    Move quest from active to completed and add rewards.
    """
    # ✏️ YOUR CODE HERE ✏️

    pass


def get_player_stats(system, player_name):
    """
    Get statistics for a player.

    Args:
        system: The quest system dictionary
        player_name: Player to get stats for

    Returns:
        dict or None: Stats dictionary with keys:
                      - "active_count": int
                      - "completed_count": int
                      - "total_rewards": int
                      - "completion_rate": float (0.0 to 1.0)
                      Returns None if player doesn't exist.
    """
    # ✏️ YOUR CODE HERE ✏️

    pass


def get_available_quests(system, player_name):
    """
    Get quests the player hasn't started or completed.

    Args:
        system: The quest system dictionary
        player_name: Player to check

    Returns:
        list: Quest IDs that are available to this player
              Empty list if player doesn't exist
    """
    # ✏️ YOUR CODE HERE ✏️

    pass


# ============================================================
# PART 4: Ownership - Add Your Own Feature
# ============================================================
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# Design and implement a new feature of your own choice!


def your_custom_feature(system, *args, **kwargs):
    """
    Implement a feature of your own design!

    Ideas:
    - Quest chains (complete quest A to unlock quest B)
    - Difficulty bonuses (harder quests give more rewards)
    - Quest categories with filtering
    - Leaderboard of top players
    - Quest recommendations based on player level
    - Achievement badges for quest milestones

    Document what your feature does in this docstring,
    then implement it below.

    Your feature: _______________
    Description: _______________
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Be creative! This is YOUR feature.

    pass


# ============================================================
# DEMONSTRATION
# ============================================================

def demonstrate_system():
    """Demonstrate the quest system in action."""
    print("=== Creating Quest System ===")
    system = create_quest_system()

    if system is None:
        print("Please implement create_quest_system() first!")
        return

    print(f"Quests: {list(system['quests'].keys())}")
    print(f"Players: {list(system['players'].keys())}")
    print()

    print("=== Adding New Content ===")
    # Add a new quest
    add_quest(system, "secret", "Secret Mission",
              "Find the hidden {{item}}", 50, "hard")
    print(f"Added secret quest: {'secret' in system['quests']}")

    # Add a new player
    add_player(system, "{{friend}}")
    print(f"Added {{{{friend}}}}: {'{{friend}}' in system['players']}")
    print()

    print("=== Quest Operations ===")
    # Start a quest
    if start_quest(system, "{{friend}}", "secret"):
        print("{{friend}} started the secret quest!")

    # Complete a quest
    reward = complete_quest(system, "{{friend}}", "secret")
    print(f"{{{{friend}}}} completed quest, earned {reward} points!")
    print()

    print("=== Player Stats ===")
    stats = get_player_stats(system, "{{friend}}")
    if stats:
        print(f"{{{{friend}}}} stats: {stats}")

    available = get_available_quests(system, "{{friend}}")
    print(f"Available quests for {{{{friend}}}}: {available}")
    print()

    print("=== Your Custom Feature ===")
    # Call your custom feature here
    # result = your_custom_feature(system, ...)
    # print(f"Custom feature result: {result}")
    print("(Implement and demonstrate your custom feature!)")


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print("{{CONTEXT_DISCOVERY_INTRO}}")
    print("=" * 60)
    print()

    print(">>> PART 1: Study the model system...")
    print()
    study_model()
    print()
    print("(Complete trace_model_access())")
    print()

    print(">>> PART 2: Design your quest system...")
    print("(Implement create_quest_system())")
    print()

    print(">>> PART 3: Implement operations...")
    print("(Implement add_quest, add_player, start_quest, complete_quest,")
    print(" get_player_stats, get_available_quests)")
    print()

    print(">>> PART 4: Add your custom feature...")
    print("(Design and implement your_custom_feature())")
    print()

    # Uncomment to demonstrate:
    # demonstrate_system()

    print()
    print("=" * 60)
    print("{{CONTEXT_TRIUMPH_COMPLETE}}")
    print()
    print("Congratulations! You've mastered dictionaries!")
    print("=" * 60)


if __name__ == "__main__":
    main()
