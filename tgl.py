"""

fungsi mengurus tanggal

isTglValid(tgl: string) -> boolean
	validasi format tanggal sesuai dd/mm/yyyy

isKabisat(y: integer) -> boolean
	cek kabisat

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
