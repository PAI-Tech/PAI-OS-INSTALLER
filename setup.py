from PAIOS import PAIOSInstaller 
vp_folders=["Apps","Backup","Bots","Cache","Config","Logs","Systems"]
apps_folder = []
backup_folder = ["PAI-DDB"]
bots_folder = []
cache_folder = []
config_folder = []
logs_folder = ["PAI-Monitor"]
system_folder = ["Scripts"]

poi = PAIOSInstaller()


poi.create_pai_sub_folders(vp_folders)
poi.create_sub_folders_for_base(apps_folder,poi.pai_folder + "Apps")
poi.create_sub_folders_for_base(backup_folder,poi.pai_folder + "Backup")
poi.create_sub_folders_for_base(bots_folder,poi.pai_folder + "Bots")
poi.create_sub_folders_for_base(cache_folder,poi.pai_folder + "Cache")
poi.create_sub_folders_for_base(config_folder,poi.pai_folder + "Config")
poi.create_sub_folders_for_base(logs_folder,poi.pai_folder + "Logs")
poi.create_sub_folders_for_base(system_folder,poi.pai_folder + "System")