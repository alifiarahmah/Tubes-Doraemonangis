from csv_stuffs import addCSVdata, getRow, getCol, readCSVdata, editCSVdata

def tambahitem():
	# menambahkan item ke dalam inventori
	# KAMUS LOKAL
	# csv_file, id, nama, desc, jml, rarity, year : string
	id = input("Masukkan ID: ")

	if id[0] == 'G':
		csv_file = "gadget.csv"
	elif id[0] == 'C':
		csv_file = "consumable.csv"
	else:
		print("Gagal menambahkan item karena ID tidak valid.")
		return

	if getRow(csv_file, id) != None:
		print("Gagal menambahkan item karena ID sudah ada.")
		return

	nama = input("Masukkan Nama: ")
	desc = input("Masukkan Deskripsi: ")
	jml = input("Masukkan Jumlah: ")
	rarity = input("Masukkan Rarity: ")

	if rarity not in 'CBAS':
		print("Input rarity tidak valid!")
		return

	if id[0] == "G":  # gadget
		year = input("Masukkan tahun ditemukan: ")
		addCSVdata(csv_file, [id, nama, desc, jml, rarity, year])
	else:
		addCSVdata(csv_file, [id, nama, desc, jml, rarity])

	print("Item telah berhasil ditambahkan ke database.")
	return

tambahitem()
