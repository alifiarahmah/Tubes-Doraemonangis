from csv_stuffs import saveCSV, readCSV

# FUNGSI UTAMA

def register(role): # -> ()

    # kalo role nya kosong, artinya belom login
    if (role == ""):
        print("Silahkan login terlebih dahulu!")
        print()
        return
    
    # kalo udah login, role nya admin, baru bisa
    elif (role == "Admin"):

        reg_nama = input("Masukkan nama: ")
        reg_username = input("Masukkan username: ")

        # cek username nya udah ada yang make ato belom (asumsi yang dicek cuma username)
        if check_regis(reg_username): # username sudah ada, langsung end
            print("Username tidak tersedia.")
            print()
            return
        else: # username belum ada, baru bisa lanjut
            reg_password = input("Masukkan password: ")
            reg_alamat = input("Masukkan alamat: ")

        # buka data, pisahin header dan isi
        data = readCSV("D:\\STEI ITB\\Semester 2\\MoonIF\\IF\\tubes2\\user.csv")
        database = data[1]
        header = data[0]

        # masukin id baru, +1 dari id terakhir
        reg_id = database[-1][0] + 1

        # jadiin input user array, tambahin ke array database
        reg_array = [reg_id, reg_username, reg_nama.title(), reg_password, reg_alamat, "User"]
        database += [reg_array]

        # save data yang baru
        saveCSV(header, database, "D:\\STEI ITB\\Semester 2\\MoonIF\\IF\\tubes2\\user.csv")

        print("Registrasi berhasil dilakukan!")
        print()
        return

    else: # x == "user", user tidak bisa registrasi
        print("Anda tidak dapat melakukan registrasi, harap hubungi Admin.")
        print()


# FUNGSI PENUNJANG

def check_regis(reg_username): # -> bool

    # buka data, cuma perlu bagian isi
    data = readCSV("D:\\STEI ITB\\Semester 2\\MoonIF\\IF\\tubes2\\user.csv")
    database = data[1]

    # indeks kolom username = 1, biar enak liatnya
    username = 1

    # kalau ketemu username sama, return true
    x = False
    for i in range(len(database)):
        if (database[i][username] == reg_username):
            x = True
    return x
