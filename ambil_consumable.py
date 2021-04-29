from csv_stuffs import readCSV, saveCSV
from tgl import isTglValid

def ambil_consumable(role):
    if (role == "Admin"): # Validasi role user
        print("Admin tidak bisa mengambil consumable")
        
    else: # Role = User
        datas_consumable = readCSV("consumable.csv")
        datas_consumable_history = readCSV("consumable_history.csv")
        
        if datas_consumable[1] == []: # Data consumable kosong
            print("Belum ada consumable tersedia")

        else: # Data consumable tidak kosong
            minta_id = input("Masukkan ID item: ") # Input id consumable yang ingin diambil
            count_check = 0
            loop = True
            history_nama = ""
            while loop: # Looping untuk validasi input id
                for i in range(len(datas_consumable[1])):
                    if minta_id == datas_consumable[1][i][0]:
                        count_check += 1
                        history_nama = datas_consumable[1][i][1]
                if count_check > 0:
                    loop = False
                else:
                    print("ID item tidak ada, ulangi!")
                    minta_id = input("Masukkan ID item: ")

            minta_jumlah = int(input("Jumlah: ")) # Input jumlah consumable yang ingin diambil
            amount_check = 0
            loop = True
            history_jumlah = 0
            while loop: # Looping untuk validasi input jumlah dengan jumlah consumable yang ada
                for i in range(len(datas_consumable[1])):
                    if minta_id == datas_consumable[1][i][0]:
                        amount_check = datas_consumable[1][i][3]
                if 0 <= minta_jumlah <= amount_check:
                    history_jumlah = minta_jumlah
                    loop = False
                else:
                    print("Jumlah yang diambil tidak valid dengan stok yang ada, ulangi!")
                    minta_jumlah = int(input("Jumlah: "))

            minta_tanggal = input("Tanggal pengambilan: ") # Input tanggal pengambilan consumable
            while not(isTglValid(minta_tanggal)): # Validasi tanggal
                print("Tanggal tidak valid, ulangi!")
                minta_tanggal = input("Tanggal peminjaman: ")
            history_tanggal = minta_tanggal

            item = ""
            for i in range(len(datas_consumable[1])):
                if minta_id == datas_consumable[1][i][0]:
                    item = datas_consumable[1][i][1]
                    jumlah = int(datas_consumable[1][i][3]) - minta_jumlah
                    datas_consumable[1][i][3] = jumlah

            print("")
            print("Item '" + str(item) + " (x" + str(minta_jumlah) + ")' telah berhasil diambil!")

            if datas_consumable_history[1] == []: # Saat consumable_history.csv masih kosong
                history_id = 1
            else: # Saat ada data di consumable_history.csv
                history_id = datas_consumable_history[1][-1][0] + 1
            history = [history_id, role, history_nama, history_tanggal, history_jumlah]
            datas_consumable_history[1].append(history) # Menggabungkan history ke csv history consumable
            
            # Simpan pengubahan pada ke-2 csv
            saveCSV(datas_consumable[0], datas_consumable[1], "consumable.csv") # 
            saveCSV(datas_consumable_history[0], datas_consumable_history[1], "consumable_history.csv")
