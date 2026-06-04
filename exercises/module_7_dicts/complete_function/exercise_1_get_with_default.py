# %% [markdown]
# {{CONTEXT_COMPLETE_FUNCTION_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי להשתמש ב-`.get()` לגישה בטוחה למילון.
# המתודה `.get()` מחזירה ערך ברירת מחדל כשמפתח לא קיים,
# במקום לזרוק `KeyError`.
#
# ## {{FUNCTION_1_TITLE}}
# {{CONTEXT_FUNCTION_1_NARRATIVE}}
#
# {{CONTEXT_FUNCTION_HINT_1}}
#
# > רמז: השתמשי ב-`stats.get(stat_name, default_value)` —
# > הארגומנט השני מוחזר כאשר המפתח לא קיים.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{FUNCTION_2_TITLE}}
# {{CONTEXT_FUNCTION_2_NARRATIVE}}
#
# {{CONTEXT_FUNCTION_HINT_2}}
#
# > רמז: השתמשי ב-`.get()` לגישה בטוחה למלאי.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{FUNCTION_3_TITLE}}
# {{CONTEXT_FUNCTION_3_NARRATIVE}}
#
# {{CONTEXT_FUNCTION_HINT_3}}
#
# > רמז: החזירי את התיאור, או `"Unknown ability"` כברירת מחדל.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{FUNCTION_4_TITLE}}
# {{CONTEXT_FUNCTION_4_NARRATIVE}}
#
# {{CONTEXT_FUNCTION_HINT_4}}
#
# 1. קבלי את הכמות הנוכחית (ברירת מחדל 0 אם הפריט לא במלאי)
# 2. הוסיפי את הכמות החדשה
# 3. שמרי בחזרה במלאי
# 4. החזירי את הסכום החדש
#
# > רמז: `inventory[item] = inventory.get(item, 0) + quantity`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_COMPLETE_FUNCTION_INTRO}}")
print("=" * 50)

print("\n=== Testing {{FUNCTION_1_TITLE}} ===")
stats = {"health": 100, "strength": 10}
print(f"Health: {get_character_stat(stats, 'health')}")
print(f"Mana (not set): {get_character_stat(stats, 'mana')}")

print("\n=== Testing {{FUNCTION_2_TITLE}} ===")
inventory = {"{{item}}": 5, "{{spell1}}": 3}
print(f"{{{{item}}}}: {get_inventory_count(inventory, '{{item}}')}")
print(f"{{{{spell2}}}} (not owned): {get_inventory_count(inventory, '{{spell2}}')}")

print("\n=== Testing {{FUNCTION_3_TITLE}} ===")
abilities = {
    "{{spell1}}": "A fundamental technique",
    "{{spell2}}": "An intermediate skill"
}
print(f"{{{{spell1}}}}: {get_ability_description(abilities, '{{spell1}}')}")
print(f"{{{{spell3}}}}: {get_ability_description(abilities, '{{spell3}}')}")

print("\n=== Testing {{FUNCTION_4_TITLE}} ===")
inv = {}
safe_add_to_inventory(inv, "{{item}}", 3)
safe_add_to_inventory(inv, "{{item}}", 2)
safe_add_to_inventory(inv, "{{spell1}}", 1)
print(f"Inventory: {inv}")

print("\n" + "=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
