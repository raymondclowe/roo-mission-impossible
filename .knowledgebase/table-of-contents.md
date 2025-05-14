# Knowledgebase

This file is hosted at github and can be updated as follows:

  - Create a hidden folder named `.knowledgebase` at the root of the project.
  - Download the `table-of-contents.md` file into the `.knowledgebase` folder using the following command:

  ```bash
    curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/.knowledgebase/table-of-contents.md > .knowledgebase/table-of-contents.md
   ```

# Getting knowledgebase files

  - If you need to download a solution file then use the command `curl https://raw.githubusercontent.com/raymondlowe/roo-mission-impossible/refs/heads/main/.knowledgebase/<solution-file-name> > .knowledgebase/<solution-file-name>`.
  - When reading the knowledgebase pay attention to the error message of the problem you are trying to solve.
  - Look in the `Errors for which this solution is applicable` field in the table of contents, if that doesn't have it then just text search the whole knowledgebase for the error message.
  - Truncate the error message to just the key phrase when searching.

# List of Knowledgebase Files

## General

- `table-of-contents.md`: An overview and quick access to all knowledgebase files.
- `.roomodes-format.md`: Guidelines for editing the `.roomodes` file, including format, validation, and best practices. Refer to this before making any changes to agent modes or the `.roomodes` file. Note the file appears hidden and doesn't show up in `ls` commands unless you use `ls -la` to view hidden files.
- `readme.md`: General information about the knowledgebase and its purpose.

## Installation Guides

- `install-remote-chrome-browser.md`: Use this guide if you encounter the error `browserType.connectOverCDP: connect ECONNREFUSED 127.0.0.1:9222`. It provides steps to install and configure a remote Chrome browser for debugging. Chrome browser is one of the ways of browsing the web.
- `install-mcp-playwright.md`: Refer to this guide if you need to set up Playwright MCP servers for browser automation or encounter issues like `playwright: command not found` or missing dependencies. Playwright is another way of browsing the web.

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
- `.roomodes-format.md`: How to safely edit the .roomodes file (format, validation, and best practices)

## Web Browsing

- `web-browsing.md`: Overview of all available web browsing tools (built-in browser, Playwright MCP, Puppeteer MCP, Remote Chrome), when to use each, and where to find setup and troubleshooting guides. Refer to this file if you need to browse the web, automate browser tasks, or troubleshoot browser access issues.

- For general prompting and configuration: `prompting-guide.md`

