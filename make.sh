#!/bin/bash
pyinstaller --onefile pyTorrent.py -y
sudo cp dist/pyTorrent /usr/bin
sudo chmod +x /usr/bin/pyTorrent