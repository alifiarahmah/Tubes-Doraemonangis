# ini biar bisa ngetes aja :v

import os
import time
import argparse
from load import load
from login import login
from register import register
from help import help
from save import save
from save import nosave
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
				tambahitem()
			elif (user_input == "ubahjumlah"):
				ubahjumlah()
			elif (user_input == "hapusitem"):
				hapusitem()
			elif (user_input == "save"):
				save()
			else:
				print("Perintah tidak valid! (Lihat 'help' untuk melihat list perintah)")

			user_input = input(">>> ")

			if (user_input == "exit"):
				ans = str(input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))

				while ((ans != 'y') and (ans != 'Y') and (ans != 'n') and (ans != 'N')):	
					print("Jawaban tidak valid, jawab dengan y/n ")
					ans = str(input("Apakah anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))
					
				if ((ans == 'y') or (ans == 'Y')):
					save()
					print("Perubahan file telah disimpan, Terima Kasih!")
				else: # ((ans == 'n') or (ans == 'N')):	 
					nosave()
					print("Terima kasih!")	 
				
else:	# Gada input argumen untuk nama folder ('')
	print("Tidak ada nama folder yang diberikan!")
	print("Usage: python kantongajaib.py <nama_folder>")

	   
			
