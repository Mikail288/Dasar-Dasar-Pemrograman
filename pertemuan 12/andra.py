class spekmobil:
    mesin = ''
    rangka = ''
    def __init__(self,mesin,rangka):
        self.mesin = mesin
        self.rangka = rangka

    def cat(self):
        print(f'{self.rangka} dicat')

# class pajero(spekmobil):
#     def __init__(self, mesin, rangka, warna):
#         super().__init__(self,)
mobil = spekmobil('v8')
mobil.cat()