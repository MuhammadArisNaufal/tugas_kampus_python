nama_pembeli = input("Masukkan Nama Anda (Pemesan) :")
no_hp_pembeli = input("Masukkan No Hp Anda (Pemesan) :")
pilih_menu = input("""pilih salah satu menu :
Menu Makanan 
           a.nasi goreng............15k 
           b.mie goreng.............12k
           c.ayam geprek............18k
Menu Minuman 
           d.aneka jus..............15k
           e.SoftDrink..............10k
           f.Sweet Ice Tea..........5k

masukan abjad menu: """)



daftar_pesanan= []
while True:
    if pilih_menu == "a":
        b = int(input("jumlah :"))
        a = 15000
    elif pilih_menu == "b":
        b = int(input("jumlah :"))
        a= 12000
    elif pilih_menu == "c":
        b = int(input("jumlah :"))
        a = 18000
    elif pilih_menu == "d":
        b = int(input("jumlah :"))
        a = 15000
    elif pilih_menu == "e":
        b = int(input("jumlah :"))
        a = 10000
    elif pilih_menu == "f":
        b = int(input("jumlah :"))
        a = 5000
        while True:
            print ("apakah ada pesanan lain? (ya/tidak) ")
            
            if == "ya"
    # else:
        # print("menu tidak tersedia")

total_harga = b*a

print("nama pembeli: ",nama_pembeli)
print("nomor hp: ",no_hp_pembeli)
print("harga yang harus dibayar",total_harga)