# תרגיל 2: מחשבון ציוני O.W.L.! 🦉

## המשימה שלך
צרי פונקציה שמחזירה את ציון ה-O.W.L. (בחינות הוגוורטס) לפי הניקוד!

## מה זה O.W.L.?
Ordinary Wizarding Levels - הבחינות שתלמידי הוגוורטס עושים בשנה החמישית!

## טבלת הציונים (מ-Harry Potter)
- 95 ומעלה = "O" (Outstanding) - מצוין!
- 85-94 = "E" (Exceeds Expectations) - עולה על הציפיות
- 70-84 = "A" (Acceptable) - מקובל
- 55-69 = "P" (Poor) - גרוע
- 40-54 = "D" (Dreadful) - נורא
- מתחת ל-40 = "T" (Troll) - טרול!

## רמז
תצטרכי להשתמש ב-`if`, `elif` ו-`else`

שימי לב לסדר! התחילי מהציון הגבוה ביותר.

## תזכורת - return
הפונקציה צריכה להחזיר (return) את האות, לא להדפיס אותה:
```python
if score >= 95:
    return "O"  # Outstanding!
elif score >= 85:
    return "E"  # Exceeds Expectations!
```

## בונוס
הוסיפי הודעה מיוחדת לכל ציון!
```python
if grade == "O":
    print("Outstanding! Hermione would be proud!")
elif grade == "T":
    print("Troll?! Even Crabbe did better!")
```

## הקוד שלך
פתחי את `exercise_2_grades.py` ומלאי את הפונקציה `get_owl_grade`
