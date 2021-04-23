import os

def load(dir_path):
	try:
		os.chdir(dir_path) # Nge-set Working Directory
		print('Selamat datang di "Kantong Ajaib!"') 
		return True
	except OSError: # Foldernya gaada
		print("Folder tidak ditemukan!")
		return False
