# תרגילים 7-9: לולאות For

## תרגיל 7: ספירה עם לולאות
`for` חוזר על פעולה כמה פעמים:

```python
for i in range(5):
    print(i)
# מדפיס: 0, 1, 2, 3, 4

for i in range(1, 6):
    print(i)
# מדפיס: 1, 2, 3, 4, 5

for i in range(2, 11, 2):
    print(i)
# מדפיס: 2, 4, 6, 8, 10 (קופץ ב-2)

for i in range(5, 0, -1):
    print(i)
# מדפיס: 5, 4, 3, 2, 1 (סופר אחורה)
```

**range עובד ככה:**
- `range(5)` = 0, 1, 2, 3, 4
- `range(1, 5)` = 1, 2, 3, 4 (לא כולל 5!)
- `range(start, stop, step)` = מ-start עד stop, קופץ ב-step

## תרגיל 8: הדפסת דפוסים
אפשר להדפיס כוכביות עם לולאה:

```python
# 5 כוכביות בשורה
print("*" * 5)  # *****

# משולש
for i in range(1, 6):
    print("*" * i)
# *
# **
# ***
# ****
# *****
```

**טיפ:** `print(..., end=" ")` מדפיס בלי לרדת שורה

## תרגיל 9: צבירת ערכים
לספור או לחבר בלולאה:

```python
total = 0
for i in range(1, 6):
    total = total + i
print(total)  # 15 (סכום 1+2+3+4+5)

# לספור
count = 0
for i in range(1, 101):
    if i % 7 == 0:
        count = count + 1
print(count)  # כמה מספרים מתחלקים ב-7
```
