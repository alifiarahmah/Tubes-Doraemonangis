"""
## daftar fungsi/prosedur yang bisa dipake ##

readCSV(csv_file: string) -> [header: array of string, datas: array of array]
	baca file csv dari csv_file
	contoh: readCSV("user.csv") -> ['nama, kelas'], [['Anto','XII MIPA 5'],['Alex','X IPS']]
		ambil headernya aja -> readCSV("user.csv")[0]
		ambil datanya aja -> readCSV("user.csv")[1]

addCSVdata(csv_file: string, inputs: array of string)
	nambah data baru ke csv, inputs dalam bentuk array

readCSVdata(csv_file: string, idx: integer, col: integer) -> string
	baca data berdasar idx dan col-nya dalam csv

editCSVdata(csv_file: string, idx: integer, col: integer, val : string)
	edit data berdasar idx dan col-nya dalam csv

delCSVdata(csv_file: string, idx: integer)
	menghapus keseluruhan data pada indeks tertentu dalam file CSV

saveCSV(header: array of string, datas: array of terserah, csv_file: string)
	menyimpan header+data dalam csv

getCol(csv_file: string, col_name: string) -> integer
	return col ke-berapa dari nama kolom dalam csv, kalau tidak ada return None
	biar enak buat edit data
	contoh: getCol("user.csv", "alamat") -> 3

getRow(csv_file: string, row_name: string) -> integer
	return row ke-berapa dari id dalam csv, kalau tidak ada return None
	biar enak buat edit data
	contoh: getRow("consumable.csv", "C1") -> 0
"""

import os

# FUNGSI PENUNJANG, CUMA BUAT FUNGSI DALAM FUNGSI

def convDataToString(header, datas): # -> string
	# convert data ke string untuk dimasukkan ke csv
	str_data = ";".join(header) + "\n"
	for data in datas:
		arr_data_string = [str(i) for i in data]
		str_data += ";".join(arr_data_string) + "\n"
	return str_data

def stringSplitStrip(string, delimiter):  # -> array of string
	# pisah string menjadi array
	arr = []
	elmt = ""
	for c in string:
		if c == delimiter:
			arr.append(elmt)
			elmt = ""
		else:
			elmt += c
	arr.append(elmt)
	return arr

def dataToInt(csv_file, arr):  # -> array mix
	# ubah tipe data yang idxnya di arr jadi integer
	for i in range(lenCol(csv_file)):
		if i in intIdxList(csv_file):
			arr[i] = int(arr[i])
	return arr

def intIdxList(csv_file): # -> array of integer
	# penunjang fungsi dataToInt
	if csv_file == "user.csv":
		return [0]
	elif csv_file == "gadget.csv":
		return [3,5]
	elif csv_file == "consumable.csv":
		return [3]
	elif csv_file == "gadget_borrow_history.csv":
		return [0,4]
	elif csv_file == "gadget_return_history.csv":
		return [0,1]
	elif csv_file == "consumable_history.csv":
		return [0,4]
	else:
		return [3]
		

def lenCol(csv_file):
	if (csv_file == "user.csv") | (csv_file == "gadget.csv"):
		return 6
	elif (csv_file == "consumable.csv") | (csv_file == "gadget_borrow_history.csv"):
		return 5
	elif (csv_file == "consumable_history.csv") | (csv_file == "gadget_return_history.csv"):
		return 4
	else:
		return 4


# FUNGSI PANGGILABLE BUAT GAMPANGIN AJA

def readCSVdata(csv_file, idx, col):
	datas = readCSV(csv_file)[1]
	return datas[idx][col]

def getCol(csv_file, col_name): # -> integer
	# return col ke-berapa dari nama kolom + csv
	# biar enak buat edit data
	header = readCSV(csv_file)[0]
	try:
		for i in range(len(header)):
			if header[i] == col_name:
				return i
	except:
		return None

def getRow(csv_file, row_id): # -> integer
	# return row ke-berapa dari id dalam csv
	# biar enak buat edit data
	datas = readCSV(csv_file)[1]
	try:
		for i in range(len(datas)):
			if datas[i][0] == row_id:
				return i
	except:
		return None


# FUNGSI UTAMA

def readCSV(csv_file):  # -> [header: array of string, datas: array of array]
	# baca data mentah dari csv
	f = open(csv_file,"r")
	raw_lines = f.readlines()
	f.close()
	lines = [raw_line.replace("\n", "") for raw_line in raw_lines]

	header = ""
	header = stringSplitStrip(lines.pop(0), ";")

	datas = []
	for line in lines:
		raw_array_of_data = stringSplitStrip(line, ";")
		array_of_data = [data.strip() for data in raw_array_of_data]
		array_of_data = dataToInt(csv_file, array_of_data)
		datas.append(array_of_data)

	return header, datas

def addCSVdata(csv_file, inputs):
	# nambah data baru ke csv, inputs dalam bentuk array
	header = readCSV(csv_file)[0]
	datas = readCSV(csv_file)[1]
	datas.append(inputs)
	saveCSV(header, datas, csv_file)

def editCSVdata(csv_file, idx, col, val):
	# edit data berdasar idx dan col-nya dalam csv
	header = readCSV(csv_file)[0]
	datas = readCSV(csv_file)[1]
	datas[idx][col] = val
	saveCSV(header, datas, csv_file)

def delCSVdata(csv_file, idx):
	# menghapus keseluruhan data pada indeks tertentu dalam file CSV
	header = readCSV(csv_file)[0]
	datas = readCSV(csv_file)[1]
	datas.pop(idx)
	saveCSV(header, datas, csv_file)

def saveCSV(header, datas, csv_file):
	# menyimpan header+data dalam csv
	data_string = convDataToString(header, datas)
	f = open(csv_file, "w")
	f.write(data_string)
	f.close()

def getListCSV(cond):
	# mengembalikan list berisi semua file csv pada Current Working Directory
	temp = []
	for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
		# membuat list sementara untuk semua file dalam direktori
		temp.extend(filenames)
		break
		
	ListCSV = []
	if (cond == "no_temp"):
		# tanpa file temp
		for i in range(len(temp)):
		# membuat list dari file yang bertipe csv dan tidak diawali 'temp_' (filter)
			if ((temp[i].rfind('.csv') == (len(temp[i])-4)) and (temp[i].find('temp_') != 0)) :
				ListCSV.append(temp[i])
				
	elif (cond == "only_temp"):
		# hanya file temp
		for i in range(len(temp)):
		# membuat list dari file yang bertipe csv dan diawali 'temp_' (filter)
			if ((temp[i].rfind('.csv') == (len(temp[i])-4)) and (temp[i].find('temp_') == 0)) :
				ListCSV.append(temp[i])
	return ListCSV
		
# referensi:
# Tutorial 1 : Read dan Save Data dari CSV tanpa library di python - Mario Gunawan
# https://13518114.medium.com/tubes-walkthrough-1-read-data-dari-csv-tanpa-library-605a6afe92db
