from modules.downloader_util import Torrent_Downloader
from argparse import ArgumentParser, BooleanOptionalAction

def main():
    parser = ArgumentParser(description="pyTorrent")
    parser.add_argument('-f', dest='magnet_list_file', type=str)
    parser.add_argument('-d', dest='download_dir', type=str)
    parser.add_argument('-nUL', dest='no_up_limit', action=BooleanOptionalAction)
    args = parser.parse_args()


    TD = Torrent_Downloader(
        magnet_list_file = args.magnet_list_file,
        download_dir = args.download_dir,
        up_limit = None if args.no_up_limit else 1000
    )

    TD.start_download()
    TD.stop_download()

if __name__ == '__main__':
    main()