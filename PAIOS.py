# PAI-Bot Python version
# PAI-Bot instance in Python language
# Created by Tamir Fridman on 6 January 2022
# Copyright PAI-Tech 2022


import os


class PAIOSInstaller:

    def __init__(self,pai_folder):
        print("PAI O/S Installer starting")
        self.pai_folder = pai_folder
        self.make_dir(self.pai_folder)
            
        
    
    def __del__(self):
        print("PAI O/S Installer ended")

    def make_dir(self,folder):
        if not os.path.exists(folder):
            os.mkdir(folder)
            print("creating folder " + folder)
        else:
            print("folder " + folder + " already exists, skipping")

    def create_pai_sub_folders(self,folders_arr):
        for folder in folders_arr:
            #checkin for uppercase folder name, if lower fix
            if folder[0:1].islower():
                folder = folder[0:1].upper() + folder[1:]
            full_path = self.pai_folder + folder
            self.make_dir(full_path)
