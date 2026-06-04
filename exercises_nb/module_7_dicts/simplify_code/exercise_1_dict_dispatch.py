# %% [markdown]
# {{CONTEXT_SIMPLIFY_CODE_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# החליפי שרשראות ארוכות של `if`/`elif` בבדיקה חכמה באמצעות מילון.
#
# {{SIMPLIFY_1_TITLE}}
# {{CONTEXT_SIMPLIFY_1_NARRATIVE}}

# %%
if ability_name == "{{spell1}}":
    return 10
elif ability_name == "{{spell2}}":
    return 25
elif ability_name == "{{spell3}}":
    return 50
elif ability_name == "{{spell4}}":
    return 15
else:
    return 0

# %% [markdown]
# {{CONTEXT_SIMPLIFY_HINT_1}}
#
# החליפי את שרשרת ה-`if`/`elif` בבדיקה במילון.
# השתמשי ב: `powers = {"ability": value, ...}`
# החזירי: `powers.get(ability_name, 0)`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{SIMPLIFY_2_TITLE}}
# {{CONTEXT_SIMPLIFY_2_NARRATIVE}}

# %%
if status == "healthy":
    message = "Ready for action!"
elif status == "{{harmful_status}}":
    message = "Needs healing."
elif status == "{{busy_activity}}":
    message = "Currently unavailable."
elif status == "resting":
    message = "Recovering energy."
else:
    message = "Status unknown."
return message

# %% [markdown]
# {{CONTEXT_SIMPLIFY_HINT_2}}
#
# השתמשי במילון כדי לקשר בין סטטוסים להודעות.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{SIMPLIFY_3_TITLE}}
# {{CONTEXT_SIMPLIFY_3_NARRATIVE}}

# %%
if command == "add":
    result = value + 10
elif command == "double":
    result = value * 2
elif command == "halve":
    result = value // 2
elif command == "reset":
    result = 0
else:
    result = value  # Unknown command, keep original
return result

# %% [markdown]
# {{CONTEXT_SIMPLIFY_HINT_3}}
#
# זה קצת יותר מסובך — כל פקודה עושה משהו שונה!
#
# גישה 1: שמרי את התוצאה של כל פעולה
#   operations = {
#       "add": value + 10,
#       "double": value * 2,
#       ...
#   }
#   return operations.get(command, value)
#
# > רמז: גישה זו מחשבת את כל הפעולות גם אם לא צריך אותן. לפריטים פשוטים כמו אלה — זה בסדר גמור.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{SIMPLIFY_4_TITLE}}
# {{CONTEXT_SIMPLIFY_4_NARRATIVE}}

# %%
counts = {}
for item in items:
    if item in counts:
        counts[item] = counts[item] + 1
    else:
        counts[item] = 1
return counts

# %% [markdown]
# {{CONTEXT_SIMPLIFY_HINT_4}}
#
# החליפי את ה-`if`/`else` בתבנית עם `.get()`:
# `counts[item] = counts.get(item, 0) + 1`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# {{SIMPLIFY_5_TITLE}}
# {{CONTEXT_SIMPLIFY_5_NARRATIVE}}

# %%
if attacker_type == "fire":
    multiplier = 1.5
elif attacker_type == "water":
    multiplier = 1.2
elif attacker_type == "earth":
    multiplier = 1.0
elif attacker_type == "air":
    multiplier = 1.3
else:
    multiplier = 1.0

return int(base_damage * multiplier)

# %% [markdown]
# {{CONTEXT_SIMPLIFY_HINT_5}}
#
# שמרי את המכפילים במילון.
# השתמשי ב-`.get()` עם ברירת מחדל `1.0` עבור סוגים לא מוכרים.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_SIMPLIFY_CODE_INTRO}}")
print("=" * 50)

print("\n=== {{SIMPLIFY_1_TITLE}} ===")
print(f"Original: {{{{spell2}}}} power = {original_get_power_a('{{spell2}}')}")
print(f"Simplified: {{{{spell2}}}} power = {simplified_get_power_a('{{spell2}}')}")

print("\n=== {{SIMPLIFY_2_TITLE}} ===")
print(f"Original: healthy = {original_get_status_message_b('healthy')}")
print(f"Simplified: healthy = {simplified_get_status_message_b('healthy')}")

print("\n=== {{SIMPLIFY_3_TITLE}} ===")
print(f"Original: double 10 = {original_process_command_c('double', 10)}")
print(f"Simplified: double 10 = {simplified_process_command_c('double', 10)}")

print("\n=== {{SIMPLIFY_4_TITLE}} ===")
items = ["{{item}}", "{{spell1}}", "{{item}}", "{{item}}"]
print(f"Original: {original_count_items_d(items)}")
print(f"Simplified: {simplified_count_items_d(items)}")

print("\n=== {{SIMPLIFY_5_TITLE}} ===")
print(f"Original: fire, 100 = {original_calculate_damage_e('fire', 100)}")
print(f"Simplified: fire, 100 = {simplified_calculate_damage_e('fire', 100)}")

print("\n" + "=" * 50)
print("{{CONTEXT_IMPROVEMENT_COMPLETE}}")
