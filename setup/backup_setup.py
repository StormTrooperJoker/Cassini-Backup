
import os
from setup.backup_parse import Backup_Parser

backup_handler = Backup_Parser()

class Setup_Dir:
    def __init__(self):


        self.BackupConf = backup_handler

    def get_directories(self):
        pass

if __name__ == "__main__":
    backup_setup = Setup_Dir()
    backup_setup.get_directories()
