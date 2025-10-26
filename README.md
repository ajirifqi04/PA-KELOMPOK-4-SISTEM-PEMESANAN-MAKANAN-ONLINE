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

**=== OUTPUT PROGRAM ===**

<img width="786" height="260" alt="Screenshot 2025-10-26 174517" src="https://github.com/user-attachments/assets/19f03314-daf1-401f-ade4-f04b5dcd85e9" />

Tampilan ini adalah Menu Utama dari program yang berfungsi sebagai gerbang otentikasi awal, memungkinkan pengguna untuk Buat Akun, Login, atau Keluar dari aplikasi.

<img width="784" height="385" alt="Screenshot 2025-10-26 174954" src="https://github.com/user-attachments/assets/7fde2a19-dab5-4469-b340-4645232686a0" />

Setelah memilih opsi '1' (Buat Akun) dari menu utama, program meminta input username, password, dan nama lengkap pengguna, lalu sistem akan memprosesnya dengan pesan Loading..., lalu menampilkan konfirmasi "Selamat! Akun kamu berhasil dibuat", dan bakal kembali ke menu utama.

# USER

<img width="787" height="293" alt="Screenshot 2025-10-26 175521" src="https://github.com/user-attachments/assets/16991b66-c0e6-4b5a-bd68-2b3d1fb92b7a" />

Setelah memilih opsi '2' (Login), pengguna diarahkan untuk memasukkan username dan password yang telah di buat sebelumnya, yang kemudian diverifikasi dan menampilkan konfirmasi "Login Berhasil! Selamat datang, (Nama Lengkap)!" lalu sistem akan memprosesnya dengan pesan Loading...

<img width="767" height="330" alt="Screenshot 2025-10-26 180258" src="https://github.com/user-attachments/assets/531a4f24-6bef-480b-b737-83834eed7837" />

dan akan memunculkan menu user seperti diatas ini setelah proses Loading...

<img width="398" height="475" alt="Screenshot 2025-10-26 180407" src="https://github.com/user-attachments/assets/d4fb4480-8812-4ac7-8068-bd91ce715386" />

Tampilan ini menunjukkan ketika anda memilih opsi '1' dari menu sebelumnya (kemungkinan Menu Admin atau Menu Setelah Login), lalu program akan memprosesnya dengan pesan Loading... dan menampilkan TABEL MENU yang berisi daftar makanan dan harganya, yaitu Mie Gacoan (10000), Udang Keju (10000), Ayam Geprek Ganja (13000), Ayam Katsu (20000), dan Nasi Goreng (15000), sebelum menunggu pengguna menekan Enter untuk kembali.

<img width="781" height="602" alt="Screenshot 2025-10-26 180629" src="https://github.com/user-attachments/assets/65415b3f-d767-4eb2-b819-c0e5fcaedd03" />

Setelah pengguna memilih opsi '2' dari menu sebelumnya, program menampilkan halaman ORDER yang tetap menyajikan TABEL MENU (termasuk Mie Gacoan, Udang Keju, Ayam Geprek Ganja, Ayam Katsu, dan Nasi Goreng beserta harganya) dan kemudian meminta pengguna untuk memasukkan nama menu yang ingin dipesan.

<img width="643" height="108" alt="Screenshot 2025-10-26 180811" src="https://github.com/user-attachments/assets/e22939fc-8b99-4369-9c1f-d4aafde81c24" />

Tampilan ini melanjutkan proses pemesanan dengan menerima input nama menu yang ingin dipesan ("Ayam Geprek Ganja") dan jumlahnya ("1"), dan kemudian mengajukan pertanyaan konfirmasi "Apakah anda ingin memesan menu lain? (Y/N)" untuk "Y" artinya iya dan "N" artinya tidak.

<img width="781" height="571" alt="Screenshot 2025-10-26 180956" src="https://github.com/user-attachments/assets/76eabe02-01a4-48b4-b5dc-e07ae935213f" />

Tampilan ketika pengguna menjawab 'Y' pada pertanyaan "Apakah anda ingin memesan menu lain?", lalu program akan otomatis mengulang proses ORDER, menampilkan kembali TABEL MENU, dan meminta pengguna untuk "Masukkan nama menu yang ingin dipesan lagi.

<img width="784" height="495" alt="Screenshot 2025-10-26 181213" src="https://github.com/user-attachments/assets/74fd1314-057d-4739-abf1-a3db0b5dfb1d" />

Setelah pengguna memesan item kedua, Mie Gacoan sejumlah 1, dan menjawab 'n' (Tidak) pada pertanyaan ingin memesanan menu lain?, program menampilkan halaman KONFIRMASI PESANAN dengan Ringkasan Pesanan (Ayam Geprek Ganja x1 dan Mie Gacoan x1) dan Total Pembayaran sebesar Rp 23.000, namun proses pembayaran gagal karena Saldo Anda: Rp 0, sehingga program menampilkan pesan "Saldo tidak cukup! Silakan top up terlebih dahulu." dan meminta pengguna menekan Enter untuk kembali ke menu user.

