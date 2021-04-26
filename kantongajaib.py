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

from tambahitem import tambahitem
from hapusitem import hapusitem
from ubahjumlah import ubahjumlah

role = ""
user_input = input(">>> ")
while (user_input != "exit"):
    if (user_input == "login"):
        role = login() # nyimpen role user
    elif (user_input == "register"):
        register(role)
    elif (user_input == "help"):
        help(role)
    
    # pilihan fungsi dari input
    elif (user_input == "tambahitem"):
        tambahitem(role)
    elif (user_input == "ubahjumlah"):
        ubahjumlah(role)
    elif (user_input == "hapusitem"):
        hapusitem(role)
    
    user_input = input(">>> ")
