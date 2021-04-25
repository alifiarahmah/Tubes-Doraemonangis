from csv_stuffs import readCSV

def cari_gadget_rarity(): # Menampilkan gadget berdasarkan rarity
  
    datas_gadget = readCSV("gadget.csv")
    
    input_rarity = str(input("Masukkan rarity: "))
    print("")
    print("Hasil pencarian:")
    print("")
                           
    count = 0
    for i in range(len(datas_gadget)):
        if input_rarity.upper() == datas_gadget[i][4]:
            print("Nama              : " + str(datas_gadget[i][1]))
            print("Deskripsi         : " + str(datas_gadget[i][2]))
            print("Jumlah            : " + str(datas_gadget[i][3]))
            print("Rarity            : " + str(datas_gadget[i][4]))
            print("Tahun Ditemukan   : " + str(datas_gadget[i][5]))
            print("")
            count += 1
                           
    if count == 0: 
        print("Tidak ada gadget yang ditemukan")
