# תרגיל 2: מחשבון עם פונקציות

## המשימה שלך
בני מחשבון שכל פעולה היא פונקציה!

## הפונקציות לכתוב
- `add(a, b)` - מחזירה a + b
- `subtract(a, b)` - מחזירה a - b
- `multiply(a, b)` - מחזירה a * b
- `divide(a, b)` - מחזירה a / b

## הפונקציה calculate
```python
def calculate(num1, num2, operation):
    if operation == "+":
        return add(num1, num2)
    # continue for other operations...
```

## בונוס
מה קורה כשמחלקים ב-0? תוסיפי בדיקה!
```python
if b == 0:
    return "Error: cannot divide by zero"
```

## הקוד שלך
פתחי את `exercise_2_calculator.py`
