# Exercise 1: Bug Hunt - Wrong Comparisons
#
# {{villain}} has sabotaged the decision-making spells!
# Each function has exactly ONE bug in its logic.
# Read the story, find the bug, and fix it.
#
# DO NOT run the code first - use your detective skills!


# ============================================================
# BUG HUNT A: The Backwards Grader
# ============================================================
"""
STORY:
The {{school}} grading system is broken! Students who score
90 or above should get "Excellent", but instead they're
getting "Needs Improvement"!

EXPECTED BEHAVIOR:
- Score 90 or above → "Excellent"
- Score below 90 → "Needs Improvement"

ACTUAL BEHAVIOR:
The grades are completely backwards.
"""

def buggy_grader(score):
    if score < 90:  # BUG IS HERE
        return "Excellent"
    else:
        return "Needs Improvement"


def fix_grader(score):
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: What comparison should we use?
    #
    # The fix:
    pass


# ============================================================
# BUG HUNT B: The Exclusive Club
# ============================================================
"""
STORY:
{{hero}} set up a spell that should grant access if someone
has EITHER the password OR the secret key. But it only works
if they have BOTH!

EXPECTED BEHAVIOR:
- Has password → Access granted
- Has secret key → Access granted
- Has neither → Access denied

ACTUAL BEHAVIOR:
Only grants access if you have BOTH password AND key.
"""

def buggy_access(has_password, has_key):
    if has_password and has_key:  # BUG IS HERE
        return "Access granted"
    else:
        return "Access denied"


def fix_access(has_password, has_key):
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: "and" vs "or" - which means "at least one"?
    #
    # The fix:
    pass


# ============================================================
# BUG HUNT C: The Wrong Age Check
# ============================================================
"""
STORY:
{{school}} needs students between ages 11 and 17 (inclusive).
But the spell is rejecting some valid students!

EXPECTED BEHAVIOR:
- Age 11-17 → "Welcome to {{school}}"
- Age below 11 or above 17 → "Not eligible"

ACTUAL BEHAVIOR:
Students exactly 11 or exactly 17 years old are rejected.
"""

def buggy_age_check(age):
    if age > 11 and age < 17:  # BUG IS HERE
        return "Welcome to {{school}}"
    else:
        return "Not eligible"


def fix_age_check(age):
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: > vs >= makes a difference at the boundaries!
    #
    # The fix:
    pass


# ============================================================
# BUG HUNT D: The Inverted Guard
# ============================================================
"""
STORY:
{{mentor}} wrote a safety spell that should block {{villain}}
and allow everyone else. But it's doing the opposite!

EXPECTED BEHAVIOR:
- Name is "{{villain}}" → "Entry blocked!"
- Any other name → "Welcome!"

ACTUAL BEHAVIOR:
{{villain}} is welcomed, everyone else is blocked!
"""

def buggy_guard(name):
    if name != "{{villain}}":  # Looks right, but...
        return "Entry blocked!"  # BUG: wrong return on wrong branch
    else:
        return "Welcome!"


def fix_guard(name):
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: The condition might be right, but are the
    #       return statements on the right branches?
    #
    # The fix:
    pass


# ============================================================
# BUG HUNT E: The Missing Elif
# ============================================================
"""
STORY:
{{friend}} wrote a temperature advisor but forgot something.
It should give different advice for hot, warm, and cold,
but warm days are being called cold!

EXPECTED BEHAVIOR:
- Above 30°C → "It's hot! Stay cool."
- Between 15-30°C → "Nice weather!"
- Below 15°C → "It's cold! Wear a jacket."

ACTUAL BEHAVIOR:
20°C is showing "It's cold!" instead of "Nice weather!"
"""

def buggy_temperature(temp):
    if temp > 30:
        return "It's hot! Stay cool."
    if temp < 15:  # BUG: Should this be elif?
        return "It's cold! Wear a jacket."
    else:
        return "Nice weather!"


def fix_temperature(temp):
    # ✏️ FIX THE BUG ✏️
    #
    # What I found: ________________________________
    # Hint: Trace through with temp = 20. What happens?
    #
    # The fix:
    pass


def main():
    print("=== Bug Hunt: Wrong Comparisons ===")
    print()
    print("Each function has exactly ONE logic bug.")
    print("Find the bug, then write the fix.")
    print()
    print("="*50)

    # Test the buggy versions to see the problems:
    print("\nBuggy Grader (score=95):", buggy_grader(95))
    print("  Expected: Excellent")

    print("\nBuggy Access (password=True, key=False):",
          buggy_access(True, False))
    print("  Expected: Access granted")

    print("\nBuggy Age Check (age=11):", buggy_age_check(11))
    print("  Expected: Welcome to {{school}}")

    print("\nBuggy Guard (name='{{villain}}'):",
          buggy_guard("{{villain}}"))
    print("  Expected: Entry blocked!")

    print("\nBuggy Temperature (temp=20):", buggy_temperature(20))
    print("  Expected: Nice weather!")

    print("\n" + "="*50)
    print("Now fix each function and test your fixes!")


main()
