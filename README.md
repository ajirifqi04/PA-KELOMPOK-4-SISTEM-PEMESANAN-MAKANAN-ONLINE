# PA-KELOMPOK-4-SISTEM-PEMESANAN-MAKANAN-ONLINE

**SISTEM PEMESANAN MAKANAN ONLINE**

# === 👥 Anggota Kelompok 4 - Sistem Informasi B ===
1. Aji Rifqi Suryana (2509116054)
2. Ghaida Suci Nahiza (2509116077)
3. Muhammad Nadhir Sultan Azzaky (2509116080)

# === 🧩 FLOWCHART ===

# MENU UTAMA

![PA DDP4-Halaman-1](https://github.com/user-attachments/assets/629945b7-8db2-48eb-895e-26769429e5b5)

# MENU ADMIN

![PA DDP4-Halaman-2](https://github.com/user-attachments/assets/84afaeeb-7436-4bb7-9dfc-f3a68217c9dd)

# MENU USER

![PA DDP4-Halaman-3](https://github.com/user-attachments/assets/a110f965-28da-4f0d-833b-8712ee9108af)

# === PENJELASAN FLOWCHART ===

# **🧩 Flowchart Menu Awal / Login & Registrasi**

Flowchart ini menjelaskan alur awal saat program pertama kali dijalankan. Flowchart ini menggambarkan tahap autentikasi awal sistem, di mana pengguna dapat membuat akun baru atau login sebagai admin maupun user untuk masuk ke tahap berikutnya.

🔹 Penjelasan Alur :

**Mulai** : Program dijalankan dan menampilkan menu utama dengan tiga pilihan yaitu:
   1. Buat Akun
   2. Login
   3. Keluar
  
**1. Buat Akun (User)** : Jika pengguna memilih “Buat Akun”, sistem meminta:
   1. Username
   2. Password
   3. Nama Lengkap

 Setelah data diisi, sistem akan menyimpan file **Database Akun CSV**, Lalu menampilkan notifikasi bahwa akun berhasil di buat

**2. Login** : Pengguna bisa login sebagai:
   1. **Admin** => Memasukkan username dan password khusus admin. Jika benar, akan diarahkan ke **Menu Admin**.
   2. **User** => Memasukkan username dan password yang sudah terdaftar, lalu akan diarahkan ke **Menu User**.

**3. Keluar**: Jika memilih "Keluar", maka program akan menampilkan notifikasi bahwa sistem selesai dijalankan, lalu berhenti.

# **🧩 Flowchart Menu Admin**

Flowchart ini menggambarkan proses yang dapat dilakukan oleh admin untuk mengelola data makanan pada sistem. Flowchart ini menunjukkan fungsi **CRUD (Create, Read, Update, Delete)** untuk data menu, di mana admin sepenuhnya mengelola daftar makanan yang akan dipesan oleh user.

🔹 Penjelasan Alur:

**Tampilan Menu Admin**: Admin memiliki 5 opsi utama yaitu:
 1. Lihat Menu : Sistem akan membaca file **Database Menu CSV** dan akan menampilkan tabel daftar menu yang tersedia.
 2. Tambah Menu : Admin diminta memasukkan nama dan harga makanan baru. Data disimpan ke file CSV, lalu sistem menampilkan notifikasi bahwa menu berhasil ditambahkan dan menampilkan tabel menu terbaru.
 3. Hapus Menu : Admin memasukkan nama menu yang ingin dihapus. Sistem membaca data di file CSV, menghapus data yang sesuai, lalu menampilkan tabel menu terbaru.
 4. Ubah Menu : Admin dapat mengubah harga dari menu tertentu. Setelah diperbarui, data disimpan kembali ke file CSV dan sistem menampilkan notifikasi bahwa menu berhasil diperbarui dan menampilkan tabel menu terbaru.
 5. Keluar : Admin dapat keluar dari sistem, dan akan menampilkan menu utama.

# **🧩 Flowchart Menu User**

Flowchart ini menggambarkan alur transaksi pengguna, mulai dari melihat menu hingga melakukan pembayaran. Sistem juga menyediakan fitur saldo dan riwayat pemesanan untuk memudahkan pengguna mengelola aktivitas mereka.

🔹 Penjelasan Alur:

**Tampilan Menu User**: User memiliki 6 opsi utama yaitu:
1. Lihat Menu : Sistem membaca file Database Menu CSV dan menampilkan daftar makanan beserta harganya.
2. Order : Pengguna memilih makanan yang ingin dipesan beserta jumlahnya, kemudian sistem secara otomatis menghitung total harga. Jika saldo pengguna mencukupi, maka transaksi akan berhasil diproses, data pesanan akan disimpan ke dalam file Database CSV, dan saldo pengguna akan otomatis berkurang sesuai total pembelian. Namun, apabila saldo tidak mencukupi, sistem akan menolak transaksi dan menampilkan peringatan agar pengguna melakukan top up terlebih dahulu. Setelah pembayaran berhasil, sistem menampilkan invoice atau struk pemesanan sebagai bukti transaksi.
4. Top Up Saldo : Pengguna dapat menambahkan saldo minimal Rp50.000 dan maksimal Rp5.000.000. Sistem akan memperbarui file **Database Akun CSV**, lalu menampilkan notifikasi bahwa saldo berhasil ditambahkan.
5. Cek Saldo : Sistem membaca data dari **Database Akun CSV** dan akan menampilkan jumlah saldo saat ini.
6. Riwayat Order : Sistem membaca data dari **Database Pesanan CSV** dan menampilkan histori pembelian (nama menu, jumlah, total harga, waktu transaksi).
7. Keluar : Menampilkan notifikasi bahwa program selesai dijalankan dan kembali ke menu utama.
