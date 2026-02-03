"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}

Topic: Building a complete simple game
Difficulty: 4-5

Combine everything you've learned to build a complete,
playable game with loops, random, input validation, and state!
"""

import random


# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}
#
# Build the core game mechanics.


def roll_stat():
    """
    Roll a random stat value.

    Returns:
        int: Random value from 3 to 18 (like 3d6)

    Roll three 6-sided dice and sum them.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def create_character(name):
    """
    Create a new character with random stats.

    Args:
        name: The character's name

    Returns:
        dict: Character with name, hp, max_hp, attack, defense

    Stats:
    - max_hp: roll_stat() + 10
    - hp: starts equal to max_hp
    - attack: roll_stat()
    - defense: roll_stat() // 2
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def create_enemy(name, difficulty):
    """
    Create an enemy scaled to difficulty.

    Args:
        name: Enemy name
        difficulty: 1-3 (easy, medium, hard)

    Returns:
        dict: Enemy with name, hp, max_hp, attack, defense

    Scale:
    - hp: 10 + (difficulty * 5) + random 1-5
    - attack: 5 + (difficulty * 2) + random 1-3
    - defense: 2 + difficulty
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}
#
# Build the combat system.


def calculate_damage(attacker, defender):
    """
    Calculate damage from attacker to defender.

    Args:
        attacker: Dict with 'attack' stat
        defender: Dict with 'defense' stat

    Returns:
        int: Damage dealt (minimum 1)

    Formula: attacker['attack'] - defender['defense'] + random(-2, 2)
    Always deal at least 1 damage.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def attack(attacker, defender):
    """
    Perform an attack.

    Args:
        attacker: The attacking character dict
        defender: The defending character dict

    Returns:
        int: Damage dealt

    Process:
    1. Calculate damage
    2. Subtract from defender's hp
    3. Print attack message with damage
    4. Return damage dealt
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def is_alive(character):
    """
    Check if a character is still alive.

    Args:
        character: Character dict with 'hp'

    Returns:
        bool: True if hp > 0
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}
#
# Build player actions.


def player_attack(player, enemy):
    """
    Player performs a basic attack.

    Args:
        player: Player character dict
        enemy: Enemy character dict

    Returns:
        int: Damage dealt
    """
    print(f"\n{{{{hero}}}} attacks {{{{villain}}}}!")
    return attack(player, enemy)


def player_defend(player):
    """
    Player takes defensive stance.

    Args:
        player: Player character dict

    Returns:
        int: Temporary defense bonus (3)

    Also prints a message about defending.
    """
    # ✏️ YOUR CODE HERE ✏️
    #
    # Print defending message
    # Return 3 (temporary defense bonus)
    pass


def player_heal(player):
    """
    Player attempts to heal.

    Args:
        player: Player character dict

    Returns:
        int: Amount healed

    Healing:
    - Heal 5 + random(1, 5) hp
    - Cannot exceed max_hp
    - Print message with amount healed
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def get_player_action():
    """
    Get the player's action choice.

    Returns:
        str: 'attack', 'defend', or 'heal'

    Display menu:
    1. Attack
    2. Defend
    3. Heal

    Accept number (1-3) or word.
    Keep asking until valid.
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}
#
# Build the combat loop.


def display_status(player, enemy):
    """
    Display current combat status.

    Format:
        ========================================
        {{hero}}: 25/30 HP    {{villain}}: 15/20 HP
        ========================================
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def combat_round(player, enemy, defending):
    """
    Execute one round of combat.

    Args:
        player: Player character dict
        enemy: Enemy character dict
        defending: Bool, True if player defended last turn

    Returns:
        tuple: (player_alive, enemy_alive, now_defending)

    Round structure:
    1. Get player action
    2. Execute player action
    3. If enemy still alive, enemy attacks
       - If player was defending, reduce damage
    4. Return status
    """
    # ✏️ YOUR CODE HERE ✏️
    pass


def battle(player, enemy):
    """
    Run a complete battle.

    Args:
        player: Player character dict
        enemy: Enemy character dict

    Returns:
        bool: True if player won

    Battle loop:
    1. Display status
    2. Run combat round
    3. Check for battle end
    4. Repeat until someone loses
    5. Announce winner
    """
    print("\n" + "=" * 50)
    print(f"   BATTLE: {{{{hero}}}} vs {enemy['name']}")
    print("=" * 50)

    defending = False

    # ✏️ YOUR CODE HERE ✏️
    #
    # While both alive:
    #   1. Display status
    #   2. Run combat round, get new defending state
    #   3. Check if battle over
    #
    # After loop: Announce winner, return result
    pass


# ============================================================
# {{PHASE_5_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_5}}
#
# Build the complete game.


def introduction():
    """
    Display game introduction.
    """
    print("=" * 50)
    print("   ARENA CHAMPION")
    print(f"   A {{{{school}}}} Adventure")
    print("=" * 50)
    print()
    print(f"{{{{hero}}}} enters {{{{location}}}} to face {{{{villain}}}}!")
    print("Victory means glory. Defeat means... starting over.")
    print()


def play_game():
    """
    Run the complete game.

    Structure:
    1. Introduction
    2. Create player character
    3. Fight through 3 enemies of increasing difficulty
    4. Track wins/losses
    5. Offer play again

    Game flow:
    - Player starts fresh each game
    - Fight enemy 1 (easy), enemy 2 (medium), enemy 3 (hard)
    - After each battle, restore some HP if won
    - If player loses, game over
    - If player wins all 3, victory!
    """
    introduction()

    playing = True
    while playing:
        print("\n--- Creating your champion ---")
        name = input("Enter your champion's name: ").strip()
        if not name:
            name = "{{hero}}"

        player = create_character(name)
        print(f"\n{name} enters the arena!")
        print(f"HP: {player['hp']} | Attack: {player['attack']} | Defense: {player['defense']}")

        # ✏️ YOUR CODE HERE ✏️
        #
        # Create three enemies with increasing difficulty:
        # enemies = [
        #     create_enemy("{{creature}}", 1),
        #     create_enemy("{{villain}}'s Minion", 2),
        #     create_enemy("{{villain}}", 3)
        # ]
        #
        # Battle loop:
        # For each enemy:
        #   1. Print "Battle X of 3"
        #   2. Run battle
        #   3. If lost, print game over, break
        #   4. If won and not last battle, restore 10 HP
        #
        # If completed all battles: Victory message!
        #
        # Ask to play again
        pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)

    print("\n=== {{PHASE_1_TITLE}} ===")
    print("Testing character creation:")
    # player = create_character("Test")
    # print(f"Player: {player}")
    # enemy = create_enemy("Goblin", 2)
    # print(f"Enemy: {enemy}")

    print("\n=== {{PHASE_2_TITLE}} ===")
    print("Testing combat:")
    # player = create_character("Test")
    # enemy = create_enemy("Target", 1)
    # damage = attack(player, enemy)
    # print(f"Enemy HP: {enemy['hp']}")

    print("\n=== {{PHASE_3_TITLE}} ===")
    print("Testing player actions:")
    # (test individual actions)

    print("\n=== {{PHASE_4_TITLE}} ===")
    print("Testing battle:")
    # player = create_character("Champion")
    # enemy = create_enemy("Challenger", 1)
    # result = battle(player, enemy)
    # print(f"Player won: {result}")

    print("\n=== {{PHASE_5_TITLE}} ===")
    print("Launch full game:")
    # play_game()

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
