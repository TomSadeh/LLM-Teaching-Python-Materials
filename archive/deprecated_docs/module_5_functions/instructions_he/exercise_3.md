# תרגיל 3: פונקציות עזר שימושיות

## המשימה שלך
צרי פונקציות שימושיות שאפשר להשתמש בהן שוב ושוב!

## הפונקציות לכתוב

### is_even(number)
מחזירה `True` אם המספר זוגי, `False` אם אי-זוגי
```python
# רמז: אם number % 2 == 0 המספר זוגי
```

### get_max(a, b)
מחזירה את המספר הגדול יותר

### get_random_item(items)
מחזירה פריט אקראי מרשימה
```python
# רמז: random.choice(items)
```

### count_letter(text, letter)
סופרת כמה פעמים האות מופיעה בטקסט
```python
# רמז: עברי על כל תו בטקסט עם לולאה
count = 0
for char in text:
    if char == letter:
        count = count + 1
```

### reverse_string(text)
מחזירה את הטקסט הפוך
```python
# רמז: text[::-1] הופך מחרוזת!
```

## הקוד שלך
פתחי את `exercise_3_helper_functions.py`
