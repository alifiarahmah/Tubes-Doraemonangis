from csv_stuffs import readCSV, readCSVdata, getCol, getRow
from tgl import sort_data_date

def lihat_riwayat_consumable(role): # Melihat riwayat pengambilan consumable
    if role == "Admin": # Validasi role = Admin
        datas_consumable_history = readCSV("consumable_history.csv")
        
        if datas_consumable_history[1] == []:
            print("Belum ada pengambilan consumable")

        else:
            sort_data_date(datas_consumable_history[1]) # mengurutkan data terbaru berdasarkan tanggal
        
            if len(datas_consumable_history[1]) <= 5: # saat data <= 5
                for i in range(len(datas_consumable_history[1])):
                    print("ID Pengambilan      : " + str(datas_consumable_history[1][i][0]))
                    nama = readCSVdata("user.csv", getRow("user.csv", int(datas_consumable_history[1][i][1])), 2)
                    print("Nama Pengambil      : " + nama)
                    #print("Nama Pengambil      : " + str(datas_consumable_history[1][i][1]))
                    cons = readCSVdata("consumable.csv", getRow("consumable.csv", str(datas_consumable_history[1][i][2])), getCol("consumable.csv", "nama"))
                    print("Nama Consumable     : " + cons)
                    #print("Nama Consumable     : " + str(datas_consumable_history[1][i][2]))
                    print("Tanggal Pengambilan : " + str(datas_consumable_history[1][i][3]))
                    print("Jumlah              : " + str(datas_consumable_history[1][i][4]))
                    print("")
            else: # saat data > 5
                idx = 0
                while idx < 5:
                    print("ID Pengambilan      : " + str(datas_consumable_history[1][idx][0]))
                    nama = readCSVdata("user.csv", getRow("user.csv", int(datas_consumable_history[1][idx][1])), 2)
                    print("Nama Pengambil      : " + nama)
                    #print("Nama Pengambil      : " + str(datas_consumable_history[1][idx][1]))
                    cons = readCSVdata("consumable.csv", getRow("consumable.csv", str(datas_consumable_history[1][idx][2])), getCol("consumable.csv", "nama"))
                    print("Nama Consumable     : " + cons)
                    #print("Nama Consumable     : " + str(datas_consumable_history[1][idx][2]))
                    print("Tanggal Pengambilan : " + str(datas_consumable_history[1][idx][3]))
                    print("Jumlah              : " + str(datas_consumable_history[1][idx][4]))
                    print("")
                    idx += 1
                
    else: # Role != Admin
        print("Anda tidak bisa mengakses riwayat!")
