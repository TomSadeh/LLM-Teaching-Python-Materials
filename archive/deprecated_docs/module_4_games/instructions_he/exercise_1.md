# תרגיל 1: נחשי את המספר 🎯

## המשימה שלך
בני משחק ניחוש מספרים!

## איך המשחק עובד
1. המחשב בוחר מספר סודי בין 1 ל-20
2. לשחקן יש 5 ניסיונות לנחש
3. אחרי כל ניחוש, אמרי "גבוה מדי!" או "נמוך מדי!"
4. אם ניחש נכון - הוא ניצח!
5. אם נגמרו הניסיונות - הפסיד

## מה לכתוב
השתמשי ב-`while True:` ו-`break`:
```python
while True:
    guess = int(input("Your guess: "))
    attempts = attempts + 1

    if guess == secret:
        print("You won!")
        break

    # check if too high or too low...

    if attempts == 5:
        print("Game over!")
        break
```

## הקוד שלך
פתחי את `exercise_1_guess_number.py` ומלאי את `play_game`