<img width="782" height="209" alt="Screenshot 2025-10-26 181504" src="https://github.com/user-attachments/assets/67c9147f-1ad1-4c75-889c-59d86608952f" />

Setelah pengguna memilih opsi '3' dari menu yang tersedia (setelah loading), program akan menampilkan halaman TOP UP SALDO dan meminta pengguna untuk "Masukkan jumlah top up: Rp" untuk mengisi ulang saldo akun mereka. Minimal top up saldo Rp 50.000 dan Maksimal Rp. 5.000.000

<img width="395" height="237" alt="Screenshot 2025-10-26 184336" src="https://github.com/user-attachments/assets/f74beece-ec53-460a-bede-37a29fa2e5fd" />

Setelah pengguna memasukkan jumlah top up yang valid sebesar Rp 100.000, lalu program akan memprosesnya (Loading.....) dan menampilkan konfirmasi keberhasilan top up untuk akun Sultan, dengan rincian Saldo lama: Rp 0, Top up: Rp 100.000, dan Saldo baru: Rp 100.000, sebelum menunggu pengguna menekan Enter untuk kembali.

<img width="777" height="521" alt="Screenshot 2025-10-26 184755" src="https://github.com/user-attachments/assets/4641e768-689c-4cb2-82bc-52dfc26205b6" />

Pada halaman KONFIRMASI PESANAN dengan total tagihan Rp 23.000 dan Saldo Anda Rp 100.000, pengguna mengonfirmasi pembayaran ('y'). Lalu program akan memproses transaksi (Loading...) dan menampilkan "Pembayaran berhasil!" dengan rincian Saldo terpotong Rp 23.000 dan Sisa saldo Rp 77.000.

<img width="782" height="439" alt="Screenshot 2025-10-26 184938" src="https://github.com/user-attachments/assets/c150840a-aee3-4747-88fd-2ead449a2593" />

Tampilan ini menunjukkan alur di mana pengguna berada di halaman KONFIRMASI PESANAN dengan Total Pembayaran: Rp 23.000 dan Saldo Anda: Rp 100.000, namun ketika pengguna menjawab 'n' (Tidak) pada pertanyaan "Konfirmasi Pembayaran?", program membatalkan transaksi dan menampilkan pesan "Pembayaran dibatalkan.".

<img width="783" height="338" alt="Screenshot 2025-10-26 185117" src="https://github.com/user-attachments/assets/7281d340-e87b-4939-bedc-663bce37f198" />

Setelah memilih opsi '4' dari menu yang tersedia (setelah loading), program menampilkan halaman CEK SALDO yang menunjukkan detail akun pengguna, yaitu Username: Sultan, Nama: Muhammad Nadhir Sultan Azzaky, dan Saldo: Rp 77,000, sebelum menunggu pengguna menekan Enter untuk kembali.

<img width="919" height="473" alt="Screenshot 2025-10-26 190427" src="https://github.com/user-attachments/assets/64506f09-4c1c-4840-a709-bf560981a15c" />

Setelah memilih opsi '5' dari menu yang tersedia (setelah loading), program menampilkan halaman RIWAYAT ORDER yang menunjukkan riwayat pesanan untuk pengguna Sultan, mencantumkan dua transaksi yang berhasil pada tanggal dan waktu yang sama (2025-10-26 18:47:30), yaitu Ayam Geprek Ganja (1) seharga Rp 13.000 dan Mie Gacoan (1) seharga Rp 10.000, sebelum meminta pengguna menekan Enter untuk kembali.

<img width="789" height="364" alt="Screenshot 2025-10-26 190608" src="https://github.com/user-attachments/assets/7dfbf78a-27ea-4ad2-9dc2-4a721c9cafca" />

Setelah pengguna memilih opsi '6' dari menu yang tersedia, program menampilkan pesan "Logout berhasil! Kembali ke menu utama..." dan kemudian memuat ulang MENU UTAMA yang menampilkan opsi awal 1. Buat Akun, 2. Login, dan 3. Keluar, serta meminta pengguna untuk "Pilih menu 1-3 :".

# ADMIN

<img width="786" height="297" alt="Screenshot 2025-10-26 190829" src="https://github.com/user-attachments/assets/415a380d-4411-4c4d-a03c-8732e507d04c" />

Tampilan ini menunjukkan bahwa pengguna memilih opsi '2' (Login) dari Menu Utama dan berhasil masuk sebagai administrator dengan memasukkan username: admin dan password yang tersembunyi, yang dikonfirmasi dengan pesan "Login sebagai ADMIN berhasil!" sebelum program memulai proses Loading untuk masuk ke menu admin.

