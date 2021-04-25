# Untuk cari_gadget_tahun
def print_gadget_tahun(data, tahun, kategori):
# print gadget berdasarkan input tahun dan kategori (=, <, <=, >, >=)
    if kategori == "=":
        count = 0
        for i in range(len(data[1])): # Pada tahun YYYY
            if tahun == int(data[1][i][5]):
                print("Nama              : " + str(data[1][i][1]))
                print("Deskripsi         : " + str(data[1][i][2]))
                print("Jumlah            : " + str(data[1][i][3]))
                print("Rarity            : " + str(data[1][i][4]))
                print("Tahun Ditemukan   : " + str(data[1][i][5]))
                print("")
                count += 1
        if count == 0:
            print("Tidak ada gadget yang ditemukan")

    elif kategori == ">":
        count = 0
        for i in range(len(data[1])): # Setelah tahun YYYY
            if tahun < int(data[1][i][5]):
                print("Nama              : " + str(data[1][i][1]))
                print("Deskripsi         : " + str(data[1][i][2]))
                print("Jumlah            : " + str(data[1][i][3]))
                print("Rarity            : " + str(data[1][i][4]))
                print("Tahun Ditemukan   : " + str(data[1][i][5]))
                print("")
                count += 1
        if count == 0:
            print("Tidak ada gadget yang ditemukan")

    elif kategori == ">=":
        count = 0
        for i in range(len(data[1])): # Pada atau setelah tahun YYYY
            if tahun <= int(data[1][i][5]):
                print("Nama              : " + str(data[1][i][1]))
                print("Deskripsi         : " + str(data[1][i][2]))
                print("Jumlah            : " + str(data[1][i][3]))
                print("Rarity            : " + str(data[1][i][4]))
                print("Tahun Ditemukan   : " + str(data[1][i][5]))
                print("")
                count += 1
        if count == 0:
            print("Tidak ada gadget yang ditemukan")

    elif kategori == "<":
        count = 0
        for i in range(len(data[1])): # Sebelum tahun YYYY
            if tahun > int(data[1][i][5]):
                print("Nama              : " + str(data[1][i][1]))
                print("Deskripsi         : " + str(data[1][i][2]))
                print("Jumlah            : " + str(data[1][i][3]))
                print("Rarity            : " + str(data[1][i][4]))
                print("Tahun Ditemukan   : " + str(data[1][i][5]))
                print("")
                count += 1
        if count == 0:
            print("Tidak ada gadget yang ditemukan")

    elif kategori == "<=":
        count = 0
        for i in range(len(data[1])): # Pada atau sebelum tahun YYYY
            if tahun >= int(data[1][i][5]):
                print("Nama              : " + str(data[1][i][1]))
                print("Deskripsi         : " + str(data[1][i][2]))
                print("Jumlah            : " + str(data[1][i][3]))
                print("Rarity            : " + str(data[1][i][4]))
                print("Tahun Ditemukan   : " + str(data[1][i][5]))
                print("")
                count += 1
        if count == 0:
            print("Tidak ada gadget yang ditemukan")

    else: # Selain =, >, <, >=, <=
        print("Jenis kategori tidak valid!")

# untuk cari_gadget_rarity
def print_gadget_rarity(data, rarity):
# print gadget berdasarkan input rarity
    count = 0
    for i in range(len(data[1])):
        if rarity.upper() == data[1][i][4]:
            print("Nama              : " + str(data[1][i][1]))
            print("Deskripsi         : " + str(data[1][i][2]))
            print("Jumlah            : " + str(data[1][i][3]))
            print("Rarity            : " + str(data[1][i][4]))
            print("Tahun Ditemukan   : " + str(data[1][i][5]))
            print("")
            count += 1

    if count == 0:
        print("Tidak ada gadget yang ditemukan")
