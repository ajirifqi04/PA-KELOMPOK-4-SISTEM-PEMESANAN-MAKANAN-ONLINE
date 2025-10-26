# PA-KELOMPOK-4-SISTEM-PEMESANAN-MAKANAN-ONLINE

**SISTEM PEMESANAN MAKANAN ONLINE**

# === 👥 Anggota Kelompok 4 - Sistem Informasi B ===
1. Aji Rifqi Suryana (2509116054)
2. Ghaida Suci Nahiza (2509116077)
3. Muhammad Nadhir Sultan Azzaky (2509116080)

# === 🧩 FLOWCHART ===

# MENU AWAL USER

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
 3. Hapus Menu : Admin memasukkan nama menu yang ingin dihapus. Sistem membaca data di file CSV, menghapus data yang sesuai, lalu memperbarui tabel menu terbaru.
 4. Ubah Menu : Admin dapat mengubah harga dari menu tertentu. Setelah diperbarui, data disimpan kembali ke file CSV dan sistem menampilkan notifikasi bahwa menu berhasil diperbarui.
 5. Keluar : Admin dapat keluar dari sistem, dan program menampilkan notifikasi bahwa sesi admin telah selesai.

# **🧩 Flowchart Menu User**

Flowchart ini menggambarkan alur transaksi pengguna, mulai dari melihat menu hingga melakukan pembayaran. Sistem juga menyediakan fitur saldo dan riwayat pemesanan untuk memudahkan pengguna mengelola aktivitas mereka.

🔹 Penjelasan Alur:

**Tampilan Menu User**: User memiliki 6 opsi utama yaitu:
1. Lihat Menu : Sistem membaca file DB Menu CSV dan menampilkan daftar makanan beserta harganya.
2. Order : Pengguna memilih makanan yang ingin dipesan beserta jumlahnya, kemudian sistem secara otomatis menghitung total harga. Jika saldo pengguna mencukupi, maka transaksi akan berhasil diproses, data pesanan akan disimpan ke dalam file pesanan.csv, dan saldo pengguna akan otomatis berkurang sesuai total pembelian. Namun, apabila saldo tidak mencukupi, sistem akan menolak transaksi dan menampilkan peringatan agar pengguna melakukan top up terlebih dahulu. Setelah pembayaran berhasil, sistem menampilkan invoice atau struk pemesanan sebagai bukti transaksi.
4. Top Up Saldo : Pengguna dapat menambahkan saldo minimal Rp50.000. Sistem akan memperbarui file **DB Akun CSV**, lalu menampilkan notifikasi bahwa saldo berhasil ditambahkan.
5. Cek Saldo : Sistem membaca data dari **DB Akun CSV** dan akan menampilkan jumlah saldo saat ini.
6. Riwayat Order : Sistem membaca data dari **DB Pesanan CSV** dan menampilkan histori pembelian (nama menu, jumlah, total harga, waktu transaksi).
7. Keluar : Menampilkan notifikasi bahwa program selesai dijalankan dan kembali ke menu utama.

# === OUTPUT PROGRAM ===

<img width="786" height="260" alt="image" src="https://github.com/user-attachments/assets/be04a21d-8d71-4aeb-834e-935b1a22b497" />

Tampilan ini adalah Menu Utama dari program yang berfungsi sebagai gerbang otentikasi awal, memungkinkan pengguna untuk Buat Akun, Login, atau Keluar dari aplikasi.

<img width="784" height="385" alt="image" src="https://github.com/user-attachments/assets/14b92baf-e341-4c94-a2b0-a405cf1ec1f4" />

Setelah memilih opsi '1' (Buat Akun) dari menu utama, program meminta input username, password, dan nama lengkap pengguna, lalu sistem akan memprosesnya dengan pesan Loading..., lalu menampilkan konfirmasi "Selamat! Akun kamu berhasil dibuat", dan bakal kembali ke menu utama.

