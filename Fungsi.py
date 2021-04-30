import parserCSV
import datetime
import os.path
import sys
import argparse

# Prosedur Register
# DESKRIPSI: prosedur meminta nama, username, password, dan alamat kemudian
#            membuat akun baru dengan data tersebut jika username unik. Jika
#            nama tidak berformat title case, nama akan diformat menjadi title
#            case. diasumsikan bahwa file CSV yang digunakan memiliki minimal
#            1 entry dan id berurut
# ALGORITMA
def register(arrayData,fileUserTemp):
    """arrayData = matrix database hasil fungsi bacaCSV yang akan digunakan"""
    def isUsernameUnique(username,data):
        # cek apakah username yang digunakan belum ada dalam file CSV
        usernameUnique = True
        for baris in range(len(data)):
            if baris != 0: # agar baris pertama tidak diikutsertakan
                if username == data[baris][1]: # 1 karena username berada di kolom 2
                    usernameUnique = False
        return usernameUnique

    nama = input("Masukan nama: ")
    username = input("Masukan username: ")
    password = input("Masukan password: ")
    alamat = input("Masukan alamat: ")

    if isUsernameUnique(username,arrayData):
        nama = nama.title()
        lastId = int(arrayData[len(arrayData)-1][0]) # 0 karena id berada pada kolom 0. -1 karena array mulai dari 0
        nextId = 1 + lastId
        arrayData.append([nextId,username,nama,alamat,password,"user"])
        print("User",username,"telah berhasil register ke dalam Kantong Ajaib sebagai user")
        parserCSV.tulisCSV(arrayData,fileUserTemp) # sebaiknya langsung tulis data baru apa nggak?
    else:
        print("Username sudah digunakan, silakan ganti username")

# Prosedur Login
# DESKRIPSI: prosedur meminta username dan password, kemudian akan melihat
#            apakah data yang diberikan sesusai dengan file CSV yang dibuka.
#            jika data benar, prosedur akan memberikan status admin/user
#            berdasarkan akun yang digunakan
# ALGORITMA
def login(arrayData):
    """arrayData = matrix database hasil fungsi bacaCSV yang akan digunakan"""
    loggedIn = False
    roleUser = ""
    loggedInUser = ""
    loggedInId = ""
    running = True
    username = input("Masukan username: ")
    password = input("Masukan password: ")

    indexUsername = parserCSV.cekIndexValue(username,arrayData,1) # username berada dalam kolom 1
    # cek apakah password sesuai untuk akun dengan username 
    if indexUsername == []:
        print("Username dan/atau Password salah. Silakan coba login lagi")
    else:
        if password == arrayData[indexUsername[0]][4]:
            roleUser = arrayData[indexUsername[0]][5]
            print("Selamat datang",username+",","status anda adalah sebagai",roleUser)
            loggedIn = True
            loggedInUser = username
            loggedInId = arrayData[indexUsername[0]][0]
            running = False
        else:
            print("Username dan/atau Password salah. Silakan coba login lagi")
    return roleUser,loggedIn,loggedInUser,loggedInId,running

# Prosedur cariRarity
# DESKRIPSI: prosedur meminta rarity, lalu melihat dari dalam database yang
#            dimiliki untuk mencari gadget yang memiliki rarity tersebut dan 
#            menuliskannya
# ALGORITMA
def cariRarity(arrayData,fileGadgetTemp):
    gadgetTemp = parserCSV.bacaCSV(fileGadgetTemp)
    rarity = input("Masukkan rarity: ")
    rarity = rarity.upper()
    indexRarity = parserCSV.cekIndexValue(rarity,arrayData,4) #rarity berada dalam kolom 4
    if indexRarity == []:
        print("Tidak terdapat gadget dengan rarity tesebut")
    else:
        print("Hasil pencarian:")
        for index in indexRarity:
            print()
            print("Nama:",gadgetTemp[index][1])
            print("Deskripsi:",gadgetTemp[index][2])
            print("Jumlah:",gadgetTemp[index][3],"buah")
            print("Rarity:",gadgetTemp[index][4])
            print("Tahun ditemukan:",gadgetTemp[index][5])
    
