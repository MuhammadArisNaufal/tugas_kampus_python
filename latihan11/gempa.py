class skalaGempa:
    lokasi=''
    skala=0

    def __init__(self, location, scale):
        self.lokasi=location
        self.skala=scale

    def dampak (self):
        if self.skala < 2:
            print('DAMPAK GEMPA\t: Gempa Tidak Berasa')
        elif self.skala < 4:
            print('DAMPAK GEMPA\t: Bangunan Retak-Retak')
        
        elif self.skala < 6:
            print('DAMPAK GEMPA\t: Bangunan Roboh')
        else:
            print('DAMPAK GEMPA\t: Bangunan Roboh dan Berpotensi Tsunami')

    def cetak(self):
        print ('\n===================================================================',
                '\nLAPORAN GEMPA!!!',
                '\n-------------------------------------------------------------------',
                '\nLOKASI GEMPA\t:',self.lokasi,
                '\nSKALA GEMPA \t:', self.skala)