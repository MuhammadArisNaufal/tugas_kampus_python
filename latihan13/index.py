# class orang :
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname

#     def cetak(self):
#         print('nama saya:',self.fname,self.lname)
    
#     def makan(self):
#         print('saya bisa makan')

# class mahasiswa (orang):
#     def __init__(self, fname, lname,prodi,angkatan):
#         super().__init__(fname, lname)
#         self.prodi = prodi
#         self.angkatan = angkatan

#     def cetak(self):
#         super().cetak()
#         print(self.prodi,self.angkatan)

# class pegawai(orang):
#     def berkerja(self):
#         print ('saya berkerja')


# # x = orang('gojo', 'satoru')
# # x.cetak()
# # x.makan()

# y = mahasiswa('geto', 'suguru', 'TI', 2023)
# y.cetak()

class animal:
    def __init__(self, namaBinatang, makanan, hidup, berkembangBiak):
        self.namaBinatang = namaBinatang
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak
    
    def cetak(self):
        print('Nama Hewan\t:', self.namaBinatang,
              '\nMakanan\t\t:', self.makanan,
              '\nHabitat\t\t:', self.hidup,
              '\nBerkembang Biak\t:', self.berkembangBiak)
        
class bdk(animal):
    def __init__(self, namaBinatang, makanan, hidup, berkembangBiak,status,sifat):
        super().__init__(namaBinatang, makanan, hidup, berkembangBiak)
        self.status = status
        self.sifat = sifat

    def cetak(self):
        super().cetak()
        print('Status\t\t:', self.status,
              '\nSifat\t\t:', self.sifat,
              '\n-------------------------------------------------')
        
class ulr(animal):
    def __init__(self, namaBinatang, makanan, hidup, berkembangBiak,status,sifat):
        super().__init__(namaBinatang, makanan, hidup, berkembangBiak)
        self.status = status
        self.sifat = sifat

    def cetak(self):
        super().cetak()
        print('Status\t\t:', self.status,
              '\nSifat\t\t:', self.sifat,
              '\n-------------------------------------------------')
        
class ikn(animal):
    def __init__(self, namaBinatang, makanan, hidup, berkembangBiak,status,sifat):
        super().__init__(namaBinatang, makanan, hidup, berkembangBiak)
        self.status = status
        self.sifat = sifat

    def cetak(self):
        super().cetak()
        print('Status\t\t:', self.status,
              '\nSifat\t\t:', self.sifat,
              '\n-------------------------------------------------')
        
class sng(animal):
    def __init__(self, namaBinatang, makanan, hidup, berkembangBiak,status,sifat):
        super().__init__(namaBinatang, makanan, hidup, berkembangBiak)
        self.status = status
        self.sifat = sifat

    def cetak(self):
        super().cetak()
        print('Status\t\t:', self.status,
              '\nSifat\t\t:', self.sifat,
              '\n-------------------------------------------------')
        
class hrm(animal):
    def __init__(self, namaBinatang, makanan, hidup, berkembangBiak,status,sifat):
        super().__init__(namaBinatang, makanan, hidup, berkembangBiak)
        self.status = status
        self.sifat = sifat

    def cetak(self):
        super().cetak()
        print('Status\t\t:', self.status,
              '\nSifat\t\t:', self.sifat,
              '\n-------------------------------------------------')
        
class srg(animal):
    def __init__(self, namaBinatang, makanan, hidup, berkembangBiak,status,sifat):
        super().__init__(namaBinatang, makanan, hidup, berkembangBiak)
        self.status = status
        self.sifat = sifat

    def cetak(self):
        super().cetak()
        print('Status\t\t:', self.status,
              '\nSifat\t\t:', self.sifat,
              '\n-------------------------------------------------')
        
class dmb(animal):
    def __init__(self, namaBinatang, makanan, hidup, berkembangBiak,status,sifat):
        super().__init__(namaBinatang, makanan, hidup, berkembangBiak)
        self.status = status
        self.sifat = sifat

    def cetak(self):
        super().cetak()
        print('Status\t\t:', self.status,
              '\nSifat\t\t:', self.sifat,
              '\n-------------------------------------------------')