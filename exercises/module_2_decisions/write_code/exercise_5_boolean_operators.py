# =============================================================================
# Write Code: Boolean Operators (and/or/not)
# =============================================================================
# Difficulty: 4
# Concepts: and, or, not, compound conditions
# =============================================================================

"""
{{CONTEXT_PROJECT_INTRO}}
{{CONTEXT_LEARNING_OBJECTIVE}}
"""

# ============================================================
# {{PHASE_1_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_1}}


def exercise_a():
    # ✏️ YOUR CODE HERE ✏️
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # {{hero}} needs BOTH high {{primary_stat}} AND a {{item}} to proceed.
    # Use 'and' to check both conditions.
    #
    # Step 1: Create stat_value = 80
    # Step 2: Create has_item = True
    # Step 3: Write an if/else using 'and':
    #         if stat_value >= 50 and has_item:
    #             print "{{hero}} is ready to proceed!"
    #         else:
    #             print "{{hero}} needs to prepare more."
    #
    # Expected output:
    #   {{hero}} is ready to proceed!
    pass


# ============================================================
# {{PHASE_2_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_2}}


def exercise_b():
    # ✏️ YOUR CODE HERE ✏️
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # {{hero}} can enter {{location}} with EITHER a key OR the password.
    # Use 'or' to check if at least one is available.
    #
    # Step 1: Create has_key = False
    # Step 2: Create knows_password = True
    # Step 3: Write an if/else using 'or':
    #         if has_key or knows_password:
    #             print "{{hero}} enters {{location}}!"
    #         else:
    #             print "{{hero}} cannot enter."
    #
    # Expected output:
    #   {{hero}} enters {{location}}!
    pass


# ============================================================
# {{PHASE_3_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_3}}


def exercise_c():
    # ✏️ YOUR CODE HERE ✏️
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # {{hero}} goes exploring only if there are no enemies nearby.
    # Use 'not' to check the opposite of a condition.
    #
    # Step 1: Create enemy_nearby = False
    # Step 2: Write an if/else using 'not':
    #         if not enemy_nearby:
    #             print "{{hero}} explores safely."
    #         else:
    #             print "{{hero}} stays hidden."
    #
    # Expected output:
    #   {{hero}} explores safely.
    pass


# ============================================================
# {{PHASE_4_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_4}}


def exercise_d():
    # ✏️ YOUR CODE HERE ✏️
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # {{hero}} can use {{spell3}} if they have enough {{secondary_stat}} AND
    # the ability is NOT on cooldown.
    # Combine 'and' with 'not'.
    #
    # Step 1: Create power = 100
    # Step 2: Create on_cooldown = False
    # Step 3: Create required_power = 50
    # Step 4: Write an if/else:
    #         if power >= required_power and not on_cooldown:
    #             print "{{hero}} uses {{spell3}}!"
    #         else:
    #             print "Cannot use {{spell3}} right now."
    #
    # Expected output:
    #   {{hero}} uses {{spell3}}!
    pass


# ============================================================
# {{PHASE_5_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_5}}


def exercise_e():
    # ✏️ YOUR CODE HERE ✏️
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # {{mentor}} determines if {{hero}} can take an advanced class.
    # Requirements: (level >= 10 AND passed_exam) OR has_special_permission
    #
    # Step 1: Create level = 8
    # Step 2: Create passed_exam = True
    # Step 3: Create has_special_permission = False
    #
    # Step 4: Write an if/else with parentheses for clarity:
    #         if (level >= 10 and passed_exam) or has_special_permission:
    #             print "{{hero}} can take the advanced class!"
    #         else:
    #             print "{{hero}} must meet the requirements first."
    #
    # Expected output (level is only 8, no special permission):
    #   {{hero}} must meet the requirements first.
    pass


# ============================================================
# {{PHASE_6_TITLE}}
# ============================================================
# {{CONTEXT_PHASE_6}}


def exercise_f():
    # ✏️ YOUR CODE HERE ✏️
    #
    # {{CONTEXT_STUDENT_TASK}}
    #
    # Create a challenge eligibility checker for {{school}}.
    # The challenge has multiple requirements that can be met different ways.
    #
    # Step 1: Create variables:
    #         hero_level = 15
    #         hero_gold = 200
    #         is_guild_member = True
    #
    # Step 2: Print f"Level: {hero_level}, Gold: {hero_gold}, Guild Member: {is_guild_member}"
    #
    # Step 3: Challenge requirements - must meet ONE of these:
    #         - High level (level >= 20)
    #         - Rich (gold >= 500)
    #         - Guild member with moderate level (is_guild_member and level >= 10)
    #
    # Step 4: Write the if/else:
    #         if hero_level >= 20 or hero_gold >= 500 or (is_guild_member and hero_level >= 10):
    #             print "{{hero}} qualifies for the challenge!"
    #         else:
    #             print "{{hero}} doesn't meet any requirement."
    #
    # Expected output (guild member with level 15 qualifies):
    #   Level: 15, Gold: 200, Guild Member: True
    #   {{hero}} qualifies for the challenge!
    pass


def main():
    print("{{CONTEXT_PROJECT_INTRO}}")
    print("=" * 50)

    print("\n=== {{PHASE_1_TITLE}} ===")
    exercise_a()

    print("\n=== {{PHASE_2_TITLE}} ===")
    exercise_b()

    print("\n=== {{PHASE_3_TITLE}} ===")
    exercise_c()

    print("\n=== {{PHASE_4_TITLE}} ===")
    exercise_d()

    print("\n=== {{PHASE_5_TITLE}} ===")
    exercise_e()

    print("\n=== {{PHASE_6_TITLE}} ===")
    exercise_f()

    print("=" * 50)
    print("{{CONTEXT_FINAL_ASSEMBLY}}")


main()
