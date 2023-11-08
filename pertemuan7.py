#no 1
kendaraan = input("""1. mobil
2. motor
Masukan Jenis kendaraan: """).lower()
jenisbensin = input("""1. pertalite
2. Pertamax
3. Pertamax Turbo
masukan jenis bensin: """).lower()
tujuan = input("""1. jakarta
2. Bekasi 
3. Depok 
4. Tangerang
5. Bogor 
masukan kota tujuan: """).lower()
# bensin = 0
# harga = 0
# jarak = 0
if jenisbensin == "pertalite":
    bensin = 12
    harga = 10000
elif jenisbensin == "petamax":
    bensin = 13
    harga = 14000
else:
    bensin = 13.5
    harga = 17000
if tujuan == "jakarta":
    jarak = 20
elif tujuan == "bekasi":
    jarak = 35.7
elif tujuan == "depok":
    jarak = 5
elif tujuan == "tangerang":
    jarak = 99
else:
    jarak = 120.6
pemakaian = jarak / bensin
totalharga = pemakaian * harga
print("========================================")
print ("Nama Kendaraan: ", kendaraan) 
print("Jenis Bensin :", jenisbensin)
print ("Kota yang dituju: ", tujuan)
print ("Pemakaian bensin: ", pemakaian)
print ("Total Harga dari bensin: ", totalharga)
print("========================================")

#no2
print("==================pesan==================")
pembeli = input("masukan nama pembeli: ")
nohp = input("Masukan No hp: ")
pesan = input("""1. minuman
2. Makanan
masukan nomor pilihan: """)

if pesan == "1":
    print("""============menu minuman============
Aneka Jus \tRp15.000
Soft Drink \tRp10.000
Sweet Ice Teat \tRp5.000 
""")
else:
    print("""============menu makanan============
Nasi Goreng \tRp15.000
Mie goreng \tRp12.000
Ayam Geprek \tRp18.000 
""")
pesanan = input("masukan pesanan: ").lower()
jumlah = int(input("masukan jumlah pesanan: "))

if pesanan == "aneka jus":
    harga = 15000
elif pesanan =="soft drink":
    harga = 10000
elif pesanan =="sweet ice tea":
    harga = 5000
elif pesanan =="nasi goreng":
    harga = 15000
elif pesanan =="mie goreng":
    harga = 12000
else:
    harga = 18000

total = harga * jumlah

print("============bon============")
print(f"""Nama Pembeli \t{pembeli}
No Hp Pembeli \t{nohp}
Menu yang di Pesan \t{pesanan}
Jumlah pesanan \t {jumlah}
Harga yang harus di bayarkan. \t {total}
""")
#no 3
print("==================no 3==================")
for i in range(1,21):
    if i % 3 == 0:
        print("STT Nurul Fikri ")
    else:
        print(i)