# Prosedur cariTahun
# DESKRIPSI: prosedur meminta tahun dan operasi, lalu melihat dari dalam database
#            yang dimiliki untuk mencari gadget yang tahunnya memenuhi operasi tersebut
#            dan menuliskannya
# ALGORITMA
def cariTahun(arrayData,fileGadgetTemp):
    gadgetTemp = parserCSV.bacaCSV(fileGadgetTemp)
    tahun = input("Masukkan tahun: ")
    operator = input("Masukkan kategori: ")

    isTahunValid = True
    try:
        int(tahun)
    except ValueError:
        isTahunValid = False

    if isTahunValid:
        indexTahun = parserCSV.cekIndexValue(tahun,arrayData,5,operator)
        if indexTahun == [-1]:
            print("Kategori tidak diterima.")
            print('Kategori yang diterima adalah "=", "<", ">", "<=", dan ">=" ')
        else:
            print("Hasil pencarian: ")
            for index in indexTahun:
                print()
                print("Nama:",gadgetTemp[index][1])
                print("Deskripsi:",gadgetTemp[index][2])
                print("Jumlah:",gadgetTemp[index][3],"buah")
                print("Rarity:",gadgetTemp[index][4])
                print("Tahun ditemukan:",gadgetTemp[index][5])
    else:
        print("Tahun tidak valid")


# Prosedur tambahitem
# DESKRIPSI: 
# ALGORITMA
def tambahitem(dataGadget,dataConsumable,fileGadgetTemp,fileConsumableTemp):
    #gadgetTemp = parserCSV.bacaCSV(fileGadgetTemp)
    #consumableTemp = parserCSV.bacaCSV(fileConsumableTemp)
    ID = input("Masukan ID: ")
    if ID[0] == 'G' :
        indexID = parserCSV.cekIndexValue(ID,dataGadget,0)
        if indexID != []:
            print("Gagal menambahkan item karena ID sudah ada.")
        else:
            Nama = input("Masukkan Nama: ")
            Deskripsi = input("Masukan Deskripsi: ")
            Jumlah = input("Masukan Jumlah: ")
            Rarity = input("Masukan Rarity: ")
            Tahun = input("Masukan tahun ditemukan: ")
            print("Item telah berhasil ditambahkan ke database.")
            arr1 = [ID, Nama, Deskripsi, Jumlah, Rarity, Tahun]
            dataGadget.append(arr1)
            parserCSV.tulisCSV(dataGadget, fileGadgetTemp)
    elif ID[0] == 'C':
        indexID = parserCSV.cekIndexValue(ID,dataConsumable,0)
        if indexID != []:
            print("Gagal menambahkan item karena ID sudah ada.")
        else:  
            Nama = input("Masukkan Nama: ")
            Deskripsi = input("Masukan Deskripsi: ")
            Jumlah = input("Masukan Jumlah: ")
            Rarity = input("Masukan Rarity: ")
            print("Item telah berhasil ditambahkan ke database.")
            arr2 = [ID, Nama, Deskripsi, Jumlah, Rarity, Tahun]
            dataConsumable.append(arr2)
            parserCSV.tulisCSV(dataConsumable,fileConsumableTemp)
    else:
        print("Gagal menambahkan item karena ID tidak valid")

