# ini biar bisa ngetes aja :v

import os
import argparse
from load import load_data
parser = argparse.ArgumentParser()                          #
parser.add_argument("Direktori", nargs='?', default='')     #   Bagian awal program
args = parser.parse_args()                                  #

if args.Direktori != '':                            
        print("Loading...")
        load_data(args.Direktori)
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
