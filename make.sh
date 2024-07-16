#!/bin/bash

pyinstaller --onefile pyTorrent.py -y
mv "dist/pyTorrent" "dist/pyTorrent_$(arch)"
