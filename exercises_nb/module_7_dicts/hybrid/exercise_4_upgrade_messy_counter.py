# %% [markdown]
# {{CONTEXT_EVALUATION_INTRO}}
#
# זו תרגיל מרובה חלקים שבו תשדרגי קוד ספירה מבולגן
# לשימוש בתבניות מילון אלגנטיות.
#
# מושגי תכנות: תבנית ספירה, `.get()`, איטרציה על מילון
#
# חלק 1: הערכה - בחני את הקוד המבולגן
# {{CONTEXT_EVALUATION_NARRATIVE}}
#
# קוד הספירה הזה עובד, אבל הוא מבולגן. נתחי מה הבעיה.

# %%
counts = []  # List of [item, count] pairs

for item in items:
    # Search for existing item in counts
    found = False
    index = 0
    while index < len(counts):
        if counts[index][0] == item:
            counts[index][1] = counts[index][1] + 1
            found = True
            break
        index = index + 1

    # If not found, add new entry
    if found == False:
        counts.append([item, 1])

return counts

# %% [markdown]
# זהי את הבעיות בקוד המבולגן:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
analysis = """
PROBLEMS WITH MESSY COUNTER:

1. Data structure choice:
   - Uses ___ instead of ___
   - Why is this problematic?

2. Search efficiency:
   - How does it find existing items?
   - What if there are 1000 different items?

3. Code complexity:
   - How many lines for the counting logic?
   - Is it easy to understand at a glance?

4. Specific issues:
   - Line "if found == False" should be:
   - The while loop could be replaced with:
"""
return analysis

# %% [markdown]
# חלק 2: גילוי - עקבי אחרי הקוד המבולגן
# {{CONTEXT_DISCOVERY_INTRO}}
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# עקבי אחרי הקוד המבולגן כדי להבין בדיוק מה הוא עושה.

# %%
items = ["a", "b", "a"]
counts = []

for item in items:
    found = False
    index = 0
    while index < len(counts):
        if counts[index][0] == item:
            counts[index][1] = counts[index][1] + 1
            found = True
            break
        index = index + 1
    if found == False:
        counts.append([item, 1])

print(counts)

# %% [markdown]
# מלאי את טבלת המעקב:
#
# items = ["a", "b", "a"]
#
# | סיבוב | item | counts לפני        | found | counts אחרי        |
# |-------|------|--------------------|-------|--------------------|
# | 1     | "a"  | []                 |       |                    |
# | 2     | "b"  |                    |       |                    |
# | 3     | "a"  |                    |       |                    |
#
# תוצאה סופית:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# חלק 3: שיפור - פשטי עם מילון
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# כתבי מחדש את הספירה תוך שימוש במילון.
#
# 1. צרי מילון ריק: `counts = {}`
# 2. עבור כל פריט ב-`items`: `counts[item] = counts.get(item, 0) + 1`
# 3. החזירי את `counts`
#
# זה אמור להיות בערך 4 שורות קוד!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. השתמשי ב-`simple_counter` כדי לקבל את מילון הספירות
# 2. הדפיסי כל פריט וספירה תוך שימוש ב-`.items()`
# 3. מצאי והדפיסי את הפריט הנפוץ ביותר
# > רמז: עקבי אחרי `max_count` ו-`max_item` בזמן האיטרציה
# 4. הדפיסי את הסך הכולל (סכום כל הספירות)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. ספרי את כל הפריטים
# 2. סנני את אלו שמעל הסף
# 3. החזירי את רשימת הפריטים (לא הספירות)

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## חלק 4: השוואה - לפני ואחרי
#
# השווי בין שתי הגישות:

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
comparison_text = """
BEFORE (messy_counter):
- Lines of code: ~15
- Data structure: list of lists
- Lookup method: linear search with while loop
- Easy to read: No

AFTER (simple_counter):
- Lines of code: ~4
- Data structure: dictionary
- Lookup method: direct key access
- Easy to read: Yes

KEY INSIGHT:
The dictionary .get(key, default) pattern is perfect for counting
because it handles both "first occurrence" and "subsequent occurrence"
in a single line of code.

WHAT I LEARNED:
-
"""
return comparison_text

# %% [markdown]
# ## הרצה ראשית

# %%
print("=" * 60)
print("{{CONTEXT_EVALUATION_INTRO}}")
print("=" * 60)
print()

test_items = [
    "{{item}}", "{{spell1}}", "{{item}}",
    "{{spell2}}", "{{item}}", "{{spell1}}"
]

print(">>> PART 1: Analyze the messy code...")
print()
print(f"Messy counter result: {messy_counter(test_items)}")
print()
print("Your analysis:")
print(analysis_part_1())

print()
print(">>> PART 2: Trace the messy code...")
print("(Complete trace_messy_counter())")
# Uncomment to verify:
# code_to_trace()

print()
print(">>> PART 3: Implement the simple version...")
print("(Implement simple_counter, count_and_report, count_above_threshold)")
print()
# Uncomment after implementing:
# print(f"Simple counter: {simple_counter(test_items)}")
# print()
# count_and_report(test_items)
# print()
# print(f"Items appearing 2+ times: {count_above_threshold(test_items, 1)}")

print()
print(">>> PART 4: Compare approaches...")
print()
print(comparison())

print()
print("=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print("=" * 60)
