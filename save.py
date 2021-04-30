import os
import time
from csv_stuffs import getListCSV
from load import copas
from load import setupFile

def nosave():
	# nosave, dipakai ketika tidak dilakukan penyimpanan di CWD pada saat exit
	# semua file baru dihapus (bisa jadi disave di folder lain sebelumnya)
	RemoveList = getListCSV("no_temp")
	for i in range(len(RemoveList)):	
		os.remove(RemoveList[i]) 
	
	# file lama (temp_) diubah kembali namanya
	RenameList = getListCSV("only_temp")
	for i in range(len(RenameList)):	
		os.rename(RenameList, RemoveList) 
	
	return None

def save(exit = False):
	# fungsi save, untuk ditengah program ataupun pada saat exit (jika dipilih yes)
	ans = str(input("Apakah anda ingin menyimpan data di folder saat ini? (y/n): "))
	ansValid = False
	while (not(ansValid)): 
		if (ans == "y") or (ans == "Y") : # penyimpanan di current working directory (cwd)
			print("Saving...")
			time.sleep(3) # efek saving...
			# file lama (_temp) dihapus, file baru menggantikan
			RemoveList = getListCSV("only_temp")
			for i in range(len(RemoveList)):	
				os.remove(RemoveList[i]) 	
				
			if (not(exit)):
				# Kasus penyimpanan di tengah program (bukan saat exit)
				# Dilakukan setupFile seperti pada load, karena ada kemungkinan program masih digunakan setelah save
				setupFile()
			
			print("Data telah disimpan pada folder saat ini!")
			ansValid = True
		elif (ans == "n") or (ans == "N") : # penyimpanan di folder/direktori lain
			print("Saving...")
			time.sleep(3)
			# file lama tidak perlu dihapus, file baru dicopy ke folder baru kemudian dihapus pada cwd, nama file lama diganti kembali 
			# file baru tidak dihapus karena mungkin masih digunakan pada program (jika tidak disave lagi, akan dihapus pada saat exit)
			folder_name = input("Masukkan nama folder penyimpanan: ")
			dir_save = os.path.dirname(os.path.abspath(__file__)) + "\\" + folder_name # direktori tujuan

			if not(os.path.exists(dir_save)):
				# Jika foldernya belum ada, dibuat dulu foldernya
				print("Folder belum ada, akan dibuat folder baru")
				os.mkdir(dir_save) # foldernya dibuat
				
			# path file tujuan = dir_save + "\\" + CopasList[i]
			# copas ke path tujuan
			CopasList = getListCSV("no_temp")
			for i in range(len(CopasList)):	
				copas(CopasList[i], dir_save + "\\" + CopasList[i]) 
				
			#copas("user.csv", dir_save + "\\user.csv")
			
			if (exit):
				# Dalam kasus ketika exit, file baru (sudah disimpan di folder lain) dihapus dan file lama (_temp) diganti kembali namanya
				nosave()
			
			print("Data telah disimpan pada folder " + folder_name + "!")
			ansValid = True	
		else: # jawaban tidak valid
			ans = str(input("Jawab dengan y(ya) atau n(tidak) !: "))	
	
	return None

