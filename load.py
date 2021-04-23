import os

def load(dir_path):
	try:
		os.chdir(dir_path) # Nge-set Working Directory
		
		os.rename("gadget.csv", "gadget_temp.csv")
		os.rename("consumable.csv", "consumable_temp.csv")
		os.rename("consumable_history.csv", "consumable_history_temp")
		os.rename("gadget_return_history.csv", "gadget_return_history_temp.csv")
		os.rename("gadget_borrow_history.csv", "gadget_borrow_history_temp.csv")
		
		g = convDataToString(header, datas)
		f = open("gadget.csv", "w+")
		f.write(g)
		
		
		print('Selamat datang di "Kantong Ajaib!"') 
		return True
	except OSError: # Foldernya gaada
		print("Folder tidak ditemukan!")
		return False
