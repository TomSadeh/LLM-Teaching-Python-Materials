# %% [markdown]
# {{CONTEXT_PROJECT_INTRO}}
# {{CONTEXT_LEARNING_OBJECTIVE}}
#
# בתרגיל הזה תלמדי להשתמש במודול `json` כדי לשמור ולטעון
# נתונים מובנים. JSON מושלם לאחסון מילונים ורשימות -
# זה כמו שפה אוניברסלית לנתונים.
#
# נושא: יסודות מודול JSON (dump, load, dumps, loads)
# רמת קושי: 3

# %%
import json

# %% [markdown]
# ## {{PHASE_1_TITLE}}
# {{CONTEXT_PHASE_1}}
#
# למדי לשמור נתוני Python לקבצי JSON.
#
# שמרי מילון לקובץ JSON.
#
# 1. צרי מילון פרופיל עבור הדמות:
#         profile = {
#             "name": "{{hero}}",
#             "level": 5,
#             "abilities": ["{{spell1}}", "{{spell2}}"],
#             "stats": {"health": 100, "energy": 50}
#         }
#
# 2. שמרי לקובץ JSON באמצעות `json.dump()`:
#         with open("profile.json", "w") as f:
#             json.dump(profile, f)
#
# 3. שמרי עם עיצוב נאה (הזחה):
#         with open("profile_pretty.json", "w") as f:
#             json.dump(profile, f, indent=2)
#
# 4. הדפיסי הודעת אישור

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# טעיני נתונים מקובץ JSON.
#
# 1. טעיני את הפרופיל ששמרת:
#         with open("profile.json", "r") as f:
#             loaded_profile = json.load(f)
#
# 2. הדפיסי את הנתונים שנטענו:
#         print(f"Loaded profile: {loaded_profile}")
#         print(f"Name: {loaded_profile['name']}")
#         print(f"Level: {loaded_profile['level']}")
#
# 3. ודאי שזה באמת מילון:
#         print(f"Type: {type(loaded_profile)}")
#
# > רמז: JSON שומרת על המבנה - מילונים נשארים מילונים!

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_2_TITLE}}
# {{CONTEXT_PHASE_2}}
#
# למדי להמיר בין מחרוזות JSON לאובייקטי Python.
#
# המירי Python למחרוזת JSON (ובחזרה) באמצעות `dumps`/`loads`.
#
# 1. צרי כמה נתונים:
#         data = {
#             "school": "{{school}}",
#             "students": ["{{hero}}", "{{heroine}}", "{{friend}}"],
#             "active": True
#         }
#
# 2. המירי למחרוזת JSON (לא לקובץ):
#         json_string = json.dumps(data)
#         print(f"JSON string: {json_string}")
#         print(f"Type: {type(json_string)}")  # It's a str!
#
# 3. המירי את מחרוזת ה-JSON חזרה ל-Python:
#         restored = json.loads(json_string)
#         print(f"Restored: {restored}")
#         print(f"Type: {type(restored)}")  # It's a dict again!
#
# > רמז: dumps = שמירה למחרוזת, loads = טעינה ממחרוזת

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# עבדי עם רשימות ב-JSON.
#
# 1. צרי רשימת רשומות:
#         records = [
#             {"name": "{{hero}}", "score": 100},
#             {"name": "{{heroine}}", "score": 150},
#             {"name": "{{friend}}", "score": 75}
#         ]
#
# 2. שמרי ל-JSON:
#         with open("records.json", "w") as f:
#             json.dump(records, f, indent=2)
#
# 3. טעיני ועברי על הפריטים:
#         with open("records.json", "r") as f:
#             loaded_records = json.load(f)
#
#         for record in loaded_records:
#             print(f"{record['name']}: {record['score']}")

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## {{PHASE_3_TITLE}}
# {{CONTEXT_PHASE_3}}
#
# למדי את מגבלות JSON ושיטות עבודה מומלצות.
#
# הביני מה JSON יכולה ולא יכולה לאחסן.
#
# 1. JSON תומכת בסוגי Python האלה:
#         supported = {
#             "string": "hello",
#             "number": 42,
#             "float": 3.14,
#             "boolean": True,
#             "null": None,
#             "list": [1, 2, 3],
#             "dict": {"nested": "value"}
#         }
#         שמרי זאת בקובץ "supported.json" וטעיני אותו בחזרה.
#
# 2. JSON לא תומכת (ישירות) בסוגים האלה:
#         - Sets: {1, 2, 3} הופך ל-[1, 2, 3] (רשימה)
#         - Tuples: (1, 2, 3) הופך ל-[1, 2, 3] (רשימה)
#         - אובייקטים מותאמים: דורשים טיפול מיוחד
#
# 3. בדקי עם set:
#         data = {"items": {"a", "b", "c"}}  # This has a set!
#         # json.dump(data, f)  # This would ERROR!
#         # Convert set to list first:
#         data["items"] = list(data["items"])
#         # Now it works
#
# 4. הדפיסי מה למדת

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# צרי מערכת שמירה וטעינה שלמה עבור {{school}}.
#
# 1. צרי מילון מצב משחק:
#         game_state = {
#             "player": "{{hero}}",
#             "level": 1,
#             "inventory": ["{{item}}", "potion"],
#             "location": "{{location}}",
#             "stats": {
#                 "health": 100,
#                 "energy": 50,
#                 "experience": 0
#             },
#             "completed_quests": []
#         }
#
# 2. צרי פונקציית שמירה:
#         def save_game(state, filename):
#             with open(filename, "w") as f:
#                 json.dump(state, f, indent=2)
#             print(f"Game saved to {filename}")
#
# 3. צרי פונקציית טעינה:
#         def load_game(filename):
#             with open(filename, "r") as f:
#                 return json.load(f)
#
# 4. בדקי שמירה וטעינה

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
print("{{CONTEXT_PROJECT_INTRO}}")
print("=" * 50)

print("\n=== {{PHASE_1_TITLE}} ===")
print("Saving and loading JSON files")
exercise_a()
exercise_b()

print("\n=== {{PHASE_2_TITLE}} ===")
print("JSON strings: dumps and loads")
exercise_c()
exercise_d()

print("\n=== {{PHASE_3_TITLE}} ===")
print("JSON best practices")
exercise_e()
exercise_f()

print("=" * 50)
print("{{CONTEXT_FINAL_ASSEMBLY}}")
print()
print("JSON Summary:")
print("  json.dump(data, file)  # Save to file")
print("  json.load(file)        # Load from file")
print("  json.dumps(data)       # Convert to string")
print("  json.loads(string)     # Parse from string")
print()
print("Supports: dict, list, str, int, float, bool, None")
print("NOT directly: set, tuple, custom objects")
