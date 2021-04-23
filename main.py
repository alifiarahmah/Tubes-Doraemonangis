# ini biar bisa ngetes aja :v

import os
import time
import argparse
from load import load
from login import login
from register import register
from help import help
from save import save
from save import save_data_class
from ubahjumlah import ubahjumlah
from hapusitem import hapusitem
from tambahitem import tambahitem

parser = argparse.ArgumentParser()						  #
parser.add_argument("Direktori", nargs='?', default='')	  #   Bagian awal program
args = parser.parse_args()								  #

if (args.Direktori != ''):		# ada input argumen untuk nama folder (tidak kosong)								  
	print("Loading...")
	time.sleep(3)
	if (load(args.Direktori)):  # load -> True kalau foldernya ada, -> False kalau gada
	
		save_data = save_data_class("","","")
		save_empty = save_data_class("","","")

		role = ""
		user_input = input(">>> ")
		while (user_input != "exit"):
			if (user_input == "login"):
				role = login() # nyimpen role user
			elif (user_input == "register"):
				register(role)
			elif (user_input == "help"):
				help(role)
			elif (user_input == "tambahitem"):
				save_data = tambahitem()
			elif (user_input == "ubahjumlah"):
				save_data = ubahjumlah()
			elif (user_input == "hapusitem"):
				save_data = hapusitem
			elif (user_input == "save"):
				if (save_data == save_empty):
					print("Tidak ada perubahan yang perlu disimpan")
				else:
					save(save_data.header, save_data.datas, save_data.csv_file)
					save_data = save_empty # reset
					print("Perubahan file telah disimpan")
			else:
				print("Perintah tidak valid! (Lihat 'help' untuk melihat list perintah)")

			user_input = input(">>> ")

			if (user_input == "exit"):
				if (save_data == save_empty):
					print("Perubahan file sudah disimpan, Terima kasih!")
				else:
					ans = str(input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))

					while ((ans != 'y') and (ans != 'Y') and (ans != 'n') and (ans != 'N')):	
						print("Jawaban tidak valid, jawab dengan y/n ")
						ans = str(input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))

					if ((ans == 'y') or (ans == 'Y')):
						save(save_data.header, save_data.datas, save_data.csv_file)
						print("Perubahan file telah disimpan, Terima Kasih!")
					else: # ((ans == 'n') or (ans == 'N')):	  
						print("Terima kasih!")	 
				
else:	# Gada input argumen untuk nama folder ('')
	print("Tidak ada nama folder yang diberikan!")
	print("Usage: python kantongajaib.py <nama_folder>")

	   
			
