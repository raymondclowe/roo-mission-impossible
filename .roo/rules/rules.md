# Common Instructions for All Agents

For every new task, you MUST:

1. Always check the `.memory` folder for relevant information.
2. Always check the `.knowledgebase` folder for relevant information.
3. Always read `readme.md` files in any folder you are looking in.
4. Whatever your 'mode' is make sure you look at the <mode>-details.json file. This file contains important information about your mode and its capabilities.

Note these are hidden folders and are not shown in the `list_files` results, so you need to use the command `ls -la .memory` and `ls -la .knowledgebase` to see them.

Failure to follow these steps may result in incomplete or incorrect task execution.

Refer to these rules before starting ANY new task.


## Troubleshooting Browser Automation (Playwright & Remote Chrome)

If you encounter issues with browser automation, follow these steps:

### 1. Consult the Knowledge Base
- Always check `.knowledgebase/table-of-contents.md` for relevant troubleshooting guides before attempting to fix any issue.
- Key files to review:
  - `install-mcp-playwright.md`: Playwright MCP server setup, common errors, and solutions.
  - `install-remote-chrome-browser.md`: Remote Chrome setup, error messages, and solutions.
  - `web-browsing.md`: Overview of browser tools and when to use each.
- Use `ls .knowledgebase` to see available guides. Download missing files as needed (see table-of-contents for instructions).

### 2. Common Error Messages & Solutions
- **Error:** `browserType.connectOverCDP: connect ECONNREFUSED 127.0.0.1:9222`
  - Solution: Follow the steps in `install-remote-chrome-browser.md` to launch Chrome in remote debugging mode and verify it is running.
- **Playwright not found or missing dependencies**
  - Solution: See `install-mcp-playwright.md` for installation and dependency instructions.

### 3. Verify Browser Status
- Check if Chrome is running in remote debugging mode:
  ```bash
  curl http://127.0.0.1:9222/json/version
  ```
  - If you get a JSON response, the browser is running.
  - If you get a connection error, Chrome is not running or not listening on the correct port.
- Check for open ports and running processes:
  ```bash
  ps aux | grep chrome
  lsof -i :9222
  ```

### 4. Escalate to Subagents When Needed
- If you cannot resolve the issue after following the above steps, escalate to Roo Tech Support or another appropriate subagent.
- Use `/new_task` to create a focused troubleshooting task if the problem persists.

### 5. Task Management
- Break down complex troubleshooting into smaller subtasks.
- Document all steps and solutions in the project memory system as per `memory-system-rules.md`.

