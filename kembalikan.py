from csv_stuffs import readCSV, readCSVdata, addCSVdata, editCSVdata, getCol, getRow
from tgl import isTglValid

def kembalikan(role, user_id):
	# mengembalikan seluruh barang. khusus user.

	# KAMUS
	# datas : array of any
	# gadget_dipinjam : array of array[1..3] of string
	# id_peminjam_col, id_gadget, nama_gadget, tgl : string
	# id_peminjaman, no, jml_pinjam, jml_awal, id : integer

	# ALGORITMA

	if role == "User":
		
		datas = readCSV("gadget_borrow_history.csv")[1]
		id_peminjam_col = getCol("gadget_borrow_history.csv", "id_peminjam")
		
		# cari data yang idnya segitu

		# memasukkan daftar gadget yang dipinjam dalam array
		# format -> [id_peminjaman, id_gadget, nama_gadget]
		gadget_dipinjam = []
		
		for i in range(len(datas)):  # iterasi tiap row dalam datas
			# untuk setiap pinjam dari user
			isnt_returned = readCSVdata("gadget_borrow_history.csv", i, getCol("gadget_borrow_history.csv", "is_returned")) == "0"
			if (readCSVdata("gadget_borrow_history.csv", i, id_peminjam_col) == user_id) & isnt_returned:
				# ambil id peminjaman
				id_peminjaman = readCSVdata("gadget_borrow_history.csv", i, getCol("gadget_borrow_history.csv", "id"))
				# ambil namanya
				id_gadget = readCSVdata("gadget_borrow_history.csv", i, getCol("gadget_borrow_history.csv", "id_gadget"))
				nama_gadget = readCSVdata("gadget.csv", getRow("gadget.csv", id_gadget), getCol("gadget.csv", "nama"))

				gadget_dipinjam.append([id_peminjaman, id_gadget, nama_gadget])

		# cek barang pinjaman
		if len(gadget_dipinjam) > 0:

			# print seluruh data
			for i in range(len(gadget_dipinjam)):
				print(str(i+1) + ".", gadget_dipinjam[i][2])
			print()

			no = int(input("Masukkan nomor peminjaman: "))
			
			# validasi nomor peminjaman
			if (no >= 1) & (no <= len(gadget_dipinjam)):
				no -= 1
				id_peminjaman = gadget_dipinjam[no][0]
				id_gadget = gadget_dipinjam[no][1]
				nama_gadget = gadget_dipinjam[no][2]
				
				# ubah kalo mau bonus
				jml_pinjam = readCSVdata("gadget_borrow_history.csv", id_peminjaman, getCol("gadget_borrow_history.csv", "jumlah"))

				tgl = input("Tanggal pengembalian: ")

				# validasi tanggal
				if isTglValid(tgl):

					# ubah jumlah di gadget.csv
					jml_awal = readCSVdata("gadget.csv", getRow("gadget.csv", id_gadget), getCol("gadget.csv", "jumlah"))
					editCSVdata("gadget.csv", getRow("gadget.csv", id_gadget), getCol("gadget.csv", "jumlah"), jml_awal+jml_pinjam)

					# catat di gadget_return_history.csv
					if len(readCSV("gadget_return_history.csv")[1]) == 0: # jika ini entry pertama
						addCSVdata("gadget_return_history.csv", [0, id_peminjaman, tgl])
					else: # jika ini entry selanjutnya
						id = int(readCSVdata("gadget_return_history.csv", (len(readCSV("gadget_return_history.csv")[1])) - 1, 0)) + 1
						addCSVdata("gadget_return_history.csv", [id, id_peminjaman, tgl])

					# edit is_returned di gadget_borrow_history.csv
					editCSVdata("gadget_borrow_history.csv", id_peminjaman, getCol("gadget_borrow_history.csv", "is_returned"), 1)

					# hapus gadget di inventori user
					inventori = "inventori_" + str(user_id) + ".csv"
					delCSVdata(inventori, getRow(inventori, id_gadget))
					
					print("Item", nama_gadget, "(x" + str(jml_pinjam) + ") telah dikembalikan.\n")
					
				else: # isTglValid(tgl) == False
					print("Tanggal tidak valid!\n")

			else:  # ~((no >= 1) & (no <= len(gadget_dipinjam)))
				print("Tidak ada barang dengan nomor peminjaman tersebut!\n")

		else: # len(data_dipinjam) 
			print("Anda belum pernah meminjam gadget apapun.\n")

	else: # role != "User"
		print("Admin tidak perlu mengembalikan barang.\n")
