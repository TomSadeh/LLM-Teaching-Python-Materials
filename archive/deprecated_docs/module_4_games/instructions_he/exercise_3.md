# תרגיל 3: משחק קוביות 🎲

## המשימה שלך
בני תור אחד של משחק קוביות!

## איך המשחק עובד
1. השחקן מטיל קובייה
2. הנקודות מתווספות לסכום התור
3. אבל! אם יוצא 1 - מפסידים את כל הנקודות של התור!
4. השחקן יכול לבחור "hold" כדי לשמור את הנקודות בבטחה

## מה לכתוב
בתוך לולאה:
1. שאלי "Roll or hold? (r/h): "
2. אם "h": צאי מהלולאה והחזירי את הנקודות
3. אם "r":
   - הטילי קובייה עם `roll_dice()`
   - אם יצא 1: הדפיסי הודעה והחזירי 0
   - אחרת: הוסיפי לסכום והדפיסי אותו

## תזכורת
```python
while True:
    choice = input("Roll or hold? (r/h): ")
    if choice == "h":
        break
    # ...
```

## הקוד שלך
פתחי את `exercise_3_dice_game.py` ומלאי את `play_turn`
