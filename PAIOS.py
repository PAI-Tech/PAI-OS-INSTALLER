# PAI-Bot Python version
# PAI-Bot instance in Python language
# Created by Tamir Fridman on 6 January 2022
# Copyright PAI-Tech 2022


import os


class PAIOSInstaller:

    def __init__(self):
        print("PAI O/S Installer starting for O/S " + os.name)
        self.pai_folder = "/var/PAI/"
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
        self.create_sub_folders_for_base(folders_arr,self.pai_folder)
    
    def create_sub_folders_for_base(self,folders_arr,base_folder):
        if not base_folder.endswith(os.path.sep):
            base_folder = base_folder + os.path.sep
        for folder in folders_arr:
            #checkin for uppercase folder name, if lower fix
            if folder[0:1].islower():
                folder = folder[0:1].upper() + folder[1:]
            full_path = base_folder + folder
            self.make_dir(full_path)

