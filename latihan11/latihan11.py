# class orang:
#     nama='gojo'
#     umur='22'

#     def bernafas(self):
#         print('saya bisa bernafas')

#     def berjalan(self):
#         self.bernafas()
#         print('saya bisa berjalan')

# mahasiswa=orang()
# print(mahasiswa.nama)
# mahasiswa.berjalan()

# dosen=orang()
# dosen.nama = 'yaga'
# print(dosen.nama)

# class orang:
#     nama=''
#     umur=''

#     def __init__(self, name, age):
#         self.nama = name
#         self.umur = age

#     def bernafas(self):
#         print('saya bisa bernafas')

#     def berjalan(self):
#         self.bernafas()
#         print('saya bisa berjalan')

# mahasiswa=orang('rocky','11')
# print(mahasiswa.nama)
# print(mahasiswa.umur)
# mahasiswa.berjalan()

class bank:
    noRek=''
    nama=''
    saldo=0
    Bank='arisu.company'

    def __init__(self, no, nasabah, saldo,):
        self.noRek=no
        self.nama=nasabah
        self.saldo=saldo
        bank.Bank +=1

    def nabung(self, uang):
        self.saldo += uang
    
    def tarik(self, uang):
        self.saldo -= uang
    
    def cetak(self):
        print(bank.Bank, self.norek, self.nama, self.saldo)