# Web Browsing in Roo Mission Impossible

There are several ways to browse the web in this project:

- **Built-in "browser" tool**: The default tool for simple web browsing tasks. Integrated and requires no additional setup.
- **Playwright MCP**: Use for advanced browser automation, scraping, or interacting with dynamic web pages. See `install-mcp-playwright.md` for setup and troubleshooting.
- **Puppeteer MCP**: An alternative to Playwright for browser automation. See `puppeter-mcp-server-config.md` for configuration and usage details.
- **Remote Chrome**: For connecting to a remote Chrome browser (e.g., for debugging or when local browser access is restricted). See `install-remote-chrome-browser.md` for setup instructions.

## How to Choose
- Use the built-in browser for simple tasks and quick lookups.
- Use Playwright or Puppeteer MCP for automation, scraping, or when you need to control the browser programmatically.
- Use Remote Chrome if you need to connect to a browser running on another machine or in a restricted environment. THIS IS THE RECOMMENDED WAY TO LET THE USER SEE WHAT YOU ARE DOING WITH THE BROWSER. IF YOU HAVE PROBLEMS WITH 'ARE YOU A HUMAN' CAPTCHA, THEN USE THIS METHOD.
- If you encounter issues with Playwright, consider switching to Puppeteer MCP as an alternative.
- If you encounter issues with both Playwright and Puppeteer, consider using Remote Chrome as a fallback option.

## Learn More
- Each tool has a dedicated guide in this knowledgebase (see Installation Guides in the table of contents).
- For Playwright: `install-mcp-playwright.md`
- For Puppeteer: `puppeter-mcp-server-config.md`
- For Remote Chrome: `install-remote-chrome-browser.md`