# USER
<img width="787" height="293" alt="image" src="https://github.com/user-attachments/assets/595616a4-7b1b-4712-88e6-90105576cf42" />

Setelah memilih opsi '2' (Login), pengguna diarahkan untuk memasukkan username dan password yang telah di buat sebelumnya, yang kemudian diverifikasi dan menampilkan konfirmasi "Login Berhasil! Selamat datang, (Nama Lengkap)!" lalu sistem akan memprosesnya dengan pesan Loading...

<img width="767" height="330" alt="image" src="https://github.com/user-attachments/assets/a0723bf4-419f-4248-be1d-be76fa7b9cf3" />

dan akan memunculkan menu user seperti diatas ini setelah proses Loading...

<img width="398" height="475" alt="image" src="https://github.com/user-attachments/assets/f02c9ea9-7eea-47c0-9487-0a411f919fa5" />

Tampilan ini menunjukkan ketika anda memilih opsi '1' dari menu sebelumnya (kemungkinan Menu Admin atau Menu Setelah Login), lalu program akan memprosesnya dengan pesan Loading... dan menampilkan TABEL MENU yang berisi daftar makanan dan harganya, yaitu Mie Gacoan (10000), Udang Keju (10000), Ayam Geprek Ganja (13000), Ayam Katsu (20000), dan Nasi Goreng (15000), sebelum menunggu pengguna menekan Enter untuk kembali.

<img width="781" height="602" alt="image" src="https://github.com/user-attachments/assets/5b11c5fa-ec32-43d4-9066-c2764b8ec2dc" />

Setelah pengguna memilih opsi '2' dari menu sebelumnya, program menampilkan halaman ORDER yang tetap menyajikan TABEL MENU (termasuk Mie Gacoan, Udang Keju, Ayam Geprek Ganja, Ayam Katsu, dan Nasi Goreng beserta harganya) dan kemudian meminta pengguna untuk memasukkan nama menu yang ingin dipesan.

<img width="641" height="112" alt="image" src="https://github.com/user-attachments/assets/e91afea7-5db4-43ed-b68c-e0601a6f84d2" />

Tampilan ini melanjutkan proses pemesanan dengan menerima input nama menu yang ingin dipesan ("Ayam Geprek Ganja") dan jumlahnya ("1"), dan kemudian mengajukan pertanyaan konfirmasi "Apakah anda ingin memesan menu lain? (Y/N)" untuk "Y" artinya iya dan "N" artinya tidak.

<img width="781" height="571" alt="image" src="https://github.com/user-attachments/assets/a118724f-8c89-4ccd-a118-48a6944daba8" />

Tampilan ketika pengguna menjawab 'Y' pada pertanyaan "Apakah anda ingin memesan menu lain?", lalu program akan otomatis mengulang proses ORDER, menampilkan kembali TABEL MENU, dan meminta pengguna untuk "Masukkan nama menu yang ingin dipesan lagi.

<img width="784" height="495" alt="image" src="https://github.com/user-attachments/assets/3176a02d-7c85-4fde-8d61-419c351c5b5d" />

Setelah pengguna memesan item kedua, Mie Gacoan sejumlah 1, dan menjawab 'n' (Tidak) pada pertanyaan ingin memesanan menu lain?, program menampilkan halaman KONFIRMASI PESANAN dengan Ringkasan Pesanan (Ayam Geprek Ganja x1 dan Mie Gacoan x1) dan Total Pembayaran sebesar Rp 23.000, namun proses pembayaran gagal karena Saldo Anda: Rp 0, sehingga program menampilkan pesan "Saldo tidak cukup! Silakan top up terlebih dahulu." dan meminta pengguna menekan Enter untuk kembali ke menu user.

<img width="782" height="209" alt="image" src="https://github.com/user-attachments/assets/469dc3a1-a565-4b62-95b3-bd60f8a33159" />

