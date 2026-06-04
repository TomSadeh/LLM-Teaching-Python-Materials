# =============================================================================
# Hybrid Exercise: The Apprentice - List Foundations
# =============================================================================
# Difficulty: 2
# Arc: Apprentice (DISCOVERY -> GUIDANCE -> GROWTH)
# Concepts: List creation, positive indexing, basic operations
# =============================================================================

# %% [markdown]
# {{CONTEXT_DISCOVERY_INTRO}}
#
# זוהי תרגיל מרובה-חלקים. השלימי כל חלק לפי הסדר.
#
# ## חלק 1: גילוי - לומדים איך רשימות עובדות
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# {{mentor}} מדגים פעולות על רשימות. נסי לנחש את הפלט
# לפני שאת מריצה את הקוד.

# %%
inventory = ["{{item}}", "potion", "map", "key"]
print(f"Items: {inventory}")
print(f"First: {inventory[0]}")
print(f"Total: {len(inventory)}")

# %% [markdown]
# הניחוש שלך עבור study_example_1:
# שורה 1: Items: _______________
# שורה 2: First: _______________
# שורה 3: Total: _______________

# %%
team = ["{{hero}}", "{{heroine}}"]
team = team + ["{{friend}}"]
print(f"Team: {team}")
print(f"Size: {len(team)}")

# %% [markdown]
# הניחוש שלך עבור study_example_2:
# שורה 1: Team: _______________
# שורה 2: Size: _______________

# %%
# YOUR MATCHES HERE
#
# After making your predictions, run the examples and verify.
# Then record whether your predictions were correct.

results = {
    "example_1_correct": "?",  # "yes" or "no"
    "example_2_correct": "?",  # "yes" or "no"
}

return results

# %% [markdown]
# ## חלק 2: הדרכה - תרגול עם פיגומים
# {{CONTEXT_GUIDANCE_INTRO}}
# {{CONTEXT_GUIDANCE_NARRATIVE}}
#
# השלימי את הפונקציה לפי המבנה שסופק לך.

# %%
# Started for you:
team_size = len(members)
first_member = members[0]

# COMPLETE THIS FUNCTION
#
# Step 1: Get the last member using index -1 OR team_size - 1
# Step 2: Return the formatted string as shown in examples
#
# Hint: For a single-member team, first and last are the same.

pass  # Replace with implementation

# %% [markdown]
# ## חלק 3: צמיחה - צרי בעצמך
# {{CONTEXT_GROWTH_INTRO}}
# {{CONTEXT_GROWTH_NARRATIVE}}
#
# עכשיו צרי פעולות על רשימות בעצמך.

# %%
# YOUR CODE HERE
#
# {{hero}} creates a roster for {{school}}.
#
# Step 1: Create a list called roster with 4 names:
#         "{{hero}}", "{{heroine}}", "{{friend}}", "{{mentor}}"
# Step 2: Print f"Full roster: {roster}"
# Step 3: Print f"Captain: {roster[0]}"
# Step 4: Print f"Advisor: {roster[3]}"
# Step 5: Print f"Team size: {len(roster)}"
#
# Expected output:
#   Full roster: ['{{hero}}', '{{heroine}}', '{{friend}}', '{{mentor}}']
#   Captain: {{hero}}
#   Advisor: {{mentor}}
#   Team size: 4
pass

# %%
# YOUR CODE HERE
#
# {{heroine}} combines two groups for a mission.
#
# Step 1: Create scouts = ["{{hero}}", "{{friend}}"]
# Step 2: Create support = ["{{heroine}}", "{{mentor}}"]
# Step 3: Combine them: full_team = scouts + support
# Step 4: Print f"Scouts: {scouts}"
# Step 5: Print f"Support: {support}"
# Step 6: Print f"Full team: {full_team}"
# Step 7: Print f"First scout: {scouts[0]}"
# Step 8: Print f"Team lead: {full_team[0]}"
#
# Expected output:
#   Scouts: ['{{hero}}', '{{friend}}']
#   Support: ['{{heroine}}', '{{mentor}}']
#   Full team: ['{{hero}}', '{{friend}}', '{{heroine}}', '{{mentor}}']
#   First scout: {{hero}}
#   Team lead: {{hero}}
pass

# %%
# YOUR CODE HERE
#
# Print elements at specific positions.
#
# Step 1: Create levels = [10, 25, 50, 75, 100]
# Step 2: Print f"Starting level: {levels[0]}"
# Step 3: Print f"Mid level: {levels[2]}"
# Step 4: Print f"Max level: {levels[4]}"
# Step 5: Calculate total = levels[0] + levels[4]
# Step 6: Print f"Range: {total}"
#
# Expected output:
#   Starting level: 10
#   Mid level: 50
#   Max level: 100
#   Range: 110
pass

# %%
print("=" * 60)
print("THE APPRENTICE: List Foundations")
print("=" * 60)

print("\n--- PART 1: DISCOVERY ---")
print("{{CONTEXT_DISCOVERY_INTRO}}")
print("\nStudy Example 1:")
study_example_1()
print("\nStudy Example 2:")
study_example_2()
print("\nYour prediction results:", part_1_check_predictions())

print("\n--- PART 2: GUIDANCE ---")
print("{{CONTEXT_GUIDANCE_INTRO}}")
print("\nTesting get_team_info:")
result1 = get_team_info(["{{hero}}", "{{heroine}}"])
print(f"Result 1: {result1}")
result2 = get_team_info(["{{mentor}}"])
print(f"Result 2: {result2}")

print("\n--- PART 3: GROWTH ---")
print("{{CONTEXT_GROWTH_INTRO}}")
print("\nBuilding roster:")
exercise_build_roster()
print("\nCombining lists:")
exercise_combine_lists()
print("\nAccess patterns:")
exercise_access_pattern()

print("\n" + "=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
