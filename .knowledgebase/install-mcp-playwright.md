# Install and Configure Playwright MCP Servers (Local & Remote)

This guide details how to install and configure the Playwright MCP (Model Context Protocol) server, enabling interaction with web browsers. It covers two primary connection methods:

1. **Local/Direct:** The MCP server manages its own browser instance directly (typically headless). Identified as `local-microsoft-playwright`.
2. **Remote/CDP:** The MCP server connects to an *existing* Chrome/Chromium browser instance via the Chrome DevTools Protocol (CDP). Identified as `remote-microsoft-playwright`.

## OS Compatibility & Recommendation

The reliability and recommended setup depend on your Linux distribution:

* **Ubuntu:** Both the Local/Direct and Remote/CDP methods are confirmed to work reliably.
  * **Recommendation:** Configure **both** servers.
  * **Rationale:**
    * The `local-microsoft-playwright` server is ideal for standard headless browser automation tasks.
    * The `remote-microsoft-playwright` server allows connecting to a potentially headed browser instance, which is useful for observing automation visually or for interactive debugging sessions.

* **Other Linux Distributions (e.g., Linux Mint):** Based on testing, only the **Remote/CDP** method (`remote-microsoft-playwright`) is confirmed to be consistently reliable. Compatibility issues have been observed with the Local/Direct method on some non-Ubuntu distributions.
  * **Recommendation:** Configure **only** the `remote-microsoft-playwright` server.

## Common Prerequisites

These steps are required regardless of which server type(s) you configure.

### 1. Check/Install npm & npx

Ensure `npm` (Node Package Manager) and `npx` (Node Package Execute) are installed. `npx` is typically included with `npm`.

```bash
which npm
which npx
```

If either command is not found, install `npm` using your distribution's package manager. For Debian/Ubuntu-based systems:

```bash
sudo apt-get update && sudo apt-get install -y npm
```

For other distributions, use the appropriate command (e.g., `dnf install npm`, `pacman -S npm`).

### 2. Install Playwright MCP Globally

Install the `@playwright/mcp` package globally using `npm`. You'll likely need `sudo` or root privileges:

```bash
sudo npm install -y -g @playwright/mcp
```

### 3. Install Playwright Browsers

Use `npx` to run the Playwright install command, which downloads the necessary browser binaries (Chromium, Firefox, WebKit) managed by Playwright:

```bash
npx -y playwright install
```

### 4. Install System Dependencies

Playwright requires certain system libraries to run the browsers correctly. Install these using the `install-deps` command (requires `sudo` or root privileges):

```bash
sudo npx -y playwright install-deps
```

## Configuration (`.roo/mcp.json`)

Configure the MCP server(s) in the `.roo/mcp.json` file within your project workspace.

### Full Example Configuration (Both Servers)

This example shows the configuration for *both* the local and remote servers.

```json
{
  "mcpServers": {
    "local-microsoft-playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ],
      "disabled": false,
      "alwaysAllow": [
        "browser_navigate",
        "browser_type",
        "browser_click",
        "browser_snapshot",
        "browser_network_requests",
        "browser_press_key"
      ]
    },
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
        "browser_click",
        "browser_snapshot",
        "browser_network_requests",
        "browser_press_key"
      ]
    }
  }
}
```

*(Note: The `"alwaysAllow"` list can be customized based on the specific browser actions you want to permit without explicit user confirmation each time.)*

### Instructions based on OS:

* **Ubuntu Users:** Include **both** the `local-microsoft-playwright` and `remote-microsoft-playwright` configurations in your `mcpServers` object as shown above.
* **Other Linux Distributions:** Include **only** the `remote-microsoft-playwright` configuration in your `mcpServers` object.

## Remote Server Prerequisite (Remote/CDP Method Only)

If you are configuring the `remote-microsoft-playwright` server (mandatory for non-Ubuntu, optional for Ubuntu), you **must** start a Chrome/Chromium browser instance with remote debugging enabled *before* attempting to use this MCP server.

