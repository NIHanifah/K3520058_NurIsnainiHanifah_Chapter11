#Menghitung selisih hari

import datetime
from datetime import timedelta

#function untuk menghitung selisih hari
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
    print("Selisih hari =", hari)
    
x = input("Masukkan tanggal :")
diffDate(x)
