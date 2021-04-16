# ini biar bisa ngetes aja :v

import os
import argparse
parser = argparse.ArgumentParser()                          #
parser.add_argument("Direktori", nargs='?', default='')     #   Bagian awal program
args = parser.parse_args()                                  #

if args.Direktori != '':                            
    try: 
        print("Loading...")
        os.chdir(args.Direktori)    #Foldernya ada        
        print('Selamat datang di "Kantong Ajaib!"')
    except OSError: # Folder gada
        print("Folder tidak ditemukan!")
else:   # Gada input nama folder
    print("Tidak ada nama folder yang diberikan!")
    print("Usage: python kantongajaib.py <nama_folder>")


from login import login
from register import register
from help import help

role = ""
user_input = input(">>> ")
while (user_input != "exit"):
    if (user_input == "login"):
        role = login() # nyimpen role user
    elif (user_input == "register"):
        register(role)
    elif (user_input == "help"):
        help(role)
    user_input = input(">>> ")
