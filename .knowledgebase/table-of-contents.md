# Knowledgebase

This file is hosted at github and can be updated as follows:

  - Create a hidden folder named `.knowledgebase` at the root of the project.
  - Download the `table-of-contents.md` file into the `.knowledgebase` folder using the following command:

  ```bash
    curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/.knowledgebase/table-of-contents.md > .knowledgebase/table-of-contents.md
   ```

# List of Knowledgebase Files

## General

- `table-of-contents.md`: An overview and quick access to all knowledgebase files.

## Installation Guides

- `install-remote-chrome-browser.md`: Use this guide if you encounter the error `browserType.connectOverCDP: connect ECONNREFUSED 127.0.0.1:9222`. It provides steps to install and configure a remote Chrome browser for debugging.
- `install-mcp-playwright.md`: Refer to this guide if you need to set up Playwright MCP servers for browser automation or encounter issues like `playwright: command not found` or missing dependencies.

## Role-Specific Details

### Astro Developer
- `astro-markdown-setup-guide.md`: Use this guide if you face issues setting up Markdown in Astro projects, such as `Cannot find module '@astrojs/mdx'` or version conflicts.
- `astro-mdx-integration-guide.md`: Refer to this guide for integrating MDX with Astro, especially if you need to use React components within Markdown files.
- `astro-research-report.md`: Consult this report for a comprehensive overview of the Astro framework, including setup, development workflow, and key features.

### Data Analyst
- `data-analysis-accessing-csv-files-with-sql.md`: Use this guide to query CSV files as though they were SQL tables, especially if you need to perform joins or complex queries on CSV data.

## Prompting and Configuration

- `prompting-guide.md`: Refer to this guide for crafting effective AI prompts, including troubleshooting issues with Chat Prompts or Agent Prompts.
- `puppeter-mcp-server-config.md`: Use this guide if you need to configure Puppeteer MCP servers as an alternative to Playwright or encounter issues with Puppeteer setup.

