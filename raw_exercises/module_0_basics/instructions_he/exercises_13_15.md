# תרגילים 13-15: אתגרים!

## תרגיל 13: FizzBuzz
אתגר תכנות מפורסם!

**הכללים:**
- עברי על מספרים 1 עד 30
- אם המספר מתחלק ב-3: הדפיסי "Fizz"
- אם המספר מתחלק ב-5: הדפיסי "Buzz"
- אם מתחלק בשניהם: הדפיסי "FizzBuzz"
- אחרת: הדפיסי את המספר

**רמז:** בדקי את התנאי "מתחלק בשניהם" קודם!

```python
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
# ...
```

## תרגיל 14: לוח הכפל
לולאות מקוננות (לולאה בתוך לולאה):

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()  # שורה חדשה

# 1  2  3
# 2  4  6
# 3  6  9
```

**טיפ:** `end="\t"` מדפיס טאב במקום שורה חדשה

## תרגיל 15: מיני פרויקט
שלבי הכל יחד!

**מנתח מספרים:**
1. בקשי מספר מהמשתמש
2. בדקי אם זוגי/אי-זוגי
3. מצאי את המחלקים שלו
4. חשבי סכום ספרות
5. בדקי אם ראשוני

**רמזים:**
```python
# זוגי?
if n % 2 == 0:  # זוגי

# מחלקים
for i in range(1, n + 1):
    if n % i == 0:
        print(i, "is a factor")

# סכום ספרות
text = str(n)  # המרה למחרוזת
for char in text:
    digit = int(char)
    # ...

# ראשוני = מתחלק רק ב-1 ובעצמו
```

בהצלחה! 🎯
