# numbers = []
# print(numbers)
# numbers.append(1)
# numbers.append(2)
# numbers.append(3)
# print(numbers)
# a = numbers.pop()
# print(a)
# print(numbers)

# names = {"ab","ba","ac","bc"}
# print(names)
# numbers = {9,2,5,4,3,6,7,8,1}
# print(numbers)

# null_set = set()
# null_set.add(1)
# null_set.add(1)
# print(null_set)

# a = set()
# a.add(3)
# a.add(6)
# a.remove(6)
# print(a)
# print(a.pop())
# print(a)

# set1 = {1,2,3}
# set2 = {2,4,6}
# set1.update(set2)
# print(set1)

# data = {
#     "mahasiswa" : {
#         "nama" : "sup",
#         "semester" : 5,
#         "hobi" : ["mancing","berenang"],
#         "pacar" : {
#             "nama" : ["susi","Indri","awewe"],
#             "selingkuhan" : ["igun","ical","daden","acam"]
#         }
#     },
#     "dosen" : {
#         "nama" : "Reza Maulana, S.Kom",
#         "alamat" : "beji"
#     }
# }
# data["mahasiswa"]["baru"] = "nyoba"
# print(data)
# print(data["mahasiswa"]["pacar"]["nama"][0])

# mahasiswa["umur"] = 18
# print(mahasiswa.keys())
# print(mahasiswa.values())
# print(mahasiswa.items())
# print(mahasiswa["hobi"][0])

# # no 1 tapi ribet
# def lulus_saja(hasil_akhir):
#     lulus = [i['nama'] for i in hasil_akhir if i['nilai'] > 65]
#     return lulus
# hasil_akhir = [ {'nama':'Reza', 'nilai':70}, {'nama':'Ciut', 'nilai':63}, {'nama':'Dian', 'nilai':80}, {'nama':'Badu', 'nilai':40} ]
# print(lulus_saja(hasil_akhir))

# no 1 lebih simpel
# def lulus_saja(hasil_akhir):
#     lulus = []
#     for i in hasil_akhir:
#         if i['nilai'] > 65:
#             lulus.append(i['nama'])
#     return lulus
# print(lulus_saja([ {'nama':'Reza', 'nilai':70}, {'nama':'Ciut', 'nilai':63}, {'nama':'Dian', 'nilai':80}, {'nama':'Badu', 'nilai':40} ]))

# no 2
# def balikan(buah):
#     balik = []
#     for i in range(len(buah)):
#         balik.append(buah[len(buah)-1-i])
#     return balik
# print(balikan(['pepaya', 'mangga', 'pisang', 'durian', 'jambu']))

# no 3
# def duplikat(buah):
#     hasil = []
#     for i in buah:
#         hasil.append(i)
#         hasil.append(i)
#     return hasil
# print(duplikat(['pepaya', 'mangga', 'pisang', 'durian', 'jambu']))

# no 4
# def konsonan(kata):
#     hasil = []
#     for i in kata:
#         if i not in ("a","e","o","u","i"," "):
#             hasil + i
#     return hasil
# konsonan("Nurul Fikri")

# def consonants(s):
#     vokal = 'aeiouAEIOU'
#     return ''.join(huruf for huruf in s if huruf not in vokal)

# print(consonants("Nurul Fikri"))

# def konsonan(kalimat):
#     hasil = ""
#     for kata in kalimat:
#         if kata not in 'AIUEOaeiou':
#             hasil += kata
#     return hasil
# print(konsonan("Nurul Fikri"))




# no 1
def lulus_saja(hasil_akhir):
    lulus = []
    for i in hasil_akhir:
        if i['nilai'] > 65:
            lulus.append(i['nama'])
    return lulus
print(lulus_saja([ {'nama':'Reza', 'nilai':70}, {'nama':'Ciut', 'nilai':63}, {'nama':'Dian', 'nilai':80}, {'nama':'Badu', 'nilai':40} ]))

# no 2
def balikan(buah):
    balik = []
    for i in range(len(buah)):
        balik.append(buah[len(buah)-1-i])
    return balik
print(balikan(['pepaya', 'mangga', 'pisang', 'durian', 'jambu']))

# no 3
def duplikat(buah):
    hasil = []
    for i in buah:
        hasil.append(i)
        hasil.append(i)
    return hasil
print(duplikat(['pepaya', 'mangga', 'pisang', 'durian', 'jambu']))

# no 4
def konsonan(kalimat):
    hasil = ""
    for kata in kalimat:
        if kata not in 'AIUEOaeiou':
            hasil += kata
    return hasil
print(konsonan("Nurul Fikri"))