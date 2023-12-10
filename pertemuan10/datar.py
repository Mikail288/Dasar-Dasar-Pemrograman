def segitiga(a,t):
    luas = a*t/2
    keliling = a+t+((a**2+t**2)**0.5)
    print("luas segitiga = ",luas)
    print("keliling segitiga = ",keliling)

def persegi(s):
    luas = s*s
    keliling = s*4
    print("luas persegi =",luas)
    print("keliling persegi = ",keliling)

def persegipanjang(p,l):
    luas = p*l
    keliling = (p + l)*2
    print("luas persegi panjang =",luas)
    print("keliling persegi panjang = ",keliling)

def belahketupat(d1,d2):
    luas = 0.5 * d1 * d2
    keliling = 2*(d1+d2)
    print("luas belah kerucut =",luas)
    print("keliling belah kerucut = ",keliling)

def jajargenjang(a,t):
    luas = a*t
    keliling = 2*(a+t)
    print("luas jajar genjang = ",luas)
    print("keliling jajar genjang = ",keliling)

def lingkaran(r):
    luas = 3.1416 * r ** 2
    keliling = 2 * 3.1416 * r
    print("luas lingkaran =",luas)
    print("keliling lingkaran = ",keliling)

def trapesium(a,a2,t):
    luas = ((a+a2)/2) * t
    keliling = a + a2 + (((a-a2)**2+t**2)**0.5)*2
    print("luas trapesium =",luas)
    print("keliling trapesium = ",keliling)