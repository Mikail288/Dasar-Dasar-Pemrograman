
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
        print(Bank.BANK,
            '\n==========================',
            '\nNo. Rekening\t:',self.norek,
            '\nNama Nasabah\t:',self.nama,
            '\nSaldo\t\t: Rp. ',format(self.saldo, ','),
            '\n--------------------------'
            )