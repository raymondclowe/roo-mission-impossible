# roo-mission-impossible
A Roo Code-based system to perform tasks using the Mission Impossible team-building strategy.

# Installation for Humans (Roo Code ignore this)

Cut and paste the Step 1 below into a new Roo Code task. The subsequent steps should execute automatically.

## Your Instructions

You are Roo Code, and you will follow these instructions step by step. For each step:
1. Download the `setup.md` file from the repository.
2. Follow the instructions inside `setup.md` sequentially.

---

### [ ] Step 1. Download Setup Instructions

Download the `setup.md` file using the following command:

```bash
curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/main/setup.md > setup.md
```

After downloading, open the file and follow the instructions sequentially.

## Agent Modes (YAML)

Agent modes are now defined as individual YAML files in the `roomodes/` directory. Each file (e.g., `roo-writer.roomode.yaml`) contains the full definition for a single agent mode. This replaces the previous system of `*-details.json` and `*-details.md` files.

### How to Add or Update Agent Modes
- To add a new agent mode, place its `.roomode.yaml` file in the `roomodes/` directory.
- To update an agent mode, edit or replace the corresponding `.roomode.yaml` file.
- Team leaders assemble teams by selecting the required `.roomode.yaml` files from `roomodes/`.
- Trainers can create or edit agent modes by editing or adding new `.roomode.yaml` files. See `roo-trainer.roomode.yaml` for a template.

### Example YAML Structure
```yaml
slug: roo-writer
name: Roo Writer
roleDefinition: |
  You are the Roo Writer, responsible for crafting compelling narratives...
groups: [read, edit, command, mcp]
source: project
customInstructions: |
  Always collaborate with the Researcher and Editor...
```

**Note:** The old `.roomodes` JSON file and `*-details.json`/`*-details.md` split are now deprecated. All agent definitions should be managed as YAML files in `roomodes/`.

# Test it out

Try giving these instructions:

```
Good morning Mr Phelps. Your missions should you choose to accept it is to load the website example.com and save the content into a markdown file. Good luck Jim.
```

