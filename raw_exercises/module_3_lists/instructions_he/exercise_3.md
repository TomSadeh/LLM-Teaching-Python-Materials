# תרגיל 3: כובע המיון! 🎩

## המשימה שלך
צרי את כובע המיון של הוגוורטס שמחלק תלמידים לבתים!

## מה לעשות
1. צרי רשימה עם 4 הבתים: Gryffindor, Hufflepuff, Ravenclaw, Slytherin
2. השתמשי ב-`random.choice()` לבחור בית
3. החזירי את הבית שנבחר

## על הבתים
- **גריפינדור** 🦁 - אמיצים ונועזים (הארי, הרמיוני, רון)
- **האפלפאף** 🦡 - נאמנים וישרים (סדריק דיגורי)
- **רייבנקלו** 🦅 - חכמים ויצירתיים (לונה לאבגוד)
- **סלית'רין** 🐍 - שאפתניים וערמומיים (דראקו מאלפוי)

## תזכורת
```python
import random
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
chosen = random.choice(houses)
```

## בונוס
הוסיפי הודעה מיוחדת לכל בית!
```python
if house == "Gryffindor":
    print("Where dwell the brave at heart!")
```

## הקוד שלך
פתחי את `exercise_3_magic_8ball.py` (שונה לכובע המיון!) ומלאי את `get_house`
