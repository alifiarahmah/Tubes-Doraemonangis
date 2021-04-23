import os

def copas(file_lama, file_baru):
	g = open(file_lama, "r")
	f = open(file_baru, "w+")
	f.write(g.read())
	g.close()
	f.close()

def load(dir_path):
	try:
		os.chdir(dir_path) # Nge-set Working Directory
		
		os.rename("gadget.csv", "gadget_temp.csv")
		os.rename("consumable.csv", "consumable_temp.csv")
		os.rename("consumable_history.csv", "consumable_history_temp")
		os.rename("gadget_return_history.csv", "gadget_return_history_temp.csv")
		os.rename("gadget_borrow_history.csv", "gadget_borrow_history_temp.csv")
		
		copas("gadget_temp.csv", "gadget.csv")
		copas("consumable_temp.csv", "consumable.csv")
		copas("consumable_history_temp", "consumable_history")
		copas("gadget_return_history_temp.csv", "gadget_return_history.csv")
		copas("gadget_borrow_history_temp.csv", "gadget_borrow_history.csv")
		
		
		print('Selamat datang di "Kantong Ajaib!"') 
		return True
	except OSError: # Foldernya gaada
		print("Folder tidak ditemukan!")
		return False