# Prosedur hapusitem
# DESKRIPSI: 
# ALGORITMA
def hapusitem(dataGadget,dataConsumable,fileGadgetTemp,fileConsumableTemp):
    ID = input("Masukan ID item: ")
    if ID[0] == 'G':
        indexID = parserCSV.cekIndexValue(ID,dataGadget,0)
        if indexID == []:
            print("Tidak ada item dengan ID tersebut.")
        else:
            answer = input("Apakah anda yakin ingin menghapus " + (dataGadget[indexID[0]][1]) + "(Y/N)?" )
            if (answer == 'Y') or (answer == 'y'):
                dataGadget.pop(indexID[0])
                print("Item telah berhasil dihapus dari database.")
                parserCSV.tulisCSV(dataGadget,fileGadgetTemp)
            elif (answer == 'N') or (answer == 'n'):
                print("Item tidak dihapus dari database")
            else:
                print("Input harus berupa Y/N")
    elif ID[0] == 'C':
        indexID = parserCSV.cekIndexValue(ID,dataConsumable,0)
        if indexID == []:
            print("Tidak ada item dengan ID tersebut.")
        else:
            answer = input("Apakah anda yakin ingin menghapus " + (dataConsumable[indexID[0]][1]) + "(Y/N)?" )
            if (answer == 'Y') or (answer == 'y'):
                dataConsumable.pop(indexID[0])
                print("Item telah berhasil dihapus dari database.")
                parserCSV.tulisCSV(dataConsumable,fileConsumableTemp)
            elif (answer == 'N') or (answer == 'n'):
                print("Item tidak dihapus dari database")
            else:
                print("Input harus berupa Y/N")
    else:
        print("Gagal menghapus item karena ID tidak valid")

# Prosedur ubahjumlah
# DESKRIPSI: 
# ALGORITMA
def ubahjumlah(dataGadget,dataConsumable,fileGadgetTemp,fileConsumableTemp):
    ID = input("Masukan ID: ")
    if ID[0] == 'G':
        indexID = parserCSV.cekIndexValue(ID,dataGadget,0)
        if indexID == []:
            print("Tidak ada item dengan ID tersebut!")
        else:
            jumlah = int(input("Masukkan Jumlah: "))
            qty = int(dataGadget[indexID[0]][3])
            if qty > jumlah:
                if jumlah > 0 :
                    print(str(jumlah) + " " + (dataGadget[indexID[0]][1]) + " berhasil ditambahkan. Stok sekarang: " +str(qty+jumlah))
                else:
                    print(str(jumlah) + " " + (dataGadget[indexID[0]][1]) + " berhasil dibuang. Stok sekarang: " + str(qty+jumlah))
                newQty = jumlah + qty
                dataGadget[indexID[0]][3] = str(newQty)
                parserCSV.tulisCSV(dataGadget,fileGadgetTemp)
            else:
                print(str(jumlah) + (dataGadget[indexID[0]][1]) + "gagal dibuang karena stok kurang. Stok sekarang: " + str(qty) + "(< " + str(jumlah) + ")")
    if ID[0] == 'C':
        indexID = parserCSV.cekIndexValue(ID,dataConsumable,0)
        if indexID == []:
            print("Tidak ada item dengan ID tersebut!")
        else:
            jumlah = int(input("Masukkan Jumlah: "))
            qty = int(dataConsumable[indexID[0]][3])
            if qty > jumlah:
                if jumlah > 0 :
                    print(str(jumlah) + (dataConsumable[indexID[0]][1]) + "berhasil ditambahkan. Stok sekarang: " +str(qty+jumlah))
                else:
                    print(str(jumlah) + (dataConsumable[indexID[0]][1]) + "berhasil dibuang. Stok sekarang: " +str(qty+jumlah))
                newQty = jumlah + qty
                dataConsumable[indexID[0]][3] = str(newQty)
                parserCSV.tulisCSV(dataConsumable,fileConsumableTemp)
            else:
                print(str(jumlah) + (dataConsumable[indexID[0]][1]) + "gagal dibuang karena stok kurang. Stok sekarang: " + str(qty) + "(< " + str(jumlah) + ")")
    else:
        print("Gagal merubah jumlah item karena ID tidak valid")

