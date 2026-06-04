# =============================================================================
# Hybrid Exercise: The Upgrade - From Repetition to Reuse
# =============================================================================
# Difficulty: 3-4
# Arc: Upgrade (EVALUATION -> IMPROVEMENT)
# Concepts: Code reuse, refactoring to functions, DRY principle
# =============================================================================

# %% [markdown]
# {{CONTEXT_EVALUATION_INTRO}}
#
# זוהי תרגילה בכמה חלקים. השלימי כל חלק לפי הסדר.
#
# ירשת קוד עם הרבה חזרות. הגיע הזמן לשדרג אותו באמצעות
# פונקציות כדי שיהיה נקי ויותר קל לתחזוקה.
#
# ## חלק 1: הערכה - השוואה בין גישות
# {{CONTEXT_EVALUATION_INTRO}}
# {{CONTEXT_EVALUATION_NARRATIVE}}
#
# השוואי בין שתי הדרכים הבאות לכתוב את אותה תוכנית.

# %%
# Greeting for hero
print("=" * 30)
print("{{hero}}")
print("=" * 30)
print("Status: Active")
print()

# Greeting for heroine
print("=" * 30)
print("{{heroine}}")
print("=" * 30)
print("Status: Active")
print()

# Greeting for mentor
print("=" * 30)
print("{{mentor}}")
print("=" * 30)
print("Status: Advisor")
print()

# %%
def show_profile(name, status="Active"):
    print("=" * 30)
    print(name)
    print("=" * 30)
    print(f"Status: {status}")
    print()

show_profile("{{hero}}")
show_profile("{{heroine}}")
show_profile("{{mentor}}", "Advisor")

# %%
# YOUR ANALYSIS
#
# Compare the two versions above.

analysis = """
Which version is better and why?

Version 1 (Repetitive):
- Lines of code: ~18
- To change the format, must edit: 3 places
- To add a new person: Copy-paste 6 lines

Version 2 (Functions):
- Lines of code: ~10
- To change the format, must edit: 1 place
- To add a new person: Add 1 line

The function version follows the DRY principle:
"Don't Repeat Yourself"

My verdict: _______________
"""
return analysis

# %% [markdown]
# ## חלק 2: שיפור - ארגון מחדש לפונקציות
# {{CONTEXT_IMPROVEMENT_INTRO}}
# {{CONTEXT_IMPROVEMENT_NARRATIVE}}
#
# ארגני מחדש את הקוד החוזר שלמטה כך שישתמש בפונקציות.

# %%
# Report header
print("*" * 40)
print("{{school}} REPORT")
print("*" * 40)

# Section 1
print("-" * 40)
print("TEAM ROSTER")
print("-" * 40)
print("  1. {{hero}}")
print("  2. {{heroine}}")
print("  3. {{friend}}")

# Section 2
print("-" * 40)
print("ACHIEVEMENTS")
print("-" * 40)
print("  1. First mission complete")
print("  2. Training passed")

# Section 3
print("-" * 40)
print("UPCOMING")
print("-" * 40)
print("  1. Advanced training")

# Report footer
print("*" * 40)
print("END OF REPORT")
print("*" * 40)

# %%
# REFACTOR TO USE FUNCTIONS
#
# Create helper functions to reduce repetition:
#
# 1. Create print_border(char, width=40) that prints a line of characters
# 2. Create print_header(title, char="*") that prints:
#    - border line
#    - title
#    - border line
# 3. Create print_section(title, items) that prints:
#    - dashed border
#    - title
#    - dashed border
#    - numbered items
# 4. Use these functions to build the same report

def print_border(char, width=40):
    # YOUR CODE HERE
    pass

def print_header(title, char="*"):
    # YOUR CODE HERE
    pass

def print_section(title, items):
    # YOUR CODE HERE
    # Use a for loop to print numbered items
    pass

# Build the report using your functions
# YOUR CODE HERE
#
# Call:
# - print_header("{{school}} REPORT")
# - print_section("TEAM ROSTER", ["{{hero}}", "{{heroine}}", "{{friend}}"])
# - print_section("ACHIEVEMENTS", ["First mission complete", "Training passed"])
# - print_section("UPCOMING", ["Advanced training"])
# - print_header("END OF REPORT")

pass

# %% [markdown]
# ## בונוס: יצירת פונקציות לשימוש חוזר

# %%
# CREATE A SET OF REUSABLE UTILITY FUNCTIONS
#
# These functions should be useful in many programs.

def repeat_char(char, times):
    """Return a string of char repeated times times."""
    # YOUR CODE HERE
    pass

def format_title(text, width=40, border_char="="):
    """
    Return a formatted title with borders.

    Example:
        format_title("News") returns:
        "========================================
         News
         ========================================"
    """
    # YOUR CODE HERE
    pass

def format_list(items, numbered=True):
    """
    Return a formatted list as a string.

    If numbered=True:
        "1. item1
         2. item2"
    If numbered=False:
        "- item1
         - item2"
    """
    # YOUR CODE HERE
    pass

# Test your utilities
print("Testing utilities:")
print(repeat_char("-", 20))
print()
print(format_title("{{school}}", 30))
print()
print(format_list(["{{hero}}", "{{heroine}}", "{{friend}}"]))
print()
print(format_list(["Item A", "Item B"], numbered=False))

# %%
print("=" * 60)
print("THE UPGRADE: From Repetition to Reuse")
print("=" * 60)

print("\n--- PART 1: EVALUATION ---")
print("{{CONTEXT_EVALUATION_INTRO}}")

print("\nVersion 1 (Repetitive):")
version_repetitive()

print("\nVersion 2 (With Functions):")
version_with_functions()

print(f"\nYour analysis:{part_1_analysis()}")

print("\n--- PART 2: IMPROVEMENT ---")
print("{{CONTEXT_IMPROVEMENT_INTRO}}")

print("\nOriginal repetitive report:")
repetitive_report()

print("\nYour improved report:")
improved_report()

print("\n--- BONUS: Utility Functions ---")
bonus_create_utilities()

print("\n" + "=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print("\nKey Lessons:")
print("1. Functions eliminate repetition (DRY principle)")
print("2. Changes only need to happen in one place")
print("3. Code becomes easier to read and maintain")
print("4. Reusable functions save time in future projects")
