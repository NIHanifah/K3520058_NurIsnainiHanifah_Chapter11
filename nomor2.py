#Memasukkan data peminjaman buku dan batas pengembalian buku

import datetime
from datetime import timedelta

myFile =  open('e:/MATKUL/Project Python/K3520058_NurIsnainiHanifah_Chapter11/bukuPinjaman.txt', "a+")

def pinjamBuku():
    #KODE TERDIRI DARI 3 DIGIT
    kodeMember = input("Masukkan kode member : ")
    namaMeber = input("Masukkan nama member : ")
    judulBuku = input("Masukkan judul buku  : ")
    tglSekarang = datetime.datetime.now().date()
    tglBatas = tglSekarang + timedelta(days =+ 7)
    tanya = input("Ulangi lagi (y/n) : ")
    myFile.write(kodeMember + '|' + namaMeber + '|' + judulBuku + '|' + str(tglSekarang) + '|' + str(tglBatas) + '\n')
    if tanya == "y":
        pinjamBuku()
    elif tanya == "n":
        myFile.close()

pinjamBuku()