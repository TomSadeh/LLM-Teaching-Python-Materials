<div dir="rtl">

# מודול 2: קבלת החלטות (if/else)

## מה תלמדי
- לגרום לתוכנית לבחור מה לעשות
- להשוות ערכים (שווה, גדול, קטן)
- להשתמש ב-`if`, `elif` ו-`else`
- ליצור תוכניות אינטראקטיביות

## שיעורים

### שיעור 1: משפט if
תוכניות יכולות לקבל החלטות! כמו כובע המיון שבוחר את הבית!

```python
house = "Gryffindor"
if house == "Gryffindor":
    print("Where dwell the brave at heart!")
```

### שיעור 2: אופרטורי השוואה
השתמשי באלה כדי להשוות ערכים:
- `==` שווה (שני סימני שווה!)
- `!=` לא שווה
- `>` גדול מ
- `<` קטן מ
- `>=` גדול או שווה
- `<=` קטן או שווה

```python
district = 12
if district == 12:
    print("You're from the coal mining district, like Katniss!")
```

### שיעור 3: if/else
מה אם התנאי לא נכון? השתמשי ב-`else`:

```python
# הגברת השמנה בודקת את הסיסמה!
password = input("Password? ")
if password == "Caput Draconis":
    print("The portrait swings open. Welcome to Gryffindor!")
else:
    print("The Fat Lady shakes her head.")
```

### שיעור 4: elif (else if)
להרבה אפשרויות, השתמשי ב-`elif`:

```python
# ציוני O.W.L. מהוגוורטס!
score = 85
if score >= 95:
    print("O - Outstanding!")
elif score >= 85:
    print("E - Exceeds Expectations!")
elif score >= 70:
    print("A - Acceptable")
else:
    print("T - Troll!")
```

---

## תרגילים
1. `exercise_1_password.py` - הכניסה למגדל גריפינדור 🦁
2. `exercise_2_grades.py` - מחשבון ציוני O.W.L. 🦉
3. `exercise_3_number_game.py` - נחשי את המספר
4. `exercise_4_quiz.py` - חידון ספרים! 📚

## דמויות לדוגמה
- **הארי פוטר:** בדקי אם המשתמש בבית הנכון
- **פרסי ג'קסון:** בדקי מי האל ההורה
- **משחקי הרעב:** בדקי מאיזה מחוז הדמות
- **שומרת הערים האבודות:** בדקי איזו כישרון יש לאלף

## טיפים
- זכרי: `=` מכניס ערך, `==` משווה ערכים
- הזחה חשובה! קוד בתוך `if` חייב להיות מוזח
- אפשר לשלב תנאים עם `and` / `or`

</div>
