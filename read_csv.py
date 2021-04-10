# Library buatan sendiri >:(

# KAM00S
header = ""
datas = []
csv_file = "gadget.csv"
int_idx = [3,5]

# KUMPULAN FUNGSI PENUNJANG

def convDataToString(header, datas):
	# convert data ke string untuk dimasukkan ke csv
	str_data = ",".join(header) + "\n"
	for data in datas:
		arr_data_string = [str(i) for i in data]
		str_data += ",".join(arr_data_string) + "\n"
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

def dataToInt(arr):  # -> array mix
	# ubah tipe data yang idxnya di arr jadi integer
	for i in range(6):
		if i in int_idx:
			arr[i] = int(arr[i])
	return arr

# FUNGSI UTAMA

def readCSV(csv_file):
	# baca data mentah dari csv
	f = open(csv_file,"r")
	raw_lines = f.readlines()
	f.close()
	lines = [raw_line.replace("\n", "") for raw_line in raw_lines]

	# pisah header dari data2
	global header
	header = stringSplitStrip(lines.pop(0), ",")

	# variabel data dalam bentuk array
	global datas
	for line in lines:
		raw_array_of_data = stringSplitStrip(line, ",")
		array_of_data = [data.strip() for data in raw_array_of_data]
		array_of_data = dataToInt(array_of_data)
		datas.append(array_of_data)

def addCSVdata(inputs):
	datas.append(inputs)

def editCSVdata(idx, col, val):
	# modifikasi data
	datas[idx][col] = val

def saveCSV(header, datas, csv_file):
	# menyimpan kembali header+data dalam csv
	data_string = convDataToString(header, datas)
	f = open(csv_file, "w")
	f.write(data_string)
	f.close()