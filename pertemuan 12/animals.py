from animal import *
class badak(animal):
    def __init__(self, nama, makanan, habitat, kembangbiak,warna,cula):
        super().__init__(nama, makanan, habitat, kembangbiak)
        self.warna = warna
        self.cula = cula
    def datahewan(self):
        print(f"nama hewan: \t\t{self.name}\njenis makanan: \t\t{self.makanan}\nhabitat: \t\t{self.habitat}\ncara berkembangbiak: \t{self.kembangbiak}\nwarna: \t\t\t{self.warna}\njumlah cula: \t\t{self.cula}")

class singa(animal):
    def __init__(self, nama, makanan, habitat, kembangbiak,carabernafas,kaki):
        super().__init__(nama, makanan, habitat, kembangbiak)
        self.carabernafas = carabernafas
        self.kaki = kaki
    def datahewan(self):
        print(f"nama hewan: \t\t{self.name}\njenis makanan: \t\t{self.makanan}\nhabitat: \t\t{self.habitat}\ncara berkembangbiak: \t{self.kembangbiak}\ncara bernafas: \t\t{self.carabernafas}\njumlah kaki: \t\t{self.kaki}\n")

class gorila(animal):
    def __init__(self, nama, makanan, habitat, kembangbiak,warnapunggung,pemimpin):
        super().__init__(nama, makanan, habitat, kembangbiak)
        self.warnapunggung = warnapunggung
        self.pemimpin = pemimpin
    def datahewan(self):
        print(f"nama hewan: \t\t{self.name}\njenis makanan: \t\t{self.makanan}\nhabitat: \t\t{self.habitat}\ncara berkembangbiak: \t{self.kembangbiak}\nwarna punggung: \t{self.warnapunggung}\napakah pemimpin kawanan:{self.pemimpin}\n")

class domba(animal):
    def __init__(self, nama, makanan, habitat, kembangbiak,suara,tanduk):
        super().__init__(nama, makanan, habitat, kembangbiak)
        self.suara = suara
        self.tanduk = tanduk
    def datahewan(self):
        print(f"nama hewan: \t\t{self.name}\njenis makanan: \t\t{self.makanan}\nhabitat: \t\t{self.habitat}\ncara berkembangbiak: \t{self.kembangbiak}\nsuara: \t\t\t{self.suara}\napakah bertanduk: \t{self.tanduk}\n")

hewan = badak('badak','herbivora','darat','melahirkan','abu abu','satu')
hewan.datahewan()
hewan = singa('singa','karnivora','darat','melahirkan','paru-paru','4')
hewan.datahewan()
hewan = gorila('gorila','omnivora','darat','melahirkan','silver','iya')
hewan.datahewan()
hewan = domba('domba','herbivora','darat','melahirkan','mengembik','iya')
hewan.datahewan()