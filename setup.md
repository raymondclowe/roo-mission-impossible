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

For example:

```bash
curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/.memory/table-of-contents.md > .memory/table-of-contents.md
```

Repeat for the other files.

---

## Step 3: Set up the Project Knowledge Base

If the `.knowledgebase` folder already exists, skip this step and proceed to Step 4 after deleting this step from this file.

# Knowledgebase

This file is hosted at github and can be updated as follows:

  - Create a hidden folder named `.knowledgebase` at the root of the project.
  - Download the `table-of-contents.md` file into the `.knowledgebase` folder using the following command:

  ```bash
    curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/.knowledgebase/table-of-contents.md > .knowledgebase/table-of-contents.md
   ```


## Step 4: Set up Mr. Phelps

1
1. Download the latest `jim-phelps-details` `.json` and `.md` files using the following commands:

```bash
curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/jim-phelps-details.json > jim-phelps-details.json

curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/jim-phelps-details.md > jim-phelps-details.md
```
2. Check for the existence of a `.roomodes` file:
   - If the file does not exist, create it by copying over the jim-phelps-details.json file to by going `cp jim-phelps-detials.json .roomodes` 
   - If the file exists, read its contents and validate that the `customModes` key exists and is an array. If not, initialize it as an empty array.

Example `.roomodes` file
```json
{
  "customModes": [
    {
      "slug": "example",
      "name": "example",
      "roleDefinition": "example",
      "customInstructions": "Always read common-instructions.md and your own -details.md file before starting work. example",
      "groups": [
        "read",
        "edit",
        "browser",
        "command",
        "mcp"
      ],
      "source": "project"
    }
  ]
}
```
3. If jim-phelps is not already in the .roomodes file then integrate the `jim-phelps` mode into the `.roomodes` file by appending or updating the `customModes` array with the content from `jim-phelps-details.json`.

4. Save the updated `.roomodes` file and validate its structure.


---

## Step 5: Set up the Tech Support agent

1. Download the latest `roo-tech-support-details` `.json` and `.md` files using the following commands:

```bash
curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/roo-tech-support-details.json > roo-tech-support-details.json
curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/roo-tech-support-details.md > roo-tech-support-details.md
```
2. Check for the existence of a `.roomodes` file:
   - If the file does not exist, create it by copying over the roo-tech-support-details.json file to by going `cp roo-tech-support-details.json .roomodes` 
   - If the file exists, read its contents and validate that the `customModes` key exists and is an array. If not, initialize it as an empty array.
3. If tech-support is not already in the .roomodes file then integrate the `tech-support` mode into the `.roomodes` file by appending or updating the `customModes` array with the content from `roo-tech-support-details.json`.
4. Save the updated `.roomodes` file and validate its structure.

## Step 6: Confirm Setup Completion

Output a message to the user indicating that the setup is complete. For example:

```
Setup complete! The 'jim-phelps' mode has been successfully configured in the .roomodes file and awaits your instructions.
```

Then change mode role to the `jim-phelps` agent mode role to begin task delegation.

## Finally

Once all the above is done then DELETE THIS `setup.md` file to avoid instructions being repeated
