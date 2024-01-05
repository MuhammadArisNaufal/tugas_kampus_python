import math
def tambah(a,b):
    hasil= a + b
    print (a,"+",b,"=",hasil)

def kurang(a,b):
    hasil= a - b
    print (a,"-",b,"=",hasil)

def kali(a,b):
    hasil= a * b
    print (a,"*",b,"=",hasil)

def pangkat(a,b):
    hasil= a ** b
    print (a,"^",b,"=",hasil)

def bagi(a,b):
    hasil= a / b
    print (a,"/",b,"=",hasil)

def logaritma(angka):
    hasil = math.log(angka)
    print ("logaritma dari", angka," adalah", hasil)

def akar(angka):
    hasil = math.sqrt(angka)
    print ("akar dari", angka, "adalah ", hasil)

def sin(angka):
    hasil = math.sin(angka)
    print ("sin dari ",angka, "adalah", hasil)

def cos(angka):
    hasil = math.cos(angka)
    print ("cos dari ", angka, "adalah ", hasil)

def tan(angka):
    hasil = math.tan(angka)
    print ("tan dari ", angka,"adalah ", hasil)