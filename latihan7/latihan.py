# Meminta pengguna memasukkan jenis bensin
jenis_bensin = input(""" Masukkan jenis bensin 
1. Pertalite
2. Premium
3. Pertamax

Masukan Input: """)

# Meminta pengguna memasukkan harga bensin per liter (dalam IDR)
# harga_bensin = float(input("Masukkan harga bensin per liter (dalam IDR): "))


# Percabangan berdasarkan jenis bensin
if jenis_bensin == "1":
    harga_per_liter = 10000  # Harga Pertalite per liter (contoh)
    konsumsi_bahan_bakar = 12  # Konsumsi bahan bakar kendaraan per liter (contoh)
elif jenis_bensin == "2":
    harga_per_liter = 14000  # Harga Premium per liter (contoh)
    konsumsi_bahan_bakar = 13  # Konsumsi bahan bakar kendaraan per liter (contoh)
elif jenis_bensin == "3":
    harga_per_liter = 17000  # Harga Pertamax per liter (contoh)
    konsumsi_bahan_bakar = 13  # Konsumsi bahan bakar kendaraan per liter (contoh)
else:
    print("Jenis bensin tidak dikenal.")
    exit()

# Meminta pengguna memasukkan nama kota tujuan
kota_tujuan = input("""Masukkan nama kota tujuan
1. Jakarta
2. Bekasi
3. Depok
4. Tanggerang
5. Bogor

Masukan Input: """)

# Percabangan berdasarkan jenis bensin
if kota_tujuan == "1":
    jarak_tujuan = 20  # Harga Pertalite per liter (contoh)
    # konsumsi_bahan_bakar = 12  # Konsumsi bahan bakar kendaraan per liter (contoh)
elif kota_tujuan == "2":
    jarak_tujuan = 35  # Harga Premium per liter (contoh)
    # konsumsi_bahan_bakar = 13  # Konsumsi bahan bakar kendaraan per liter (contoh)
elif kota_tujuan == "3":
    jarak_tujuan = 5  # Harga Pertamax per liter (contoh)
    # konsumsi_bahan_bakar = 13  # Konsumsi bahan bakar kendaraan per liter (contoh)
elif kota_tujuan == "4":
    jarak_tujuan = 99  # Harga Pertamax per liter (contoh)
    # konsumsi_bahan_bakar = 13  # Konsumsi bahan bakar kendaraan per liter (contoh)
elif kota_tujuan == "5":
    jarak_tujuan = 120  # Harga Pertamax per liter (contoh)
    # konsumsi_bahan_bakar = 13  # Konsumsi bahan bakar kendaraan per liter (contoh)
else:
    print("Kota tidak ada dalam list.")
    exit()

# Meminta pengguna memasukkan konsumsi bahan bakar (jarak per liter)
# konsumsi_bahan_bakar = float(input("Masukkan konsumsi bahan bakar (kilometer per liter): "))

# Meminta pengguna memasukkan jarak ke kota tujuan (dalam kilometer)
# jarak_tujuan = float(input("Masukkan jarak ke kota tujuan (dalam kilometer): "))

# Menghitung jumlah bensin yang diperlukan
bensin_diperlukan = int(jarak_tujuan / konsumsi_bahan_bakar)

# Menghitung biaya perjalanan
biaya_perjalanan = int(bensin_diperlukan * harga_per_liter)

# Menampilkan informasi perjalanan
# print("Informasi Perjalanan:")
# print("Jenis Bensin:", jenis_bensin)
# print("Harga Bensin per Liter:", harga_per_liter, "IDR/liter")
# print("Konsumsi Bahan Bakar Kendaraan:", konsumsi_bahan_bakar, "km/liter")
# print("Kota Tujuan:", kota_tujuan)
# print("Jarak ke Kota Tujuan:", jarak_tujuan, "kilometer")
print("Jumlah Bensin yang Diperlukan:", bensin_diperlukan, "liter")
print("Biaya Perjalanan:", biaya_perjalanan, "IDR")
