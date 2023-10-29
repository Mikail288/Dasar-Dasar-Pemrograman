#Nama: Muhammad Mikail Musa
#ROmbel: TI-01
motor =["Yamaha XSR","sport retro, klasik","150cc","hitam","2"]
motor.append("Rp37.780.000")
motor.append("tipe150cc")
motor.insert(2,"Yamaha")
print(motor)

luas = 0
print("Kalkulator luas\n1. Luas Persegi\n2. Luas lingkaran\n3. Luas segi tiga")
pilihan = int(input("Pilih perhitungan luas: "))
match pilihan:
    case 1:
        s = int(input("masukan panjang sisi: "))
        luas = s*s
        print("luas persegi adalah: ",luas)
    case 2:
        r = int(input("masukan jari jari: "))
        luas = 3.14*r*r
        print("luas lingkaran adalah: ",luas)
    case 3:
         t = int(input("masukan tinggi segi tiga: "))
         a = int(input("masukan alas segi tiga: "))
         luas = 1/2*a*t
         print("luas segi tiga adalah: ",luas)
    case _:
        print("perhitungan tidak valid, coba masukan pilihan dengan angka 1 sampai 3")

 