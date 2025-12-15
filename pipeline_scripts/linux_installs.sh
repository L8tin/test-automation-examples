#! /bin/bash
# Created by Leighton J Cook 12/15/2025

echo    "OS Version"
cat /etc/os-release

# Could run installs here
pip install -r requirements.txt
pip list

sudo apt-get update
sudo apt-get install -y chromium-chromedriver

# Check versions
chromium-browser --version
chromedriver --version
