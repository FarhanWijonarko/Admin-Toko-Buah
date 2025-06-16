# 🛒 Admin Toko Buah

Program **Admin Toko Buah** adalah aplikasi berbasis CLI (Command Line Interface) sederhana yang memungkinkan pengguna untuk mengelola data buah-buahan di sebuah toko, termasuk menambah stok, menghapus buah, dan melakukan proses pembelian.

## 📦 Fitur

1. **Menampilkan Daftar Buah**  
   Menampilkan buah-buahan yang tersedia lengkap dengan index, nama, stok, dan harga.

2. **Menambahkan Buah Baru**  
   Pengguna dapat menambahkan buah baru jika belum ada sebelumnya.

3. **Menghapus Buah**  
   Pengguna bisa menghapus buah berdasarkan index dari daftar buah.

4. **Membeli Buah**  
   Pembeli dapat memilih buah berdasarkan index, menentukan jumlah pembelian, dan melihat total harga beserta proses pembayaran dan kembalian.

5. **Keluar**  
   Menutup program.

## 🧮 Contoh Tampilan Menu

```
      Selamat Datang di Pasar Buah

      List Menu
      ]1. Menampilkan Daftar Buah
      ]2. Menambahkan Buah
      ]3. Menghapus Buah
      ]4. Membeli Buah
      ]5. Keluar
```

## 🧰 Teknologi yang Digunakan

- Python 3
- Library: [`tabulate`](https://pypi.org/project/tabulate/) untuk tampilan tabel di terminal

## 🚀 Cara Menjalankan Program

1. **Clone repository:**

   ```bash
   git clone https://github.com/FarhanWijonarko/Admin-Toko-Buah.git
   cd Admin-Toko-Buah
   ```

2. **Install library `tabulate` (jika belum terinstall):**

   ```bash
   pip install tabulate
   ```

3. **Jalankan program:**

   ```bash
   python admin_toko_buah.py
   ```

## 📌 Catatan

- ✅ Data buah yang stok-nya habis tidak akan ditampilkan dalam daftar.
- 🛒 Sistem pembelian memiliki fitur keranjang sementara (chart) untuk menghitung total harga, termasuk validasi uang dan perhitungan kembalian.
- ⌨️ Program berbasis input manual dan dijalankan sepenuhnya lewat terminal.
- ⚠️ Jika nama buah sudah ada di daftar, sistem akan menolak penambahan.

---

> Dibuat oleh Farhan Wijonarko
