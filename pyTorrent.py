from modules.downloader_util import Torrent_Downloader
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="pyTorrent args parser")
    parser.add_argument('-f', dest='magnet_list_file', type=str)
    parser.add_argument('-d', dest='download_dir', type=str)
    args = parser.parse_args()

    TD = Torrent_Downloader(
        args.magnet_list_file,
        args.download_dir)

    TD.start_download()

if __name__ == '__main__':
    main()