Setelah pengguna memilih opsi '3' dari menu yang tersedia (setelah loading), program akan menampilkan halaman TOP UP SALDO dan meminta pengguna untuk "Masukkan jumlah top up: Rp" untuk mengisi ulang saldo akun mereka.

<img width="395" height="237" alt="image" src="https://github.com/user-attachments/assets/448d4ac3-c0d0-468f-94c0-aa04c0317827" />

Setelah pengguna memasukkan jumlah top up yang valid sebesar Rp 100.000, lalu program akan memprosesnya (Loading.....) dan menampilkan konfirmasi keberhasilan top up untuk akun Sultan, dengan rincian Saldo lama: Rp 0, Top up: Rp 100.000, dan Saldo baru: Rp 100.000, sebelum menunggu pengguna menekan Enter untuk kembali.

<img width="777" height="521" alt="image" src="https://github.com/user-attachments/assets/f332c343-3a08-43fd-80b6-580bc4c696d7" />

Setelah top up saldo, program menampilkan kembali halaman KONFIRMASI PESANAN dengan Total Pembayaran: Rp 23.000 dan Saldo Anda: Rp 100.000, dan ketika pengguna menjawab 'y' (Ya) pada "Konfirmasi Pembayaran?", program memprosesnya (Loading.....) dan menampilkan pesan "Pembayaran berhasil!" dengan rincian Saldo terpotong: Rp 23.000 dan Sisa saldo: Rp 77.000.

<img width="782" height="439" alt="image" src="https://github.com/user-attachments/assets/f99850e7-7985-496e-b01d-845ba34c958a" />

Tampilan ini menunjukkan alur di mana pengguna berada di halaman KONFIRMASI PESANAN dengan Total Pembayaran: Rp 23.000 dan Saldo Anda: Rp 100.000, namun ketika pengguna menjawab 'n' (Tidak) pada pertanyaan "Konfirmasi Pembayaran?", program membatalkan transaksi dan menampilkan pesan "Pembayaran dibatalkan.".

<img width="783" height="338" alt="image" src="https://github.com/user-attachments/assets/aea0569b-2bd2-43da-831b-ef6e51911904" />

Setelah memilih opsi '4' dari menu yang tersedia (setelah loading), program menampilkan halaman CEK SALDO yang menunjukkan detail akun pengguna, yaitu Username: Sultan, Nama: Muhammad Nadhir Sultan Azzaky, dan Saldo: Rp 77,000, sebelum menunggu pengguna menekan Enter untuk kembali.

<img width="919" height="473" alt="image" src="https://github.com/user-attachments/assets/19ca9ca4-01b6-43a0-b1ab-08d13e186db7" />

Setelah memilih opsi '5' dari menu yang tersedia (setelah loading), program menampilkan halaman RIWAYAT ORDER yang menunjukkan riwayat pesanan untuk pengguna Sultan, mencantumkan dua transaksi yang berhasil pada tanggal dan waktu yang sama (2025-10-26 18:47:30), yaitu Ayam Geprek Ganja (1) seharga Rp 13.000 dan Mie Gacoan (1) seharga Rp 10.000, sebelum meminta pengguna menekan Enter untuk kembali.

<img width="789" height="364" alt="image" src="https://github.com/user-attachments/assets/aa647e8e-5f10-4cfd-8c92-e093486851be" />

Setelah pengguna memilih opsi '6' dari menu yang tersedia, program menampilkan pesan "Logout berhasil! Kembali ke menu utama..." dan kemudian memuat ulang MENU UTAMA yang menampailkan opsi awal 1. Buat Akun, 2. Login, dan 3. Keluar, serta meminta pengguna untuk "Pilih menu 1-3 :".

# ADMIN

<img width="786" height="297" alt="image" src="https://github.com/user-attachments/assets/f3206032-eeb8-4037-afec-1a61db1b57cc" />

