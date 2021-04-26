import os

def load_data(dir_path):
    try:
        os.chdir(dir_path) # Nge-set Working Directory
        print('Selamat datang di "Kantong Ajaib!"') 
    except OSError: # Foldernya gaada
        print("Folder tidak ditemukan!")
