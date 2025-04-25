# Setup Instructions

Follow these steps sequentially to set up the project:

## Step 1: Self-update

First, check if the `roo-mission-impossible.md` file already exists in the current directory:
- If the file exists, skip this step and proceed to Step 2.
- If the file does not exist, download it using the following command:

```bash
curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/main/README.md > roo-mission-impossible.md
```

Verify that the file contains valid content before proceeding.

---

## Step 2: Set up the Project Memory System

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

For example:

```bash
curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/.memory/table-of-contents.md > .memory/table-of-contents.md
```

Repeat for the other files.

---

## Step 3: Set up Mr. Phelps

1. Check for the existence of a `.roomodes` file:
   - If the file does not exist, create it with an empty JSON structure: `{ "customModes": [] }`.
   - If the file exists, read its contents and validate that the `customModes` key exists and is an array. If not, initialize it as an empty array.

2. Download the latest `jim-phelps-details.json` file using the following command:

```bash
curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/jim-phelps-details.json > jim-phelps-details.json
```

3. Integrate the `jim-phelps` mode into the `.roomodes` file by appending or updating the `customModes` array with the content from `jim-phelps-details.json`.

4. Save the updated `.roomodes` file and validate its structure.

---

## Step 4: Confirm Setup Completion

Output a message to the user indicating that the setup is complete. For example:

```
Setup complete! The 'jim-phelps' mode has been successfully configured in the .roomodes file and awaits your instructions.
```

Then switch to the `jim-phelps` mode to begin task delegation.