#biodata 1
#biodata1= """nama: Muhammad Aris Naufal
#nim2: 0110223020
#kelas: TI01
#no telp: 08xxxxxxxxxx
#alamat: Bogor"""
#print(biodata1)

#biodata 2
#biodata2= """nama: Fahdan Zulfa Alsauqi
#nim2: 011022304
#kelas: TI01
#no telp: 08xxxxxxxxxx
#alamat: Bogor"""
#print(biodata2)

#berat badan ideal
#tinggi_badan= 175
#bbil= ((tinggi_badan-100)-((tinggi_badan-100)*0.10))
#bbip= ((tinggi_badan-100)-((tinggi_badan-100)*0.15))
#print(bbil)
#print(bbip)

#konversi celcius ke farenheit
#celcius= 4
#farenheit= (celcius*9/5)+32
#print(farenheit)

#keliling dan luas tabung
#r= 3
#t= 15
#keliling= int(2*(r+t))
#luas= int(3.14*t*(r+2*t))
#print (keliling)
#print(luas) 

#x = 10
#hasil = (x < 11) and (x > 1) or (x > 9)

#print (hasil)

#pelanggan = "Aris"
#total = 200000

#if (total > 100000): 
#    keterangan = "congratulations!"

#if (total == 200000):
#    keterangan = "yohohoho!"

#else : 
#    keterangan = "thanks for your purchase"


#print ("selamat", pelanggan, "total belanja anda Rp.", total, keterangan)

#nama = "Eren Jaeger"
#matpel = "rumbling"
#nilai = 80

#keterangan = "lulus" if nilai >= 60 else "gagal"

#print ("Nama siswa\t:", nama, "\nMata Pelajaran\t:", matpel, "\nNilai \t \t:", nilai, "\nKeterangan\t:", keterangan)

#nama = "Eren Jaeger"
#matpel = "rumbling"
#nilai = 90

#if (nilai > 85) and (nilai <= 100 ):
#    keterangan = "A"
#elif (nilai > 75) and (nilai <= 85):
#    keterangan = "B"
#elif (nilai > 60) and (nilai <= 75):
#    keterangan = "C"
#elif (nilai > 30) and (nilai <= 60):
#    keterangan = "D"
#else:
#    keterangan = "E"

#print ("Nama siswa\t:", nama, "\nMata Pelajaran\t:", matpel, "\nNilai \t \t:", nilai, "\nGrade\t\t:", keterangan)

#nama = "John Doe"
#umur = 15

#if (umur > 0) and (umur < 18 ):
#    keterangan = "Anak-anak"
#elif (umur > 18) and (umur <= 65):
#    keterangan = "Dewasa"
#else:
#    keterangan = "Lanjut Usia"

#print ("Nama\t\t:", nama, "\nUsia\t\t:", umur,"\nketerangan\t:", keterangan)

#nilai = 30
#keterangan = "nilai ebih dari 50" if nilai >= 50 else "nilai kurang dari 50"

# print ("\nNilai \t \t:", nilai, "\nKeterangan\t:", keterangan)

# # mylist = ["spacy", "motor", "125", "putih", "2"]
# mylist.append ("13.200.000")
# mylist.append ("matic")
# mylist.insert (2, "honda")

# print (mylist)

# pilihanrumus =input("""
#             *** PILIH OPERASI ***
#                 1. HITUNG PERSEGI
#                 2. HITUNG LINGKARAN
#                 3. HITUNG SEGITIGA

#                 MASUKAN PILIHAN:""")
# match pilihanrumus:
#     case "1":
#         s = int(input("masukan sisi: "))
#         persegi =s*s
#         print ("luas persegi =", persegi)
#     case "2":
#         r = int(input("masukan jari-jari: "))
#         phi = 3.14
#         lingkaran = phi*r*r
#         print ("luas lingkaran =", lingkaran)
#     case "3":
#         a = int(input("masukan alas: "))
#         t = int(input("masukan tinggi: "))
#         segitiga = int(1/2*a*t)
#         print ("luas segitiga =", segitiga)