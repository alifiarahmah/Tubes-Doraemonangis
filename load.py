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
	# Membuat file temp untuk menyimpan file dengan data awal (temp_namafile.csv), Program akan bekerja pada file dengan nama asli (default)
	# Ketika perubahan file disave, file default akan tetap ada, file temp akan dihapus
	# Dalam kasus perubahan tidak di-save, file temp menggantikan kembali file default (yang mungkin telah diubah sebelumnya) 
	ListCSV = getListCSV("no_temp") # List semua file csv non temp_
	for i in range(len(ListCSV)):
		copas(ListCSV[i], "temp_" + ListCSV[i]) # dibuat duplikatnya (temp) satu per satu 
	
def load(folder_name):
	if (os.path.exists(folder_name)): # foldernya ada
		os.chdir(folder_name) # Nge-set Current Working Directory (CWD tidak akan berubah lagi sampai program di reboot)
		setupFile() # menyiapkan file
		print('Selamat datang di "Kantong Ajaib!"') 
		return True
	else: # Foldernya gaada
		print("Folder tidak ditemukan!")
		return False

def load_inventori(user_id):
	# membuat file inventori untuk user jika belum ada
	file_name = "inventori_" + str(user_id) + ".csv" # nama file inventori, hanya mengandung id user
	if not(os.path.exists(file_name)):
		f = open(file_name, 'w+')
		f.write('id;nama;rarity;jumlah')
		f.close()
		# bikin file temp, seperti pada file lain saat load
		copas(file_name, "temp_" + file_name)
	

