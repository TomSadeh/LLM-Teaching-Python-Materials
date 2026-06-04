# %% [markdown]
# {{CONTEXT_SETBACK_INTRO}}
#
# זוהי תרגילה מרובת חלקים שבה את מצילה מערכת לוח תוצאות שקרסה.
# התחרות מחר ויש לתקן את המערכת!
#
# מושגי תכנות: מילונים, פעולות CRUD, מיון, טיפול בשגיאות
#
# חלק 1: המשבר - אבחני את הקריסה
# {{CONTEXT_SETBACK_NARRATIVE}}
#
# לוח התוצאות קרס במהלך הטורניר אמש!
# קראי את השגיאה והביני מה השתבש.
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "leaderboard.py", line 23, in <module>
#     update_score(leaderboard, "NewPlayer", 50)
#   File "leaderboard.py", line 15, in update_score
#     leaderboard[player_name] += points
# KeyError: 'NewPlayer'

# %%
leaderboard[player_name] += points

# %% [markdown]
# ## אבחני את השגיאה
#
# ענני על השאלות הבאות:
#
# 1. איזה סוג שגיאה קרה?
#    תשובה:
#
# 2. למה קרתה השגיאה?
#    תשובה:
#
# 3. מה הקוד ניסה לעשות?
#    תשובה:
#
# 4. מה ההבדל בין עדכון שחקנת קיימת
#    לבין הוספת שחקנת חדשה?
#    תשובה:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 2: חקירה - עקבי אחרי לוגיקת הניקוד
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# עקבי אחרי ההתנהגות המיועדת כדי להבין
# כיצד לוח התוצאות אמור לעבוד.

# %%
leaderboard = {"{{hero}}": 100, "{{heroine}}": 150}

# Update existing player
leaderboard["{{hero}}"] = leaderboard.get("{{hero}}", 0) + 50

# Add new player
leaderboard["{{friend}}"] = leaderboard.get("{{friend}}", 0) + 75

print(leaderboard)

# %% [markdown]
# ## מלאי את טבלת המעקב
#
# | שלב | פעולה                  | `.get()` מחזיר | לוח התוצאות אחרי           |
# |------|------------------------|----------------|----------------------------|
# | 0    | מצב התחלתי             | -              | {"{{hero}}": 100, "{{heroine}}": 150} |
# | 1    | עדכון {{hero}} +50     | 100            |                            |
# | 2    | הוספת {{friend}} +75   |                |                            |
#
# מה מודפס?

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 3: שיפור - בני מחדש את לוח התוצאות
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# בני מערכת לוח תוצאות חזקה מאפס.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# בדקי תחילה אם השחקנת קיימת.
# אם היא קיימת, החזירי `False` (אל תדרסי).
# אם היא חדשה, הוסיפי אותה עם `initial_score` והחזירי `True`.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# השתמשי ב-`.get()` כדי לטפל בבטחה בשחקניות חדשות.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# כתבי את הפונקציה הבאה:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. המירי את המילון לרשימת זוגות (שם, ניקוד) בעזרת `.items()`
# 2. מיינו לפי ניקוד (רמז: השתמשי ב-`sorted()` עם פרמטר `key`)
# 3. החזירי את `n` הראשונות
#
# > רמז: `sorted(items, key=lambda x: x[1], reverse=True)`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# קבלי את כל השחקניות ממוינות לפי ניקוד
# הדפיסי עם דירוג: `"1. PlayerName: 150 points"`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 4: צמיחה - הוסיפי תכונות חדשות
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# הוסיפי תכונות מתקדמות ללוח התוצאות.
#
# מיינו את כל השחקניות לפי ניקוד, ואז מצאי את מיקום השחקנית.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# כתבי את הפונקציה הבאה:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# השאירי את כל השחקניות אבל אפסי את הניקוד שלהן ל-0.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## MAIN

# %%
print("=" * 60)
print("{{CONTEXT_SETBACK_INTRO}}")
print("=" * 60)
print()

print(">>> PART 1: Diagnose the crash...")
print("(Complete diagnose_crash())")
print()

print(">>> PART 2: Trace the logic...")
print("(Complete trace_leaderboard())")
# Uncomment to verify:
# code_to_trace()
print()

print(">>> PART 3: Rebuild the leaderboard...")
print("(Implement all leaderboard functions)")
print()
# Uncomment after implementing Part 3:
# board = create_leaderboard()
# add_player(board, "{{hero}}", 100)
# add_player(board, "{{heroine}}", 150)
# add_player(board, "{{friend}}", 75)
# print(f"Leaderboard: {board}")
#
# update_score(board, "{{hero}}", 60)
# update_score(board, "NewPlayer", 200)  # Should not crash!
# print(f"After updates: {board}")
#
# print(f"{{{{hero}}}}'s score: {get_score(board, '{{hero}}')}")
# print(f"Top 3: {get_top_players(board, 3)}")
# print()
# display_leaderboard(board)

print()
print(">>> PART 4: Add new features...")
print("(Implement get_rank, get_players_above, reset_scores)")
# Uncomment after implementing Part 4:
# print(f"{{{{hero}}}}'s rank: {get_rank(board, '{{hero}}')}")
# print(f"Players above 100: {get_players_above(board, 100)}")
# reset_scores(board)
# print(f"After reset: {board}")

print()
print("=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print("=" * 60)
