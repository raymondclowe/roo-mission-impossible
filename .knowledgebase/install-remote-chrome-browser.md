
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
- If you are using a remote Chrome browser, start it with the following command. Make it run in the background.:

```bash

/usr/bin/google-chrome-stable  --remote-debugging-port=9222 
--user-data-dir=/tmp/chrome &
```

