# pyTorrent
Python and linux shell util to download lists of torrents

## Setup 
Clone this repo 
```shell
git clone https://github.com/Eric106/pyTorrent
```
Install dependencies
```shell
sudo apt install transmission-cli tmux
```
You may also want to add the [pyTorrent binary](./dist/) to your `/usr/bin/` directory. Use the [install.sh](./install.sh) scrip
```shell
sudo bash install.sh
```

## Run
You need to provide a `file.txt` with the magnet links (one per line), as follows
```txt
magnet:?xt=urn:btih:DED7E2789886BB......
magnet:?xt=urn:btih:F3DCDC3A1FC67B......
```
Then simply run the [pyTorrent binary](./dist/) using as parameters the `file.txt` and the download directory
```shell
pyTorrent -f file.txt -d download_dir/
```

## Make binary 
> (**OPTIONAL**) Install conda enviroment and compile binary
```shell
conda create -n pyTorr python==3.10.* -y ; conda activate pyTorr ; pip install -r requirements.txt
```
```shell
bash make.sh
```
This will create a fresh [binary](./dist/) for your distro at `dist/`

