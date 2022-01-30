from PAIOS import PAIOSInstaller 
vp = "/var/PAI/"
vp_folders=["Apps","Backup","Bots","Cache","Config","Logs","Systems"]
apps_folder = ["Dusty"]
backup_folder = ["PAI-DDB"]
bots_folder = []
cache_folder = ["PAI-BOT"]
config_folder = []
logs_folder = ["PAI-Monitor"]
system_folder = ["Scripts"]

poi = PAIOSInstaller(vp)


poi.create_pai_sub_folders(vp_folders)
poi.create_sub_folders_for_base(apps_folder,vp + "Apps")
poi.create_sub_folders_for_base(backup_folder,vp + "Backup")
poi.create_sub_folders_for_base(bots_folder,vp + "Bots")
poi.create_sub_folders_for_base(cache_folder,vp + "Cache")
poi.create_sub_folders_for_base(config_folder,vp + "Config")
poi.create_sub_folders_for_base(logs_folder,vp + "Logs")
poi.create_sub_folders_for_base(system_folder,vp + "System")
#poi.make_dir(vp + "Bots/netbot")

"Event-Man-Bot","NET-BOT","Master-Bot","Maestro-Docker","PAI-Prompt","PAI-BU","PAI-Monitor","PAI-Restore"