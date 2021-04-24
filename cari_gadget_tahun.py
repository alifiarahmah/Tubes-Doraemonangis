from csv_stuffs import readCSV

def cari_gadget_tahun(): # Menampilkan gadget berdasarkan tahun ditemukan
    datas_gadget = readCSV("gadget.csv")
    
    input_tahun = int(input("Masukkan tahun: "))
    input_kategori = input("Masukkan kategori: ")
    print("")
    print("Hasil pencarian")
    print("")
    
    if input_kategori == "=":
        count = 0
        for i in range(len(datas_gadget)): # Pada tahun YYYY
            if input_tahun == int(datas_gadget[i][5]):
                print("Nama              : " + str(datas_gadget[i][1]))
                print("Deskripsi         : " + str(datas_gadget[i][2]))
                print("Jumlah            : " + str(datas_gadget[i][3]))
                print("Rarity            : " + str(datas_gadget[i][4]))
                print("Tahun Ditemukan   : " + str(datas_gadget[i][5]))
                print("")
                count += 1
        if count == 0:
            print("Tidak ada gadget yang ditemukan")
            
    elif input_kategori == ">": # Setelah tahun YYYY
        count = 0
        for i in range(len(datas_gadget)):
            if int(datas_gadget[i][5]) > input_tahun:
                print("Nama              : " + str(datas_gadget[i][1]))
                print("Deskripsi         : " + str(datas_gadget[i][2]))
                print("Jumlah            : " + str(datas_gadget[i][3]))
                print("Rarity            : " + str(datas_gadget[i][4]))
                print("Tahun Ditemukan   : " + str(datas_gadget[i][5]))
                print("")
                count += 1
        if count == 0:
            print("Tidak ada gadget yang ditemukan")
            
    elif input_kategori == "<": # Sebelum tahun YYYY
        for i in range(len(datas_gadget)):
            count = 0
            if int(datas_gadget[i][5]) < input_tahun:
                print("Nama              : " + str(datas_gadget[i][1]))
                print("Deskripsi         : " + str(datas_gadget[i][2]))
                print("Jumlah            : " + str(datas_gadget[i][3]))
                print("Rarity            : " + str(datas_gadget[i][4]))
                print("Tahun Ditemukan   : " + str(datas_gadget[i][5]))
                print("")
                count += 1
        if count == 0:
            print("Tidak ada gadget yang ditemukan")
            
    elif input_kategori == ">=": # Pada atau setelah tahun YYYY
        count = 0
        for i in range(len(datas_gadget)):
            if int(datas_gadget[i][5]) >= input_tahun:
                print("Nama              : " + str(datas_gadget[i][1]))
                print("Deskripsi         : " + str(datas_gadget[i][2]))
                print("Jumlah            : " + str(datas_gadget[i][3]))
                print("Rarity            : " + str(datas_gadget[i][4]))
                print("Tahun Ditemukan   : " + str(datas_gadget[i][5]))
                print("")
                count += 1
        if count == 0:
            print("Tidak ada gadget yang ditemukan")
            
    elif input_kategori == "<=": # Pada atau sebelum tahun YYYY
        count = 0
        for i in range(len(datas_gadget)):
            if int(datas_gadget[i][5]) <= input_tahun:
                print("Nama              : " + str(datas_gadget[i][1]))
                print("Deskripsi         : " + str(datas_gadget[i][2]))
                print("Jumlah            : " + str(datas_gadget[i][3]))
                print("Rarity            : " + str(datas_gadget[i][4]))
                print("Tahun Ditemukan   : " + str(datas_gadget[i][5]))
                print("")
                count += 1
        if count == 0:
            print("Tidak ada gadget yang ditemukan")
            
    else: # Kategori selain =, >, <, >=, <=
        print("Jenis kategori tidak valid!")