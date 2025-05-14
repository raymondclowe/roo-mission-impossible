import os
import json
import glob

def main():
    # Find all *-details.json files and jim-phelps-details.json
    files = glob.glob("*-details.json")
    if "jim-phelps-details.json" not in files and os.path.exists("jim-phelps-details.json"):
        files.insert(0, "jim-phelps-details.json")
    else:
        # Ensure jim-phelps-details.json is first if present
        files = [f for f in files if f != "jim-phelps-details.json"]
        if os.path.exists("jim-phelps-details.json"):
            files = ["jim-phelps-details.json"] + files
    all_modes = []
    for fname in files:
        with open(fname, "r") as f:
            data = json.load(f)
            if isinstance(data, dict) and "customModes" in data:
                all_modes.extend(data["customModes"])
            else:
                all_modes.append(data)
    with open(".roomodes.all", "w") as out:
        json.dump({"customModes": all_modes}, out, indent=2)
    print(f".roomodes.all created with {len(all_modes)} modes from {len(files)} files.")

if __name__ == "__main__":
    main()
