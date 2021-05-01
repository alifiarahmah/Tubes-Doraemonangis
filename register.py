from csv_stuffs import saveCSV, readCSV

# FUNGSI UTAMA

def register(role): # -> ()

    # Validasi status login
    if (role == ""):
        print("Silahkan login terlebih dahulu!")
        return
    
    # Sudah login sebagai Admin
    elif (role == "Admin"):

        reg_nama = input("Masukkan nama     : ")
        reg_username = input("Masukkan username : ")

        # Validasi username
        if check_regis(reg_username):
            print("Username tidak tersedia.")
            return
        else: 
            reg_password = input("Masukkan password : ")
            reg_alamat = input("Masukkan alamat   : ")

        data = readCSV("user.csv")
        database = data[1]
        header = data[0]

        reg_id = database[-1][0] + 1

        reg_array = [reg_id, reg_username, reg_nama.title(), reg_password, reg_alamat, "User"]
        database += [reg_array]

        saveCSV(header, database, "user.csv")

        print("User " + reg_username + " telah berhasil register ke dalam Kantong Ajaib.")
        return

    else: # Sudah login sebagai User
        print("Anda tidak dapat melakukan registrasi, harap hubungi Admin.")


# FUNGSI PENUNJANG

def check_regis(reg_username): # -> bool

    data = readCSV("user.csv")
    database = data[1]

    # Simplifikasi indeks kolom
    username = 1

    # Validasi username
    x = False
    for i in range(len(database)):
        if (database[i][username] == reg_username):
            x = True
    return x
