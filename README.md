# roo-mission-impossible
A Roo Code based system to do tasks, using the Mission Impossible team building strategy

# Installation for humans (Roo Code ignore this)

Cut and paste the Step 1 below into a new Roo Code task, that's it, the next steps should be automatic.

## Your instructions

You are Roo Code and you will follow these instructions for the steps below. For each step complete it then mark it done by chaing `[ ]` into `[X]`. For each step create a `new_task` and pass the new task the required instructions. Once a task has returned then mark it completed and move to the next task. Always create separate tasks. Never repeat tasks.

### [ ] Step 1. Self-update

First check if the roo-mission-impossible.md file has already been downloaded, if it has then step 1 is complete. Proceed with step 2.

But if the file does not exist yet, then get it by executing curl to download the latest version of these instructions as follows;

```
curl [https://github.com/raymondlowe/roo-mission-impossible/edit/main/README.md](https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/README.md) > roo-mission-impossible.md
```
Then you will use `read_file` to read the file roo-mission-impossible.md and proceed with the next step which is Step 2.

### [ ] Step 2. Set up Mr Phelps

Check for a file called .roomodes.  

Open this file and look for a key called "customModes".

Create, update or insert an item with the slug "mr-phelps" as follows:

```
{
  "customModes": [
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
  ]
}
```

If there is already a mr-phelps mode then update it to match this. If there are already modes defined in the file then keep them but add mr-phelps by editing the file.

### [ ] Step 3. Tell user it is completed

Indicate to the user that this task is now completed.

