import datetime
import time
from csv_stuffs import readCSV, readCSVdata, getRow, getCol, editCSVdata, addCSVdata

def prng(): # -> real
	# pseudo-random number generator.
	h = int(datetime.datetime.now().strftime("%H"))
	m = int(datetime.datetime.now().strftime("%M"))
	s = int(datetime.datetime.now().strftime("%S"))
	j = int(datetime.datetime.now().strftime("%j"))
	percentage = round((h * m + s * j) % 100) # apakah terlalu wangy
	if percentage == 0:
		prng()
	return percentage

def chooser(arr):
	# choose an element from array by prng approach
	if len(arr) > 0:
		kocokan = prng()
		bobot_elmt = 100 / len(arr)
		i = 1
		for elmt in arr:
			if kocokan <= bobot_elmt * i:
				return elmt
			else:
				i += 1
	return None

def numchooser(n):
	# memilih bilangan dari 1 sampai n
	if n > 0:
		numlist = []
		for i in range(1, n+1):
			numlist.append(i)
		return chooser(numlist)
	else:
		return 0

def raritychooser(rarity):
	# pilih rarity, yang banyak-sedikit chancenya ditentukan persentase
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
		else:
			for j in range(2):
				arr.append(rarity[i][0])
	
	return chooser(arr)

def nextrarity(rarity):
	if rarity == 'C':
		return 'B'
	elif rarity == 'B':
		return 'A'
	return 'S'

def searchrarity(rarity):
	items = []
	datas = readCSV("consumable.csv")[1]
	for i in range(len(datas)):
		if datas[i][getCol("consumable.csv", "rarity")] == rarity:
			items.append(datas[i])
	return items

# FUNGSI2 UTAMA

def filteritem(user_id):
	# masuk2in yang punya si user dari consumable history ke inventory
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

def korbaninitem(user_id, inventory):
	user_id_col = 1

	# print daftar inventory ke layar
	print("\nInventory:")
	num = 1
	for i in range(len(inventory)):
		if int(inventory[i][3]) > 0:
			print(str(num) + ".", inventory[i][1], "(Rarity " + inventory[i][2] + ")", inventory[i][3])
		num += 1
	print()

	# input prompt
	num = int(input("Pilih consumable yang mau digunakan: "))

	if (num >= 1) & (num <= len(inventory)): # validasi jumlah
		
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

	if role == "User":
		rarity = [['B', 0], ['A', 0], ['S', 0]]

		inventory = []
		inventory = filteritem(str(user_id))

		if len(inventory) > 0:

			prompt = 'y'
			while prompt in "Yy":
				
				result = korbaninitem(user_id, inventory)
				bekal = result[0] # rarity + persentase
				inventory = result[1] # sisa inventory

				# masukin bekel ke rarity
				if bekal[0] == 'B':
					rarity[0][1] += bekal[1]
				elif bekal[0] == 'A':
					rarity[1][1] += bekal[1]
				elif bekal[0] == 'S':
					rarity[2][1] += bekal[1]

				prompt = input("Tambahkan item lagi? (y/n): ")
				if prompt not in 'YyNn':
					prompt = input("Tambahkan item lagi? (y/n): ")

			print("\nRolling...")
			time.sleep(2)

			rarity_result = raritychooser(rarity)
			gacha_result = chooser(searchrarity(rarity_result))

			stok_database = int(readCSVdata("consumable.csv", getRow("consumable.csv", gacha_result[0]), getCol("consumable.csv", "jumlah")))
			jml_result = numchooser(stok_database)

			if jml_result > 0:
				print("Selamat, anda mendapatkan", jml_result, gacha_result[1], "(Rank " + rarity_result + ")!")
			else:
				print("Maaf, anda sedang tidak beruntung. Coba lagi.")

			# ubahjumlah di consumable.csv
			editCSVdata("consumable.csv", getRow("consumable.csv", gacha_result[0]), getCol("consumable.csv", "jumlah"), stok_database-jml_result)
			
			# tambah entry ke consumable_history.csv
			id = int(len(readCSV("consumable_history.csv")[1])+1)
			tgl = datetime.datetime.now().strftime('%d/%m/%Y')
			addCSVdata("consumable_history.csv", [id, user_id, gacha_result[0], tgl, jml_result])

		else:
			print("Inventory kosong. Anda tidak dapat melakukan gacha.")


	else:
		print("Admin tidak dapat melakukan gacha.")