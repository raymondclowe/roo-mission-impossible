Check the file .roo/mcp.json for a playwright configuration. Update or add as necessary to have these settings:

```json
{
  "mcpServers": {    
    "remote-microsoft-playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest",
        "--cdp-endpoint",
        "http://127.0.0.1:9222"
      ],
      "disabled": false,
      "alwaysAllow": [
        "browser_navigate",
        "browser_type",
        "navigate",
        "browser_click",
        "browser_snapshot",
        "browser_network_requests",
        "browser_scroll_down",
        "browser_press_key"
      ]
    }  
}
}
```

Make sure npm and npx are installed.

Check by going:

```bash
which npm
```
```bash
which npx
```

If they are not installed, install them using the following command:

```bash
sudo apt-get install -y npm
```

Then, install the MCP Playwright using the following command:

```bash
npm install -g @playwright/mcp
```

Use the playwright install command to install the browsers:

```bash
playwright install
```

Test the MCP Playwright setup by using the `browser_navigate` command in the remote-microsoft-playwright mcp server to open example.com:
  ```json
  {
    "tool": "browser_navigate",
    "args": { "url": "https://example.com" }
  }
  ```



If you see no errors then the MCP Playwright is installed correctly.

With the playwright mcp server installed and the remote chrome browser running as per the instructions in `install-remote-chrome-browser.md`, you can now run use the mcp tools to access the web. Try opening example.com using the `use_mcp_tool` to run the `remote-microsoft-playwright` server to use the `browser_navigate` to open example.com

