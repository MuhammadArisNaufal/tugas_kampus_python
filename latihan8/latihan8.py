# def hello():
#     print ("yowaimo")
#     print ("gojo")

# hello()
# hello()

# def panggil():
#     hello()
#     print ("hehehe")

# panggil()

# def say(aing,ti):
#     print ("nami aing teh", aing)
#     print ("nu aing tinggal na ti ", ti)

# say ("yuji", "lombok")
# say ("lombok", "yuji")

# def tambah(angka1, angka2):
#     hasil = angka1 + angka2
#     print("Hasil penjumlahan:", hasil)

# tambah (2,1)

# def penjumlahan(angka1, angka2):
#     hasil = angka1 * angka2
#     return hasil

# penjumlahan = (3*2)

# print("Hasil penjumlahan:", penjumlahan)

# def biodata(nama, alamat, gender, umur, hobi):
#     print ("Nama :",nama)
#     print ("Alamat :", alamat)
#     print ("Gender :", gender)
#     print ("Umur :", umur)
#     print ("Hobi :", hobi)

# biodata ("Muhammad Aris", "Bogor", "Pria", "20", "Berkarya")

# def nilai(score):
#     if score<=60 :
#         print ("gagal")
#     elif score<=70 :
#         print("baik") 
#     elif score<=80 :
#         print("sangat baik") 
#     else :
#         print("istimewa") 

# nilai (60)

# def ganjil(bil):
#     ganjil = [x for x in range(1, bil) if x % 2 != 0]
#     return ganjil

# nilai = 100

# print(ganjil(nilai))

# # mencari nilai ganjil dengan while
# def nilai (numbers):
#     bil=0
#     while bil<=numbers:       
#         bil +=1
#         if (bil % 2 != 0):
#             print(bil)        
#         if (bil == numbers):
#             break
        
# nilai(100)

# mencari nilai ganjil dengan for
def nilai (numbers):
    for i in range(1,numbers):
        if i%2 ==0:
            print (i, end=",")

        
nilai(100)