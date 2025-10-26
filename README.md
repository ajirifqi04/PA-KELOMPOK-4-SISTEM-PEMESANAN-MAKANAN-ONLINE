# PA-KELOMPOK-4-SISTEM-PEMESANAN-MAKANAN-ONLINE

**SISTEM PEMESANAN MAKANAN ONLINE**

=== 👥 Anggota Kelompok 4 - Sistem Informasi B ===
1. Aji Rifqi Suryana (2509116054)
2. Ghaida Suci Nahiza (2509116077)
3. Muhammad Nadhir Sultan Azzaky (2509116080)

 === 🧩 FLOWCHART ===

# MENU AWAL USER
![WhatsApp Image 2025-10-26 at 15 17 48_73f7484e](https://github.com/user-attachments/assets/64bcbf1c-925d-4fc2-8af7-7575a34f6d90)

# MENU ADMIN
![WhatsApp Image 2025-10-26 at 15 18 03_7421f319](https://github.com/user-attachments/assets/a4d234db-00e7-4020-9cc4-86a0238ed02d)

# MENU UTAMA USER
![WhatsApp Image 2025-10-26 at 15 18 21_d0ad5cfa](https://github.com/user-attachments/assets/a12072b4-928b-4725-9192-833c83eb16ab)

=== PENJELASAN FLOWCHART ===

**🧩 Flowchart Menu Awal / Login & Registrasi**

Flowchart ini menjelaskan alur awal saat program pertama kali dijalankan. Flowchart ini menggambarkan tahap autentikasi awal sistem, di mana pengguna dapat membuat akun baru atau login sebagai admin maupun user untuk masuk ke tahap berikutnya.

🔹 Penjelasan Alur:

**Mulai**: Program dijalankan dan menampilkan menu utama dengan tiga pilihan yaitu:
   1. Buat Akun
   2. Login
   3. Keluar
  
**1. Buat Akun (User)**: Jika pengguna memilih “Buat Akun”, sistem meminta:
   1. Username
   2. Password
   3. Nama Lengkap
 Setelah data diisi, sistem akan menyimpan file **DB Akun CSV**, Lalu menampilkan notifikasi bahwa akun berhasil di buat

**2. Login**: Pengguna bisa login sebagai:
   1. **Admin** => Memasukkan username dan password khusus admin. Jika benar, akan diarahkan ke **Menu Admin**.
   2. **User** => Memasukkan username dan password yang sudah terdaftar, lalu akan diarahkan ke **Menu User**.

**3. Keluar**: Jika memilih "Keluar", maka program akan menampilkan notifikasi bahwa sistem selesai dijalankan, lalu berhenti.

**🧩 Flowchart Menu Admin**

Flowchart ini menggambarkan proses yang dapat dilakukan oleh admin untuk mengelola data makanan pada sistem. Flowchart ini menunjukkan fungsi **CRUD (Create, Read, Update, Delete)** untuk data menu, di mana admin sepenuhnya mengelola daftar makanan yang akan dipesan oleh user.

🔹 Penjelasan Alur:

**Tampilan Menu Admin**: Admin disajikan 5 opsi utama yaitu:
 1. Lihat Menu : Sistem akan membaca file **DB Menu CSV** dan akan menampilkan tabel daftar menu yang tersedia.
 2. Tambah Menu : Admin diminta memasukkan nama dan harga makanan baru. Data disimpan ke file CSV, lalu sistem menampilkan notifikasi bahwa menu berhasil ditambahkan dan menampilkan tabel menu terbaru.
 3. Hapus Menu : Admin memasukkan nama menu yang ingin dihapus. Sistem membaca file CSV, menghapus data yang sesuai, lalu memperbarui tabel menu terbaru.
 4. Ubah Menu : Admin dapat mengubah harga dari menu tertentu. Setelah diperbarui, data disimpan kembali ke file CSV dan sistem menampilkan notifikasi bahwa menu berhasil diperbarui.
 5. Keluar : Admin dapat keluar dari sistem, dan program menampilkan notifikasi bahwa sesi admin telah selesai.

**🧩 3. Flowchart Menu User**

Flowchart ini menggambarkan alur transaksi pengguna, mulai dari melihat menu hingga melakukan pembayaran. Sistem juga menyediakan fitur saldo dan riwayat pemesanan untuk memudahkan pengguna mengelola aktivitas mereka.

🔹 Penjelasan Alur:

**Tampilan Menu User**: User disajikan 6 opsi utama yaitu:
1. Lihat Menu : Sistem membaca file DB Menu CSV dan menampilkan daftar makanan beserta harganya.
2. Order : Pengguna memilih makanan yang ingin dipesan beserta jumlahnya, kemudian sistem secara otomatis menghitung total harga. Jika saldo pengguna mencukupi, maka transaksi akan berhasil diproses, data pesanan akan disimpan ke dalam file pesanan.csv, dan saldo pengguna akan otomatis berkurang sesuai total pembelian. Namun, apabila saldo tidak mencukupi, sistem akan menolak transaksi dan menampilkan peringatan agar pengguna melakukan top up terlebih dahulu. Setelah pembayaran berhasil, sistem menampilkan invoice atau struk pemesanan sebagai bukti transaksi.
4. Top Up Saldo : Pengguna dapat menambahkan saldo minimal Rp50.000. Sistem akan memperbarui file **DB Akun CSV**, lalu menampilkan notifikasi bahwa saldo berhasil ditambahkan.
5. Cek Saldo : Sistem membaca data dari **DB Akun CSV** dan akan menampilkan jumlah saldo saat ini.
6. Riwayat Order : Sistem membaca data dari **DB Pesanan CSV** dan menampilkan histori pembelian (nama menu, jumlah, total harga, waktu transaksi).
7. Keluar : Menampilkan notifikasi bahwa program selesai dijalankan dan kembali ke menu utama.

=== OUTPUT PROGRAM ===

<img width="786" height="260" alt="image" src="https://github.com/user-attachments/assets/be04a21d-8d71-4aeb-834e-935b1a22b497" />

Tampilan ini adalah Menu Utama dari program yang berfungsi sebagai gerbang otentikasi awal, memungkinkan pengguna untuk Buat Akun, Login, atau Keluar dari aplikasi.

<img width="784" height="385" alt="image" src="https://github.com/user-attachments/assets/14b92baf-e341-4c94-a2b0-a405cf1ec1f4" />

Setelah memilih opsi '1' (Buat Akun) dari menu utama, program meminta input username, password, dan nama lengkap pengguna, lalu sistem akan memprosesnya dengan pesan Loading..., lalu menampilkan konfirmasi "Selamat! Akun kamu berhasil dibuat", dan bakal kembali ke menu utama.

<img width="787" height="293" alt="image" src="https://github.com/user-attachments/assets/595616a4-7b1b-4712-88e6-90105576cf42" />

Setelah memilih opsi '2' (Login), pengguna diarahkan untuk memasukkan username dan password yang telah di buat sebelumnya, yang kemudian diverifikasi dan menampilkan konfirmasi "Login Berhasil! Selamat datang, (Nama Lengkap)!" lalu sistem akan memprosesnya dengan pesan Loading...

<img width="767" height="330" alt="image" src="https://github.com/user-attachments/assets/a0723bf4-419f-4248-be1d-be76fa7b9cf3" />

dan akan memunculkan menu user seperti diatas ini setelah proses Loading...

<img width="398" height="475" alt="image" src="https://github.com/user-attachments/assets/f02c9ea9-7eea-47c0-9487-0a411f919fa5" />

Tampilan ini menunjukkan ketika anda memilih opsi '1' dari menu sebelumnya (kemungkinan Menu Admin atau Menu Setelah Login), lalu program akan memprosesnya dengan pesan Loading... dan menampilkan TABEL MENU yang berisi daftar makanan dan harganya, yaitu Mie Gacoan (10000), Udang Keju (10000), Ayam Geprek Ganja (13000), Ayam Katsu (20000), dan Nasi Goreng (15000), sebelum menunggu pengguna menekan Enter untuk kembali.

<img width="781" height="602" alt="image" src="https://github.com/user-attachments/assets/5b11c5fa-ec32-43d4-9066-c2764b8ec2dc" />

Setelah pengguna memilih opsi '2' dari menu sebelumnya, program menampilkan halaman ORDER yang tetap menyajikan TABEL MENU (termasuk Mie Gacoan, Udang Keju, Ayam Geprek Ganja, Ayam Katsu, dan Nasi Goreng beserta harganya) dan kemudian meminta pengguna untuk memasukkan nama menu yang ingin dipesan.


Tampilan ini melanjutkan proses pemesanan dengan menerima input nama menu yang ingin dipesan ("Ayam Geprek Ganja") dan jumlahnya ("1"), dan kemudian mengajukan pertanyaan konfirmasi "Apakah anda ingin memesan menu lain? (Y/N)" untuk "Y" artinya iya dan "N" artinya tidak.

<img width="781" height="571" alt="image" src="https://github.com/user-attachments/assets/a118724f-8c89-4ccd-a118-48a6944daba8" />

Tampilan ketika pengguna menjawab 'Y' pada pertanyaan "Apakah anda ingin memesan menu lain?", lalu program akan otomatis mengulang proses ORDER, menampilkan kembali TABEL MENU, dan meminta pengguna untuk "Masukkan nama menu yang ingin dipesan lagi.

<img width="784" height="495" alt="image" src="https://github.com/user-attachments/assets/3176a02d-7c85-4fde-8d61-419c351c5b5d" />

Setelah pengguna memesan item kedua, Mie Gacoan sejumlah 1, dan menjawab 'n' (Tidak) pada pertanyaan ingin memesanan menu lain?, program menampilkan halaman KONFIRMASI PESANAN dengan Ringkasan Pesanan (Ayam Geprek Ganja x1 dan Mie Gacoan x1) dan Total Pembayaran sebesar Rp 23.000, namun proses pembayaran gagal karena Saldo Anda: Rp 0, sehingga program menampilkan pesan "Saldo tidak cukup! Silakan top up terlebih dahulu." dan meminta pengguna menekan Enter untuk kembali ke menu user.

<img width="782" height="209" alt="image" src="https://github.com/user-attachments/assets/469dc3a1-a565-4b62-95b3-bd60f8a33159" />

Setelah pengguna memilih opsi '3' dari menu yang tersedia (setelah loading), program akan menampilkan halaman TOP UP SALDO dan meminta pengguna untuk "Masukkan jumlah top up: Rp" untuk mengisi ulang saldo akun mereka.

