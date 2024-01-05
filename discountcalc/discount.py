import tkinter as tk
from tkinter import messagebox

def hitung_diskon():
    harga_awal = entry_harga_awal.get()
    diskon = entry_diskon.get()

    if harga_awal and diskon:
        harga_awal = float(harga_awal)
        diskon = float(diskon)

        if harga_awal >= 0 and 0 <= diskon <= 100:
            nilai_diskon = (diskon / 100) * harga_awal
            harga_setelah_diskon = harga_awal - nilai_diskon
            hasil_label.config(text=f"Harga Setelah Diskon: ${harga_setelah_diskon:.2f}")
        else:
            messagebox.showerror("Error", "Input tidak valid")
    else:
        messagebox.showerror("Error", "Masukkan angka yang valid")

# Membuat GUI
app = tk.Tk()
app.title("Kalkulator Diskon")

# Label dan Entry untuk Harga Awal
label_harga_awal = tk.Label(app, text="Harga Awal:")
label_harga_awal.pack()

entry_harga_awal = tk.Entry(app)
entry_harga_awal.pack()

# Label dan Entry untuk Persentase Diskon
label_diskon = tk.Label(app, text="Diskon (%):")
label_diskon.pack()

entry_diskon = tk.Entry(app)
entry_diskon.pack()

# Tombol untuk Menghitung Diskon
hitung_button = tk.Button(app, text="Hitung Diskon", command=hitung_diskon)
hitung_button.pack()

# Label untuk Menampilkan Hasil
hasil_label = tk.Label(app, text="")
hasil_label.pack()

# Menjalankan aplikasi
app.mainloop()
