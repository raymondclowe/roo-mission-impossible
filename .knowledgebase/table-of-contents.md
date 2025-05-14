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

## Web Browsing Tools

There are several ways to browse the web in this project:

- **Built-in "browser" tool**: This is the default tool for simple web browsing tasks. It is integrated and requires no additional setup.
- **Playwright MCP**: Use the Playwright MCP server for advanced browser automation, scraping, or when you need to interact with dynamic web pages. See `install-mcp-playwright.md` for setup and troubleshooting.
- **Puppeteer MCP**: Puppeteer MCP is an alternative to Playwright for browser automation. See `puppeter-mcp-server-config.md` for configuration and usage details.
- **Remote Chrome**: For cases where you need to connect to a remote Chrome browser (e.g., for debugging or when local browser access is restricted), see `install-remote-chrome-browser.md` for setup instructions.

**How to choose:**
- Use the built-in browser for simple tasks and quick lookups.
- Use Playwright or Puppeteer MCP for automation, scraping, or when you need to control the browser programmatically.
- Use Remote Chrome if you need to connect to a browser running on another machine or in a restricted environment.

**Learn more:**
- Each tool has a dedicated guide in this knowledgebase (see Installation Guides above).
- For Playwright: `install-mcp-playwright.md`
- For Puppeteer: `puppeter-mcp-server-config.md`
- For Remote Chrome: `install-remote-chrome-browser.md`
- For general prompting and configuration: `prompting-guide.md`

