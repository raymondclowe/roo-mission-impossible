import os
import json

REQUIRED_FIELDS = {"slug", "name", "roleDefinition", "groups", "source"}
OPTIONAL_FIELDS = {"customInstructions"}
ALLOWED_GROUPS = {"read", "edit", "browser", "command", "mcp"}


def validate_mode_obj(obj, filename):
    errors = []
    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in obj:
            errors.append(f"Missing required field '{field}' in {filename}")
    # Check groups
    groups = obj.get("groups", None)
    if not isinstance(groups, list):
        errors.append(f"'groups' must be a list in {filename}")
    else:
        if not (0 <= len(groups) <= 5):
            errors.append(f"'groups' must have 0 to 5 items in {filename}")
        for g in groups:
            if g not in ALLOWED_GROUPS:
                errors.append(f"Invalid group '{g}' in {filename}")
    # Check for extra fields
    allowed_fields = REQUIRED_FIELDS | OPTIONAL_FIELDS
    for key in obj:
        if key not in allowed_fields:
            errors.append(f"Unexpected field '{key}' in {filename}")
    return errors

def check_json_file(filepath):
    with open(filepath, "r") as f:
        try:
            data = json.load(f)
        except Exception as e:
            return [f"JSON parse error in {filepath}: {e}"]
    # Accept either a list or a single object
    if isinstance(data, list):
        objs = data
    elif isinstance(data, dict):
        # If it looks like the .roomodes.example format
        if "customModes" in data and isinstance(data["customModes"], list):
            objs = data["customModes"]
        else:
            objs = [data]
    else:
        return [f"Top-level JSON must be an object or list in {filepath}"]
    errors = []
    for obj in objs:
        errors.extend(validate_mode_obj(obj, filepath))
    return errors

def main():
    for fname in os.listdir('.'):
        if fname.endswith('.json'):
            errs = check_json_file(fname)
            if errs:
                print(f"Errors in {fname}:")
                for e in errs:
                    print(f"  - {e}")
            else:
                print(f"{fname}: OK")

if __name__ == "__main__":
    main()
