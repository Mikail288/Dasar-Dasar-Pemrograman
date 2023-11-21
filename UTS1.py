# Mulai
# Baca NIM
# Jika NIM ganjil
#     Masukkan panjang diagonal 1 dan diagonal 2
#     Hitung luas layang-layang
#     Hitung keliling layang-layang
#     Tampilkan hasil perhitungan
# Lainnya
#     Masukkan panjang sisi alas 1, sisi alas , dan tinggi
#     Hitung luas trapesium
#     Hitung keliling trapesium
#     Tampilkan hasil perhitungan
# Akhir

# nim=int(input("Masukan NIM anda: "))
# if nim % 2 !=0:
#     d1 = float(input("Masukkan panjang diagonal 1: "))
#     d2 = float(input("Masukkan panjang diagonal 2: "))
#     luas_layang = (d1 * d2) / 2
#     keliling_layang = 2 * (d1 + d2)
#     print("luas: ", luas_layang)
#     print("keliling", keliling_layang)
# else:
#     a1 = float(input("Masukkan panjang sisi alas: "))
#     a2 = float(input("Masukkan panjang sisi atas: "))
#     t = float(input("Masukkan tinggi: "))
#     luas_trapesium = (a1 + a2) * t / 2
#     miringkuadrat = t**2 + ((a1-a2)/2)**2
#     miring = miringkuadrat**0.5
#     keliling_trapesium = a1 + a2 + miring + miring
#     print("Luas:", luas_trapesium)
#     print("Keliling:",keliling_trapesium)


# mulai
# baca panjang sisi alas
# baca panjang sisi atas
# baca tinggi
# luas trapesium = (alas + atas) dikali tinggi dibagi 2
# sisi miring kuadrat = tinggi kuadrat ditambah ((alas - atas) dibagi 2) kuadrat
# sisi miring = sisi miring kuadrat dikuadrat 0,5
# keliling trapesium = alas + atas + (miring dikali 2)
# print ("luas", luas trapesium)
# print ("keliling", keliling trapesium)
# akhir
a1 = float(input("Masukkan panjang sisi alas: "))
a2 = float(input("Masukkan panjang sisi atas: "))
t = float(input("Masukkan tinggi: "))
luas_trapesium = (a1 + a2) * t / 2
miringkuadrat = t**2 + ((a1-a2)/2)**2
miring = miringkuadrat**0.5
keliling_trapesium = a1 + a2 + miring + miring
print("Luas:", luas_trapesium)
print("Keliling:",keliling_trapesium)