### 1. Start Remote Chrome/Chromium

Follow the instructions in `.knowledgebase/install-remote-chrome-browser.md` to launch the browser correctly. The typical command enables debugging on port 9222.

### 2. Verify Connection

Before using the remote server, verify that the browser is running and the debugging port is accessible:

```bash
curl http://127.0.0.1:9222/json/version
```

* A successful connection will return JSON data about the browser.
* If you get `curl: (7) Failed to connect to 127.0.0.1 port 9222: Connection refused`, the browser is not running or not listening correctly. Revisit the instructions in `.knowledgebase/install-remote-chrome-browser.md`.
* If `curl` is not installed, install it (e.g., `sudo apt install -y curl`).

## Starting the MCP Servers

You **do not** need to start the Playwright MCP servers manually. Based on the configurations in `.roo/mcp.json`, the required server process (`local-microsoft-playwright` and/or `remote-microsoft-playwright`) will be started automatically by the system the first time a tool requests to use it.

## Testing the Setup

Test the configured server(s) by asking your AI assistant (like Roo) to perform a simple browser action.

### Testing Local Server (`local-microsoft-playwright`) - Ubuntu Only

If you configured the local server on Ubuntu, use this example:

```xml
<use_mcp_tool>
<server_name>local-microsoft-playwright</server_name>
<tool_name>browser_navigate</tool_name>
<arguments>
{
  "url": "https://example.com"
}
</arguments>
</use_mcp_tool>
```

### Testing Remote Server (`remote-microsoft-playwright`) - Ubuntu & Other Linux

Ensure the prerequisite remote browser is running (see "Remote Server Prerequisite" section above). Then use this example:

```xml
<use_mcp_tool>
<server_name>remote-microsoft-playwright</server_name>
<tool_name>browser_navigate</tool_name>
<arguments>
{
  "url": "https://example.com"
}
</arguments>
</use_mcp_tool>
```

If the navigation is successful, the setup is complete.

## Troubleshooting

### Common Issues for Both Server Types

* **Permission Errors (`EACCES`) during `npm install -g`**: Use `sudo` as shown in the "Install Playwright MCP Globally" section.
* **`playwright: command not found`**: Use `npx playwright ...` for commands like `install` and `install-deps` as shown in the installation steps.
* **Missing Dependencies Warning**: Run the command from the "Install System Dependencies" section (`sudo npx -y playwright install-deps`).

### Remote Server (`remote-microsoft-playwright`) Specific Issues

* **MCP Server Connection Error (`No connection found for server...`)**:
  * Verify the remote Chrome browser is running and listening on the correct port (usually 9222). You can check this using `curl`:
    ```bash
    curl http://127.0.0.1:9222/json/version
    ```
  * If `curl` fails to connect (e.g., `Connection refused`), the remote Chrome browser is not running or accessible on that port. Start it following the instructions in `.knowledgebase/install-remote-chrome-browser.md`.
  * If `curl` connects successfully (it might show HTML or a JSON response about the browser), the issue might be with the MCP server itself. Check for any error messages in the terminal.

  * **chrome-stable not installed** 
    * If you see an error message indicating that `chrome-stable` is not installed, ensure you have the correct version of Chrome/Chromium installed. You can install it using your distribution's package manager (e.g., `sudo apt install -y chromium-browser` for Ubuntu).
    * If you are using a different browser, ensure that the MCP server is configured to connect to that specific browser instance.

### Local Server (`local-microsoft-playwright`) Specific Issues

* **Browser Launch Failures**: On non-Ubuntu distributions, the local server may fail to launch browsers correctly. This is why we recommend using the remote server method for these systems.
* **Headless Browser Issues**: If you encounter problems with the headless browser, try reinstalling the Playwright browsers with `npx playwright install --force`.
