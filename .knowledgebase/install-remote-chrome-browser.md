# error messages for which this is the solution

```
Error:
Error: browserType.connectOverCDP: connect ECONNREFUSED 127.0.0.1:9222
Call log:
  - <ws preparing> retrieving websocket url from http://127.0.0.1:9222
```

# Solution: Install Remote Chrome Browser
- Check that chrome is installed
```bash
which google-chrome
```
- Check that the version is 114 or higher
```bash
google-chrome --version
```
- If not installed, install the latest version of Chrome
```bash
sudo apt-get install -y wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get install -y ./google-chrome-stable_current_amd64.deb
```
- Launch the Chrome browser in remote debugging mode using the following command:
       ```bash
       /usr/bin/google-chrome-stable \
         --remote-debugging-port=9222 \
         --user-data-dir=/tmp/chrome \
         --no-first-run \
         --no-default-browser-check \
         --disable-popup-blocking \
         --disable-infobars \
         --disable-automation \
         --start-maximized &
       ```
- Verify the Chrome instance is running by executing:
  ```bash
  curl http://127.0.0.1:9222/json/version
  ```
  This should return a JSON object confirming the instance is active.

  - Check your list of MCP servers to see if remote-microsoft-playwright already exists, if not then install it by adding this to the mcp.json file in this folder:
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
    Append it to any existing mcpServers section in the `.roo/mcp.json` file. If the section does not exist, create it.
- Ensure the MCP Playwright configuration in `.roo/mcp.json` uses the following `--cdp-endpoint`:
  ```json
  "--cdp-endpoint": "http://127.0.0.1:9222"
  ```
- Test the MCP Playwright setup by using the `browser_navigate` command to open example.com:
  ```json
  {
    "tool": "browser_navigate",
    "args": { "url": "https://example.com" }
  }
  ```

