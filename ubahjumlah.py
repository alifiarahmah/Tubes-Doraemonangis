from csv_stuffs import getRow, getCol, readCSVdata, editCSVdata

def ubahjumlah(role):
	# mengubah jumlah barang dalam inventory

	# KAMUS LOKAL
	# id, csv_file, nama : string
	# id_idx, col, jml, jml_awal : integer

	# ALGORITMA
	
	# validasi role Admin
	if (role == "Admin"):

		id = input("Masukkan ID: ")

		# validasi format ID
		if (id[0] == "G") | (id[0] == "C"):

			if id[0] == "G":
				csv_file = "gadget.csv"
			else: # id[0] == "C"
				csv_file = "consumable.csv"

			id_idx = getRow(csv_file, id)

			# validasi keberadaan id di inventory

			if id_idx != None: # id ada di inventory

				col = getCol(csv_file, "jumlah")
				jml = int(input("Masukkan jumlah: "))
				nama = readCSVdata(csv_file, id_idx, getCol(csv_file, "nama"))
				stok = int(readCSVdata(csv_file, id_idx, getCol(csv_file, "jumlah")))

				# validasi jumlah dan stok
				if stok + jml > 0:

					editCSVdata(csv_file, id_idx, col, str(stok + jml))

					if jml > 0: # menambah item
						print(abs(jml), nama, "berhasil ditambahkan.", end=" ")
					elif jml < 0: # mengurang item
						print(abs(jml), nama, "berhasil dibuang.", end=" ")
					else: # jml == 0
						print("Stok", nama, "tetap sama.", end=" ")

					print("Stok sekarang:", readCSVdata(csv_file, id_idx, getCol(csv_file, "jumlah")), "\n")

				else:  # stok + jml < 0
					print(abs(jml), nama, "gagal dibuang karena stok kurang.", end=" ")
					print("Stok sekarang:", str(stok), "( <", str(abs(jml)), ")\n")

			else:  # id tidak ada di inventory
				print("Tidak ada item dengan ID tersebut!\n")

		else: # format id salah
			print("Tidak ada item dengan ID tersebut!\n")

	else: # role != "Admin"
		print("Anda tidak dapat melakukan perubahan pada item!\n")