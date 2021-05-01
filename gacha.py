import datetime
import time
from csv_stuffs import readCSV, readCSVdata, getRow, getCol, editCSVdata, addCSVdata

def prng(): # -> integer
	# pseudo-random number generator. menghasilkan nilai pseudo-random di antara 1-100

	# KAMUS LOKAL
	# h, m, s, j, percentage : integer

	# ALGORITMA

	h = int(datetime.datetime.now().strftime("%H"))
	m = int(datetime.datetime.now().strftime("%M"))
	s = int(datetime.datetime.now().strftime("%S"))
	j = int(datetime.datetime.now().strftime("%j"))

	percentage = round((h * m + s * j) % 100)
	if percentage == 0: # jika nol, lakukan prng ulang
		prng()
	return percentage

def chooser(arr): # -> any
	# memilih satu elemen dari suatu array dengan pendekatan prng

	# KAMUS LOKAL
	# kocokan, i : integer
	# bobot_elmt : real
	# elmt : any

	# ALGORITMA

	if len(arr) > 0:
		kocokan = prng()
		bobot_elmt = 100 / len(arr)
		i = 1
		for elmt in arr:
			if kocokan <= bobot_elmt * i:
				return elmt
			else:  # kocokan > bobot_elmt * i
				i += 1
	return None

def numchooser(n): # -> integer
	# memilih bilangan dari 1 sampai n. Jika n = 0, mengembalikan nilai 0

	# KAMUS LOKAL
	# numlist : array[1..n] of integer
	# i : integer

	# ALGORITMA

	if n > 0:
		numlist = []
		for i in range(1, n+1):
			numlist.append(i)
		return chooser(numlist)
	return 0

def raritychooser(rarity): # -> character
	# memilih rarity dengan tinggi-rendah chance ditentukan bobot persentase rarity

	# KAMUS LOKAL
	# max1, max2, max3 : integer
	# arr : array[1..10] of character

	# ALGORITMA

	# mengurutkan bobot rarity
	max1 = int(max([rarity[0][1], rarity[2][1], rarity[1][1]]))
	if max1 == rarity[0][1]:
		max2 = int(max([rarity[1][1], rarity[2][1]]))
		max3 = int(min([rarity[1][1], rarity[2][1]]))
	elif max1 == rarity[2][1]:
		max2 = int(max([rarity[0][1], rarity[1][1]]))
		max3 = int(min([rarity[0][1], rarity[1][1]]))
	else:
		max2 = int(max([rarity[0][1], rarity[2][1]]))
		max3 = int(min([rarity[0][1], rarity[2][1]]))

	arr = ['C']
	for i in range(len(rarity)):
		if rarity[i][1] == max1:
			for j in range(4):
				arr.append(rarity[i][0])
		elif rarity[i][1] == max2:
			for j in range(3):
				arr.append(rarity[i][0])
		else:  # rarity[i][1] == max3
			for j in range(2):
				arr.append(rarity[i][0])
	
	return chooser(arr)

def nextrarity(rarity): # -> character
	# mengembalikan rarity satu tingkat di atasnya
	
	# ALGORITMA
	
	if rarity == 'C':
		return 'B'
	elif rarity == 'B':
		return 'A'
	return 'S'

def searchrarity(rarity): # -> array of array of any
	# mencari item di consumable.csv dengan rarity tertentu

	# KAMUS LOKAL
	# items, datas : array of array of any
	# i : integer

	# ALGORITMA

	items = []
	datas = readCSV("consumable.csv")[1]
	for i in range(len(datas)):
		if datas[i][getCol("consumable.csv", "rarity")] == rarity:
			items.append(datas[i])
	return items

# FUNGSI2 UTAMA

def filteritem(user_id): # -> array of array of any
	# mengembalikan data consumable milik user yang pernah diambil

	# KAMUS LOKAL
	# datas_all, inventory : array of array of any
	# item_id, stok, item_numambil, item_name, item_rarity : string

	# ALGORITMA

	datas_all = readCSV("consumable_history.csv")[1]
	inventory = []
	for i in range(len(datas_all)):
		if datas_all[i][1] == user_id: # ada pengambilan dari user
			item_id = datas_all[i][2]
			stok = datas_all[i][4]
			item_numambil = datas_all[i][0]
			item_name = readCSVdata("consumable.csv", getRow("consumable.csv", item_id), getCol("consumable.csv", "nama"))
			item_rarity = readCSVdata("consumable.csv", getRow("consumable.csv", item_id), getCol("consumable.csv", "rarity"))
			inventory.append([item_id, item_name, item_rarity, stok, item_numambil])
	return inventory

