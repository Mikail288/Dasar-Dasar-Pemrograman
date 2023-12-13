class gempa:
    lokasi = ""
    skala = ""

    def __init__(self,lokasi,skala):
        self.skala = skala
        self.lokasi = lokasi
    
    def dampak(self):
        if self.skala < 2:
            print("dampak gempa tidak berasa")
        elif self.skala >= 2 and self.skala <= 4:
            print("dampak gempa bangunan retak-retak")
        elif self.skala > 4 and self.skala < 7:
            print("dampak gempa bangunan roboh")
        else:
            print("dampak gempa bangunan roboh dan berpotensi tsunami")
