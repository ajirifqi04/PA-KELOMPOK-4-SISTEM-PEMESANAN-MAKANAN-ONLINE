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

Flowchart ini menjelaskan alur awal saat program pertama kali dijalankan.

🔹 Penjelasan Alur:

**Mulai**: Program dijalankan dan menampilkan menu utama dengan tiga pilihan yaitu:
  1. Buat Akun
  2. Login
  3. Keluar
  
**1. Buat Akun (User)**
Jika pengguna memilih “Buat Akun”, sistem meminta:
  1. Username
  2. Password
  3. Nama Lengkap
 Setelah data diisi, sistem akan menyimpan file **DB Akun CSV**, Lalu menampilkan notifikasi bahwa akun berhasil di buat

**2. Login**
Pengguna bisa login sebagai:
  1. **Admin** => Memasukkan username dan password khusus admin. Jika benar, akan diarahkan ke **Menu Admin**.
  2. **User** => Memasukkan username dan password yang sudah terdaftar, lalu akan diarahkan ke **Menu User**.

**3. Keluar**: Jika memilih "Keluar", maka program akan menampilkan notifikasi bahwa sistem selesai dijalankan, lalu berhenti.

**🧩 Flowchart Menu Admin**

Flowchart ini menggambarkan proses yang dapat dilakukan oleh admin untuk mengelola data makanan pada sistem.

🔹 Penjelasan Alur:

**Tampilan Menu Admin**: Admin disajikan 5 opsi utama yaitu:
 1. Lihat Menu : Sistem akan membaca file **DB Menu CSV** dan akan menampilkan tabel daftar menu yang tersedia.
 2. Tambah Menu : Admin diminta memasukkan nama dan harga makanan baru. Data disimpan ke file CSV, lalu sistem menampilkan notifikasi bahwa menu berhasil ditambahkan dan menampilkan tabel menu terbaru.
 3. Hapus Menu : Admin memasukkan nama menu yang ingin dihapus. Sistem membaca file CSV, menghapus data yang sesuai, lalu memperbarui tabel menu terbaru.
 4. Ubah Menu : Admin dapat mengubah harga dari menu tertentu. Setelah diperbarui, data disimpan kembali ke file CSV dan sistem menampilkan notifikasi bahwa menu berhasil diperbarui.
 5. Keluar : Admin dapat keluar dari sistem, dan program menampilkan notifikasi bahwa sesi admin telah selesai.
