# %% [markdown]
# {{CONTEXT_DISCOVERY_INTRO}}
#
# זוהי תרגיל רב-שלבי שבו את יורשת מערכת הגדרות מקוננת,
# מבינה את המבנה שלה, מרחיבה אותה ומתקנת בעיות.
#
# מושגי תכנות: מילונים מקוננים, גישה בטוחה, נתונים ברמות מרובות
#
# חלק 1: גילוי - הבנת ה-Config המקונן
# {{CONTEXT_DISCOVERY_NARRATIVE}}
#
# {{mentor}} השאירה מאחוריה את מערכת ההגדרות הזו.
# למדי את המבנה המקונן לפני שתבצעי שינויים.

# %%
CONFIG = {
    "player": {
        "name": "{{hero}}",
        "stats": {
            "health": 100,
            "mana": 50,
            "strength": 10
        },
        "preferences": {
            "difficulty": "normal",
            "hints_enabled": True
        }
    },
    "display": {
        "resolution": "1920x1080",
        "fullscreen": False,
        "colors": {
            "background": "dark",
            "text": "light"
        }
    },
    "audio": {
        "master_volume": 80,
        "music_volume": 60,
        "effects_volume": 100
    }
}

# %%
player_name = CONFIG["player"]["name"]
player_health = CONFIG["player"]["stats"]["health"]
bg_color = CONFIG["display"]["colors"]["background"]
music_vol = CONFIG["audio"]["music_volume"]

print(f"Player: {player_name}")
print(f"Health: {player_health}")
print(f"Background: {bg_color}")
print(f"Music: {music_vol}")

# %% [markdown]
# השלימי את טבלת המעקב
#
# עבור כל שורה, עקבי אחרי הנתיב דרך המילונים המקוננים.
#
# | Variable      | Path                           | Value        |
# |---------------|--------------------------------|--------------|
# | player_name   | CONFIG["player"]["name"]       | "{{hero}}"   |
# | player_health | CONFIG["player"]["stats"][?]   |              |
# | bg_color      | CONFIG[?][?][?]                |              |
# | music_vol     | CONFIG[?][?]                   |              |
#
# כמה רמות עמוק כל גישה?
# - player_name: 2 רמות
# - player_health: ? רמות
# - bg_color: ? רמות
# - music_vol: ? רמות

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# חלק 2: בעלות - הרחבת ה-Config
# {{CONTEXT_OWNERSHIP_INTRO}}
# {{CONTEXT_OWNERSHIP_NARRATIVE}}
#
# הוסיפי קטעי הגדרות חדשים ופונקציות לגישה אליהם בצורה בטוחה.
#
# 1. התחילי עם ה-config
# 2. עבור כל מפתח ב-keys:
#    - אם הערך הנוכחי הוא מילון ויש בו את המפתח, התקדמי פנימה
#    - אחרת, החזירי `None`
# 3. החזירי את הערך הסופי
#
# > רמז: השתמשי בלולאה על המפתחות, ובדקי כל שלב

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# 1. עברי על כל המפתחות פרט לאחרון:
#    - אם מפתח לא קיים, צרי מילון ריק
#    - היכנסי למילון המקונן
# 2. השתמשי במפתח האחרון כדי לקבוע את הערך
#
# זה מסובך קצת! עבדי על זה שלב אחר שלב.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# הוסיפי את המבנה המקונן ל-`config["controls"]`

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# חלק 3: חקירה - איתור באגים בגישה מקוננת
# {{CONTEXT_INVESTIGATION_INTRO}}
# {{CONTEXT_INVESTIGATION_NARRATIVE}}
#
# מצאי ותקני באגים בקוד ה-config המקונן הזה.
#
# הודעת השגיאה:
# --------------
# Traceback (most recent call last):
#   File "config.py", line 5, in <module>
#     sensitivity = config["controls"]["mouse"]["sensitivity"]
# KeyError: 'controls'

# %%
sensitivity = config["controls"]["mouse"]["sensitivity"]
return sensitivity

# %% [markdown]
# השגיאה קרתה כי: _______________
#
# השתמשי ב-`get_config_value` או בבדיקה ידנית כדי לגשת ל-`sensitivity` בצורה בטוחה,
# והחזירי ערך ברירת מחדל אם לא נמצא.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %%
config["player"]["stats"][stat_name] = new_value

# %% [markdown]
# מה אם `config["player"]` לא קיים?
# מה אם `config["player"]["stats"]` לא קיים?
#
# צרי גרסה שמוודאת שהנתיב קיים לפני העדכון.

# %%
# ✏️ כתבי את הקוד שלך כאן

# %% [markdown]
# ## ראשי

# %%
print("=" * 60)
print("{{CONTEXT_DISCOVERY_INTRO}}")
print("=" * 60)
print()

print(">>> PART 1: Understanding the nested config...")
print()
print("CONFIG structure:")
for section in CONFIG:
    print(f"  {section}: {list(CONFIG[section].keys())}")
print()
print("(Study code_to_trace() and complete trace_nested_access())")
# Uncomment to verify:
# code_to_trace()

print()
print(">>> PART 2: Extending the config...")
print("(Implement get_config_value, set_config_value, add_controls_config)")
print()
# Uncomment after implementing:
# print(f"Safe get player name: {get_config_value(CONFIG, 'player', 'name')}")
# print(f"Safe get missing: {get_config_value(CONFIG, 'missing', 'key')}")
# test_cfg = {}
# set_config_value(test_cfg, "test_value", "a", "b", "c")
# print(f"After set_config_value: {test_cfg}")
# add_controls_config(CONFIG)
# print(f"Controls added: {'controls' in CONFIG}")

print()
print(">>> PART 3: Debugging nested access...")
print("(Implement fixed_get_sensitivity, fixed_update_stats)")
print()
# Uncomment after implementing:
# empty_config = {}
# print(f"Sensitivity from empty config: {fixed_get_sensitivity(empty_config)}")
# fixed_update_stats(empty_config, "health", 200)
# print(f"After update: {empty_config}")

print()
print("=" * 60)
print("{{CONTEXT_TRIUMPH_COMPLETE}}")
print("=" * 60)
