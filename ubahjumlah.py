from csv_stuffs import getRow, getCol, readCSVdata, editCSVdata
from save import save_data_class

def ubahjumlah():
	# mengubah jumlah barang dalam inventory
	# KAMUS LOKAL
	# id, csv_file, nama : string
	# id_idx, col, jml, jml_awal : integer

	id = input("Masukkan ID: ")

	if id[0] == "G": # gadget
		csv_file = "gadget.csv"
	elif id[0] == "C": # consumable
		csv_file = "consumable.csv"

	id_idx = getRow(csv_file, id)

	if id_idx == None: # id tidak ada di inventory
		print("Tidak ada item dengan ID tersebut!")
	else:
		col = getCol(csv_file, "jumlah")
		jml = int(input("Masukkan jumlah: "))
		nama = readCSVdata(csv_file, id_idx, getCol(csv_file, "nama"))
		jml_awal = int(readCSVdata(csv_file, id_idx, getCol(csv_file, "jumlah")))

		if jml_awal + jml < 0: # stok kurang, error
			print(abs(jml), nama, "gagal dibuang karena stok kurang.", end=" ")
			
			print("Stok sekarang:", str(jml_awal), "( <", str(abs(jml)), ")")
			
		else: # valid
			
			
			if jml > 0:
				print(abs(jml), nama, "berhasil ditambahkan.", end=" ")
				print("Stok sekarang:", (readCSVdata(csv_file, id_idx, getCol(csv_file, "jumlah")) + jml))
			elif jml < 0:
				print(abs(jml), nama, "berhasil dibuang.", end=" ")
				print("Stok sekarang:", (readCSVdata(csv_file, id_idx, getCol(csv_file, "jumlah")) + jml))
			else:
				print("Stok tetap sama.", end=" ")
				
			header_save, datas_save, csv_file_save = editCSVdata(csv_file, id_idx, col, str(jml_awal+jml))
			
			return save_data_class(header_save, datas_save, csv_file_save)
	return None
	
