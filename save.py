import os
from load import copas
from load import setupFile

def save():
	# fungsi save, untuk ditengah program ataupun pada saat exit (jika dipilih yes)
	ans = str(input("Apakah anda ingin menyimpan perubahan di folder ini? (y/n): "))
	ansValid = False
	while (not(ansValid)): 
		if ans == "y":	# penyimpanan di current working directory (cwd)
			# file lama (_temp) dihapus, file baru menggantikan
			os.remove("gadget_temp.csv")
			os.remove("consumable_temp.csv")
			os.remove("consumable_history_temp.csv")
			os.remove("gadget_return_history_temp.csv")
			os.remove("gadget_borrow_history_temp.csv")
			
			# sama seperti load, karena ada kemungkinan program masih digunakan setelah save
			setupFile()
			
			ansValid = True
		elif ans == "n": # penyimpanan di folder/direktori lain
			# file lama tidak perlu dihapus, file baru dicopy ke folder baru kemudian dihapus pada cwd, nama file lama diganti kembali 
			# file baru tidak dihapus karena mungkin masih digunakan pada program (jika tidak disave lagi, akan dihapus pada saat exit)
			folder_name = input("Masukkan nama folder penyimpanan: ")
			dir_save = os.path.dirname(os.path.abspath(__file__)) + "\\" + folder_name # direktori tujuan

			if not(os.path.exists(dir_save)):
				# Jika foldernya belum ada, dibuat dulu foldernya
				print("Folder belum ada, akan dibuat folder baru")
				os.mkdir(dir_save) # foldernya dibuat
				
			# path file tujuan = dir_save + "\\csv_file"
			# copas ke path tujuan
			copas("gadget.csv", dir_save + "\\gadget.csv")
			copas("consumable.csv", dir_save + "\\consumable.csv")
			copas("consumable_history.csv", dir_save + "\\consumable_history.csv")
			copas("gadget_return_history.csv", dir_save + "\\gadget_return_history.csv")
			copas("gadget_borrow_history.csv", dir_save + "\\gadget_borrow_history.csv")
				
			ansValid = True	
		else: # jawaban tidak valid
			ans = str(input("Jawab dengan y(ya) atau n(tidak) !: "))	
	
	return None

def nosave():
	# nosave, hanya pada exit (jika dipilih no)
	# semua file baru dihapus (bisa jadi disave di folder lain sebelumnya)
	os.remove("gadget.csv")
	os.remove("consumable.csv")
	os.remove("consumable_history.csv")
	os.remove("gadget_return_history.csv")
	os.remove("gadget_borrow_history.csv")
	
	# file lama (_temp) diubah kembali namanya
	os.rename("gadget_temp.csv", "gadget.csv")
	os.rename("consumable_temp.csv", "consumable.csv")
	os.rename("consumable_history_temp.csv", "consumable_history")
	os.rename("gadget_return_history_temp.csv", "gadget_return_history.csv")
	os.rename("gadget_borrow_history_temp.csv", "gadget_borrow_history.csv")
	
	return None