<img width="402" height="471" alt="Screenshot 2025-10-26 191114" src="https://github.com/user-attachments/assets/c0d4cb8e-b0af-415e-abc9-016921c350d3" />

Setelah memilih opsi '1' dari Menu Admin (ditunjukkan oleh Pilih 1-5 : 1) dan melalui proses Loading..., program menampilkan TABEL MENU yang berisi daftar item dan harganya, yaitu Mie Gacoan (10000), Udang Keju (10000), Ayam Geprek Ganja (13000), Ayam Katsu (20000), dan Nasi Goreng (15000), sebelum meminta pengguna menekan Enter untuk kembali.

<img width="788" height="573" alt="Screenshot 2025-10-26 191540" src="https://github.com/user-attachments/assets/cc553ead-978e-49f3-9eca-b28397ecc304" />

Setelah memilih opsi '2' dari Menu Admin (Pilih 1-5 : 2) dan melalui proses Loading..., program menampilkan halaman TAMBAH MENU yang juga menyajikan TABEL MENU yang sudah ada, kemudian meminta pengguna untuk "Masukkan nama menu yang ingin ditambahkan:".

<img width="582" height="706" alt="Screenshot 2025-10-26 201406" src="https://github.com/user-attachments/assets/cac0789c-51a7-4d7e-90aa-669e7abe1380" />

Setelah pengguna memasukkan nama menu ("Dimsum") dan harga ("4000") yang ingin ditambahkan, program memprosesnya (Loading.....) dan menampilkan konfirmasi "Menu berhasil ditambahkan!", kemudian menunjukkan DAFTAR MENU TERBARU yang kini mencakup Dimsum seharga 4000 dan juga Mie Ayam seharga 20000 (yang kemungkinan ditambahkan sebelumnya), sebelum meminta pengguna menekan Enter untuk kembali.

<img width="786" height="597" alt="Screenshot 2025-10-26 201842" src="https://github.com/user-attachments/assets/ce0c2990-ddd0-47e5-b0b6-3c385a2f279e" />

Setelah memilih opsi '3' dari Menu Admin (Pilih 1-5 : 3) dan melalui proses Loading..., program menampilkan halaman HAPUS MENU yang menyajikan TABEL MENU lengkap (termasuk item terbaru Mie Ayam dan Dimsum), kemudian meminta administrator untuk "Masukkan nama menu yang ingin dihapus :".

<img width="555" height="634" alt="Screenshot 2025-10-26 202024" src="https://github.com/user-attachments/assets/c62fa17d-e12e-47fc-8c40-20a77f7edac7" />

Setelah admin memasukkan nama menu "Dimsum" untuk dihapus, program memprosesnya (Loading.....) dan menampilkan konfirmasi "Menu 'Dimsum' berhasil dihapus!", kemudian menunjukkan DAFTAR MENU TERBARU di mana Dimsum sudah tidak ada lagi, dan meminta pengguna menekan Enter untuk kembali.

<img width="778" height="596" alt="Screenshot 2025-10-26 202319" src="https://github.com/user-attachments/assets/9b9b75b0-a648-4c2f-8c4d-143bbd13d21d" />

Setelah memilih opsi '4' dari Menu Admin (Pilih 1-5 : 4) dan melalui proses Loading..., program menampilkan halaman UPDATE MENU yang menyajikan TABEL MENU yang ada saat ini, kemudian meminta administrator untuk "Masukkan nama menu yang ingin diupdate :".

<img width="664" height="156" alt="Screenshot 2025-10-26 202514" src="https://github.com/user-attachments/assets/2e7e02f4-1152-4c40-9377-71fe5e04d790" />

Setelah administrator memasukkan nama menu "Ayam Katsu" untuk di-update dan memasukkan harga baru: 15000, program memprosesnya (Loading.....) dan menampilkan konfirmasi "Menu 'Ayam Katsu' berhasil diupdate dengan harga Rp 15000!", sebelum menunggu pengguna menekan Enter untuk kembali.

<img width="388" height="448" alt="Screenshot 2025-10-26 202558" src="https://github.com/user-attachments/assets/4ba2442b-9e4a-482b-89b0-7c42c6208c66" />

Tampilan ini menunjukkan TABEL MENU terbaru setelah proses update, di mana harga Ayam Katsu telah berhasil diperbarui menjadi 15000 (sebelumnya 20000), dan program menunggu pengguna menekan Enter untuk kembali.

<img width="499" height="86" alt="Screenshot 2025-10-26 203410" src="https://github.com/user-attachments/assets/9ce95ede-ff99-44b2-a415-4b6514e67ad4" />

Setelah memilih opsi '5' dari Menu Admin (Pilih 1-5 : 5), program mengonfirmasi "Logout berhasil! Kembali ke menu utama..." dan akan mengalihkan tampilan ke Menu Utama (Login/Buat Akun/Keluar).
