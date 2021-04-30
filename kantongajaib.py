import Fungsi
import argparse
import os

# PEMANGGILAN FUNGSI OPEN (F14)
parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help="Lokasi savefile untuk kantongajaib.py")
args = parser.parse_args()
fileUser = args.nama_folder + "/user.csv"
fileGadget = args.nama_folder + "/gadget.csv"
fileConsumable = args.nama_folder + "/consumable.csv"
fileConsumableHistory = args.nama_folder + "/consumable_history.csv"
fileGadgetBorrowHistory = args.nama_folder + "/gadget_borrow_history.csv"
fileGadgetReturnHistory = args.nama_folder + "/gadget_return_history.csv"

# membaca file yang diberikan dan membuat file temporary
userTemp = Fungsi.parserCSV.bacaCSV(fileUser)
fileUserTemp = "user_temp.csv"
Fungsi.parserCSV.tulisCSV(userTemp,fileUserTemp)
gadgetTemp = Fungsi.parserCSV.bacaCSV(fileGadget)
fileGadgetTemp = "gadget_temp.csv"
Fungsi.parserCSV.tulisCSV(gadgetTemp,fileGadgetTemp)
consumableTemp = Fungsi.parserCSV.bacaCSV(fileConsumable)
fileConsumableTemp = "consumable_temp.csv"
Fungsi.parserCSV.tulisCSV(consumableTemp,fileConsumableTemp)
consumableHistoryTemp = Fungsi.parserCSV.bacaCSV(fileConsumableHistory)
fileConsumableHistoryTemp = "consumable_history_temp.csv"
Fungsi.parserCSV.tulisCSV(consumableHistoryTemp,fileConsumableHistoryTemp)
gadgetBorrowHistoryTemp = Fungsi.parserCSV.bacaCSV(fileGadgetBorrowHistory)
fileGadgetBorrowHistoryTemp = "gadget_borrow_history_temp.csv"
Fungsi.parserCSV.tulisCSV(gadgetBorrowHistoryTemp,fileGadgetBorrowHistoryTemp)
gadgetReturnHistoryTemp = Fungsi.parserCSV.bacaCSV(fileGadgetReturnHistory)
fileGadgetReturnHistoryTemp = "gadget_return_history_temp.csv"
Fungsi.parserCSV.tulisCSV(gadgetReturnHistoryTemp,fileGadgetReturnHistoryTemp)


loggedIn = False
roleUser = ""
loggedInUser = ""
loggedInId = ""
running = True
# loop login/register
while running:
    command = input(">>> ")
    if command == "login":
        roleUser,loggedIn,loggedInUser,loggedInId,running = Fungsi.login(userTemp)
    elif command == "exit":
        Fungsi.exit()
    else:
        print("Tolong untuk login terlebih dahulu.")

running = True
while running:
    command = input(">>> ")
    if command == "login":
        print("Anda sudah terlogin dengan username",loggedInUser,"sebagai",roleUser)
    elif command == "register" and roleUser == "admin": #khusus admin
        Fungsi.register(userTemp,fileUserTemp)
    elif command == "carirarity":
        Fungsi.cariRarity(gadgetTemp,fileGadgetTemp)
    elif command == "caritahun":
        Fungsi.cariTahun(gadgetTemp,fileGadgetTemp)
    elif command == "tambahitem" and roleUser == "admin": 
        Fungsi.tambahitem(gadgetTemp,consumableTemp,fileGadgetTemp,fileConsumableTemp)
    elif command == "hapusitem" and roleUser == "admin": 
        Fungsi.hapusitem(gadgetTemp,consumableTemp,fileGadgetTemp,fileConsumableTemp)
    elif command == "ubahjumlah" and roleUser == "admin": 
        Fungsi.ubahjumlah(gadgetTemp,consumableTemp,fileGadgetTemp,fileConsumableTemp)
    elif command == "pinjam" and roleUser == "user":
        Fungsi.pinjam(gadgetTemp,gadgetBorrowHistoryTemp,fileGadgetTemp,fileGadgetBorrowHistoryTemp,loggedInId)
    #untuk F9
    elif command == "kembali" and roleUser == "user":
        pass
    #untuk F10
    elif command == "minta" and roleUser == "user":
        pass
    elif command == "riwayatpinjam" and roleUser == "admin": 
        Fungsi.cekBorrowHistory(gadgetBorrowHistoryTemp,userTemp,gadgetTemp)
    elif command == "riwayatkembali" and roleUser == "admin": 
        Fungsi.cekReturnHistory(gadgetReturnHistoryTemp,gadgetBorrowHistoryTemp,userTemp,gadgetTemp)
    elif command == "riwayatambil" and roleUser == "admin":
        Fungsi.riwayatambil(consumableHistoryTemp,consumableTemp,userTemp)
    elif command == "save":
        Fungsi.savefile()
    elif command == "help":
        Fungsi.help(roleUser)
    elif command == "exit":
        Fungsi.exit()
    else:
        print('Perintah tidak diketahui. Gunakan perintah "help" untuk melihat perintah yang dapat digunakan.')