import os
from csv_stuffs import getListCSV

def copas(file_lama, file_baru):
	# membuat file baru dengan isi yang sama dengan file lama (khusus csv)
	g = open(file_lama, "r")
	f = open(file_baru, "w+")
	f.write(g.read())
	g.close()
	f.close()

def setupFile():
	# Membuat file temp untuk menyimpan file dengan data awal, Program akan bekerja pada file asli
	# Dalam kasus perubahan tidak di-save, file temp kembali menggantikan file asli (yang mungkin telah dimodif) 
	ListCSV = getListCSV("no_temp")
	for i in range(len(ListCSV)):
		copas(ListCSV[i], "temp_" + ListCSV[i]) 
	
def load(folder_name):
	if (os.path.exists(folder_name)): # foldernya ada
		os.chdir(folder_name) # Nge-set Current Working Directory (CWD tidak akan berubah lagi sampai program di reboot)
		setupFile() # menyiapkan file
		print('Selamat datang di "Kantong Ajaib!"') 
		return True
	else: # Foldernya gaada
		print("Folder tidak ditemukan!")
		return False

def SetInventori(user_id):
	file = "inventori_" + str(user_id) + ".csv" 
	if not(os.path.exists(file)):
		f = open(file, 'w+')
		f.write('id_gadget,nama_gadget,jumlah_gadget,id_consumable,nama_consumable,jumlah_consumable')
		f.close()
	copas(path, "temp_" + path)
	
# https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
