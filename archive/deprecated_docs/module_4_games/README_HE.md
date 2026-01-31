<div dir="rtl">

# מודול 4: משחקים פשוטים

## מה תלמדי
- לולאת המשחק - להמשיך לשחק עד שנגמר
- לולאות `while` לחזרה עד שתנאי מתקיים
- לשלב הכל: לולאות, if/else, רשימות, אקראי
- לבנות משחקים שלמים!

## שיעורים

### שיעור 1: לולאת while
לולאת `while` ממשיכה כל עוד משהו נכון:

```python
lives = 3
while lives > 0:
    print("You have", lives, "lives left")
    lives = lives - 1
print("Game over!")
```

### שיעור 2: תבנית לולאת משחק
רוב המשחקים עוקבים אחרי התבנית הזו:

```python
playing = True
while playing:
    # 1. להראות משהו לשחקן
    # 2. לקבל קלט מהשחקן
    # 3. לבדוק מה קרה
    # 4. אולי לשים playing = False כדי לסיים
```

### שיעור 3: לצאת מלולאה
השתמשי ב-`break` כדי לצאת מלולאה מיד:

```python
while True:
    answer = input("Continue? (y/n): ")
    if answer == "n":
        break
    print("Let's keep going!")
```

### שיעור 4: לספור נקודות
עקבי אחרי נקודות עם משתנה:

```python
score = 0
# השחקן עשה משהו טוב
score = score + 10
print("Score:", score)
```

---

## תרגילים
1. `exercise_1_guess_number.py` - נחשי את המספר (עם רמזים!)
2. `exercise_2_rock_paper_scissors.py` - משחק קלאסי נגד המחשב
3. `exercise_3_dice_game.py` - הטילי קוביות ונסי את המזל
4. `exercise_4_your_game.py` - צרי משחק משלך!

## טיפים
- בדקי את המשחק על ידי שאת משחקת בו בעצמך
- חשבי מה יכול להשתבש (קלט לא טוב, וכו')
- הוסיפי הודעות כיפיות כדי לעשות את זה יותר מרגש!

</div>
