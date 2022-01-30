from PAIOS import PAIOSInstaller 

vp_folders=["Bots","Apps","Logs","backup"]
bots_folder = ["Netbot","MasterBot"]

poi = PAIOSInstaller()


poi.create_pai_sub_folders(vp_folders)
poi.create_sub_folders_for_base(bots_folder,poi.pai_folder + "Bots")

