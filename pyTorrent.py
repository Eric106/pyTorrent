from modules.downloader_util import Torrent_Downloader


TD = Torrent_Downloader(
    magnet_list_file='to_download.txt',
    download_dir='/mnt/d/Servers/Movies/Oscars2023/')

TD.start_download()