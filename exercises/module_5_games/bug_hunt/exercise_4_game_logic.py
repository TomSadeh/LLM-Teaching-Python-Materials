# %% [markdown]
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_MISSION}}
#
# נושא: מציאת באגים בלוגיקת משחקים
# רמת קושי: 3-4
#
# באגים בלוגיקת משחקים הם עדינים - הקוד רץ אבל המשחק לא עובד כמו שצריך.
# הבאגים האלה קשורים למצב המשחק, תנאי ניצחון וניקוד.

# %%
import random

# %% [markdown]
# ## {{CASE_1_TITLE}}
# {{CONTEXT_CASE_1_NARRATIVE}}
#
# המשחק הזה אמור להסתיים כשמישהי מגיעה ל-10 נקודות.
#
# התנהגות צפויה:
# המשחק מסתיים מיד כשמישהי מגיעה ל-10 נקודות
#
# התנהגות בפועל:
# המשחק תמיד משחק את כל 10 הסיבובים, אפילו אחרי שמישהי ניצחה
#
# {{CONTEXT_INVESTIGATION_PROMPT_1}}

# %%
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

# %% [markdown]
# מה מצאתי: ________________________________
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CASE_2_TITLE}}
# {{CONTEXT_CASE_2_NARRATIVE}}
#
# המשחק הזה אמור לאפס את הניקוד בין משחקים.
#
# התנהגות צפויה:
# כל משחק חדש מתחיל עם ניקוד 0-0
#
# התנהגות בפועל:
# הניקוד עובר ממשחק למשחק!
#
# {{CONTEXT_INVESTIGATION_PROMPT_2}}

# %%
player_total = 0  # BUG: Global variables persist between games!

# %%
enemy_total = 0

# %%
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

# %% [markdown]
# מה מצאתי: ________________________________
#
# התיקון (אל תשתמשי ב-globals - השתמשי במשתנים מקומיים):

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CASE_3_TITLE}}
# {{CONTEXT_CASE_3_NARRATIVE}}
#
# המשחק הזה מבוסס תורות ואמור להתחלף בין השחקניות.
#
# התנהגות צפויה:
# שחקנית 1, שחקנית 2, שחקנית 1, שחקנית 2, ...
#
# התנהגות בפועל:
# שחקנית 1 משחקת פעמיים, ואז החלפת התורות מתבלבלת
#
# {{CONTEXT_INVESTIGATION_PROMPT_3}}

# %%
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

# %% [markdown]
# מה מצאתי: ________________________________
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CASE_4_TITLE}}
# {{CONTEXT_CASE_4_NARRATIVE}}
#
# המשחק הזה אמור לעקוב אחרי השיא בצורה נכונה.
#
# התנהגות צפויה:
# שיא חדש רק אם הניקוד הנוכחי גבוה מהשיא הקודם
#
# התנהגות בפועל:
# תמיד מדפיס `New high score!` אפילו לניקוד נמוך יותר
#
# {{CONTEXT_INVESTIGATION_PROMPT_4}}

# %%
print(f"Your score: {current_score}")
print(f"High score: {high_score}")

if current_score > high_score:
    high_score = current_score  # Updates local only!

print("New high score!")  # BUG: This runs unconditionally!
return high_score

# %% [markdown]
# מה מצאתי: ________________________________
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CASE_5_TITLE}}
# {{CONTEXT_CASE_5_NARRATIVE}}
#
# לולאת המשחק הזו אמורה לטפל ב"שחקי שוב?" בצורה נכונה.
#
# התנהגות צפויה:
# לשאול "שחקי שוב?" אחרי כל משחק, ולצאת על "no"
#
# התנהגות בפועל:
# משחקת פעם אחת בלבד, ולעולם לא שואלת שוב
#
# {{CONTEXT_INVESTIGATION_PROMPT_5}}

# %%
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

# %% [markdown]
# מה מצאתי: ________________________________
#
# התיקון:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
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
