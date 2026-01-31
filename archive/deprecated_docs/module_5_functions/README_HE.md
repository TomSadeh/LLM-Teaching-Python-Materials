<div dir="rtl">

# מודול 5: פונקציות - הפקודות שלך

## מה תלמדי
- למה פונקציות עושות קוד יותר טוב
- פרמטרים: לתת מידע לפונקציות
- ערכי החזרה: לקבל מידע בחזרה
- ערכי ברירת מחדל לפרמטרים
- לבנות קוד שאפשר להשתמש בו שוב ושוב

## שיעורים

### שיעור 1: למה פונקציות?
בלי פונקציות, חוזרים על עצמך:

```python
# לצייר 3 ריבועים - הרבה קוד חוזר!
for i in range(4):
    t.forward(50)
    t.right(90)

t.penup()
t.forward(100)
t.pendown()

for i in range(4):
    t.forward(50)
    t.right(90)

# ... ושוב ושוב!
```

עם פונקציות - כותבים פעם אחת, משתמשים הרבה פעמים!

### שיעור 2: פונקציות עם פרמטרים
פרמטרים נותנים לך לשנות מה הפונקציה עושה:

```python
def draw_square(t, size):
    for i in range(4):
        t.forward(size)
        t.right(90)

# עכשיו אפשר לצייר ריבועים בגדלים שונים!
draw_square(t, 50)   # קטן
draw_square(t, 100)  # גדול
draw_square(t, 200)  # ענק!
```

### שיעור 3: ערכי החזרה
פונקציות יכולות להחזיר תוצאה:

```python
def add_numbers(a, b):
    result = a + b
    return result

total = add_numbers(5, 3)
print(total)  # 8
```

**return** שולח ערך בחזרה. **print** רק מראה על המסך.

### שיעור 4: פרמטרים עם ברירת מחדל
תני לפרמטרים ערך ברירת מחדל:

```python
def greet(name, greeting="Hello"):
    print(greeting + ", " + name + "!")

greet("מאיה")              # Hello, מאיה!
greet("מאיה", "Hi there")  # Hi there, מאיה!
```

### שיעור 5: החזרות מרובות
להחזיר דברים שונים לפי תנאים:

```python
def check_age(age):
    if age >= 18:
        return "adult"
    elif age >= 13:
        return "teenager"
    else:
        return "child"
```

---

## תרגילים
1. `exercise_1_shapes.py` - צרי פונקציות לציור צורות
2. `exercise_2_calculator.py` - בני מחשבון עם פונקציות
3. `exercise_3_helper_functions.py` - פונקציות שימושיות לשימוש חוזר
4. `exercise_4_turtle_art.py` - אומנות צב עם פונקציות מותאמות!

## טיפים
- אם כתבת את אותו קוד פעמיים, עשי ממנו פונקציה!
- תני לפונקציות שמות ברורים שמתארים מה הן עושות
- שמרי על פונקציות קצרות - עבודה אחת לכל פונקציה

</div>
