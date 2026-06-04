# =============================================================================
# Match the Output: Code to Shape
# =============================================================================
# Difficulty: 3-4
# Concepts: loop count to sides, turn angles to shape type
# =============================================================================

# %% [markdown]
# {{CONTEXT_MATCH_OUTPUT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}

# %%
import turtle

# %% [markdown]
# ## {{MATCH_SET_1_TITLE}}
# {{CONTEXT_MATCH_SET_1_NARRATIVE}}
#
# התאימי כל קטע קוד לצורה שהוא מצייר.
#
# ## קטעי הקוד

# %%
t = turtle.Turtle()
t.speed(0)
for i in range(3):
    t.forward(80)
    t.right(120)

# %%
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(150, 0)
t.pendown()
for i in range(4):
    t.forward(60)
    t.right(90)

# %%
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-150, 0)
t.pendown()
for i in range(6):
    t.forward(40)
    t.right(60)

# %% [markdown]
# ## פלטים אפשריים
#
# פלט A: משולש (Triangle)
# ---------
# צורה סגורה בת 3 צלעות שוות.
# הצב מסתובב 120 מעלות בכל פינה.
#
# פלט B: ריבוע (Square)
# ---------
# צורה סגורה בת 4 צלעות שוות.
# הצב מסתובב 90 מעלות בכל פינה.
#
# פלט C: משושה (Hexagon)
# ---------
# צורה סגורה בת 6 צלעות שוות.
# הצב מסתובב 60 מעלות בכל פינה.
#
# ## התשובות שלך
#
# כתבי את האות (A, B או C) שמתאימה לכל קטע קוד.
#
# > רמז: הסתכלי על `range(N)` כדי למצוא את מספר הצלעות.
# > זווית הסיבוב קובעת את סוג הצורה:
# > - Triangle: 120 מעלות (360 / 3)
# > - Square: 90 מעלות (360 / 4)
# > - Hexagon: 60 מעלות (360 / 6)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
matches = {
    "snippet_1": "?",
    "snippet_2": "?",
    "snippet_3": "?",
}

return matches

# %% [markdown]
# ## {{MATCH_SET_2_TITLE}}
# {{CONTEXT_MATCH_SET_2_NARRATIVE}}
#
# קטעי הקוד האלה נראים דומים אבל מייצרים תוצאות שונות!
# {{hero}} צריכה לזהות כל תבנית.
#
# ## קטעי הקוד

# %%
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200, -100)
t.pendown()
for i in range(5):
    t.forward(80)
    t.right(72)

# %%
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(0, -100)
t.pendown()
for i in range(5):
    t.forward(80)
    t.right(144)

# %%
t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(200, -100)
t.pendown()
for i in range(5):
    t.forward(80)
    t.left(72)

# %% [markdown]
# ## פלטים אפשריים
#
# פלט D: מחומש (Pentagon)
# ---------
# צורה סגורה וסדירה בת 5 צלעות.
# זווית סיבוב: 72 מעלות (360/5).
# מסתובבת ימינה (`right`) בכל פינה.
#
# פלט E: כוכב בן 5 קצוות (5-Pointed Star)
# ---------
# צורה של כוכב עם 5 קצוות.
# זווית סיבוב: 144 מעלות (גדולה יותר מאשר פולייגון).
# הקווים חוצים זה את זה דרך המרכז.
#
# פלט F: מחומש נגד כיוון השעון (Pentagon counterclockwise)
# ---------
# צורה סגורה וסדירה בת 5 צלעות.
# זווית סיבוב: 72 מעלות.
# מסתובבת שמאלה (`left`) בכל פינה — מצייר בכיוון הפוך.
#
# ## התשובות שלך
#
# > רמז: השווי את זוויות הסיבוב והכיוונים!
# > - 72 מעלות = 360/5, יוצרת מחומש סדיר
# > - 144 מעלות = 2 * 72, יוצרת תבנית כוכב
# > - `left` לעומת `right` קובע לאיזה כיוון הצורה מצוירת

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
matches = {
    "snippet_4": "?",
    "snippet_5": "?",
    "snippet_6": "?",
}

return matches

# %%
print("{{CONTEXT_MATCH_OUTPUT_INTRO}}")
print("=" * 50)

print("\n=== {{MATCH_SET_1_TITLE}} ===")
print("\nRunning all snippets...")
snippet_1()
snippet_2()
snippet_3()
print("\nYour matches:", your_matches_set1())

print("\n=== {{MATCH_SET_2_TITLE}} ===")
snippet_4()
snippet_5()
snippet_6()
print("\nYour matches:", your_matches_set2())

print("\n" + "=" * 50)
print("{{CONTEXT_VERIFICATION_COMPLETE}}")
turtle.done()
