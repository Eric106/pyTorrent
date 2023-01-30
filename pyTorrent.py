from modules.downloader_util import Torrent_Downloader


TD = Torrent_Downloader('to_download.txt','/mnt/d/Servers/Movies/Oscars2023/')

TD.start_download()