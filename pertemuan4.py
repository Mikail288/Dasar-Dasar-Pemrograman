
nama = "Mikel"
usia = 12
if(usia >= 65):
    kategori = "Lanjut Usia"
elif(usia >= 18 and usia < 65):
    kategori = "Dewasa"
else:
    kategori = "Anak-anak"

print("Nama Siswa \t:",nama,
      "\nNilai \t\t:",usia,
      "\nKeterangan \t:",kategori)

pertama = 90
kedua = 20
if(pertama > kedua):
    keterangan = " lebih besar dari "
elif(pertama == kedua):
    keterangan = " Sama dengan "
else:
    keterangan =" lebih kecil dari "

print(pertama,keterangan,kedua)