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
from cari_gadget_rarity import cari_gadget_rarity
from cari_gadget_tahun import cari_gadget_tahun

parser = argparse.ArgumentParser()						  #
parser.add_argument("Direktori", nargs='?', default='')	  #   Bagian awal program
args = parser.parse_args()								  #

if (args.Direktori != ''):		# ada input argumen untuk nama folder (tidak kosong)								  
	print("Loading...")
	time.sleep(3)
	if (load(args.Direktori)):  # load -> True kalau foldernya ada, -> False kalau gada

		role = ""
		user_id = 0
    
		user_input = input(">>> ")
    
		while (user_input != "exit"):
			if (user_input == "login"):
				tuple_login = login(role, user_id) # nyimpen role dan user id
				role = tuple_login[0]
				user_id = tuple_login[1]
			elif (user_input == "register"):
				register(role)
			elif (user_input == "help"):
				help(role)
        
      			# Pilihan fungsi dari input
			elif (user_input == "tambahitem"):
				tambahitem(role)
			elif (user_input == "ubahjumlah"):
				ubahjumlah(role)
			elif (user_input == "hapusitem"):
				hapusitem(role)
			elif (user_input == "save"):
				save()
			elif (user_input == "caritahun"):
				cari_gadget_tahun()
			elif (user_input == "carirarity"):
				cari_gadget_rarity()
			else:
				print("Perintah tidak valid! (Lihat 'help' untuk melihat list perintah)")
				print()

			user_input = input(">>> ")
			
		exit()
			
				
else:	# Gada input argumen untuk nama folder ('')
	print("Tidak ada nama folder yang diberikan!")
	print("Usage: python kantongajaib.py <nama_folder>")
	print()


