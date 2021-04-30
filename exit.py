import sys
from save import save
from save import nosave

def exit(role):
	if (role == ""):
		sys.exit("Terima kasih!")
		
	# else
	ans = str(input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))

	while ((ans != 'y') and (ans != 'Y') and (ans != 'n') and (ans != 'N')):	
		print("Jawaban tidak valid, jawab dengan y/n ")
		ans = str(input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))

	if ((ans == 'y') or (ans == 'Y')):
		save(True) # nilai True diperlukan khusus untuk penyimpanan ketika exit (lihat file save.py)
		print("Perubahan file telah disimpan, Terima Kasih!")
	else: # ((ans == 'n') or (ans == 'N'))
		nosave()
		print("Terima kasih!")	
	
	
	return None
