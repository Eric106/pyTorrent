# pyTorrent
Python and linux shell util to download torrents

## Setup 
Clone this repo 
```shell
git clone https://github.com/Eric106/pyTorrent
```
Install dependencies
```shell
sudo apt install transmission-cli tmux
```
(*OPTIONAL*) Install conda enviroment
```shell
conda create -n pyTorr python==3.9.* -y ; conda activate pyTorr
```

## Run
**NOTE:** You must run it with python>=3.9.*

You need to provide a `file.txt` with the magnet links (one per line), as follows
```txt
magnet:?xt=urn:btih:DED7E2789886BB......
magnet:?xt=urn:btih:F3DCDC3A1FC67B......
```
Then simply run the script using as parameters the `file.txt` and the download directory
```shell
python pyTorrent -f file.txt -d download_dir/
```
