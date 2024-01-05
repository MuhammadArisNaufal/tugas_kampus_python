class bank:
    noRek=''
    nama=''
    saldo=0
    Bank='arisu.company'

    def __init__(self, no, nasabah, saldo,):
        self.noRek=no
        self.nama=nasabah
        self.saldo=saldo
      

    def nabung(self, uang):
        self.saldo += uang
    
    def tarik(self, uang):
        self.saldo -= uang
    
    def cetak(self):
        print(bank.Bank, self.noRek, self.nama, self.saldo)