from PAIOS import PAIOSInstaller 
vp = "/var/PAI/"
vp_folders=["Bots","Apps","Logs","backup"]


poi = PAIOSInstaller(vp)


poi.create_pai_sub_folders(vp_folders)
