from csv_stuffs import readCSV
from procedure_gadget import print_gadget_tahun

def cari_gadget_tahun(): # Menampilkan gadget berdasarkan tahun ditemukan
    datas_gadget = readCSV("gadget.csv")
    
    input_tahun = int(input("Masukkan tahun: "))
    input_kategori = input("Masukkan kategori: ")
    print("")
    print("Hasil pencarian")
    print("")
    
    print_gadget_tahun(datas_gadget, input_tahun, input_kategori)
