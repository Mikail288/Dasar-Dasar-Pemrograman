# Fungsi menampilkan Profil
def profil(nama, alamat, gender, umur, hoby):
    print(f"Nama: \t\t{nama}")
    print(f"Alamat: \t{alamat}")
    print(f"jenis kelamin: \t{gender}")
    print(f"umur: \t\t{umur}")
    print(f"hobi: \t\t{hoby}")
profil("mikel","depok","laki-laki","20","main")

# Fungsi indikator nilai
def nilai(n):
    if(n > 80 and n <= 100):
        print("istimewa")
    elif(n > 70 and n <=80):
        print("sangat baik")
    elif(n > 60 and n <=70):
        print("baik")
    else:
        print("gagal")
nilai(60)

# Fungsi menampilkan angka ganjil
def ganjil(g):
    for i in range(1,g+1):
        if i%2 !=0:
            print(i)
ganjil(100)