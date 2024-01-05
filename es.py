# Daftar menu
nama_pemesan : input("masukan nama pemesan: ")

menu = {
    'nasi goreng': 15000,
    'mie goreng': 12000,
    'ayam goreng': 20000,
    'soto ayam': 18000,
    'es teh': 5000,
}

while True:
    # Inisialisasi daftar pesanan
    daftar_pesanan = []

    print("Menu:")
    for item, harga in menu.items():
        print(f"{item.capitalize()}: {harga} IDR")

    while True:
        # Meminta pengguna memasukkan pesanan
        pesanan = input("Masukkan pesanan (ketik 'selesai' untuk menyelesaikan pesanan, 'tambah' untuk menambah pesanan baru): ")

        # Mengecek apakah pengguna ingin menyelesaikan pesanan
        if pesanan.lower() == 'selesai':
            break  # Keluar dari loop pesanan jika pengguna mengetik 'selesai'
        elif pesanan.lower() == 'tambah':
            # Loop bersarang untuk menambah pesanan baru
            while True:
                pesanan_baru = input("Tambahkan pesanan baru (ketik 'selesai' untuk kembali): ")
                if pesanan_baru.lower() == 'selesai':
                    break  # Keluar dari loop pesanan baru jika pengguna mengetik 'selesai'
                elif pesanan_baru.lower() in menu:
                    daftar_pesanan.append(pesanan_baru)
                else:
                    print("Menu tidak valid. Silakan pilih dari menu.")
        elif pesanan.lower() in menu:
            # Menambahkan pesanan ke daftar pesanan
            daftar_pesanan.append(pesanan)
        else:
            print("Menu tidak valid. Silakan pilih dari menu.")

    # Menampilkan daftar pesanan
    print("\nDaftar Pesanan Anda:")
    total_harga = 0
    for pesanan in daftar_pesanan:
        harga = menu.get(pesanan.lower(), 0)
        total_harga += harga
        print(f"- {pesanan.capitalize()}: {harga} IDR")

    print(f"\nTotal Harga: {total_harga} IDR")

    # Mengecek apakah pengguna ingin memesan lagi
    pesan_lagi = input("Apakah Anda ingin memesan lagi? (ya/tidak): ")
    if pesan_lagi.lower() != 'ya':
        break  # Keluar dari loop utama jika pengguna tidak ingin memesan lagi
