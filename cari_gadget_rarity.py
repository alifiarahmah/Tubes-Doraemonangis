from csv_stuffs import readCSV
from procedure_gadget import print_gadget_rarity

def cari_gadget_rarity(): # Menampilkan gadget berdasarkan rarity
    datas_gadget = readCSV("gadget.csv")
    
    input_rarity = str(input("Masukkan rarity: "))
    
    if (input_rarity not in 'CBAS'):
        print("Rarity tidak valid!")
    else:
        print("")
        print("Hasil pencarian:")
        print("")
                           
        print_gadget_rarity(datas_gadget, input_rarity)