Tampilan ini menunjukkan bahwa pengguna memilih opsi '2' (Login) dari Menu Utama dan berhasil masuk sebagai administrator dengan memasukkan username: admin dan password yang tersembunyi, yang dikonfirmasi dengan pesan "Login sebagai ADMIN berhasil!" sebelum program memulai proses Loading untuk masuk ke menu admin.

<img width="582" height="706" alt="image" src="https://github.com/user-attachments/assets/2367c4e0-61ee-4b12-8340-494ebb53a86d" />

Setelah pengguna memasukkan nama menu ("Dimsum") dan harga ("4000") yang ingin ditambahkan, program memprosesnya (Loading.....) dan menampilkan konfirmasi "Menu berhasil ditambahkan!", kemudian menunjukkan DAFTAR MENU TERBARU yang kini mencakup Dimsum seharga 4000 dan juga Mie Ayam seharga 20000 (yang kemungkinan ditambahkan sebelumnya), sebelum meminta pengguna menekan Enter untuk kembali.

<img width="786" height="597" alt="image" src="https://github.com/user-attachments/assets/e4173104-eff3-4409-b0f9-51354b9c2e52" />


Setelah memilih opsi '3' dari Menu Admin (Pilih 1-5 : 3) dan melalui proses Loading..., program menampilkan halaman HAPUS MENU yang menyajikan TABEL MENU lengkap (termasuk item terbaru Mie Ayam dan Dimsum), kemudian meminta administrator untuk "Masukkan nama menu yang ingin dihapus :".

<img width="555" height="634" alt="image" src="https://github.com/user-attachments/assets/21ed5a19-9699-4af0-a192-85dc6605e036" />

Setelah admin memasukkan nama menu "Dimsum" untuk dihapus, program memprosesnya (Loading.....) dan menampilkan konfirmasi "Menu 'Dimsum' berhasil dihapus!", kemudian menunjukkan DAFTAR MENU TERBARU di mana Dimsum sudah tidak ada lagi, dan meminta pengguna menekan Enter untuk kembali.

<img width="778" height="596" alt="image" src="https://github.com/user-attachments/assets/e488d669-fe77-46ea-8ee1-1d9d401271f8" />

Setelah memilih opsi '4' dari Menu Admin (Pilih 1-5 : 4) dan melalui proses Loading..., program menampilkan halaman UPDATE MENU yang menyajikan TABEL MENU yang ada saat ini, kemudian meminta administrator untuk "Masukkan nama menu yang ingin diupdate :".

<img width="664" height="156" alt="image" src="https://github.com/user-attachments/assets/1afbaae0-a716-4032-a3c1-95de9ae2ec35" />

Setelah administrator memasukkan nama menu "Ayam Katsu" untuk di-update dan memasukkan harga baru: 15000, program memprosesnya (Loading.....) dan menampilkan konfirmasi "Menu 'Ayam Katsu' berhasil diupdate dengan harga Rp 15000!", sebelum menunggu pengguna menekan Enter untuk kembali.

<img width="388" height="448" alt="image" src="https://github.com/user-attachments/assets/287f5bcd-2929-470e-879d-b621b09125f4" />

Tampilan ini menunjukkan TABEL MENU terbaru setelah proses update, di mana harga Ayam Katsu telah berhasil diperbarui menjadi 15000 (sebelumnya 20000), dan program menunggu pengguna menekan Enter untuk kembali.

<img width="499" height="86" alt="image" src="https://github.com/user-attachments/assets/e1df9147-9722-45fc-8b57-48e4333d2984" />

Setelah memilih opsi '5' dari Menu Admin (Pilih 1-5 : 5), program mengonfirmasi "Logout berhasil! Kembali ke menu utama..." dan akan mengalihkan tampilan ke Menu Utama (Login/Buat Akun/Keluar).

<img width="402" height="471" alt="image" src="https://github.com/user-attachments/assets/a1e221c0-edaf-47fd-8ca8-120c064ad76e" />

