from csv_stuffs import readCSV, readCSVdata, getCol, getRow, editCSVdata, addCSVdata
from tgl import isTglValid

def pinjam(role, user_id):
	# meminjam gadget. khusus user

	# KAMUS LOKAL
	# item_id, tgl, item
	# id, jml_pinjam, stok : int

	# ALGORITMA

	# validasi role User
	if role == "User":

		item_id = input("Masukkan ID item: ")

		if getRow("gadget.csv", item_id) != None: # ID item ada di database
			
			# cek lagi dipinjam atau ga
			if getRow("inventori_" + str(user_id) + ".csv", item_id) == None: # ID item tidak ada di inventori user
				tgl = input("Tanggal peminjaman: ")

				# validasi tanggal
				if isTglValid(tgl):

					jml_pinjam = int(input("Jumlah peminjaman: "))

					if jml_pinjam > 0:

						if getRow("gadget.csv", item_id) != None:  # ID item ada di database

							item = readCSVdata("gadget.csv", getRow("gadget.csv", item_id), getCol("gadget.csv", "nama"))
							stok = int(readCSVdata("gadget.csv", getRow("gadget.csv", item_id), getCol("gadget.csv", "jumlah")))

							# validasi jumlah peminjaman

							if stok >= jml_pinjam:
								# ubah jumlah di gadget.csv
								editCSVdata("gadget.csv", getRow("gadget.csv", item_id), getCol("gadget.csv", "jumlah"), str(stok-jml_pinjam))

								# catat ke gadget_borrow_history
								id = int(len(readCSV("gadget_borrow_history.csv")[1])+1)
								addCSVdata("gadget_borrow_history.csv", [id, user_id, item_id, tgl, jml_pinjam, 0])
								
								# catat ke inventory user
								addCSVdata("inventori_" + str(user_id) + ".csv", [item_id, item, str(jml_pinjam)])
								
								print("Item", item, "(x" + str(jml_pinjam) + ")", "berhasil dipinjam!\n")

							elif stok == 0:
								print("Item", item, "gagal dipinjam karena stok habis.\n")

							else: # stok < jml_pinjam
								print("Item", item, "gagal dipinjam karena jumlah peminjaman melebihi stok.\n")


					else: # jml_pinjam < 0
						print("Jumlah peminjaman tidak valid!\n")

				else: # isTglValid(tgl) == False
					print("Tanggal tidak valid!\n")
			
			else: # ID item ada di inventori user
				print("Tidak bisa meminjam gadget yang sedang dipinjam")
				
		else: # ID tidak ada di database
			print("Tidak ada item dengan ID tersebut!\n")

	else: # role == "Admin"
		print("Admin tidak perlu melakukan peminjaman pada item.\n")
