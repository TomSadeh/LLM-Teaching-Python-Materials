# =============================================================================
# Output Prediction: Turtle Position
# =============================================================================
# Difficulty: 1
# Concepts: turtle movement, direction, forward(), backward(), right(), left()
# =============================================================================

# %% [markdown]
# {{CONTEXT_PREDICTION_INTRO}}
# {{CONTEXT_PREDICTION_PURPOSE}}

# %%
import turtle

# %% [markdown]
# ## {{CHALLENGE_1_TITLE}}
# {{CONTEXT_CHALLENGE_1_NARRATIVE}}

# %% locked
# {{hero}} commands the {{creature}} to move forward
t = turtle.Turtle()
t.forward(100)
t.forward(50)
print(f"Final X position: {t.xcor()}")

# %% [markdown]
# הצב מתחילה במיקום (0, 0) ופונה ימינה (מזרח).
# אחרי `forward(100)`, היא נמצאת ב־(100, 0).
# אחרי עוד `forward(50)`, איפה היא תהיה?
#
# Final X position: _______________
#
# > רמז: `forward()` מוסיפה למיקום בכיוון שהצב פונה אליו. הצב פונה ימינה, אז קדימה פירושו ימינה (X גדל).
#
# {{CONTEXT_PREDICTION_GUIDANCE_1}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_2_TITLE}}
# {{CONTEXT_CHALLENGE_2_NARRATIVE}}

# %% locked
# Navigating through {{location}}
t = turtle.Turtle()
t.forward(80)
t.backward(30)
print(f"Final X position: {t.xcor()}")

# %% [markdown]
# מתחילים ב־(0, 0), פונים ימינה:
# - `forward(80)` מגיעה ל־X = ?
# - `backward(30)` זוזה אחורה, אז X = ?
#
# Final X position: _______________
#
# > רמז: `backward()` זזה בכיוון ההפוך מהכיוון שהצב פונה אליו, אבל הצב ממשיכה לפנות לאותו הכיוון.
#
# {{CONTEXT_PREDICTION_GUIDANCE_2}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_3_TITLE}}
# {{CONTEXT_CHALLENGE_3_NARRATIVE}}

# %% locked
# Charting a path to {{place}}
t = turtle.Turtle()
t.right(90)
t.forward(60)
print(f"Final Y position: {t.ycor()}")

# %% [markdown]
# הצב מתחילה ופונה ימינה (מזרח).
# `right(90)` מסובבת אותה 90 מעלות בכיוון השעון — לאן היא פונה עכשיו?
# אחר כך `forward(60)` מזיזה אותה 60 יחידות בכיוון הזה.
#
# Final Y position: _______________
#
# > רמז: פנייה ימינה ממזרח מכוונת אותך דרומה. בגרפיקת הצב, דרום אומר ש־Y קטן (כיוון Y שלילי).
#
# {{CONTEXT_PREDICTION_GUIDANCE_3}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{CHALLENGE_4_TITLE}}
# {{CONTEXT_CHALLENGE_4_NARRATIVE}}

# %% locked
# A journey around {{school}}
t = turtle.Turtle()
t.forward(50)
t.left(90)
t.forward(50)
print(f"Position: ({t.xcor()}, {t.ycor()})")

# %% [markdown]
# מתחילים ב־(0, 0), פונים ימינה (מזרח):
# - `forward(50)` מגיעה למיקום (?, ?)
# - `left(90)` מסובבת 90 מעלות נגד כיוון השעון — עכשיו פונים לאן?
# - `forward(50)` מגיעה למיקום (?, ?)
#
# Position: (_____, _____)
#
# > רמז: פנייה שמאלה ממזרח מכוונת אותך צפונה. צפון אומר ש־Y גדל (כיוון Y חיובי).
#
# {{CONTEXT_PREDICTION_GUIDANCE_4}}

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("=== {{CHALLENGE_1_TITLE}} ===")
print("-- Actual Output --")
challenge_a_code()
print("\n-- Your Prediction --")
challenge_a_prediction()

print("\n=== {{CHALLENGE_2_TITLE}} ===")
print("-- Actual Output --")
challenge_b_code()
print("\n-- Your Prediction --")
challenge_b_prediction()

print("\n=== {{CHALLENGE_3_TITLE}} ===")
print("-- Actual Output --")
challenge_c_code()
print("\n-- Your Prediction --")
challenge_c_prediction()

print("\n=== {{CHALLENGE_4_TITLE}} ===")
print("-- Actual Output --")
challenge_d_code()
print("\n-- Your Prediction --")
challenge_d_prediction()

print("\n" + "=" * 50)
print("{{CONTEXT_VERIFICATION_COMPLETE}}")
turtle.done()
