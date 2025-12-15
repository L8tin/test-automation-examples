#! /bin/bash
# Created by Leighton J Cook 12/15/2025
echo "pipeline_scripts Initialized"

echo    "[linux_installs.sh] - os-release version"
cat /etc/os-release

pip install -r requirements.txt
echo    "[linux_installs.sh] - pip list"
pip list

sudo apt-get update
sudo apt-get install -y chromium-chromedriver

# Check versions
chromium-browser --version
chromedriver --version

echo "[linux_installs.sh] - pipeline_scripts Completed"
