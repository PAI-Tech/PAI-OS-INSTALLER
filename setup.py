
"""
This script installs PAI O/S folders

Author: Eran Caballero
Since : 9/25/2019
Copyright PAI-TECH 2022, all right reserved

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version
3 of the License, or (at your option) any later version.
"""


from PAIOS import PAIOSInstaller 

#Local varibles
vp_folders=["Apps","Backup","Bots","Cache","Config","Logs","Systems"]
apps_folder = []
backup_folder = ["PAI-DDB"]
bots_folder = []
cache_folder = []
config_folder = []
logs_folder = ["PAI-Monitor"]
system_folder = ["Scripts"]

poi = PAIOSInstaller()

print("Starting PAI-O/S folders installation")
poi.create_pai_sub_folders(vp_folders)
poi.create_sub_folders_for_base(apps_folder,poi.pai_folder + "Apps")
poi.create_sub_folders_for_base(backup_folder,poi.pai_folder + "Backup")
poi.create_sub_folders_for_base(bots_folder,poi.pai_folder + "Bots")
poi.create_sub_folders_for_base(cache_folder,poi.pai_folder + "Cache")
poi.create_sub_folders_for_base(config_folder,poi.pai_folder + "Config")
poi.create_sub_folders_for_base(logs_folder,poi.pai_folder + "Logs")
poi.create_sub_folders_for_base(system_folder,poi.pai_folder + "System")
print("PAI-O/S folders installation done")