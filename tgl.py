"""

fungsi lain selain per-CSV-an duniawi yang mungkin bisa membantu

validasiTanggal(tgl: string) -> bool
	return 1 jika format tanggal valid

"""

def validasiTanggal(tgl):
	# validasi format tanggal sesuai dd/mm/yyyy
	if len(tgl) == 9:
		if (tgl[2] == '/') & (tgl[5] == '/'):
			d = int(tgl[0]) * 10 + int(tgl[1])
			m = int(tgl[3]) * 10 + int(tgl[4])
			y = int(tgl[6]) * 1000 + int(tgl[7]) * 100 + int(tgl[8]) * 10 + int(tgl[9])
			
			if (m >= 1) & (m <= 12): # bulan valid (jan-des)
				if ((m <= 7) & (m % 2 == 1)) | ((m >= 8) & (m % 2 == 0)): # 31 hari
					if (d >= 1) & (d <= 31):
						return 1
				else: # 30 hari
					if (d >= 1) & (d <= 30):
						return 1
	return 0
