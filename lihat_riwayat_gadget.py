from csv_stuffs import readCSV
from tgl import sort_data_date

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
                    print("Nama Peminjam       : " + str(datas_gadget_borrow_history[1][i][1]))
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
                    print("Nama Peminjam       : " + str(datas_gadget_borrow_history[1][idx][1]))
                    for j in range(len(datas_gadget[1])):
                        if datas_gadget_borrow_history[1][idx][2] == datas_gadget[1][j][0]:
                            print("Nama Gadget         : " + str(datas_gadget[1][j][1]))
                    print("Tanggal Peminjaman  : " + str(datas_gadget_borrow_history[1][idx][3]))
                    print("Jumlah              : " + str(datas_gadget_borrow_history[1][idx][4]))
                    print("")
                    idx += 1
                    
    else: # Role != Admin
        print("Anda tidak bisa mengakses riwayat!)
              
# Melihat Riwayat Pengembalian Gadget
