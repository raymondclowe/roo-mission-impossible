# Setup Instructions

Follow these steps sequentially to set up the project. After each step is complete delete it from this file.

## Step 1: Self-update

First, check if the `setup.md` file already exists in the current directory:
- If the file exists, skip this step and proceed to Step 2 after deleting this step from this file.
- If the file does not exist, download it using the following command:

```bash
curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/main/setup.md > setup.md
```

Verify that the file contains valid content before proceeding.

---

## Step 2: Set up the Project Memory System

If the `.memory` folder already exists, skip this step and proceed to Step 3 after deleting this step from this file.

1. Create a hidden folder named `.memory` at the root of the project.
2. Download the `memory-system-rules.md` file into the `.memory` folder using the following command:

```bash
curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/memory-system-rules.md > .memory/memory-system-rules.md
```

3. Inside the `.memory` folder, create the following markdown files by downloading the template examples using curl:
   - `table-of-contents.md`
   - `state.md`
   - `learnings.md`
   - `references.md`
   - `readme.md`

For example:

```bash
curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/.memory/table-of-contents.md > .memory/table-of-contents.md
curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/.memory/readme.md > .memory/readme.md
```

Repeat for the other files.

---

## Step 3: Set up the Project Knowledge Base

If the `.knowledgebase` folder already exists, skip this step and proceed to Step 4 after deleting this step from this file.

# Knowledgebase

This file is hosted at github and can be updated as follows:

  - Create a hidden folder named `.knowledgebase` at the root of the project.
  - Download the `table-of-contents.md` and `readme.md` files into the `.knowledgebase` folder using the following commands:

  ```bash
    curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/.knowledgebase/table-of-contents.md > .knowledgebase/table-of-contents.md
    curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/.knowledgebase/readme.md > .knowledgebase/readme.md
   ```

## Step 4: Set up Mr. Phelps

1. Download the latest `jim-phelps.roomode.yaml` file using the following command:

```bash
curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/main/roomodes/jim-phelps.roomode.yaml -o roomodes/jim-phelps.roomode.yaml
```

2. Activate this mode by merging it into your project-level `.roomodes` YAML file at the root of your project. If `.roomodes` does not exist, create it with the following structure:

```yaml
customModes: []
```

3. Use the provided Python script to merge any `.roomode.yaml` file from the `roomodes/` directory into `.roomodes`. This script will avoid duplicates and ensure all active modes are in the `customModes:` array.

**merge_mode.py:**
```python
import yaml
import sys
import os

roomodes_file = '.roomodes'
new_mode_file = sys.argv[1]  # e.g. 'roomodes/jim-phelps.roomode.yaml'

try:
    with open(roomodes_file, 'r') as f:
        data = yaml.safe_load(f)
    if 'customModes' not in data:
        data['customModes'] = []
except FileNotFoundError:
    data = {'customModes': []}

with open(new_mode_file, 'r') as f:
    new_mode = yaml.safe_load(f)

# Avoid duplicates by slug
if not any(m.get('slug') == new_mode.get('slug') for m in data['customModes']):
    data['customModes'].append(new_mode)
else:
    print(f"Mode with slug '{new_mode.get('slug')}' already exists in .roomodes.")

with open(roomodes_file, 'w') as f:
    yaml.dump(data, f, sort_keys=False)
```

Run it as:
```bash
python3 merge_mode.py roomodes/jim-phelps.roomode.yaml
```

4. Repeat the download and merge process for any additional agent modes you wish to activate from the `roomodes/` directory.

---

## Step 5: Set up the Tech Support agent

1. Download the latest `roo-tech-support.roomode.yaml` file using the following command:

```bash
curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/main/roomodes/roo-tech-support.roomode.yaml -o roomodes/roo-tech-support.roomode.yaml
```

2. Activate this mode by merging it into `.roomodes` using the same script:

```bash
python3 merge_mode.py roomodes/roo-tech-support.roomode.yaml
```

---

## Step 6: Set up Additional Agent Modes (YAML)

All agent modes should remain as individual YAML files in the `roomodes/` directory for modularity and version control. To activate any mode, merge its YAML into the `.roomodes` file using the script above. Only modes present in `.roomodes` are active.

Each agent mode YAML file should include a `whenToUse` property that describes the situations or triggers for activating that mode. This helps team leaders and trainers understand when each agent is appropriate to add to a team.

### Mode-Specific Instructions via Files/Directories

For better organization and version control, you can provide detailed instructions for each mode using dedicated files or directories. The preferred method is to use a directory named `.roo/rules-{mode-slug}/` for each mode. For example, for the mode slug `roo-writer`, use:

```
.roo/rules-roo-writer/
    01-style-guide.md
    02-formatting.txt
```

Reference these files in the `customInstructions` or `roleDefinition` fields of your `.roomode.yaml` file, and instruct agents to consult them as needed.

**Example YAML snippet:**
```yaml
slug: roo-writer
name: Roo Writer
roleDefinition: |
  You are the Roo Writer, responsible for crafting compelling narratives...
  For detailed instructions, see files in `.roo/rules-roo-writer/`.
whenToUse: |
  Use this mode when you need to generate, edit, or refine written content for the project, or when a writing specialist is required.
groups: [read, edit, command, mcp]
source: project
customInstructions: |
  Always collaborate with the Researcher and Editor...
  Refer to `.roo/rules-roo-writer/` for style and formatting guidance.
```

---

## Step 7: Team Assembly and Trainer Instructions

- Team leaders (e.g., Jim Phelps) and trainers should activate agent modes by merging the required `.roomode.yaml` files from `roomodes/` into `.roomodes` using the provided script.
- Trainers can create or edit agent modes by editing or adding new YAML files in `roomodes/`, then merging them into `.roomodes` as needed.
- Only modes present in `.roomodes` are active for the project.

---

## Step 8: Confirm Setup Completion

Output a message to the user indicating that the setup is complete. For example:

```
Setup complete! The 'jim-phelps' mode has been successfully configured and awaits your instructions.
```

Then change mode role to the `jim-phelps` agent mode role to begin task delegation.

## Finally

Once all the above is done then DELETE THIS `setup.md` file to avoid instructions being repeated
