# Exercise 1: Add Error Handling - File I/O
#
# Each function works for good input but crashes on bad input.
# Add try/except blocks to handle errors gracefully.
#
# Theme: Managing {{school}}'s file-based record system


import json
import os


# ============================================================
# ERROR HANDLING A: Reading a File
# ============================================================

def original_read_file(filepath):
    """ORIGINAL: Crashes if file doesn't exist"""
    with open(filepath, "r") as f:
        return f.read()


def safe_read_file(filepath, default=""):
    """
    Read contents of a file safely.

    Should handle:
    - File not found → return default
    - Permission denied → return default with message
    - None filepath → return default

    Args:
        filepath: Path to the file
        default: Value to return if reading fails

    Returns:
        str: File contents or default
    """
    # ✏️ ADD ERROR HANDLING ✏️
    # Hint: FileNotFoundError, PermissionError, TypeError

    pass


# ============================================================
# ERROR HANDLING B: Writing a File
# ============================================================

def original_write_file(filepath, content):
    """ORIGINAL: Crashes if path is invalid or permission denied"""
    with open(filepath, "w") as f:
        f.write(content)
    return True


def safe_write_file(filepath, content):
    """
    Write content to a file safely.

    Should handle:
    - Invalid path → return False with message
    - Permission denied → return False with message
    - None content → write empty string

    Args:
        filepath: Path to write to
        content: Content to write

    Returns:
        bool: True if successful, False otherwise
    """
    # ✏️ ADD ERROR HANDLING ✏️

    pass


# ============================================================
# ERROR HANDLING C: Loading JSON
# ============================================================

def original_load_json(filepath):
    """ORIGINAL: Crashes if file missing or JSON invalid"""
    with open(filepath, "r") as f:
        return json.load(f)


def safe_load_json(filepath, default=None):
    """
    Load JSON from a file safely.

    Should handle:
    - File not found → return default
    - Invalid JSON → return default with message "Invalid JSON format"
    - Empty file → return default

    Args:
        filepath: Path to JSON file
        default: Value to return if loading fails

    Returns:
        dict/list or default: Parsed JSON or default
    """
    # ✏️ ADD ERROR HANDLING ✏️
    # Hint: json.JSONDecodeError for bad JSON

    pass


# ============================================================
# ERROR HANDLING D: Saving JSON
# ============================================================

def original_save_json(filepath, data):
    """ORIGINAL: Crashes if data not serializable or path invalid"""
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    return True


def safe_save_json(filepath, data):
    """
    Save data to a JSON file safely.

    Should handle:
    - Invalid path → return False with message
    - Non-serializable data → return False with message "Cannot convert to JSON"
    - None filepath → return False

    Args:
        filepath: Path to save to
        data: Data to serialize

    Returns:
        bool: True if successful, False otherwise
    """
    # ✏️ ADD ERROR HANDLING ✏️
    # Hint: TypeError for non-serializable data

    pass


# ============================================================
# ERROR HANDLING E: File Existence Check
# ============================================================

def original_check_and_read(filepath):
    """ORIGINAL: Race condition - file could be deleted between check and read"""
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return f.read()
    return None


def safe_check_and_read(filepath, default=None):
    """
    Check if file exists and read it atomically.

    This version uses try/except instead of checking first,
    which is the "EAFP" (Easier to Ask Forgiveness than Permission) approach.

    Should handle:
    - File not found → return default
    - Any other error → return default

    Args:
        filepath: Path to the file
        default: Value to return if reading fails

    Returns:
        str or default: File contents or default
    """
    # ✏️ ADD ERROR HANDLING ✏️
    # Don't check if exists - just try to read!

    pass


# ============================================================
# ERROR HANDLING F: Processing Config File
# ============================================================

def original_load_config(filepath):
    """ORIGINAL: Assumes file exists and is valid JSON with expected keys"""
    with open(filepath, "r") as f:
        config = json.load(f)
    return {
        "name": config["name"],
        "level": config["level"],
        "settings": config["settings"]
    }


def safe_load_config(filepath, defaults=None):
    """
    Load configuration with defaults for missing values.

    Should handle:
    - File not found → use all defaults
    - Invalid JSON → use all defaults
    - Missing keys → use default for that key

    Default values if none provided:
        name: "Unknown"
        level: 1
        settings: {}

    Args:
        filepath: Path to config file
        defaults: Dict of default values (optional)

    Returns:
        dict: Configuration with all keys guaranteed
    """
    # ✏️ ADD ERROR HANDLING ✏️
    # Use dict.get() for missing keys after loading

    if defaults is None:
        defaults = {"name": "Unknown", "level": 1, "settings": {}}

    pass


# ============================================================
# ERROR HANDLING G: Batch File Processing
# ============================================================

def original_process_all_files(filepaths):
    """ORIGINAL: Stops on first error"""
    results = []
    for path in filepaths:
        with open(path, "r") as f:
            results.append(f.read())
    return results


def safe_process_all_files(filepaths):
    """
    Process multiple files, continuing even if some fail.

    Should handle:
    - Individual file errors → skip that file, continue with others
    - Return dict with successes, failures, and error messages

    Args:
        filepaths: List of file paths to process

    Returns:
        dict: {
            "successes": [(path, content), ...],
            "failures": [(path, error_message), ...]
        }
    """
    # ✏️ ADD ERROR HANDLING ✏️
    # Don't let one bad file stop the whole process!

    pass


def main():
    # Create a test file for demonstrations
    test_file = "test_data.txt"
    test_json = "test_data.json"

    print("=== Test A: Reading Files ===")
    # Create test file first
    with open(test_file, "w") as f:
        f.write("Hello from {{school}}!")

    print(f"Read existing file: {safe_read_file(test_file)}")
    print(f"Read missing file: {safe_read_file('nonexistent.txt')}")
    print(f"Read None: {safe_read_file(None)}")

    print("\n=== Test B: Writing Files ===")
    print(f"Write valid: {safe_write_file('output.txt', '{{hero}} was here')}")
    # print(f"Write invalid path: {safe_write_file('/invalid/path/file.txt', 'test')}")

    print("\n=== Test C: Loading JSON ===")
    # Create test JSON
    with open(test_json, "w") as f:
        json.dump({"hero": "{{hero}}", "spells": ["{{spell1}}", "{{spell2}}"]}, f)

    print(f"Load valid JSON: {safe_load_json(test_json)}")
    print(f"Load missing: {safe_load_json('missing.json', {'default': True})}")

    # Create invalid JSON
    with open("bad.json", "w") as f:
        f.write("not valid json {{{")
    print(f"Load invalid JSON: {safe_load_json('bad.json', {'error': True})}")

    print("\n=== Test F: Config Loading ===")
    # Create partial config
    with open("partial_config.json", "w") as f:
        json.dump({"name": "{{hero}}"}, f)  # Missing level and settings

    print(f"Load partial config: {safe_load_config('partial_config.json')}")
    print(f"Load missing config: {safe_load_config('missing_config.json')}")

    print("\n=== Test G: Batch Processing ===")
    files = [test_file, "missing1.txt", test_json, "missing2.txt"]
    result = safe_process_all_files(files)
    print(f"Successes: {len(result.get('successes', []))}")
    print(f"Failures: {len(result.get('failures', []))}")

    # Cleanup test files
    for f in [test_file, test_json, "output.txt", "bad.json", "partial_config.json"]:
        if os.path.exists(f):
            os.remove(f)

    print("\nTest files cleaned up!")


main()
