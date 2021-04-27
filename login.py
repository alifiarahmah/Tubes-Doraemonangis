from csv_stuffs import readCSV

# FUNGSI UTAMA

def login(role, user_id): # -> (string,int)
    
    if (role == ""):
        log_username = input("Masukkan username: ")
        log_password = input("Masukkan password: ")

        # Validasi login
        validasi = check_login(log_username, log_password)
        if (validasi[0] == True): # Login valid
            print("Halo " + log_username + "! Selamat datang di Kantong Ajaib.")
            print()
            return validasi[1], validasi[2]
        else: # Login tidak valid
            print("Username atau password salah!")
            print()
            return validasi[1], validasi[2]
        
    else: # Role sudah ada, sudah login sebelumnya
        print("Anda sudah login!")
        print()
        return role, user_id
        
# FUNGSI PENUNJANG

def check_login(log_username, log_password): # -> (bool,string,int)

    data = readCSV("user.csv")
    database = data[1]

    # Simplifikasi indeks kolom
    id_user = 0
    username = 1
    password = 4
    role = 5

    # Validasi role dan id user
    x = False
    y = ""
    z = 0
    
    for i in range(len(database)):
        if (database[i][username] == log_username and database[i][password] == log_password):
            x = True
            y = database[i][role]
            z = database[i][id_user]
    return x,y,z
