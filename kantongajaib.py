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
from exit import exit

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
				tambahitem(role)
			elif (user_input == "ubahjumlah"):
				ubahjumlah(role)
			elif (user_input == "hapusitem"):
				hapusitem(role)
			elif (user_input == "save"):
				save()
			else:
				print("Perintah tidak valid! (Lihat 'help' untuk melihat list perintah)")

			user_input = input(">>> ")

			if (user_input == "exit"):
				exit() 
				
else:	# Gada input argumen untuk nama folder ('')
	print("Tidak ada nama folder yang diberikan!")
	print("Usage: python kantongajaib.py <nama_folder>")

	   
			
