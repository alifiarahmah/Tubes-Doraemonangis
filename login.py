# maaf kalo gagal paham soal github :)
from csv_stuffs import readCSV

# FUNGSI UTAMA

def login(): # -> string
    log_username = input("Masukkan username: ")
    log_password = input("Masukkan password: ")

    # validasi berupa tuple (boolean,string)
    validasi = check_login(log_username, log_password)
    if (validasi[0] == True): # kalau berhasil login, return role nya
        print("Berhasil login!")
        print()
        return validasi[1]
    else: # kalau salah, return "", jadi variabel di main nggak berubah nilainya
        print("Username atau password salah!")
        print()
        return validasi[1]

# FUNGSI PENUNJANG

def check_login(log_username, log_password): # -> (bool,string)

    # buka data csv, cuma perlu bagian isi
    data = readCSV("user.csv")
    database = data[1]

    # indeks kolom username = 1, password = 4, role = 5
    username = 1
    password = 4
    role = 5

    # kalo username dan password terdapat di database, return (true,role nya)
    # kalo username dan password berbeda di database, return (false,"")
    x = False
    y = ""
    for i in range(len(database)):
        if (database[i][username] == log_username and database[i][password] == log_password):
            x = True
            y = database[i][role]
    return x,y
