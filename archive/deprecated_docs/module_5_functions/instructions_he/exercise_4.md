# תרגיל 4: אומנות צב עם פונקציות מותאמות! 🎨

## המשימה שלך
צרי יצירת אומנות באמצעות פונקציות שאת בונה!

## פונקציות לכתוב

### draw_square(t, size, color="black")
ריבוע מלא בצבע
```python
t.fillcolor(color)
t.begin_fill()
# draw square...
t.end_fill()
```

### draw_flower(t, petal_size, num_petals)
פרח עם עלי כותרת!
```python
# לכל עלה: צייר עיגול וסובב
for i in range(num_petals):
    t.circle(petal_size)
    t.right(360 / num_petals)
```

### draw_row_of_shapes(t, shape_func, count, spacing)
שורה של צורות עם רווח ביניהן

## create_art - היצירתיות שלך!
השתמשי בפונקציות שבנית ליצור משהו מגניב!

רעיונות:
- גן פרחים
- דפוס ריבועים בצבעים
- שורת צורות שגדלות
- סצנה שלמה!

## הקוד שלך
פתחי את `exercise_4_turtle_art.py`
