# %% [markdown]
# {{CONTEXT_SETBACK_INTRO}}
#
# זוהי תרגיל מרובה-חלקים שעוקב אחרי המסע לבניית משחק ניחוש מספרים.
# השלימי כל חלק לפי הסדר.
#
# מושגי תכנות: לולאות `while`, `random`, השוואות, אימות קלט

# %%
import random

# %% [markdown]
# ## PART 1: The Broken Game
# {{CONTEXT_SETBACK_NARRATIVE}}
#
# הניסיון הראשון של {{hero}} במשחק ניחוש היה מלא בבאגים.
# {{villain}} מצא את כל הפגמים וניצל אותם!
#
# מצאי ותקני את 3 הבאגים בקוד שלמטה.
#
# מספר באגים למציאה: 3

# %%
secret = random.randint(0, 9)  # BUG 1: Should be 1-10, not 0-9
guesses = 0
max_guesses = 5

print("Guess my number (1-10)!")

while guesses < max_guesses:
    guess_str = input("Your guess: ")

    if not guess_str.isdigit():
        print("Please enter a number!")
        continue

    guess = int(guess_str)

    if guess < secret:  # BUG 2: Logic inverted! < should give "higher" hint
        print("Go lower!")
    elif guess > secret:
        print("Go higher!")
    else:
        print(f"Correct! You got it in {guesses} guesses!")
        return True
    # BUG 3: guesses is never incremented!

print(f"Out of guesses! The number was {secret}")
return False

# %% [markdown]
# מה מצאתי:
# באג 1: ________________________________
# באג 2: ________________________________
# באג 3: ________________________________

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## PART 2: Building Better
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# עכשיו בני משחק ניחוש תקין עם התכונות הבאות:
# - טווח שניתן להגדרה (מינימום עד מקסימום)
# - ניחושים ללא הגבלה
# - מעקב אחר מספר הניחושים
# - אימות שהקלט נמצא בטווח
#
# 1. בדקי אם `guess_str` הוא מספר (השתמשי ב-`.lstrip('-').isdigit()` למספרים שליליים)
#    אם לא, החזירי `(False, "Not a number")`
# 2. המירי למספר שלם
# 3. בדקי אם הוא בטווח
#    אם לא, החזירי `(False, f"Out of range ({min_val}-{max_val})")`
# 4. החזירי `(True, integer_value)`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# השווי את הניחוש ל-`secret` והחזירי/הדפיסי את התגובה המתאימה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. צרי את ה-`secret` עם `random.randint(min_val, max_val)`
# 2. אתחלי `guess_count = 0`
# 3. לופי עד שניחשת נכון:
#    - קבלי קלט
#    - אמתי עם `validate_guess()`
#    - אם לא תקין, הדפיסי שגיאה והמשיכי
#    - הגדילי את `guess_count`
#    - קבלי רמז עם `give_hint()`
#    - אם נכון, צאי מהלולאה
# 4. החזירי את `guess_count`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## PART 3: The Championship
# {{CONTEXT_CONFRONTATION_INTRO}}
# {{CONTEXT_CONFRONTATION_NARRATIVE}}
#
# בני את משחק הניחוש המלא לאליפות:
# - מיטב מתוך 3 סיבובים
# - עקבי אחר הניצחונות של {{hero}} ושל {{villain}}
# - {{villain}} מנחש לפי אסטרטגיה פשוטה
# - מי שמנחש בפחות ניסיונות מנצח בסיבוב
#
# 1. חשבי `middle = (min_val + max_val) // 2`
# 2. אם `middle < secret` — הטווח החדש הוא `(middle + 1, max_val)`
# 3. אם `middle > secret` — הטווח החדש הוא `(min_val, middle - 1)`
# 4. החזירי `(middle, new_min, new_max)`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
secret = random.randint(min_val, max_val)
guesses = 0
current_min = min_val
current_max = max_val

print(f"\n{{{{villain}}}}'s turn! (Secret: {secret})")

while True:
    guess, current_min, current_max = computer_guess(
        current_min, current_max, secret
    )
    guesses += 1
    print(f"{{{{villain}}}} guesses: {guess}")

    if guess == secret:
        print(f"{{{{villain}}}} got it in {guesses} guesses!")
        return guesses
    elif guess < secret:
        print("Too low...")
    else:
        print("Too high...")

# %%
print("=" * 50)
print("   GUESSING CHAMPIONSHIP")
print(f"   {{{{hero}}}} vs {{{{villain}}}}")
print("=" * 50)
print()

hero_wins = 0
villain_wins = 0
round_num = 0

# %% [markdown]
# כל עוד אף שחקן לא הגיע ל-2 ניצחונות:
# 1. הגדילי את מספר הסיבוב
# 2. הדפיסי כותרת סיבוב וניקוד נוכחי
# 3. {{hero}} מנחשת (השתמשי ב-`play_guessing_round`)
# 4. {{villain}} מנחש (השתמשי ב-`computer_play_round`)
# 5. השווי את מספרי הניחושים, תני נקודה למנצח/ת
# 6. הכריזי על מנצח/ת הסיבוב
#
# אחרי הלולאה: הכריזי על אלופת האליפות

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## MAIN

# %%
print("=" * 60)
print("{{CONTEXT_SETBACK_INTRO}}")
print("=" * 60)
print()

print(">>> PART 1: Fix the broken game...")
print("(Review buggy_guessing_game() and implement fixed_guessing_game())")
print()
# Uncomment to test:
# fixed_guessing_game()

print()
print(">>> PART 2: Build better validation and hints...")
print("(Implement validate_guess, give_hint, play_guessing_round)")
print()
# Uncomment to test:
# guesses = play_guessing_round(1, 20)
# print(f"You won in {guesses} guesses!")

print()
print(">>> PART 3: The Championship awaits...")
print("(Implement computer_guess and championship_match)")
print()
# Uncomment to test:
# championship_match()

print()
print("=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print("=" * 60)
