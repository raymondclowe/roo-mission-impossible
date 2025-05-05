`puppeteer` is an alternative to `playwright` and `browser`.


```json
{
 "mcpServers": {
   "github.com/modelcontextprotocol/servers/tree/main/src/puppeteer": {
     "command": "npx",
     "args": [
       "-y",
       "@modelcontextprotocol/server-puppeteer"
     ],
     "env": {
       "PUPPETEER_LAUNCH_OPTIONS": "{\"executablePath\": \"/home/rcl/.cache/puppeteer/chrome/linux-131.0.6778.204/chrome-linux64/chrome\", \"args\": [\"--no-sandbox\", \"--disable-setuid-sandbox\"]}",
       "DISPLAY": ":0"
     },
     "disabled": false,
     "alwaysAllow": []
   }
 }
}

```

Adjust executable paths as necessary depending on installation.
