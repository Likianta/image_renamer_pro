from threading import Thread

from lk_utils.toolbox import *


def main(idir):
    """
    workflow:
        user selects files, then press custom key
            python script actions
                ctrl + c (copy selected files into clipboard)
                get clipboard data (<list filepaths>)
                renaming
                over
                
    """
    subdirs = file_sniffer.findall_subdirs(idir)
    subdirs.insert(0, idir)
    
    image_filetypes = (
        '.bmp', 'gif', '.jpeg', '.jpg', '.png', 'webp'
    )
    
    for d in subdirs:
        files = file_sniffer.find_files(d, image_filetypes)
        for f in files:
            pass


def detect_name_pattern(filename):
    pass


class Watcher(Thread):
    """
    REF: https://stackoverflow.com/questions/14685999/trigger-an-event-when
    -clipboard-content-changes
    """
    
    def __init__(self, trigger, call_func):
        super().__init__()
        self.trigger = trigger
        self.call_func = call_func
    
    def run(self) -> None:
        pass



if __name__ == "__main__":
    main()
