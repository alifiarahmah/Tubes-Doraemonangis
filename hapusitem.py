from csv_stuffs import getRow, getCol, readCSV, saveCSV, readCSVdata
from save import save_data_class

def hapusitem():
	# menghapus item di database
	# KAMUS LOKAL
	# id, csv_file, nama, prompt : string
	# header : array of string
	# datas : array of ada string ada integer
	
	id = input("Masukkan ID item: ")

	if id[0] == 'G':
		csv_file = "gadget.csv"
	elif id[0] == 'C':
		csv_file = "consumable.csv"
	else:
		print("Tidak ada item dengan ID tersebut.")
		return
	
	if getRow(csv_file, id) == None:
		print("Tidak ada item dengan ID tersebut.")
		return

	nama = readCSVdata(csv_file, getRow(csv_file, id), getCol(csv_file, "nama"))
	prompt = input("Apakah anda yakin ingin menghapus " +  nama + " (Y/N)?")
	
	if prompt in 'Yy':

		header = readCSV(csv_file)[0]
		datas = readCSV(csv_file)[1]
		datas.pop(getRow(csv_file, id))
		

		print("Item telah berhasil dihapus dari database.")
		return save_data_class(header, datas, csv_file)
	else:
		print("Oke ga jadi ya h3h3.")
		return
