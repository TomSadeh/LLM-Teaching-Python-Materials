# תרגילים 10-12: פונקציות

## תרגיל 10: פונקציות בסיסיות
פונקציה היא קטע קוד עם שם:

```python
def say_hello():
    print("Hello!")

# לקרוא לפונקציה:
say_hello()  # מדפיס Hello!
say_hello()  # מדפיס Hello! שוב
```

**למה פונקציות?**
- לא צריך לכתוב את אותו קוד שוב ושוב
- קוד מסודר ונקי יותר
- קל לתקן באג במקום אחד

## תרגיל 11: פונקציות עם פרמטרים
פרמטרים נותנים מידע לפונקציה:

```python
def greet(name):
    print("Hello, " + name + "!")

greet("Maya")   # Hello, Maya!
greet("Dan")    # Hello, Dan!

def print_times(message, times):
    for i in range(times):
        print(message)

print_times("Wow!", 3)  # מדפיס Wow! שלוש פעמים
```

## תרגיל 12: פונקציות שמחזירות ערך
`return` שולח ערך בחזרה:

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

def double(n):
    return n * 2

x = double(7)
print(x)  # 14
```

**ההבדל בין print ל-return:**
- `print()` מראה על המסך
- `return` שולח ערך שאפשר להשתמש בו

```python
def with_print(n):
    print(n * 2)

def with_return(n):
    return n * 2

with_print(5)           # מדפיס 10, אבל לא מחזיר
x = with_return(5)      # לא מדפיס, אבל x = 10
print(x + 1)            # מדפיס 11
```
