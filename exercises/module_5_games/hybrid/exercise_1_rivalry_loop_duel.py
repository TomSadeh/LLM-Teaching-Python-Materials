# %% [markdown]
# {{CONTEXT_SETBACK_INTRO}}
#
# זוהי תרגילה רב-חלקית שעוקבת אחרי המסע של {{hero}} מתבוסה לניצחון.
# השלימי כל חלק לפי הסדר.
#
# מושגי תכנות: לולאות `while`, `random`, מצב משחק, תנאים

# %%
import random

# %% [markdown]
# ## חלק 1: התבוסה
# {{CONTEXT_SETBACK_NARRATIVE}}
#
# הקוד של {{hero}} מהמשחק האחרון היה מלא בבאגים. בגלל זה {{villain}} ניצח.
# מצאי ותקני את 3 הבאגים כדי שזה לא יקרה שוב.
#
# באגים למציאה: 3

# %%
player_a_score = 0
player_b_score = 0
rounds_played = 0
max_rounds = 5

print(f"=== {{{{hero}}}} vs {{{{villain}}}} ===")
print()

while rounds_played < max_rounds:  # BUG 1: Should be <=, misses round 5
    rounds_played += 1
    print(f"--- Round {rounds_played} ---")

    # {{hero}}'s turn
    player_a_result = random.choice(["success", "success", "fail"])
    if player_a_result == "success":
        player_a_score + 1  # BUG 2: Should be player_a_score += 1
        print(f"{{{{hero}}}} scores! Total: {player_a_score}")
    else:
        print(f"{{{{hero}}}} misses...")

    # {{villain}}'s turn
    player_b_result = random.choice(["success", "success", "fail"])
    if player_b_result == "success":
        player_b_score += 1
        print(f"{{{{villain}}}} scores. Total: {player_b_score}")
    else:
        print(f"{{{{villain}}}} misses!")

    print()

print("=== FINAL RESULT ===")
print(f"{{{{hero}}}}: {player_a_score}")
print(f"{{{{villain}}}}: {player_b_score}")

if player_a_score >= player_b_score:  # BUG 3: Should be > for hero win, = is tie
    print(f"{{{{villain}}}} wins!")
else:
    print(f"{{{{hero}}}} wins!")

# %% [markdown]
# ## תקני את הקוד למטה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: אימון
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# {{hero}} צריכה יכולת חדשה: המהלך העוצמתי.
#
# מהלך עוצמתי הוא סיכון גבוה, תגמול גבוה:
# - סיכוי של 40%: הצלחה קריטית (2 נקודות!)
# - סיכוי של 30%: הצלחה רגילה (נקודה אחת)
# - סיכוי של 30%: כישלון (0 נקודות)
#
# ממשי את המהלך העוצמתי ולולאת אימון לתרגל אותו.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
result = random.choice(["success", "success", "fail"])
if result == "success":
    return 1
return 0

# %%
total_points = 0
attempts = 0

print("=== TRAINING SESSION ===")
print(f"{{{{hero}}}} practices for the rematch against {{{{villain}}}}.")
print()
print("Commands: 'r' = regular move, 'p' = power move, 'q' = quit")
print()

# %% [markdown]
# ממשי את לולאת האימון:
# 1. בקשי קלט מהמשתמשת (`r`/`p`/`q`)
# 2. בצעי את המהלך שנבחר
# 3. הציגי את התוצאה ואת הסכום השוטף
# 4. המשיכי עד שמקישים `q`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
pass

print()
print("=== TRAINING COMPLETE ===")
print(f"Total points: {total_points}")
print(f"Attempts: {attempts}")
if attempts > 0:
    print(f"Average: {total_points / attempts:.2f} points per attempt")

# %% [markdown]
# ## חלק 3: ההתמודדות
# {{CONTEXT_CONFRONTATION_INTRO}}
# {{CONTEXT_CONFRONTATION_NARRATIVE}}
#
# המשחק החוזר! בני את ההתמודדות המלאה:
# - 5 סיבובי תחרות
# - {{hero}} יכולה לבחור מהלך רגיל או עוצמתי בכל סיבוב
# - {{villain}} תמיד משתמש במהלכים רגילים
# - אם תיקו אחרי 5 סיבובים: מוות פתאומי עד שמישהו מוביל
#
# השתמשי בכל מה שלמדת. זה המבחן הסופי.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
#

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print(f"--- Round {round_num} ---")
print(f"Score: {{{{hero}}}} {player_a_score} - {player_b_score} {{{{villain}}}}")

# %% [markdown]
#

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("=" * 50)
print("   THE FINAL SHOWDOWN")
print(f"   {{{{hero}}}} vs {{{{villain}}}}")
print("=" * 50)
print()

player_a_score = 0
player_b_score = 0

# %% [markdown]
# 1. משחק ראשי: 5 סיבובים
# 2. בדקי מי ניצחת
# 3. אם תיקו: מוות פתאומי
# 4. הכריזי על המנצחת

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## ראשי

# %%
print("=" * 60)
print("{{CONTEXT_SETBACK_INTRO}}")
print("=" * 60)
print()

print(">>> PART 1: Analyzing the defeat...")
print("(Review buggy_match() and implement fixed_match())")
print()
# Uncomment to test:
# fixed_match()

print()
print(">>> PART 2: Training begins...")
print("(Implement attempt_power_move() and training_session())")
print()
# Uncomment to test:
# training_session()

print()
print(">>> PART 3: The showdown awaits...")
print("(Implement all showdown functions)")
print()
# Uncomment to test:
# the_showdown()

print()
print("=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print("=" * 60)
