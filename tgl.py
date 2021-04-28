import datetime

"""

fungsi yang berhubungan dengan tanggal

isTglValid(tgl: string) -> boolean
	validasi format tanggal sesuai dd/mm/yyyy

isKabisat(y: integer) -> boolean
	cek kabisat

sort_data_date(arr_data) -> arr_data

"""

def isKabisat(y):
	if (y % 400 == 0) | ((y % 100 != 0) & (y % 4 == 0)):
		return True
	return False

def isTglValid(tgl): # -> boolean
	# validasi format tanggal sesuai dd/mm/yyyy
	if len(tgl) == 10:
		if (tgl[2] == '/') & (tgl[5] == '/'):
			d = int(tgl[0]) * 10 + int(tgl[1])
			m = int(tgl[3]) * 10 + int(tgl[4])
			y = int(tgl[6]) * 1000 + int(tgl[7]) * 100 + int(tgl[8]) * 10 + int(tgl[9])

			if (m >= 1) & (m <= 12): # bulan valid (jan-des)
				if ((m == 2) & isKabisat(y) & (d >= 1) & (d <= 29)) | ((m == 2) & (d >= 1) & (d <= 28)): # Khusus Februari
					return True
				elif ((m <= 7) & (m % 2 == 1)) | ((m >= 8) & (m % 2 == 0)): # 31 hari
					if (d >= 1) & (d <= 31):
						return True
				else: # 30 hari
					if (d >= 1) & (d <= 30):
						return True

def sort_data_date(arr_data):
# sort data berdasarkan tanggal
    for i in range(1, len(arr_data)): # dimulai dari index ke-1

        init_date = str(datetime.datetime.strptime(arr_data[i][3], "%d/%m/%Y"))
        # inisiasi tanggal dalam format yyyy/mm/dd
        init_data = arr_data[i]

        j = i - 1
        next_date = str(datetime.datetime.strptime(arr_data[j][3], "%d/%m/%Y"))
        while j >= 0 and init_date > next_date:
            arr_data[j + 1] = arr_data[j]
            j -= 1
            next_date = str(datetime.datetime.strptime(arr_data[j][3], "%d/%m/%Y"))
        arr_data[j + 1] = init_data
