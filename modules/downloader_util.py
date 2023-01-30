import sys
from os import system
from time import sleep
from subprocess import check_output, CalledProcessError
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Torrent_Downloader():

    magnet_list_file: str = field(init=True)
    download_dir: str = field(init=True)
    magnet_list: list[str] = field(init=False)

    def __post_init__(self):
        try:
            is_transmission_cli = check_output(['which','transmission-cli']) == "/usr/bin/transmission-cli"
            is_tmux = check_output(['which','tmux']) == '/usr/bin/tmux'
            if is_transmission_cli and is_tmux:
                print('transmission-cli and tmux Installed...')
        except CalledProcessError as e:
            print(f"{e} \nPlease install dependencies with: sudo apt install transmission-cli tmux")
            sys.exit()

        magnet_list_file = open(self.magnet_list_file, 'r')
        object.__setattr__(self,'magnet_list',
            [line.rstrip() for line in magnet_list_file.readlines()]
        )
        magnet_list_file.close()
    
    def start_download(self):
        tmux_session_name = 'pyTorrent'
        system(f"tmux new-session -d -s {tmux_session_name}")
        for magnet in self.magnet_list:
            print(magnet,'\n')
            download_command = f'transmission-cli \\"{magnet}\\" -w {self.download_dir}'
            system(f"tmux send-keys -t {tmux_session_name}.0 \"{download_command}\" ENTER")
            download_complete : bool = False
            verify_command = ['tmux', 'capture-pane', '-p', '-t' ,tmux_session_name]
            stop_command = f'tmux send-keys -t {tmux_session_name}.0 C-c'
            while not download_complete:
                tmux_content = check_output(verify_command).decode()
                tmux_content = '\n'.join(tmux_content.split('\n')[-5:])
                download_complete = 'seeding' in tmux_content.lower()
                sleep(5)
                if download_complete:
                    system(stop_command)
                    sleep(10)