Setelah memilih opsi '1' dari Menu Admin (ditunjukkan oleh Pilih 1-5 : 1) dan melalui proses Loading..., program menampilkan TABEL MENU yang berisi daftar item dan harganya, yaitu Mie Gacoan (10000), Udang Keju (10000), Ayam Geprek Ganja (13000), Ayam Katsu (20000), dan Nasi Goreng (15000), sebelum meminta pengguna menekan Enter untuk kembali.

<img width="788" height="573" alt="image" src="https://github.com/user-attachments/assets/dd46f055-bcc7-4624-8871-ce8023676c64" />

Setelah memilih opsi '2' dari Menu Admin (Pilih 1-5 : 2) dan melalui proses Loading..., program menampilkan halaman TAMBAH MENU yang juga menyajikan TABEL MENU yang sudah ada, kemudian meminta pengguna untuk "Masukkan nama menu yang ingin ditambahkan:".

# MENU AwAL

<img width="794" height="342" alt="image" src="https://github.com/user-attachments/assets/85af7f73-ace6-4fe8-8a90-336c671e8bc9" />

Tampilan ini menunjukkan respons program pada MENU UTAMA ketika pengguna memasukkan input yang tidak valid (0) pada prompt "Pilih menu 1-3 :", di mana program menampilkan pesan kesalahan "Pilihan tidak tersedia!" dan meminta pengguna "Tekan Enter untuk kembali..." ke menu.

<img width="382" height="89" alt="image" src="https://github.com/user-attachments/assets/5e6a91df-fa85-477b-bda7-fec78400c83e" />

Setelah memilih opsi '3' (Keluar) dari Menu Utama, program mengakhiri operasinya dengan menampilkan pesan "Keluar Program! Terima kasih.".

# MENU LOGIN
<img width="767" height="268" alt="image" src="https://github.com/user-attachments/assets/4da2dfcc-2968-4bf3-920b-529191934021" />

Tampilan ini menunjukkan kegagalan login di halaman LOGIN setelah pengguna memasukkan username: sultan dan password (tersembunyi), di mana program menampilkan pesan kesalahan "Username atau Password anda salah!" dan meminta pengguna untuk "Masukkan username anda:" lagi.

















































<img width="783" height="620" alt="image" src="https://github.com/user-attachments/assets/c9054904-7cb6-4171-84d2-ee2c1a3f791d" />

Tampilan ini menunjukkan alur di mana pengguna berada di halaman ORDER dengan TABEL MENU yang tersedia, namun ketika pengguna memasukkan nama menu yang tidak terdaftar (Udang Rambutan), program menampilkan pesan kesalahan "Menu tidak ditemukan!" dan meminta pengguna untuk menekan Enter untuk mencoba lagi.

<img width="780" height="499" alt="image" src="https://github.com/user-attachments/assets/2207b3d5-3c8a-442c-966e-20774289995a" />

Tampilan ini menunjukkan halaman KONFIRMASI PESANAN dengan Total Pembayaran: Rp 23.000 dan Saldo Anda: Rp 77.000, bisa di lihat program menolak dua kali input konfirmasi pembayaran yang tidak valid (baik karakter 'a' maupun '\') karena hanya menerima Y atau N, dan kembali meminta pengguna untuk memasukkan Konfirmasi Pembayaran? (Y/N) yang benar.

<img width="783" height="375" alt="image" src="https://github.com/user-attachments/assets/ca7f0cb8-ea43-4083-a905-c66970a665ff" />

Setelah memilih menu '3' (TOP UP SALDO), program menolak dua kali input top up yang tidak valid: yang pertama karena nilainya (Rp -1) "harus lebih dari Rp50.000!" dan yang kedua karena inputnya (@) "harus berupa angka!", kemudian program kembali meminta pengguna untuk memasukkan jumlah top up yang valid.