# Prosedur pinjam
# DESKRIPSI: 
# ALGORITMA
def pinjam(dataGadget,dataPinjamGadget,fileGadgetTemp,filePinjamGadgetTemp,loggedInId):
    IdItem = input("Masukan ID: ")
    lastId = int(dataPinjamGadget[len(dataPinjamGadget)-1][0])
    nextId = 1 + lastId
    indexID = parserCSV.cekIndexValue(IdItem,dataGadget,0)
    if indexID == []:
        print("Tidak ada item dengan ID tersebut!")
    else:
        tanggal = input("Tanggal peminjaman: ")
        jumlah = input("Jumlah peminjaman: ")
        qty = int(dataGadget[indexID[0]][3])
        if qty >= jumlah: 
            print("Item "+(dataGadget[indexID[0]][1])+" (x "+str(jumlah)+") berhasil dipinjam!")
            newQty = qty - int(jumlah)
            dataGadget[indexID[0]][3] = str(newQty)
            dataPinjamGadget.append([nextId,loggedInId,IdItem,tanggal,jumlah,False])
            parserCSV.tulisCSV(dataGadget,fileGadgetTemp)
            parserCSV.tulisCSV(dataPinjamGadget,filePinjamGadgetTemp)
        else:
            print("Item "+(dataGadget[indexID[0]][1])+"gagal dipinjam karena stok kurang.")

# Prosedur F09
# DESKRIPSI: 
# ALGORITMA

# Prosedur F10
# DESKRIPSI: 
# ALGORITMA

# Prosedur cekBorrowHistory
# DESKRIPSI: Prosedur digunakan oleh Admin sebagai bantuan untuk melihat riwayat
#            peminjaman gadget. Data bisa dibaca dari file yang tersedia. Bila terdapat
#            lebih dari 5 entry, keluarkan 5 entry paling baru, dan pengguna dapat
#            mengeluarkan 5 entry tambahan bila diinginkan.
# ALGORITMA
def cekBorrowHistory (borrowData,userData,gadgetData):
    tanggal = [borrowData[i][3] for i in range(1,len(borrowData))] #memisahkan tanggal dari borrowData
    # mengurutkan gadget_borrow_history berdasarkan tanggal
    dates = [datetime.datetime.strptime(ts, "%d/%m/%Y") for ts in tanggal]
    dates.sort(reverse=True)
    sortedDates = [datetime.datetime.strftime(ts, "%d/%m/%Y") for ts in dates]
    # .pop() tidak bisa digunakan untuk lebih dari 1 elemen, sehingga digantikan dengan ini
    lastFiveDates = sortedDates[:5:] 
    del sortedDates[:5]

    def cetakInfoPeminjaman(listOfDates):
        for date in listOfDates:
            indexTanggal = parserCSV.cekIndexValue(date,borrowData,3)
            for index in indexTanggal:
                idPeminjaman = borrowData[index][0]
                idPeminjam = borrowData[index][1]
                indexPeminjam = parserCSV.cekIndexValue(idPeminjam,userData,0)
                namaPeminjam = userData[indexPeminjam[0]][2]
                idGadget = borrowData[index][2]
                indexGadget = parserCSV.cekIndexValue(idGadget,gadgetData,0)
                namaGadget = gadgetData[indexGadget[0]][1]
                tanggalPeminjaman = borrowData[index][3]
                jumlah = borrowData[index][4]
                is_returned = borrowData[index][5]
                print("ID Peminjaman      : " + idPeminjaman)
                print("Nama Pengambil     : " + namaPeminjam)
                print("Nama Gadget        : " + namaGadget)
                print("Tanggal Peminjaman : " + tanggalPeminjaman)
                print("Jumlah             : " + jumlah)
                if is_returned == "True":
                    print("Gadget sudah dikembalikan")
                else:
                    print("Gadget belum dikembalikan")
            if len(indexTanggal) > 1:
                listOfDates.remove(date)
    cetakInfoPeminjaman(lastFiveDates)
    running = True
    while len(sortedDates) > 0 and running:
        lanjut = input("Lihat halaman selanjutnya? (Y/N) ")
        if lanjut == 'Y' or lanjut == 'y':
            lastFiveDates = sortedDates[:5:] 
            del sortedDates[:5]
            cetakInfoPeminjaman(lastFiveDates)
        elif lanjut == 'N' or lanjut == 'n':
            running = False
        else:
            print("Input yang diterima hanyalah Y/N")

