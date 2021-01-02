import datetime

tglSekarang = datetime.datetime.now().date()

#Melakukan penjumlahan data pada file yang sudah di buat
myFile=open("e:/MATKUL/Project Python/K3520058_NurIsnainiHanifah_Chapter11/bukuPinjaman.txt", "r")
lineFile=myFile.readlines()
a = 0

dataKode = []
inputData = input("Masukkan kode member : ")


#perulangan untuk menjumlahkan data
for file in lineFile:
    file = lineFile[a].strip()
    b = file[0] + file[1] + file[2]
    dataKode += [b]
    a += 1

def diffDate(x):
    tglSekarang = datetime.datetime.now()
    thn, bln, tgl = x.split('-')
    thn, bln, tgl = int(thn), int(bln), int(tgl)
    if tglSekarang.month == 1:
        if bln == 1:
            hari = tgl - tglSekarang.day
        elif bln == 2:
            hari = 31-tglSekarang.day + tgl
        elif bln > 2:
            if thn == tglSekarang.year:
                hari = (31-tglSekarang.day) + 28 + ((bln-3) * 30) + round((bln-2)/2) + tgl
            elif thn != tglSekarang.year:
                hari = (31 - tgl) + tglSekarang.day
    elif tglSekarang.month == 2:
        if bln == 1:
            hari = 365 + tgl
        elif bln == 2:
            hari = tgl - tglSekarang.day
        elif bln > 2:
            hari = (28 - tglSekarang.day) + ((bln-2)*30) + round((bln-2)/2) + tgl
    elif tglSekarang.month == 12:
        if bln == 1:
            hari = (31 - tglSekarang.day) + tgl
        elif bln == 2:
            hari = (31 - tglSekarang.day) + 31 + tgl
        elif bln > 2:
            hari = (31 - tglSekarang.day) + 31 + tgl + ((bln-3) * 30) + round((bln-3)/2)
    elif tglSekarang.month >= 3:
        if bln == 1:
            hari = 365 + tgl + ((bln-1)*30) + round((bln-2)/2)
        elif bln == 2:
            hari = 365 + tgl + ((bln-1)*30) + round((bln-2)/2)
        elif bln > 2:
            hari = (30 - tglSekarang.day) + ((bln-2)*30) + round((bln-2/2)) + tgl

    if hari > 7:
        terlambat = hari - 7
        denda = terlambat * 2000
        print("Terlambat                       =", terlambat, 'hari')
        print("Denda                           = Rp", denda)
    elif hari <= 7:
        print("Terlambat                       = 0")
        print("Denda                           = Rp 0")



b = 0
while b <= len(dataKode):
    data = lineFile[b].split('|')
    if inputData == dataKode[b]:  
        print("Data Peminjaman Buku") 
        print("Kode Member                     =", data[0])
        print("Nama Member                     =", data[1])
        print("Judul Buku                      =", data[2])
        print("Tanggal Mulai Peminjaman        =", data[3])
        print("Tanggal Pengembalian Peminjaman =", tglSekarang)
        x = data[3]
        diffDate(x)
        break
    b += 1
    if b == len(dataKode):
        print("Data tidak ditemukan")
        break
