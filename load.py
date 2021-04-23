import os

def copas(file_lama, file_baru):
	g = open(file_lama, "r")
	f = open(file_baru, "w+")
	f.write(g.read())
	g.close()
	f.close()

def load(dir_path):
	try:
		os.chdir(dir_path) # Nge-set Current Working Directory
		
		# dibuat file baru untuk dimodif dalam program
		# file temp untuk menyimpan file ori/lama, dalam kasus perubahan tidak di-save, file temp menggantikan file baru kembali
		copas("gadget.csv", "gadget_temp.csv")
		copas("consumable.csv", "consumable_temp.csv")
		copas("consumable_history", "consumable_history_temp")
		copas("gadget_return_history.csv", "gadget_return_history_temp.csv")
		copas("gadget_borrow_history.csv", "gadget_borrow_history_temp.csv")	
		
		print('Selamat datang di "Kantong Ajaib!"') 
		return True
	except OSError: # Foldernya gaada
		print("Folder tidak ditemukan!")
		return False
