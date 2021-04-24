from csv_stuffs import readCSV

# FUNGSI UTAMA

def login(): # -> string
    log_username = input("Masukkan username: ")
    log_password = input("Masukkan password: ")

    # Validasi login
    validasi = check_login(log_username, log_password)
    if (validasi[0] == True): # Login valid
        print("Halo " + log_username + "! Selamat datang di Kantong Ajaib.")
        print()
        return validasi[1]
    else: # Login tidak valid
        print("Username atau password salah!")
        print()
        return validasi[1]

# FUNGSI PENUNJANG

def check_login(log_username, log_password): # -> (bool,string)

    data = readCSV("user.csv")
    database = data[1]

    # Simplifikasi indeks kolom
    username = 1
    password = 4
    role = 5

    # Validasi role user
    x = False
    y = ""
    for i in range(len(database)):
        if (database[i][username] == log_username and database[i][password] == log_password):
            x = True
            y = database[i][role]
    return x,y
