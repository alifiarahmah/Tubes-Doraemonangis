from csv_stuffs import addCSVdata, getRow, getCol, readCSVdata, editCSVdata

def tambahitem(role):
	# menambahkan item ke dalam inventory

	# KAMUS LOKAL
	# csv_file, id, nama, desc, jml, rarity, year : string

	# ALGORITMA

	# validasi role Admin
	if (role == "Admin"):
		id = input("Masukkan ID: ")

		idnum = ""
		for i in range(1,len(id)):
			idnum += id[i]

		# validasi format ID G<angka> atau C<angka>
		if ((id[0] == 'G') | (id[0] == 'C')) & idnum.isnumeric():

			if id[0] == 'G':
				csv_file = "gadget.csv"
			else: # id[0] == 'C'
				csv_file = "consumable.csv"

			# validasi keberadaan id di inventory
			if getRow(csv_file, id) == None: # id belum ada

				nama = input("Masukkan Nama: ")
				desc = input("Masukkan Deskripsi: ")
				jml = input("Masukkan Jumlah: ")

				# validasi jumlah
				if int(jml) > 0: 

					rarity = input("Masukkan Rarity: ")

					# validasi rarity
					if rarity in 'CBAS':

						if id[0] == "G":  # gadget
							year = input("Masukkan tahun ditemukan: ")
							addCSVdata(csv_file, [id, nama, desc, jml, rarity, year])
						else:  # consumable
							addCSVdata(csv_file, [id, nama, desc, jml, rarity])

						print("Item telah berhasil ditambahkan ke database.\n")
						return

					else: # rarity tidak valid
						print("Input rarity tidak valid!\n")
						return

				else: # jml < 0
					print("Jumlah tidak valid!\n")
					return

			else:  # getRow(csv_file, id) != None
				print("Gagal menambahkan item karena ID sudah ada.\n")
				return

		else: # (id[0] != G) & (id[0] != C)
			print("Gagal menambahkan item karena ID tidak valid.\n")
			return

	else: # role != "Admin"
		print("Anda tidak dapat melakukan perubahan pada item!\n")