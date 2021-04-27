from csv_stuffs import readCSV
from procedure_gadget import print_gadget_rarity

def cari_gadget_rarity(): # Menampilkan gadget berdasarkan rarity
    datas_gadget = readCSV("gadget.csv")
    
    input_rarity = str(input("Masukkan rarity: "))
    print("")
    print("Hasil pencarian:")
    print("")
                           
    print_gadget_rarity(datas_gadget, input_rarity)
