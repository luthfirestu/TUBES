# Program parserCSV
# Deskripsi: program berisi berbagai fungsi untuk melakukan manipulasi file CSV
#            seperti membaca, merubah, dan menulis tanpa menggunakan fungsi .split
# list fungsi: bacaCSV untuk membaca dan merubah file CSV menjadi matrix siap olah
#              ubahData untuk merubah isi matrix hasil fungsi bacaCSV
#              tulisCSV untuk menyimpan matrix menjadi file CSV

# KAMUS
# delimiter = string yang menentukan delimiter (pemisah) CSV (umumnya koma atau semikolon)
delimiter = ";" #dapat diubah sesuai dengan delimiter yang digunakan


# Definisi, Spesifikasi, dan Realisasi Fungsi/Prosedur

# Fungsi bacaCSV
# DESKRIPSI: fungsi menerima nama file csv, kemudian membaca CSV dan 
#            merubahnya menjadi sebuah matrix dengan baris pertama
#            berisi label dan baris selanjutnya berisi data
# SPESIFIKASI: string -> [[string]]
# KAMUS
# csv = file csv yang dibuka
# csvRawLines = isi file csv per baris (array of strings)
# csvLines = isi file csv per baris dengan line break ("\n") sudah dihilangkan (array of strings)
# rawArrayDataCSV = isi file csv per sel sebelum dibersihkan (matrix of strings/array of array of strings)
# isiSel = isi data dalam masing-masing sel rawArrayDataCSV (string)
# isiBarisDataCSV = isi file csv per baris (array of strings)
# arrayDataCSV = isi file csv per sel setelah dibersihkan (matrix of strings/array of array of strings)
# REALISASI
def bacaCSV(namaFile):
    """membaca file CSV menjadi matrix database siap diolah
    namaFile = (string)"""
    csv = open(namaFile,"r")
    csvRawLines = csv.readlines()
    csv.close
    csvLines = [line.replace("\n","") for line in csvRawLines] #menghilangkan line breaks

    rawArrayDataCSV = [] 
    for line in csvLines: #menggantikan fungsi .split
        isiBarisDataCSV = []
        isiSel = ""
        for c in line:
            if c == delimiter:
                isiBarisDataCSV.append(isiSel)
                isiSel = ""
            else:
                isiSel += c
        isiBarisDataCSV.append(isiSel) #agar kolom terakhir csv tetap terbaca
        rawArrayDataCSV.append(isiBarisDataCSV)
    
    while [''] in rawArrayDataCSV:
        rawArrayDataCSV.remove(['']) #menghapus baris kosong
    arrayDataCSV = [[data.strip() for data in baris] for baris in rawArrayDataCSV] 
    # membersihkan/menghilangkan spasi di awal dan akhir array data
    # tidak dilakukan perubahan type data menjadi integer karena kolom yang 
    # berisi integer berbeda-beda untuk masing-masing CSV

    return arrayDataCSV

# Prosedur ubahData
# DESKRIPSI: prosedur menerima variabel matrix berisikan hasil fungsi 
#            bacaCSV (data), baris (baris) dan kolom (kolom) data yang ingin 
#            diubah, serta nilai yang diinginkan (value)
# REALISASI
def ubahData(data, baris, kolom, value):
    if baris == 0:
        print("error ini seharusnya tidak terlihat di produk akhir")
        print("tidak bisa merubah baris berindex 0 karena berisi id CSV yang tidak boleh diubah")
    else:
        data[baris][kolom] = value

# Prosedur tulisCSV
# DESKRIPSI: prosedur menerima matrix hasil fungsi bacaCSV (data) dan nama file
#            CSV baru (namaFileCSVBaru), kemudian menuliskan matrix tersebut ke 
#            dalam file tersebut
# KAMUS
# matrixString = matrix data dengan tiap sel berisi string ([[string]])
# csv = isi matrix data dalam bentuk string yang siap diubah menjadi CSV (string)
# REALISASI
def tulisCSV(data,namaFileCSVBaru):
    """menuliskan database data ke file CSV baru
    data = matrix database yang akan ditulis
    namaFileCSVBaru = (string)"""
    #merubah seluruh isi matrix menjadi string
    matrixString = [[str(data[baris][kolom]) for kolom in range(len(data[0]))] for baris in range(len(data))] 
    #merubah matrix menjadi sebuah string
    barisCSV = []
    for baris in range(len(matrixString)):
        barisBaru = delimiter.join(matrixString[baris])
        barisCSV.append(barisBaru)
    csv = "\n".join(barisCSV)

    f = open(namaFileCSVBaru,"w+")
    f.write(csv)
    f.close()

def cekIndexValue(value,data,kolom,operator="="):
    """ fungsi mencari seluruh index dimana sebuah nilai (value) yang memenuhi 
    operator dalam kolom yang ditentukan dalam matrix data, dan mengembalikan 
    list tersebut. operator selain = hanya menerima value angka (type tetap string)
    output [-1] jika operator tidak sesuai dengan spesifikasi
    value = (string)
    data = matrix database hasil fungsi bacaCSV yang akan digunakan
    kolom = lokasi kolom value yang ingin dicari (integer)
    operator = menentukan hubungan dengan value yang dicari. operator yang
    diterima adalah =, <, >, <=, dan >= (string)"""
    listOfIndex = []
    for index in range(1,len(data)): # pengecekan dimulai dari baris 1 agar label data tidak terhitung
        if operator == "=":
            if value == data[index][kolom]:
                listOfIndex.append(index)
        elif operator == "<":
            if int(data[index][kolom]) < int(value):
                listOfIndex.append(index)
        elif operator == "<=":
            if int(data[index][kolom]) <= int(value):
                listOfIndex.append(index)
        elif operator == ">":
            if int(data[index][kolom]) > int(value):
                listOfIndex.append(index)
        elif operator == ">=":
            if int(data[index][kolom]) >= int(value):
                listOfIndex.append(index)
        else:
            return [-1]
    return listOfIndex

# CONTOH APLIKASI     
# data = bacaCSV("test.csv")
#   membuka file bernama test.csv
# ubahData(data,1,0,10)
#   merubah nilai baris kedua kolom pertama data menjadi 10
# cekIndexValue(10,data,0)
#   1 (karena hasil pemanggilan fungsi ubahData yang sebelumnya)
# tulisCSV(data,"hasil.csv")
#   membuat file baru bernama hasil.csv dari data yang telah diubah
