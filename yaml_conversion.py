import os
import json
import yaml

DETAILS_DIR = "./"  # Directory containing *-details.json and *-details.md
OUTPUT_DIR = "./roomodes"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def write_yaml_with_header(data, yaml_path, slug):
    header = f"# Auto-converted from {slug}-details.json and {slug}-details.md\n"
    with open(yaml_path, "w") as f:
        f.write(header)
        yaml.dump(data, f, sort_keys=False, allow_unicode=True, default_flow_style=False)

for filename in os.listdir(DETAILS_DIR):
    if filename.endswith("-details.json"):
        slug = filename.replace("-details.json", "")
        json_path = os.path.join(DETAILS_DIR, filename)
        md_path = os.path.join(DETAILS_DIR, f"{slug}-details.md")
        yaml_path = os.path.join(OUTPUT_DIR, f"{slug}.roomode.yaml")

        try:
            with open(json_path, "r") as f:
                data = json.load(f)
        except Exception as e:
            print(f"Error reading {json_path}: {e}")
            continue

        # Merge in markdown instructions if present
        if os.path.exists(md_path):
            with open(md_path, "r") as f:
                instructions = f.read()
            # Use block scalar for multi-line markdown
            data["customInstructions"] = instructions

        try:
            write_yaml_with_header(data, yaml_path, slug)
            print(f"Converted {slug} to {yaml_path}")
        except Exception as e:
            print(f"Error writing {yaml_path}: {e}")