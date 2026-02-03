"""
{{CONTEXT_INVESTIGATION_INTRO}}
{{CONTEXT_INVESTIGATION_MISSION}}

Topic: Finding bugs in game logic
Difficulty: 3-4

Game logic bugs are subtle - the code runs but the game doesn't work right.
These bugs involve game state, win conditions, and scoring.
"""

import random


# ============================================================
# {{CASE_1_TITLE}}
# ============================================================
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# This game should end when a player reaches 10 points.
#
# EXPECTED BEHAVIOR:
# Game ends immediately when someone reaches 10 points
#
# ACTUAL BEHAVIOR:
# Game always plays all 10 rounds, even after someone wins
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}


def buggy_score_game():
    """This code has exactly ONE bug. Find it!"""
    player_score = 0
    computer_score = 0
    rounds = 0

    print("First to 10 wins!")

    while rounds < 10:  # BUG: Should check score conditions too!
        rounds += 1
        print(f"\n--- Round {rounds} ---")

        # Random scoring
        if random.random() < 0.5:
            player_score += 2
            print(f"You score! ({player_score}-{computer_score})")
        else:
            computer_score += 2
            print(f"Computer scores! ({player_score}-{computer_score})")

    # Winner announcement
    if player_score > computer_score:
        print("You win!")
    else:
        print("Computer wins!")


def fix_score_game():
    """
    Fix the game to end when someone reaches 10 points.

    The while condition should check both:
    - rounds < 10 (maximum rounds)
    - player_score < 10 (player hasn't won yet)
    - computer_score < 10 (computer hasn't won yet)
    """
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    #
    # The fix:
    pass


# ============================================================
# {{CASE_2_TITLE}}
# ============================================================
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# This game should reset scores between rounds.
#
# EXPECTED BEHAVIOR:
# Each new game starts with 0-0 score
#
# ACTUAL BEHAVIOR:
# Scores carry over from previous games!
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}


player_total = 0  # BUG: Global variables persist between games!
enemy_total = 0


def buggy_battle():
    """This code has exactly ONE bug. Find it!"""
    global player_total, enemy_total
    # BUG: Never reset! Should set both to 0 here.

    print(f"Battle start! Scores: {player_total}-{enemy_total}")

    for round_num in range(1, 4):
        print(f"Round {round_num}")
        if random.random() < 0.6:
            player_total += 1
            print("You hit!")
        else:
            enemy_total += 1
            print("Enemy hits!")

    print(f"Final: {player_total}-{enemy_total}")


def fix_battle():
    """
    Fix the battle to reset scores at the start.

    Add score reset at the beginning of the function:
    player_total = 0
    enemy_total = 0
    """
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    #
    # The fix (don't use globals - use local variables):
    pass


# ============================================================
# {{CASE_3_TITLE}}
# ============================================================
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# This turn-based game should alternate between players.
#
# EXPECTED BEHAVIOR:
# Player 1, Player 2, Player 1, Player 2, ...
#
# ACTUAL BEHAVIOR:
# Player 1 goes twice, then alternates wrong
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}


def buggy_turns():
    """This code has exactly ONE bug. Find it!"""
    current_player = 1
    turns_taken = 0

    while turns_taken < 6:
        print(f"Player {current_player}'s turn")
        turns_taken += 1

        # Switch players
        if current_player == 1:
            current_player = 2
        if current_player == 2:  # BUG: Should be elif!
            current_player = 1


def fix_turns():
    """
    Fix the turn alternation.

    The second 'if' should be 'elif' - otherwise after
    setting player to 2, it immediately sets back to 1!
    """
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    #
    # The fix:
    pass


# ============================================================
# {{CASE_4_TITLE}}
# ============================================================
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# This game should track high scores correctly.
#
# EXPECTED BEHAVIOR:
# New high score only if current > previous high
#
# ACTUAL BEHAVIOR:
# Always says "New high score!" even for lower scores
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}


def buggy_high_score(current_score, high_score):
    """This code has exactly ONE bug. Find it!"""
    print(f"Your score: {current_score}")
    print(f"High score: {high_score}")

    if current_score > high_score:
        high_score = current_score  # Updates local only!

    print("New high score!")  # BUG: This runs unconditionally!
    return high_score


def fix_high_score(current_score, high_score):
    """
    Fix the high score checker.

    The "New high score!" message should only print
    when the score is actually updated.
    """
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    #
    # The fix:
    pass


# ============================================================
# {{CASE_5_TITLE}}
# ============================================================
# {{CONTEXT_CASE_5_NARRATIVE}}
#
# This game loop should handle the "play again" correctly.
#
# EXPECTED BEHAVIOR:
# Ask to play again after each game, quit on "no"
#
# ACTUAL BEHAVIOR:
# Only plays once, never asks to play again
#
# {{CONTEXT_INVESTIGATION_PROMPT_5}}


def buggy_play_again():
    """This code has exactly ONE bug. Find it!"""
    playing = True

    while playing:
        print("Playing a round...")
        score = random.randint(1, 100)
        print(f"You scored: {score}")

        response = input("Play again? (yes/no): ")
        if response.lower() == "no":
            playing = False
            break  # BUG: break exits immediately, print below never runs
        # Missing: if yes, should continue loop
        # But also: the break prevents "Thanks for playing" from showing

        print("Thanks for playing!")  # This line is unreachable after "no"


def fix_play_again():
    """
    Fix the play again loop.

    The "Thanks for playing!" should print after the loop ends,
    not inside it. Also consider the flow for both yes and no.
    """
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    #
    # The fix:
    pass


def main():
    print("{{CONTEXT_INVESTIGATION_INTRO}}")
    print("=" * 50)

    print("\n=== {{CASE_1_TITLE}} ===")
    print("Testing score game:")
    # buggy_score_game()
    print("(Notice: plays all 10 rounds even if someone wins early)")

    print("\n=== {{CASE_2_TITLE}} ===")
    print("Testing battle (run twice to see the bug):")
    # buggy_battle()
    # print()
    # buggy_battle()  # Second time has wrong starting scores!

    print("\n=== {{CASE_3_TITLE}} ===")
    print("Testing turn system:")
    buggy_turns()
    print("(Notice: Player 1 only appears once!)")

    print("\n=== {{CASE_4_TITLE}} ===")
    print("Testing high score:")
    result = buggy_high_score(50, 100)  # 50 is NOT a high score!
    print(f"Returned: {result}")
    print("(Says 'New high score' even though 50 < 100)")

    print("\n=== {{CASE_5_TITLE}} ===")
    print("Testing play again:")
    # buggy_play_again()

    print("\n" + "=" * 50)
    print("{{CONTEXT_INVESTIGATION_COMPLETE}}")


main()
