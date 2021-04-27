from csv_stuffs import getRow, getCol, readCSV, saveCSV, readCSVdata

def hapusitem(role):
	# menghapus item di database

	# KAMUS LOKAL
	# id, csv_file, nama, prompt : string
	# header : array of string
	# datas : array of ada string ada integer

	# ALGORITMA

	# validasi role Admin
	if (role == "Admin"):

		id = input("Masukkan ID item: ")

		# validasi format id
		if (id[0] == 'G') | (id[0] == 'C'):

			if id[0] == 'G':
				csv_file = "gadget.csv"
			else: # id[0] == 'C'
				csv_file = "consumable.csv"

			# validasi keberadaan id di inventory
			if getRow(csv_file, id) != None: # id ada di inventory

				nama = readCSVdata(csv_file, getRow(csv_file, id), getCol(csv_file, "nama"))
				prompt = input("Apakah anda yakin ingin menghapus", nama, "(Y/N)?")

				if prompt in 'Yy':

					header = readCSV(csv_file)[0]
					datas = readCSV(csv_file)[1]
					datas.pop(getRow(csv_file, id)) # mengeluarkan item
					saveCSV(header, datas, csv_file)

					print("Item telah berhasil dihapus dari database.\n")

				else: # prompt not in 'Yy'
					print("Proses dibatalkan.\n")

			else: # id tidak ada di inventory
				print("Tidak ada item dengan ID tersebut!\n")

		else: # format ID tidak valid
			print("Tidak ada item dengan ID tersebut!\n")

	else: # role != "Admin"
		print("Anda tidak dapat melakukan perubahan pada item!\n")
