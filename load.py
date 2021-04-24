import os

def copas(file_lama, file_baru):
	# meng-copy file 
	g = open(file_lama, "r")
	f = open(file_baru, "w+")
	f.write(g.read())
	g.close()
	f.close()

def setupFile():
	# Membuat file temp untuk menyimpan file dengan data awal, Program akan bekerja pada file asli
	# Dalam kasus perubahan tidak di-save, file temp menggantikan file asli (yang mungkin telah dimodif) kembali
	copas("gadget.csv", "gadget_temp.csv")
	copas("consumable.csv", "consumable_temp.csv")
	copas("consumable_history", "consumable_history_temp")
	copas("gadget_return_history.csv", "gadget_return_history_temp.csv")
	copas("gadget_borrow_history.csv", "gadget_borrow_history_temp.csv")	
	
def load(dir_path):
	try:
		os.chdir(dir_path) # Nge-set Current Working Directory (CWD tidak akan berubah lagi sampai program di reboot)
		setupFile()
		print('Selamat datang di "Kantong Ajaib!"') 
		return True
	except OSError: # Foldernya gaada
		print("Folder tidak ditemukan!")
		return False
