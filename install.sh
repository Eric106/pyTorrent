#!/bin/bash

binary="dist/pyTorrent_$(arch)"

if [ -f $binary ]; then
    sudo cp $binary /usr/bin/pyTorrent
    echo "The file $binary has been copied to /usr/bin/pyTorrent"
else
    echo "The file $binary does not exist in the current directory"
fi
