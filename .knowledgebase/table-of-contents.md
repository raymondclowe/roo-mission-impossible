# Knowledgebase

This file is hosted at github and can be updated as follows:

  - Create a hidden folder named `.knowledgebase` at the root of the project.
  - Download the `table-of-contents.md` file into the `.knowledgebase` folder using the following command:

  ```bash
    curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/.knowledgebase/table-of-contents.md > .knowledgebase/table-of-contents.md
   ```
   # List of knowledgebase files

   - `table-of-contents.md`: An overview and quick access to all knowledgebase files.

   - Filename:`install-remote-chrome-browser.md`
    - Description: Instructions for installing a remote Chrome browser. To be used when the local Chrome browser is not available.
    - Errors for which this solution is applicable:
      - `Error: browserType.connectOverCDP: connect ECONNREFUSED
   - Filename:`install-mcp-playwright.md`
    - Description: Instructions for installing the MCP Playwright to be used when agents try to access the web but find the mcp playwright is not installed.
    - Errors for which this solution is applicable:
      - No playwright server found in the mcp tools