# Prosedur cekReturnHistory
# DESKRIPSI: Prosedur yang digunakan oleh admin untuk melihat riwayat pengembalian
#            gadget. Data dapat dibaca dari file yang tersedia. Jika terdapat lebih
#            dari 5 entry, keluarkan 5 entry paling baru, dan pengguna dapat menggunakan
#            lima entry tambahan bila diinginkan.
# ALGORITMA
def cekReturnHistory (returnData,borrowData,userData,gadgetData):
    tanggal = [returnData[i][2] for i in range(1,len(returnData))] #memisahkan tanggal dari returnData
    # mengurutkan gadget_return_history berdasarkan tanggal
    dates = [datetime.datetime.strptime(ts, "%d/%m/%Y") for ts in tanggal]
    dates.sort(reverse=True)
    sortedDates = [datetime.datetime.strftime(ts, "%d/%m/%Y") for ts in dates]
    # .pop() tidak bisa digunakan untuk lebih dari 1 elemen, sehingga digantikan dengan ini
    lastFiveDates = sortedDates[:5:] 
    del sortedDates[:5]

    def cetakInfoPengembalian(listOfDates):
        for date in listOfDates:
            indexTanggal = parserCSV.cekIndexValue(date,returnData,2)
            for index in indexTanggal:
                idPengembalian = returnData[index][0]
                idPeminjaman = borrowData[index][1] # kalo F12 error kemungkinan karena baris ini
                indexPeminjaman = parserCSV.cekIndexValue(idPeminjaman,borrowData,0)
                idPeminjam = borrowData[indexPeminjaman[0]][1]
                indexPeminjam = parserCSV.cekIndexValue(idPeminjam,userData,0)
                namaPeminjam = userData[indexPeminjam[0]][2]
                idGadget = borrowData[indexPeminjaman[0]][2]
                indexGadget = parserCSV.cekIndexValue(idGadget,gadgetData,0)
                namaGadget = gadgetData[indexGadget[0]][1]
                tanggalPengembalian = returnData[index][2]
                print("ID Pengembalian      :",idPengembalian)
                print("Nama Pengambil       :",namaPeminjam)
                print("Nama Gadget          :",namaGadget)
                print("Tanggal Pengembalian :",tanggalPengembalian,"\n")
            if len(indexTanggal) > 1:
                listOfDates.remove(date)
    cetakInfoPengembalian(lastFiveDates)
    running = True
    while len(sortedDates) > 0 and running:
        lanjut = input("Lihat halaman selanjutnya? (Y/N) ")
        if lanjut == 'Y' or lanjut == 'y':
            lastFiveDates = sortedDates[:5:] 
            del sortedDates[:5]
            cetakInfoPengembalian(lastFiveDates)
        elif lanjut == 'N' or lanjut == 'n':
            running = False
        else:
            print("Input yang diterima hanyalah Y/N")

# Prosedur riwayatambil
# DESKRIPSI: 
# ALGORITMA
def riwayatambil(consumable_history,consumable,user):
    f = parserCSV.bacaCSV(consumable_history)
    consumable = parserCSV.bacaCSV(consumable)
    f2 = parserCSV.bacaCSV(user)
    def carinama_consumable(Index1):
        for i in range (len(consumable)):
            if f[Index1][2] == consumable[i][0] :
                return(consumable[i][1])
    def carinama_pengambil(Index):
        for i in range (len(f2)):
            if f[Index][1] == f2[i][0]: #mecocokan ID user pada consumable_history.csv dengan ID user di user.csv
                return f2[i][2] #mengembalikan nama user yang pernah ambil consumable
    i=1
    for i in range (len(f)-1):
        i+=1
        consum = carinama_consumable(i)
        nama = carinama_pengambil(i)
        print ("ID Pengambilan : " + str(f[i][0]))
        print ("Nama Pengambil : " + str(nama))
        print ("Nama Consumable : " + str(consum))
        print ("Tanggal Pengambilan : " + str(f[i][3]))
        print ("Jumlah : " + str(f[i][4]))
        print ()

