# %% [markdown]
# {{CONTEXT_OWNERSHIP_INTRO}}
#
# זהו פרויקט הסיום שלך: בני את המשחק שלך!
# עקבי אחרי השלבים המודרכים כדי ליצור משחק שלם ומלוטש.
#
# מושגי תכנות: כל מה שלמדנו במודול 5!

# %%
import random

# %% [markdown]
# ## חלק 1: עצבי את המשחק שלך
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# לפני שמתחילים לכתוב קוד, עצבי את המשחק!
#
# ענּי על השאלות האלה (בהערות או על נייר):
# 1. על מה המשחק שלך? (נושא, סיפור)
# 2. מה השחקנית עושה? (פעולות, מטרות)
# 3. איך השחקנית מנצחת? (תנאי ניצחון)
# 4. איך השחקנית מפסידה? (תנאי הפסד, או שאין?)
# 5. מה הופך אותו לכיף? (אקראיות, בחירות, אתגר)
#
# עיצוב המשחק שלי
# ----------------
# נושא: ________________________________
# מטרה: ________________________________
# תנאי ניצחון: ________________________________
# תנאי הפסד: ________________________________
# המנגנון המרכזי: ________________________________
#
# פעולות השחקנית:
# 1. ________________________________
# 2. ________________________________
# 3. ________________________________
#
# מצב משחק לעקוב אחריו:
# - ________________________________
# - ________________________________
# - ________________________________
#
# ## חלק 2: בני את הבסיס
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# ממשי את מנגנוני המשחק הבסיסיים.
#
# צרי והחזירי את מצב המשחק ההתחלתי שלך

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# הגדירי את הפעולות האפשריות
# הציגי תפריט
# קבלי ואמתי את הקלט
# החזירי את הפעולה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# טפלי בכל פעולה אפשרית
# עדכני את `game_state` בהתאם
# החזירי תיאור של מה שקרה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: הוסיפי תנאי ניצחון והפסד
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# הגדירי מתי המשחק מסתיים.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 4: הפכי את המשחק לעמיד לשגיאות
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# הוסיפי בדיקת קלט וטיפול בשגיאות בכל המשחק.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 5: הוסיפי ליטוש
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# גרמי למשחק שלך להרגיש שלם!
#
# צרי פתיחה מרתקת למשחק שלך
# השתמשי ב-`{{placeholders}}` לתוכן שאינו תלוי נושא!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 6: המשחק המלא
# {{CONTEXT_TRIUMPH_COMPLETE}}
#
# חברי הכול יחד!

# %%
while game_state.get("playing", True):
    # ✏️ YOUR CODE HERE ✏️
    #
    # 1. Display current status
    # 2. Check win condition
    #    If won: display_end_message, break
    # 3. Check lose condition
    #    If lost: display_end_message, break
    # 4. Get player action
    # 5. If action is "quit", break
    # 6. Process action
    # 7. Display result message
    pass

# %%
display_intro()

playing = True
while playing:
    game_state = initialize_game()

    if game_state is None:
        print("Failed to initialize game!")
        break

    game_loop(game_state)

    playing = ask_play_again()

print("\nThanks for playing!")
print(f"{{{{exclamation}}}} Until next time!")

# %% [markdown]
# ## תוכנית ראשית

# %%
print("=" * 60)
print("   BUILD YOUR OWN GAME")
print("   Module 5 Capstone Project")
print("=" * 60)
print()

print(">>> PART 1: Design your game (see comments above)")
print()

print(">>> PART 2: Build the core")
print("(Implement initialize_game, display_status, get_player_input, process_action)")
print()
# Test core:
# state = initialize_game()
# display_status(state)
# action = get_player_input(state)
# result = process_action(state, action)
# print(result)

print(">>> PART 3: Add win/lose conditions")
print("(Implement check_win, check_lose, display_end_message)")
print()

print(">>> PART 4: Make it crash-proof")
print("(Implement validate_game_state, safe_update_stat)")
print()

print(">>> PART 5: Add polish")
print("(Implement display_intro, display_help, ask_play_again)")
print()

print(">>> PART 6: Launch your game!")
print()
# play_game()

print("=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print("=" * 60)
