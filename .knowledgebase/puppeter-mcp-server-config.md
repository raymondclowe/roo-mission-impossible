# Install and Configure Puppeteer MCP Server

This guide provides detailed instructions for setting up and configuring the Puppeteer MCP (Model Context Protocol) server as an alternative to Playwright or browser-based automation. Puppeteer is a Node.js library that provides a high-level API to control Chrome or Chromium over the DevTools Protocol.

## When to Use Puppeteer MCP Server

- If you encounter compatibility issues with Playwright or browser-based automation.
- If you need a lightweight and flexible alternative for browser automation tasks.
- If your project requires specific Puppeteer features or configurations.

## Prerequisites

1. **Node.js and npm Installed**
   Ensure you have Node.js (v16 or higher) and npm installed on your system. Verify installation with:
   ```bash
   node -v
   npm -v
   ```

2. **Chrome or Chromium Installed**
   Puppeteer requires Chrome or Chromium. Install the latest version if not already installed:
   ```bash
   sudo apt-get install -y chromium-browser
   ```

## Installation Steps

### 1. Install Puppeteer MCP Globally
Install the Puppeteer MCP package globally using npm:
```bash
sudo npm install -g @modelcontextprotocol/server-puppeteer
```

### 2. Configure Puppeteer MCP Server
Create or update the `.roo/mcp.json` file in your project workspace with the following configuration:
```json
{
  "mcpServers": {
    "puppeteer": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-puppeteer"
      ],
      "env": {
        "PUPPETEER_LAUNCH_OPTIONS": "{\"executablePath\": \"/usr/bin/chromium-browser\", \"args\": [\"--no-sandbox\", \"--disable-setuid-sandbox\"]}",
        "DISPLAY": ":0"
      },
      "disabled": false,
      "alwaysAllow": [
        "browser_navigate",
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

### 3. Verify Puppeteer Installation
Run the following command to verify Puppeteer is installed and working:
```bash
npx puppeteer --version
```

## Testing the Setup

1. **Start the Puppeteer MCP Server**
   The server will start automatically when a tool requests to use it. Alternatively, you can start it manually:
   ```bash
   npx @modelcontextprotocol/server-puppeteer
   ```

2. **Test Browser Navigation**
   Use the `browser_navigate` command to open a website:
   ```json
   {
     "tool": "browser_navigate",
     "args": { "url": "https://example.com" }
   }
   ```

## Troubleshooting

### Common Issues

1. **Permission Errors (`EACCES`)**
   Use `sudo` for global installations or ensure proper permissions for the npm directory.

2. **Missing Dependencies**
   Install required system libraries:
   ```bash
   sudo apt-get install -y libx11-xcb1 libxcomposite1 libxcursor1 libxdamage1 libxi6 libxtst6 libnss3 libxrandr2 libasound2 libpangocairo-1.0-0 libatk1.0-0 libcups2 libdbus-1-3 libgdk-pixbuf2.0-0 libxss1 libglib2.0-0
   ```

3. **Browser Launch Failures**
   Ensure the `PUPPETEER_LAUNCH_OPTIONS` in `.roo/mcp.json` points to the correct Chrome/Chromium executable path.

4. **Environment Variable Issues**
   Set the `DISPLAY` environment variable to `:0` for headless environments.

## Additional Resources

- [Puppeteer Documentation](https://pptr.dev/)
- [Model Context Protocol GitHub](https://github.com/modelcontextprotocol/servers)

By following this guide, you can successfully set up and use Puppeteer MCP Server for browser automation tasks.