# Prosedur savefile
# DESKRIPSI: 
# ALGORITMA
def savefile():
    filename = ['gadget.csv', 'gadget_borrow_history.csv', 'user.csv', 'gadget_return_history.csv', 'consumable_history.csv', 'consumable.csv']
    tempfilename = ['gadget_temp.csv', 'gadget_borrow_history_temp.csv', 'user_temp.csv', 'gadget_return_history_temp.csv', 'consumable_history_temp.csv', 'consumable_temp.csv']
    def cekfile(folder): #cek apakah file dalam folder yang dituju sudah ada
        for i in range (len(filename)):
            if os.path.isfile(folder + "/" +filename[i])== True : #file sudah ada
                os.remove(folder + '/' + filename[i]) #remove file lama
                open(folder + "/"+ filename[i], 'wb').write(open(tempfilename[i], 'rb').read()) #save file baru

            else: #file belum ada
                open(folder + "/" + filename[i], 'wb').write(open(tempfilename[i], 'rb').read())#save file baru
    folder = input ("Masukkan folder penyimpanan : ") #input nama folder untuk penyimpanan
    if os.path.exists(folder) == True: #folder dengan nama tsb sudah ada
        cekfile(folder)

    else : #folder dengan nama tsb belum ada
        try:
            os.makedirs(folder) #bikin folder baru
        except WindowsError:
            print("Nama folder tidak valid")
            return
        for i in range (len(filename)):
            open(folder + "/" + filename[i], 'wb').write(open(tempfilename[i], 'rb').read()) #save file ke folder

# Prosedur help
# DESKRIPSI:
# ALGORITMA
def help(roleUser):
    if roleUser == "admin" :
        print("============ HELP ==============")
        print ("register - untuk melakukan registrasi bagi pengguna baru")
        print ("login - melakukan login ke dalam sistem (berlaku jika anda sudah mempunyai akun)")
        print ("carirarity - mencari gadget berdasarkan rarity tertentu")
        print ("caritahun - mencari gadget berdasarkan tahun")
        print ("tambahitem - menambahkan item ke dalam inventory")
        print ("hapusitem - menghapus item pada database")
        print ("ubahjumlah - mengubah jumlah gadget atau consumable yang terdapat pada sistem")
        print ("riwayatpinjam - melihat riwayat peminjaman gadget")
        print ("riwayatkembali - melihat riwayat pengembalian gadget")
        print ("riwayatambil - melihat riwayat pengambilan consumable")
        print ("save - menyimpan data ke dalam file")
        print ("help - menampilkan panduan penggunaan sistem")
        print ("exit - keluar dari aplikasi")
    elif roleUser == "user" :
        print("============ HELP ==============")
        print ("login - melakukan login ke dalam sistem (berlaku jika anda sudah mempunyai akun)")
        print ("carirarity - mencari gadget dengan rarity tertentu")
        print ("caritahun - mencari gadget berdasarkan tahun")
        print ("pinjam - melakukan peminjaman gadget")
        print ("kembali - mengembalikan gadget secara seutuhnya")
        print ("minta - meminta consumable")
        print ("save - menyimpan data ke dalam file")
        print ("help - menampilkan panduan penggunaan sistem")
        print ("exit - keluar dari aplikasi")

# Prosedur exit
# DESKRIPSI:
# ALGORITMA
def exit ():
    simpan = input(("Apakah anda ingin melakukan penyimpanan file yang telah diubah? Y/N \n"))
    def hapusFileTemp():
        tempfilename = ['gadget_temp.csv', 'gadget_borrow_history_temp.csv', 'user_temp.csv', 'gadget_return_history_temp.csv', 'consumable_history_temp.csv', 'consumable_temp.csv']
        for name in tempfilename:
            os.remove(name)
    if simpan == "y" or simpan =="Y" :
        savefile() #pemanggilan fungsi savefile() dari file F15.py
        hapusFileTemp()
        sys.exit() #terminate program

    elif simpan == "N" or simpan == "n" :
        hapusFileTemp()
        sys.exit() #terminate program