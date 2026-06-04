# %% [markdown]
# {{CONTEXT_SETBACK_INTRO}}
#
# זוהי תרגיל רב-חלקי לבניית משחק אבן-נייר-מספריים.
# השלימי כל חלק כדי להגיע מקוד עם באגים למשחק שלם!
#
# מושגי תכנות: לולאות `while`, `random`, תנאים, מצב משחק

# %%
import random

# %% [markdown]
# ## חלק 1: משחק אבן-נייר-מספריים עם באגים
# {{CONTEXT_SETBACK_NARRATIVE}}
#
# המשחק הראשון של {{hero}} היה מלא בבאגים. {{villain}} ניצל אותם!
# מצאי ותקני את 3 הבאגים.
#
# מספר באגים למצוא: 3

# %%
# BUG 1: Wrong comparison - paper vs rock
if player == "rock" and computer == "scissors":
    return "player"
elif player == "paper" and computer == "scissors":  # BUG: should be rock!
    return "player"
elif player == "scissors" and computer == "paper":
    return "player"
# BUG 2: These conditions are duplicates of player wins!
elif player == "rock" and computer == "paper":
    return "player"  # BUG: Should return "computer"!
elif player == "paper" and computer == "scissors":
    return "computer"
elif player == "scissors" and computer == "rock":
    return "computer"
# BUG 3: Missing the equals case properly
else:
    return None  # BUG: Should explicitly check for tie

# %%
choices = ["rock", "paper", "scissors"]

player = input("Choose (rock/paper/scissors): ").lower()
computer = random.choice(choices)

print(f"You chose: {player}")
print(f"{{{{villain}}}} chose: {computer}")

result = buggy_determine_winner(player, computer)
if result == "player":
    print("You win!")
elif result == "computer":
    print("{{{{villain}}}} wins!")
else:
    print("It's a tie!")

# %% [markdown]
# > רמז: בדקי קודם תיקו עם `player == computer`
# > אחר כך בדקי את שלושת תנאי הניצחון של השחקן
# > שאר המקרים הם ניצחון המחשב

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: בניית הליבה
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# בני פונקציות אבן-נייר-מספריים תקינות מאפס.
#
# 1. הגדירי `valid_choices` וקיצורים: `shortcuts = {'r': 'rock', 'p': 'paper', 's': 'scissors'}`
# 2. לולאת `While True`
# 3. קבלי קלט ממשתמשת, המרי לאותיות קטנות
# 4. בדקי אם הקלט נמצא בקיצורים, המרי
# 5. בדקי אם הקלט נמצא ב-`valid_choices`
# 6. אם תקין — החזירי. אחרת — הדפיסי שגיאה.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. קבלי את בחירת השחקן
# 2. קבלי את בחירת המחשב
# 3. הדפיסי את הבחירות (השתמשי ב-{{villain}} עבור המחשב)
# 4. קבעי מנצח באמצעות `fixed_determine_winner`
# 5. הכריזי על התוצאה
# 6. החזירי את התוצאה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: האליפות
# {{CONTEXT_CONFRONTATION_INTRO}}
# {{CONTEXT_CONFRONTATION_NARRATIVE}}
#
# בני את המשחק המלא עם:
# - מעקב ניקוד
# - לולאת "שחקי שוב"
# - סטטיסטיקות משחק

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print(f"\n=== First to {rounds_to_win} wins! ===\n")

player_wins = 0
computer_wins = 0
ties = 0

# %% [markdown]
# כל עוד אף שחקן לא צברה מספיק ניצחונות:
# 1. שחקי סיבוב
# 2. עדכני את המונה המתאים
# 3. הציגי את הניקוד הנוכחי
# 4. בדקי אם יש מנצחת
#
# אחרי הלולאה: הכריזי על מנצחת המשחק

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("=" * 50)
print("   ROCK PAPER SCISSORS CHAMPIONSHIP")
print(f"   {{{{hero}}}} vs {{{{villain}}}}")
print("=" * 50)

total_games = 0
player_championships = 0
villain_championships = 0

# %% [markdown]
# לולאת "שחקי שוב":
# 1. בקשי את אורך המשחק (1, 2 או 3 עבור מיטב מתוך 3/5/7)
# 2. המרי ל-`rounds_to_win` (2, 3 או 4)
# 3. שחקי מחזור
# 4. עדכני את נתוני האליפות
# 5. הציגי את התוצאה הכוללת
# 6. שאלי אם לשחק שוב
#
# בסוף: הציגי ברכת פרידה ותוצאה סופית

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## ראשי

# %%
print("=" * 60)
print("{{CONTEXT_SETBACK_INTRO}}")
print("=" * 60)
print()

print(">>> PART 1: Fix the buggy RPS...")
print("(Review buggy_determine_winner and implement fixed version)")
print()
# Test the fix:
# print("Testing fixed winner logic:")
# test_cases = [
#     ("rock", "scissors", "player"),
#     ("paper", "rock", "player"),
#     ("scissors", "paper", "player"),
#     ("rock", "paper", "computer"),
#     ("paper", "scissors", "computer"),
#     ("scissors", "rock", "computer"),
#     ("rock", "rock", "tie"),
# ]
# for p, c, expected in test_cases:
#     result = fixed_determine_winner(p, c)
#     status = "OK" if result == expected else "FAIL"
#     print(f"  {p} vs {c}: {result} ({status})")

print()
print(">>> PART 2: Build the core game...")
print("(Implement get_player_choice, get_computer_choice, play_round)")
print()
# Uncomment to test:
# result = play_round()
# print(f"Result: {result}")

print()
print(">>> PART 3: The Championship awaits...")
print("(Implement display_score, play_match, championship)")
print()
# Uncomment to play:
# championship()

print()
print("=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print("=" * 60)