def korbaninitem(user_id, inventory): # -> array[1..2] of  any
	# Menerima item yang dipilih user dan mengembalikan chance rarity di atas rarity item yang dipilih
	
	# KAMUS LOKAL
	# num : 

	# ALGORITMA

	# print daftar inventory ke layar
	print("\nInventory:")
	num = 1
	for i in range(len(inventory)):
		if int(inventory[i][3]) > 0:
			print(str(num) + ".", inventory[i][1], "(Rarity " + inventory[i][2] + ")", inventory[i][3])
		num += 1
	print()

	# prompt pilihan consumable
	num = int(input("Pilih consumable yang mau digunakan: "))

	if (num >= 1) & (num <= len(inventory)): # validasi prompt pilihan consumable
		
		item_id = inventory[num-1][0]
		item_name = inventory[num-1][1]
		item_rarity = inventory[num-1][2]
		item_numambil = inventory[num-1][4]
		stok = int(inventory[num-1][3])

		jml = int(input("Jumlah yang digunakan: "))

		if (jml > 0) & (jml <= stok): # validasi stok
			
			# kurangin jml dari inventory
			inventory[num-1][3] = str(stok-jml)
			# biar jumlah ada ngaruhnya juga meskipun dikit
			chance = round(prng() * 0.01 * jml, 2)
			
			print(jml, item_name, "ditambahkan!")
			print("Chance mendapatkan rarity", nextrarity(item_rarity), "+" + str(chance) + "%")
			return [[nextrarity(item_rarity), chance], inventory]

		else:
			print("Input jumlah tidak valid karena tidak sesuai dengan stok.")

	else:
		print("Input tidak valid!")

def gacha(role, user_id):
	# memberikan barang tertentu ke user secara pseudo-random. 
	# chance dapat ditingkatkan dengan menambahkan barang dari inventory

	# KAMUS LOKAL
	# rarity: array[1..3] of array[1..2] of any
	# inventory: array of array of any
	# prompt, rarity_result: character
	# result, bekal: array[1..2] of any
	# gacha_result: array of any
	# stok_database, jml_result, id: integer
	# tgl: string

	# ALGORITMA

	# validasi role User
	if role == "User":
		rarity = [['B', 0], ['A', 0], ['S', 0]]
		inventory = filteritem(str(user_id))

		# validasi inventory
		if len(inventory) > 0:

			prompt = 'y'
			while prompt in "Yy":
				
				# tambah chance dengan item di inventory
				result = korbaninitem(user_id, inventory)
				bekal = result[0] # rarity + persentase
				inventory = result[1] # sisa inventory

				# persentase ditambahkan ke rarity
				if bekal[0] == 'B':
					rarity[0][1] += bekal[1]
				elif bekal[0] == 'A':
					rarity[1][1] += bekal[1]
				elif bekal[0] == 'S':
					rarity[2][1] += bekal[1]

				# prompt mengulang tambah chance item
				prompt = input("Tambahkan item lagi? (y/n): ")
				if prompt not in 'YyNn':
					prompt = input("Tambahkan item lagi? (y/n): ")

			print("\nRolling...")
			time.sleep(2)

			# pilih rarity
			rarity_result = raritychooser(rarity)
			# pilih item dengan rarity sesuai
			gacha_result = chooser(searchrarity(rarity_result))

			# cek stok database
			stok_database = int(readCSVdata("consumable.csv", getRow("consumable.csv", gacha_result[0]), getCol("consumable.csv", "jumlah")))
			# pilih jumlah item yang diberikan sesuai stok database
			jml_result = numchooser(stok_database)

			# validasi jumlah yang diberikan
			if jml_result > 0:
				print("Selamat, anda mendapatkan", jml_result, gacha_result[1], "(Rank " + rarity_result + ")!")
			else: # jml_result == 0
				print("Maaf, anda sedang tidak beruntung. Coba lagi.")

			# kurangi jumlah item hasil gacha di consumable.csv
			editCSVdata("consumable.csv", getRow("consumable.csv", gacha_result[0]), getCol("consumable.csv", "jumlah"), stok_database-jml_result)
			
			# tambah entry hasil gacha ke consumable_history.csv
			id = int(len(readCSV("consumable_history.csv")[1])+1)
			tgl = datetime.datetime.now().strftime('%d/%m/%Y')
			addCSVdata("consumable_history.csv", [id, user_id, gacha_result[0], tgl, jml_result])

		else: # len(inventory) == 0
			print("Inventory kosong. Anda tidak dapat melakukan gacha.")

	else: # role != user
		print("Admin tidak dapat melakukan gacha.")