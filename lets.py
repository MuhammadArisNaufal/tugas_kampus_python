mylist = ["spacy", "motor", "125", "putih", "2"]
mylist.append ("13.200.000")
mylist.append ("matic")
mylist.insert (2, "honda")

print (mylist)

pilihanrumus =input("""
            *** PILIH OPERASI ***
                1. HITUNG PERSEGI
                2. HITUNG LINGKARAN
                3. HITUNG SEGITIGA

                MASUKAN PILIHAN:""")
match pilihanrumus:
    case "1":
        s = int(input("masukan sisi: "))
        persegi =s*s
        print ("luas persegi =", persegi)
    case "2":
        r = int(input("masukan jari-jari: "))
        phi = 3.14
        lingkaran = phi*r*r
        print ("luas lingkaran =", lingkaran)
    case "3":
        a = int(input("masukan alas: "))
        t = int(input("masukan tinggi: "))
        segitiga = int(1/2*a*t)
        print ("luas segitiga =", segitiga)
    case _ :
        print ("pilihan tidak tersedia")