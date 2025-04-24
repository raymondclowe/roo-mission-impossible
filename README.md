# roo-mission-impossible
A Roo Code-based system to perform tasks using the Mission Impossible team-building strategy.

# Installation for Humans (Roo Code ignore this)

Cut and paste the Step 1 below into a new Roo Code task. The subsequent steps should execute automatically.

## Your Instructions

You are Roo Code, and you will follow these instructions step by step. For each step:
1. Complete the task.
2. After each task is completed, use the diff tool to remove that entire step from the markdown file.

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

### [ ] Step 2. Set up the Project Memory System and Mr. Phelps

1. **Set up the Project Memory System**:
   - Create a hidden folder named `.memory` at the root of the project.
   - Download the `memory-system-rules.md` file into the `.memory` folder using the following command:

   ```bash
   curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/memory-system-rules.md > .memory/memory-system-rules.md
   ```

   - Inside the `.memory` folder, create the following markdown files:
     - `table-of-contents.md`: An overview and quick access to all memory files.
     - `state.md`: Tracks what has been done, what is in progress, and what remains to be done.
     - `learnings.md`: Documents key insights, challenges faced, and solutions implemented.
     - `references.md`: Contains links to relevant documents, research, or external resources.
   - Follow the file naming standards outlined in the `memory-system-rules.md` file.
   - Ensure all team members are familiar with the memory system rules and their responsibilities.

2. **Set up Mr. Phelps**:
   - Check for the existence of a `.roomodes` file:
     - If the file does not exist, create it with an empty JSON structure: `{ "customModes": [] }`.
     - If the file exists, read its contents and parse it as JSON. Validate that the `customModes` key exists and is an array. If not, initialize it as an empty array.
   - Download the latest `jim-phelps-details.json` file using the following command:

   ```bash
   curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/jim-phelps-details.json > jim-phelps-details.json
   ```

   - Ensure the file is saved in the root directory of the project.
   - Verify that the file contains valid JSON and includes the `jim-phelps` mode definition.
   - Integrate the `jim-phelps` mode into the `.roomodes` file by appending or updating the `customModes` array with the content from `jim-phelps-details.json`.
   - Save the updated `.roomodes` file and validate its structure.

---

### [ ] Step 3. Confirm Setup Completion

Output a message to the user indicating that the setup is complete. For example:

```
Setup complete! The 'jim-phelps' mode has been successfully configured in the .roomodes file and awaits your instructions.
```

Then switch to the `jim-phelps` mode to begin task delegation.

