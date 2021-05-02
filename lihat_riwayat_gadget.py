from csv_stuffs import readCSV, readCSVdata, getRow, getCol
from tgl import sort_data_date, sort_data_date_1

# Melihat Riwayat Peminjaman Gadget
def lihat_riwayat_pinjam_gadget(role): # Melihat riwayat pengambilan consumable
    if role == "Admin": # Validasi role Admin
        datas_gadget_borrow_history = readCSV("gadget_borrow_history.csv")
        datas_gadget = readCSV("gadget.csv")

        sort_data_date(datas_gadget_borrow_history[1]) # Mengurutkan data terbaru berdasarkan tanggal

        if datas_gadget_borrow_history[1] == []: # gadget_borrow_history.csv kosong
            print("Belum ada peminjaman gadget")

        else: # gadget_borrow_history.csv tidak kosong
            if len(datas_gadget_borrow_history[1]) <= 5: # saat data <= 5
                for i in range(len(datas_gadget_borrow_history[1])):
                    print("ID Peminjaman       : " + str(datas_gadget_borrow_history[1][i][0]))
                    nama = readCSVdata("user.csv", getRow("user.csv", int(datas_gadget_borrow_history[1][i][1])), 2)
                    print("Nama Peminjam       : " + nama)
                    for j in range(len(datas_gadget[1])):
                        if datas_gadget_borrow_history[1][i][2] == datas_gadget[1][j][0]:
                            print("Nama Gadget         : " + str(datas_gadget[1][j][1]))
                    print("Tanggal Peminjam    : " + str(datas_gadget_borrow_history[1][i][3]))
                    print("Jumlah              : " + str(datas_gadget_borrow_history[1][i][4]))
                    print("")
            else: # saat data > 5
                idx = 0
                while idx < 5:
                    print("ID Peminjaman       : " + str(datas_gadget_borrow_history[1][idx][0]))
                    nama = readCSVdata("user.csv", getRow("user.csv", int(datas_gadget_borrow_history[1][idx][1])), 2)
                    print("Nama Peminjam       : " + nama)
                    for j in range(len(datas_gadget[1])):
                        if datas_gadget_borrow_history[1][idx][2] == datas_gadget[1][j][0]:
                            print("Nama Gadget         : " + str(datas_gadget[1][j][1]))
                    print("Tanggal Peminjaman  : " + str(datas_gadget_borrow_history[1][idx][3]))
                    print("Jumlah              : " + str(datas_gadget_borrow_history[1][idx][4]))
                    print("")
                    idx += 1
                    
    else: # Role != Admin
        print("Anda tidak bisa mengakses riwayat!")
              
# Melihat Riwayat Pengembalian Gadget
def lihat_riwayat_kembalikan_gadget(role): # Melihat riwayat pengambilan consumable
    if role == "Admin": # Validasi role Admin
        datas_gadget_return_history = readCSV("gadget_return_history.csv")
        datas_gadget_borrow_history = readCSV("gadget_borrow_history.csv")
        datas_gadget = readCSV("gadget.csv")

        if datas_gadget_return_history[1] == []: # Data kosong
            print("Belum ada gadget yang dikembalikan")

        else: # Data tidak kosong
            sort_data_date_1(datas_gadget_return_history[1]) # Mengurutkan data terbaru berdasarkan tanggal

            if len(datas_gadget_return_history[1]) <= 5: # saat data <= 5
                for i in range(len(datas_gadget_return_history[1])):

                    # Menampilkan ID pengambilan
                    print("ID Pengembalian        : " + str(datas_gadget_return_history[1][i][0]))

                    for j in range(len(datas_gadget_borrow_history[1])):
                        if datas_gadget_return_history[1][i][1] == datas_gadget_borrow_history[1][j][0]:
                            # Menampilkan nama Pengambil
                            nama = readCSVdata("user.csv", getRow("user.csv", int(datas_gadget_borrow_history[1][j][1])), 2)
                            print("Nama Pengambil         : " + nama)
                            #print("Nama Pengambil         : " + str(datas_gadget_borrow_history[1][j][1]))

                    for k in range(len(datas_gadget_borrow_history[1])):
                        if datas_gadget_return_history[1][i][1] == datas_gadget_borrow_history[1][k][0]:
                            for l in range(len(datas_gadget[1])):
                                if datas_gadget_borrow_history[1][k][2] == datas_gadget[1][l][0]:
                                    # Menampilkan nama gadget yang diambil
                                    print("Nama Gadget            : " + str(datas_gadget[1][l][1]))

                    # Menampilkan tanggal
                    print("Tanggal Pengembalian   : " + str(datas_gadget_return_history[1][i][2]))
                    print("")

            else: # saat data > 5
                idx = 0
                while idx < 5:

                    # Menampilkan ID pengambilan
                    print("ID Pengambilan        : " + str(datas_gadget_return_history[1][idx][0]))

                    for j in range(len(datas_gadget_borrow_history[1])):
                        if datas_gadget_return_history[1][idx][1] == datas_gadget_borrow_history[1][j][0]:
                            # Menampilkan nama Pengambil
                            nama = readCSVdata("user.csv", getRow("user.csv", int(datas_gadget_borrow_history[1][j][1])), 2)
                            print("Nama Pengambil        : " + nama)
                            #print("Nama Pengambil        : " + str(datas_gadget_borrow_history[1][j][1]))

                    for k in range(len(datas_gadget_borrow_history[1])):
                        if datas_gadget_return_history[1][idx][1] == datas_gadget_borrow_history[1][k][0]:
                            for l in range(len(datas_gadget[1])):
                                if datas_gadget_borrow_history[1][k][2] == datas_gadget[1][l][0]:
                                    # Menampilkan nama gadget yang diambil
                                    print("Nama Gadget           : " + str(datas_gadget[1][l][1]))

                    print("Tanggal Pengembalian  : " + str(datas_gadget_return_history[1][idx][2]))
                    print("")
                    idx += 1
                    
    else: # Role != Admin
        print("Anda tidak bisa mengakses riwayat!")
