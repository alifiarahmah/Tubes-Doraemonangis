import os
from csv_stuffs import saveCSV 

# class object buat nyimpen data yang mau disave (dipakai diluar file ini)
class save_data_class(): 
	def __init__(self, header, datas, csv_file):
		self.header = header
		self.datas = datas
		self.csv_file = csv_file

	
def save(header, datas, csv_file):
	if ((header == "") and (datas == "") and (csv_file == "")):
		print("Tidak ada perubahan yang perlu disimpan")
		return None
	# else
	ans = str(input("Apakah anda ingin menyimpan perubahan di folder ini? (y/n): "))
	
	ansValid = False
		   
	while (not(ansValid)): 
		if ans == "y":	# penyimpanan di current working directory (cwd)
			saveCSV(header, datas, csv_file)
			ansValid = True
		elif ans == "n": # penyimpanan di folder/direktori lain
			folder_name = input("Masukkan nama folder penyimpanan: ")
			dir_save = os.path.dirname(os.path.abspath(__file__)) + "\\" + folder_name # direktori tujuan

			if os.path.exists(dir_save):
				# foldernya udah ada
				path = dir_save + "\\" + csv_file # direktori file tujuan
				saveCSV(header, datas, path)
			else:
				# foldernya belum ada
				print("Folder belum ada, akan dibuat folder baru")
				os.mkdir(dir_save) # foldernya dibuat
				path = dir_save + "\\" + csv_file # direktori file tujuan
				saveCSV(header, datas, path)
			ansValid = True	
		else: # jawaban tidak valid
			ans = str(input("Jawab dengan y(ya) atau n(tidak) !: "))	
	
	return None

def nosave():
	os.remove("gadget.csv")
	os.remove("consumable.csv")
	os.remove("consumable_history.csv")
	os.remove("gadget_return_history.csv")
	os.remove("gadget_borrow_history.csv")
	
	os.rename("gadget_temp.csv", "gadget.csv")
	os.rename("consumable_temp.csv", "consumable.csv")
	os.rename("consumable_history_temp.csv", "consumable_history")
	os.rename("gadget_return_history_temp.csv", "gadget_return_history.csv")
	os.rename("gadget_borrow_history_temp.csv", "gadget_borrow_history.csv")
	
	return None
