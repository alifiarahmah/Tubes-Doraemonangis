from csv_stuffs import addCSVdata, getRow, getCol, readCSVdata, editCSVdata
from save import save_data_class

def tambahitem():
	# menambahkan item ke dalam inventory
	# KAMUS LOKAL
	# csv_file, id, nama, desc, jml, rarity, year : string
	
	id = input("Masukkan ID: ")

	if id[0] == 'G': # id gadget
		csv_file = "gadget.csv"
	elif id[0] == 'C': # id consumable
		csv_file = "consumable.csv"
	else: # id tidak valid
		print("Gagal menambahkan item karena ID tidak valid.")
		return

	if getRow(csv_file, id) != None: # id ada di database
		print("Gagal menambahkan item karena ID sudah ada.")
		return

	nama = input("Masukkan Nama: ")
	desc = input("Masukkan Deskripsi: ")
	jml = input("Masukkan Jumlah: ")

	if int(jml) < 0: # jumlah negatif
		print("Jumlah tidak valid!")
		return

	rarity = input("Masukkan Rarity: ")

	if rarity not in 'CBAS': # rarity tidak valid
		print("Input rarity tidak valid!")
		return

	if id[0] == "G":  # gadget
		year = input("Masukkan tahun ditemukan: ")
		header_save, datas_save, csv_file_save = addCSVdata(csv_file, [id, nama, desc, jml, rarity, year])
	else: # consumable
		header_save, datas_save, csv_file_save = addCSVdata(csv_file, [id, nama, desc, jml, rarity])

	print("Item telah berhasil ditambahkan ke database.")
	
	return save_data_class(header_save, datas_save, csv_file_save)
