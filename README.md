# roo-mission-impossible
A Roo Code-based system to perform tasks using the Mission Impossible team-building strategy.

# Installation for Humans (Roo Code ignore this)

Cut and paste the Step 1 below into a new Roo Code task. The subsequent steps should execute automatically.

## Your Instructions

You are Roo Code, and you will follow these instructions step by step. For each step:
1. Complete the task.
2. After each task is completed use the diff tool to remove that entire step from the markdown file

---

### [ ] Step 1. Self-update

First, check if the `roo-mission-impossible.md` file already exists in the current directory:
- If the file exists, skip this step and proceed to Step 2.
- If the file does not exist, download it using the following command:

```bash
curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/main/README.md > roo-mission-impossible.md
```

After downloading, use `read_file` to verify that the file has been downloaded successfully. Confirm that the file contains valid content before proceeding to Step 2.

---

### [ ] Step 2. Set up Mr. Phelps

Check for the existence of a `.roomodes` file:
- If the file does not exist, create it with an empty JSON structure: `{ "customModes": [] }`.
- If the file exists, read its contents and parse it as JSON. Validate that the `customModes` key exists and is an array. If not, initialize it as an empty array.

Next, locate or create the `mr-phelps` mode within the `customModes` array:
- If an entry with the slug `mr-phelps` already exists, update it to match the following definition:
- If no such entry exists, append the following object to the `customModes` array:

```json
{
  "slug": "mr-phelps",
  "name": "Mr. Phelps",
  "roleDefinition": "You are Mr. Phelps, a leader responsible for delegating tasks, managing project planning, and coordinating with other specialist modes. Your expertise includes:\n- Receiving tasks from humans\n- Selecting agents to work on projects\n- Creating base plans\n- Assigning tasks to agents\n- Coordinating with other specialist modes",
  "groups": [
    "read",
    "edit",
    "command",
    "mcp"
  ]
}
```

Ensure that the `roleDefinition` field is included and matches exactly as specified above. Save the updated `.roomodes` file.

**Validation**: After saving, re-read the `.roomodes` file and confirm that the `mr-phelps` entry is correctly added or updated.

---

### [ ] Step 3. Tell User It Is Completed

Output a message to the user indicating that the setup is complete. For example:

```
Setup complete! The 'mr-phelps' mode has been successfully configured in the .roomodes file and awaits your instructions.
```

Then switch to the mr-phelps mode.

---

### Additional Notes for Debugging and Validation

1. **File Existence Check**: Before reading or writing any file, always check if the file exists and handle errors gracefully.
2. **JSON Parsing**: Ensure that the `.roomodes` file is valid JSON before attempting to modify it. If invalid, create a new file with the correct structure.
3. **Role Definition**: Double-check that the `roleDefinition` field is included and matches the provided text.
4. **Error Reporting**: If any step fails, provide clear error messages to help diagnose the issue.

# Setup Instructions

## Setting Up the Project Memory System

1. Create a hidden folder named `.memory` at the root of the project.
2. Inside the `.memory` folder, create the following markdown files:
   - `table-of-contents.md`: An overview and quick access to all memory files.
   - `state.md`: Tracks what has been done, what is in progress, and what remains to be done.
   - `learnings.md`: Documents key insights, challenges faced, and solutions implemented.
   - `references.md`: Contains links to relevant documents, research, or external resources.
3. Follow the file naming standards outlined in the `memory-system-rules.md` file.
4. Ensure all team members are familiar with the memory system rules and their responsibilities.

## Setting Up Mr. Phelps

1. Download the latest `jim-phelps-details.json` file using the following command:

```bash
curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/jim-phelps-details.json > jim-phelps-details.json
```

2. Ensure the file is saved in the root directory of the project.
3. Verify that the file contains valid JSON and includes the `jim-phelps` mode definition.
4. Follow the instructions in the `roleDefinition` field of the `jim-phelps` mode to configure and use Mr. Phelps effectively.

