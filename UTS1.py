# pilihanrumus =input("""*** PILIH OPERASI ***
# 1. HITUNG LUAS TRAPESIUM
# 2. HITUNG KELILING TRAPESIUM

# MASUKAN PILIHAN:""")
# match pilihanrumus:
#     case "1":
#         a = int(input("masukan sisi A: "))
#         b = int(input ("masukan sisi B: "))
#         t = int(input("masukan tingggi: "))
#         luas =int(1/2*a+b*t)
#         print ("luas trapesium =", luas)
#     case "2":
#         ab = int(input("masukan sis AB: "))
#         bc = int(input("masukan sis BC: "))
#         cd = int(input("masukan sis CD: "))
#         da = int(input("masukan sis DA: "))
#         keliling = int(ab+bc+cd+da)
#         print ("keliling trapesium=", keliling)
#     case _ :
#         print ("pilihan tidak tersedia")

    
a = int(input("masukan nomor pertama: "))
b = int(input("masukan nomor kedua: "))
operator = input("""PILIH OPERATOR
- tambah
- kurang
- kali
- bagi
- pangkat

MASUKAN OPERATORNYA: """)

if operator == "tambah":
    partikel = "+"
    pilihan = "tambah"
    hasil = int(a+b)
elif operator == "kurang":
    partikel = "-"
    pilihan = "kurang"
    hasil = int(a-b)
elif operator == "kali":
    partikel = "*"
    pilihan = "kali"
    hasil = int(a*b)
elif operator == "bagi":
    partikel = "/"
    pilihan = "bagi"
    hasil = int(a/b)
elif operator == "pangkat":
    partikel = "**"
    pilihan = "pangkat"
    hasil = int(a**b)
else : 
    print("pilihan tidak tersedia")

print ("angka pertama:", a)
print ("angka kedua:", b)
print ("operator pilihan:", pilihan)
print ("hasil perhitungan operator:", a, partikel, b, "=", hasil)