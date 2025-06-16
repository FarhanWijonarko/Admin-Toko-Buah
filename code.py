from tabulate import tabulate

# create header
headers = ["Index", "Nama", "Stock", "Harga"] #headers tabel
headerChart = ["Index" ,"Nama", "Qty", "Total Harga"]#headers chart


data = [
    ["Apel", 20, 10000],
    ["Jeruk", 15, 15000],
    ["Anggur", 25, 20000]
]

chart = []
total = 0
uniqueData = []


while True:
    print("""
          Selamat Datang di Pasar Buah
          
          List Menu
          ]1. Menampilkan Daftar Buah
          ]2. Menambahkan Buah
          ]3. Menghapus Buah
          ]4. Membeli Buah
          ]5. Keluar
          """)
    pilihan = int(input("Masukan Pilihan : "))
    if pilihan == 1:
        updateData = []
        for item in data:
            if item[1] != 0:
                updateData.append(item)
        data.clear()
        data = updateData     
            
        print(tabulate(data, headers=headers, showindex=True, tablefmt="grid"))
    elif pilihan == 2:
        dataBaru = []
        nama = str(input("Masukan Nama Buah : "))
        
        
        for i in range (len(data)):
            uniqueData.append(data[i][0].lower())
            
        if nama.lower() in uniqueData:
            print("Buah Sudah Ada")

        else:
            stockBaru = int(input("Masukan Stock Buah : "))
            hargaBaru = int(input("Masukan Harga Buah : ")) 
            capital = nama.capitalize()
            dataBaru.append(capital)
            dataBaru.append(stockBaru)
            dataBaru.append(hargaBaru)
            data.append(dataBaru)
            print("Buah Berhasil Ditambahkan")
                
        
    elif pilihan == 3:
        print(tabulate(data, headers=headers, showindex=1, tablefmt="grid"))
        removeIndex = int(input("Masukan Index Buah Yang Dihapus : "))
        for i in range(len(data)):
            if i == removeIndex:
                del data[removeIndex]
                print("Buah Berhasil Dihapus")
                break
        else:
            print("Index Tidak Ditemukan")
                
    elif pilihan == 4: #loop utama 
        print(tabulate(data, headers=headers, showindex=1, tablefmt="grid"))
        beliIndex = int(input("Masukan Index Buah Yang Dibeli : "))

        for i in range(len(data)):
            if i == beliIndex:
                qtyIndex = int(input("Masukan Jumlah Buah Yang Dibeli : "))
                
                if qtyIndex > data[beliIndex][1]:
                    print("Stock Tidak Mencukupi")
                    break
                else:
                    uniqueChart = []
                    chartSementara = []
                    total = 0
                    for i in range(len(chart)):
                        uniqueChart.append(chart[i][0].lower())

                        if data[beliIndex][0].lower() in uniqueChart:
                            chart[i][1] += qtyIndex
                            chart[i][2] = chart[i][1] * data[beliIndex][2]
                            totalHarga = chart[i][2]
                            break
                    else:
                        chartSementara.append(str(data[beliIndex][0]))
                        chartSementara.append(qtyIndex)
                        totalHarga = qtyIndex * data[beliIndex][2]
                        chartSementara.append(totalHarga)
                        chart.append(chartSementara)

                    # kurang stok di data
                    data[beliIndex][1] -= qtyIndex
                    total += totalHarga
                    
                    
                    print(tabulate(chart, headers=headerChart, showindex=1, tablefmt="grid"))
                    
                    
                    while True:
                        nanya = str(input("Apakah data chart mau di simpan? (ya/tidak) : "))
                        if nanya.lower() == "tidak":
                            print(f"Total yang harus dibayar {total}") 
                            while True:
                                duit = int(input("Masukan Uang Anda : "))
                                if duit > total:
                                    kembalian = duit - total
                                    print(f"Kembalian anda {kembalian}")
                                    chart.clear()
                                    break
                                elif duit == total:
                                    print("Uang Anda Pas")
                                    chart.clear()
                                    break
                                else:
                                    print("Uang Anda Kurang")  
                            break  # keluar dari loop `nanya`
                        elif nanya.lower() == "ya":
                            break

                        else:
                            print("Pilihan Tidak Ditemukan") 
                    break     

        else:
            print("Index Tidak Ditemukan")
    elif pilihan == 5:
        print("Terima Kasih")
        break
    else:
        print("Pilihan Tidak Ditemukan")
            
        
