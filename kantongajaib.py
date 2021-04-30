# ini biar bisa ngetes aja :v

import os
import time
import argparse
from load import load, setInventori
from login import login
from register import register
from help import help
from save import save, nosave
from ubahjumlah import ubahjumlah
from hapusitem import hapusitem
from tambahitem import tambahitem
from exit import exit
from cari_gadget_rarity import cari_gadget_rarity
from cari_gadget_tahun import cari_gadget_tahun
from pinjam import pinjam
from kembalikan import kembalikan
from ambil_consumable import ambil_consumable
from lihat_riwayat_gadget import lihat_riwayat_pinjam_gadget, lihat_riwayat_kembalikan_gadget
from lihat_riwayat_consumable import lihat_riwayat_consumable

parser = argparse.ArgumentParser()						  #
parser.add_argument("Direktori", nargs='?', default='')	  #   Bagian awal program
args = parser.parse_args()								  #

if (args.Direktori != ''):		# ada input argumen untuk nama folder (tidak kosong)								  
	print("Loading...")
	time.sleep(3)
	if (load(args.Direktori)):  # F14 load -> True kalau foldernya ada, -> False kalau gada

		role = ""
		user_id = 0
    
		user_input = input(">>> ")
	
		while (role == ""):
			if (user_input == "login"): # F02
				tuple_login = login(role, user_id) 
				role = tuple_login[0]
				user_id = tuple_login[1]
			elif (user_input == "help"): # F16
				help(role)
			elif (user_input == "exit"): # F17
				exit(role)
			else: 
				print("Silahkan login terlebih dahulu!")
				
			print()
			user_input = input(">>> ")
		
		setInventori(user_id)
		
		while (user_input != "exit"):
			if (user_input == "register"): # F01
				register(role)
			elif (user_input == "login"): # F02 Sudah dijalankan
				print("Anda sudah login!")
			elif (user_input == "carirarity"): # F03
				cari_gadget_rarity()
			elif (user_input == "caritahun"): # F04
				cari_gadget_tahun()
			elif (user_input == "tambahitem"): # F05
				tambahitem(role)
			elif (user_input == "hapusitem"): # F06
				hapusitem(role)
			elif (user_input == "ubahjumlah"): # F07
				ubahjumlah(role)
			elif (user_input == "pinjam"): # F08
				pinjam(role, user_id)
			elif (user_input == "kembalikan"): # F09
				kembalikan(role, user_id)
			elif (user_input == "minta"): # F10
				ambil_consumable(role)
			elif (user_input == "riwayatpinjam"): # F11
				lihat_riwayat_pinjam_gadget(role)
			elif (user_input == "riwayatkembali"): # F12
				lihat_riwayat_kembalikan_gadget(role)
			elif (user_input == "riwayatambil"): # F13
				lihat_riwayat_consumable(role)
			elif (user_input == "save"): # F15
				save()
			elif (user_input == "help"): # F16
				help(role)
			
			else:
				print("Perintah tidak valid! (Lihat 'help' untuk melihat list perintah)")
			
			print()
			user_input = input(">>> ")
			
		exit(role) # F17
			
				
else:	# Gada input argumen untuk nama folder ('')
	print("Tidak ada nama folder yang diberikan!")
	print("Usage: python kantongajaib.py <nama_folder>")
	print()


