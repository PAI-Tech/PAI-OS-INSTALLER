from PAIOS import PAIOSInstaller 
vp = "/var/PAI/"
vp_folders=["Bots","Apps","Logs","backup"]
bots_folder = ["Netbot","MasterBot"]

poi = PAIOSInstaller(vp)


poi.create_pai_sub_folders(vp_folders)
poi.create_sub_folders_for_base(bots_folder,vp + "Bots")
#poi.make_dir(vp + "Bots/netbot")
