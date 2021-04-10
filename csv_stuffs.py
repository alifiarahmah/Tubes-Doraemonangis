# Library buatan sendiri >:(

## daftar fungsi/prosedur yang bisa dipake ##
# readCSV(csv_file: string) -> [header: array of string, datas: array of array]
	# baca file csv dari csv_file
# addCSVdata(csv_file: string, inputs: array of string)
	# nambah data baru ke csv, inputs dalam bentuk array
# editCSVdata(csv_file: string, idx: integer, col: integer, val)
	# edit data berdasar idx dan col-nya dalam csv
# saveCSV(header: array of string, datas: array of terserah, csv_file: string)
	# menyimpan header+data dalam csv
# getCol(csv_file: string, col_name: string) -> integer
	# return col ke-berapa dari nama kolom dalam csv, biar enak aja
	# biar enak buat edit data
# getRow(csv_file: string, col_name: string) -> integer
	# return row ke-berapa dari id dalam csv, biar enak aja
	# biar enak buat edit data

# FUNGSI PENUNJANG, CUMA BUAT FUNGSI DALAM FUNGSI

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

def dataToInt(csv_file, arr):  # -> array mix
	# ubah tipe data yang idxnya di arr jadi integer
	for i in range(6):
		if i in intIdxList(csv_file):
			arr[i] = int(arr[i])
	return arr

def intIdxList(csv_file):
	# penunjang fungsi dataToInt
	if csv_file == "user.csv":
		return [0]
	elif csv_file == "gadget.csv":
		return [3,5]
	elif csv_file == "consumable.csv":
		return [3]
	

# FUNGSI PANGGILABLE BUAT GAMPANGIN AJA

def getCol(csv_file, col_name):
	# return col ke-berapa dari nama kolom + csv, biar enak aja
	# biar enak buat edit data
	header = readCSV(csv_file)[0]
	for i in range(len(header)):
		if header[i] == col_name:
			return i

def getRow(csv_file, row_id):
	# return col ke-berapa dari judul kolom + csv, biar enak aja
	# biar enak buat edit data
	datas = readCSV(csv_file)[1]
	for i in range(len(datas)):
		if datas[i][0] == row_id:
			return i


# FUNGSI UTAMA

def readCSV(csv_file):
	# baca data mentah dari csv
	f = open(csv_file,"r")
	raw_lines = f.readlines()
	f.close()
	lines = [raw_line.replace("\n", "") for raw_line in raw_lines]

	header = ""
	header = stringSplitStrip(lines.pop(0), ",")

	datas = []
	for line in lines:
		raw_array_of_data = stringSplitStrip(line, ",")
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

def saveCSV(header, datas, csv_file):
	# menyimpan header+data dalam csv
	data_string = convDataToString(header, datas)
	f = open(csv_file, "w")
	f.write(data_string)
	f.close()