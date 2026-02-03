# =============================================================================
# Which is Better: Return vs Print
# =============================================================================
# Difficulty: 3
# Concepts: When to use return, when to use print, function design
# =============================================================================

"""
{{CONTEXT_COMPARISON_INTRO}}
{{CONTEXT_COMPARISON_DECISION}}
"""


# ============================================================
# Scenario 1: A Calculation Function
# ============================================================
# You need a function that calculates a score.
# You want to use the result in other calculations.

def calculate_score_v1(base, bonus):
    """Version 1: Prints the result"""
    result = base + bonus
    print(f"Score: {result}")


def calculate_score_v2(base, bonus):
    """Version 2: Returns the result"""
    result = base + bonus
    return result


def analysis_scenario_1():
    # YOUR ANALYSIS
    #
    # Consider: Which version lets you use the score in more calculations?

    analysis = """
    Better version: Version 2 (return)

    Reasons:
    1. Returns the value so it can be stored and reused
    2. Can be used in further calculations
    3. More flexible - caller decides whether to print

    When to use Version 1 (print):
    - When you ONLY need to display the value once
    - In debugging, to see intermediate values

    When to use Version 2 (return):
    - When you need to use the value in calculations
    - When building reusable functions
    - Almost always the better choice for functions
    """
    return analysis


# ============================================================
# Scenario 2: A Greeting Function
# ============================================================
# You need a function that shows a greeting to the user.

def greet_user_v1(name):
    """Version 1: Prints directly"""
    print(f"Hello, {name}!")
    print(f"Welcome to {{school}}!")


def greet_user_v2(name):
    """Version 2: Returns the greeting"""
    return f"Hello, {name}!\nWelcome to {{school}}!"


def analysis_scenario_2():
    # YOUR ANALYSIS
    #
    # Consider: What if you want to modify the greeting before showing it?

    analysis = """
    Better version: ??? (it depends!)

    Reasons:
    1.
    2.

    When to use Version 1 (print):
    -

    When to use Version 2 (return):
    -
    """
    return analysis


# ============================================================
# Scenario 3: A Status Check Function
# ============================================================
# You need to check if a user is qualified.

def check_status_v1(level):
    """Version 1: Prints status message"""
    if level >= 10:
        print("Qualified!")
    else:
        print("Not yet qualified")


def check_status_v2(level):
    """Version 2: Returns boolean"""
    return level >= 10


def analysis_scenario_3():
    # YOUR ANALYSIS
    #
    # Consider: What if you need to make a decision based on the status?

    analysis = """
    Better version: ???

    Reasons:
    1.
    2.

    When to use Version 1:
    -

    When to use Version 2:
    -
    """
    return analysis


# ============================================================
# Scenario 4: A Report Generator
# ============================================================
# You need to create a formatted report.

def create_report_v1(title, content):
    """Version 1: Prints the report"""
    print("=" * 40)
    print(title)
    print("=" * 40)
    print(content)
    print("=" * 40)


def create_report_v2(title, content):
    """Version 2: Returns the report as a string"""
    lines = [
        "=" * 40,
        title,
        "=" * 40,
        content,
        "=" * 40
    ]
    return "\n".join(lines)


def analysis_scenario_4():
    # YOUR ANALYSIS
    #
    # Consider: What if you want to save the report to a file?

    analysis = """
    Better version: ???

    Reasons:
    1.
    2.

    When to use Version 1:
    -

    When to use Version 2:
    -
    """
    return analysis


# ============================================================
# Scenario 5: Combined Approach
# ============================================================
# Sometimes you want both: calculate AND display.

def process_score_combined(base, bonus):
    """Best practice: Return the value, let caller decide to print"""
    result = base + bonus
    return result


def display_score(score):
    """Separate function for display logic"""
    print(f"Final Score: {score}")
    print("=" * 20)


def analysis_scenario_5():
    # YOUR ANALYSIS
    #
    # Consider: How does separating concerns help?

    analysis = """
    The combined approach:
    - One function calculates (returns value)
    - Another function displays (prints formatted output)

    Benefits:
    1.
    2.
    3.

    This is called "separation of concerns" - each function has
    one clear job.
    """
    return analysis


def main():
    print("{{CONTEXT_COMPARISON_INTRO}}")
    print("=" * 50)

    print("\n=== Scenario 1: Calculation ===")
    print("\nVersion 1 (prints):")
    calculate_score_v1(100, 25)
    print("Can we use this value? Let's try:")
    result1 = calculate_score_v1(100, 25)
    print(f"Stored value: {result1}")

    print("\nVersion 2 (returns):")
    result2 = calculate_score_v2(100, 25)
    print(f"Stored value: {result2}")
    doubled = result2 * 2
    print(f"Doubled: {doubled}")
    print(f"\nYour analysis:{analysis_scenario_1()}")

    print("\n=== Scenario 2: Greeting ===")
    print("\nVersion 1 (prints):")
    greet_user_v1("{{hero}}")
    print("\nVersion 2 (returns):")
    greeting = greet_user_v2("{{hero}}")
    print(greeting)
    print(f"\nYour analysis:{analysis_scenario_2()}")

    print("\n=== Scenario 3: Status Check ===")
    print("\nVersion 1 (prints):")
    check_status_v1(15)
    print("\nVersion 2 (returns):")
    is_qualified = check_status_v2(15)
    print(f"Qualified? {is_qualified}")
    if is_qualified:
        print("Access granted!")
    print(f"\nYour analysis:{analysis_scenario_3()}")

    print("\n=== Scenario 4: Report ===")
    print("\nVersion 1 (prints directly):")
    create_report_v1("{{school}} Report", "Status: Active")
    print("\nVersion 2 (returns string):")
    report = create_report_v2("{{school}} Report", "Status: Active")
    print(report)
    print(f"\nYour analysis:{analysis_scenario_4()}")

    print("\n=== Scenario 5: Combined Approach ===")
    score = process_score_combined(100, 50)
    display_score(score)
    # Can also use score in calculations
    bonus_score = score * 1.5
    display_score(int(bonus_score))
    print(f"\nYour analysis:{analysis_scenario_5()}")

    print("\n" + "=" * 50)
    print("{{CONTEXT_EVALUATION_COMPLETE}}")


main()
