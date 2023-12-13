# class Orang:
#     nama = ""
#     umur = ""
#     def __init__(self,name,age):
#         self.nama = name
#         self.umur = age
#     def bernafas(self):
#         print("nafas cuy dan berumur", self.umur)
#     def berjalan(self):
#         self.bernafas()
#         print(self.nama, "bisa jalan juga")
        

# mahasiswa = Orang("acong","19")
# print(mahasiswa.nama)
# print(mahasiswa.umur)
# mahasiswa.berjalan()

class Bank:
    norek = ""
    nama = ""
    saldo = 0
    BANK = "Bank syariah NF"

    def __init__(self,no,nama,saldo):
        self.norek = no
        self.nama = nama
        self.saldo = saldo

    def nabung(self, uang):
        self.saldo += uang

    def tarik(self, uang):
        self.saldo -= uang
    
    def cetak(self):
        print(Bank.BANK)
        print("Nomor rekening: ",self.norek)
        print("Nama nasabah: ", self.nama)
        print("saldo: ",format(self.saldo,','))