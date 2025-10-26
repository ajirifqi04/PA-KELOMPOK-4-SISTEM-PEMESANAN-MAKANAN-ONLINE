import csv
import os
from prettytable import PrettyTable
import pwinput
from datetime import datetime
import time

akun_file = 'akun2.csv'
menu_file = 'menu.csv'
pesanan_file ='pesanan.csv'

# === CLEAR SCREEN ===

def clear():
    os.system('cls')

# === Loading ===

def loading(teks="Loading", durasi=1.5):
    print(teks, end="", flush=True)
    for _ in range(5):
        time.sleep(durasi / 5)
        print(".", end="", flush=True)
    print()

# === Lihat Menu ===

def lihat_menu():
    print("==================================")
    print("|                                |")
    print("|           TABEL MENU           |")
    print("|                                |")
    print("==================================")
    
    try:
        tabel = PrettyTable(["Nama", "Harga"])
        PrettyTable.header
        with open(menu_file, 'r') as f:
            menu = csv.reader(f)
            for baris in menu:
                tabel.add_row([baris[0], baris[1]])
        print(tabel)
    
    except KeyboardInterrupt:
            print("\nProgram diberhentikan karena kamu menekan CTRL+C :)")
            print("\nKeluar dari program")
    except EOFError:
            print("\nProgram diberhentikan karena kamu menekan CTRL+Z :)")
            print("\nKeluar dari program")
            loading()

            
# === Tambah Menu ===

def tambah_menu():
    clear()
    print("=====================================================================")
    print("|                                                                   |")
    print("|                           TAMBAH MENU                             |")
    print("|                                                                   |")
    print("=====================================================================")
    lihat_menu()
    
    try:
        while True:
            nama = input("Masukkan nama menu yang ingin ditambahkan: ").strip()
            if not nama.replace(" ", "").isalpha():
                print("Nama menu hanya boleh huruf(tanpa angka atau simbol)!\n")
                continue

            while True:
                try:
                    harga = int(input("Masukkan harga: ").strip())
                    if harga < 1000:
                        print("Harga harus di atas 1000! Coba lagi.\n")
                        continue  
                    break  
                except ValueError:
                    print("Input tidak valid! Harga harus berupa angka.\nSilakan coba lagi.\n")

            with open(menu_file, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([nama, harga])
            loading("Loading")
            print("\nMenu berhasil ditambahkan!\n")
            
            print("===================================================")
            print("|                DAFTAR MENU TERBARU              |")
            print("===================================================")
            lihat_menu()  
            break  
    
    except KeyboardInterrupt:
        print("\nProgram diberhentikan karena kamu menekan CTRL+C :)")
        print("Keluar dari program")
    except EOFError:
        print("\nProgram diberhentikan karena kamu menekan CTRL+Z :)")
        print("Keluar dari program")
        exit


# === Hapus Menu ===

def hapus_menu():
    clear()
    print("=====================================================================")
    print("|                           HAPUS MENU                              |")
    print("=====================================================================")
    lihat_menu()
    
    try:
        while True:
            nama = input("\nMasukkan nama menu yang ingin dihapus : ").strip()
            if not nama.replace(" ", "").isalpha():
                print("Nama menu hanya boleh huruf (tanpa angka atau simbol)!\n")
                continue

            data_baru = []
            ditemukan = False

            with open(menu_file, 'r', newline='') as f:
                reader = csv.reader(f)
                for baris in reader:
                    if len(baris) > 0 and baris[0].strip().lower() == nama.lower():
                        ditemukan = True 
                    else:
                        data_baru.append(baris)

            if not ditemukan:
                print(f"Menu '{nama}' tidak ditemukan! Silakan coba lagi.\n")
                continue

            with open(menu_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data_baru)

            loading("Loading")
            print(f"Menu '{nama}' berhasil dihapus!\n")

            print("===============================================")
            print("|              DAFTAR MENU TERBARU            |")
            print("===============================================")
            lihat_menu()
            break
    
    except KeyboardInterrupt:
            print("\nProgram diberhentikan karena kamu menekan CTRL+C :)")
            print("\nKeluar dari program")
    except EOFError:
            print("\nProgram diberhentikan karena kamu menekan CTRL+Z :)")
            print("\nKeluar dari program")
            loading()



# === Update Menu ===

def update_menu():
    clear()
    print("=====================================================================")
    print("|                                                                   |")
    print("|                           UPDATE MENU                             |")
    print("|                                                                   |")
    print("=====================================================================")  
    lihat_menu()
    try:
        while True:
            nama = input("Masukkan nama menu yang ingin diupdate: ").strip()
            if not nama.replace(" ", "").isalpha():
                print("Nama menu hanya boleh huruf (tanpa angka atau simbol)!\n")
                continue
            
            menu = False
            with open(menu_file, 'r') as f:
                data = list(csv.reader(f))
            
            for baris in data:
                if baris[0].strip() == nama:
                    menu = True
                    break
            
            if not menu:
                print(f"Menu '{nama}' tidak ditemukan! Coba lagi.\n")
                continue

            while True:
                try:
                    harga = int(input("Masukkan harga baru: ").strip())
                    if harga < 1000:
                        print("Harga harus di atas 1000! Coba lagi.\n")
                        continue
                    break  
                except ValueError:
                    print("Input harus berupa angka! Coba lagi.\n")
            

            for baris in data:
                if baris[0].strip() == nama:
                    baris[1] = str(harga) 
            
            with open(menu_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)
            loading("Loading")
            print(f"Menu '{nama}' berhasil diupdate dengan harga Rp {harga}!")
            break  
        
    except KeyboardInterrupt:
            print("\nProgram diberhentikan karena kamu menekan CTRL+C :)")
            print("\nKeluar dari program")
    except EOFError:
            print("\nProgram diberhentikan karena kamu menekan CTRL+Z :)")
            print("\nKeluar dari program")
            loading()



# === Buat Akun ===

def buat_akun():
    clear()
    print("=====================================================================")
    print("|                                                                   |")
    print("|                            BUAT AKUN                              |")
    print("|                                                                   |")
    print("=====================================================================")
    try:
        while True:
            username = input("Masukkan username anda: ").strip()
            if username.lower() == "admin":
                print("Anda tidak bisa memakai username admin!")
                continue
            if not username.isalpha():
                print("Username hanya boleh berisi huruf (tanpa angka, spasi, atau simbol)!\n")
                continue
            break

        password = pwinput.pwinput("Masukkan password anda: ")
        while True:
            nakap = input("Masukkan nama lengkap anda: ").strip()
            if nakap.replace(" ", "").isalpha():
                break
            else:
                print("Nama lengkap hanya boleh berisi huruf dan spasi!\n")

        with open(akun_file, 'a', newline='') as f:
            data = csv.writer(f)
            data.writerow([username, password, nakap, 'user', '0'])
        loading("Loading")
        print("\nSelamat! Akun kamu berhasil dibuat.\n")

    except KeyboardInterrupt:
            print("\nProgram diberhentikan karena kamu menekan CTRL+C :)")
            print("\nKeluar dari program")
    except EOFError:
            print("\nProgram diberhentikan karena kamu menekan CTRL+Z :)")
            print("\nKeluar dari program")
            loading()


# === Login ===

def login():
    clear()
    print("=====================================================================")
    print("|                                                                   |")
    print("|                               LOGIN                               |")
    print("|                                                                   |")
    print("=====================================================================")
    
    try: 
        while True:
            username = input("Masukkan username anda: ").strip()
            password = pwinput.pwinput("Masukkan password anda: ")

            if username == "admin" and password == "123":
                print("\nLogin sebagai ADMIN berhasil!")
                loading("Loading")
                menu_admin()
                return  

            elif not username.isalpha():
                print("Username hanya boleh berisi huruf (tanpa angka, spasi, atau simbol)!\n")
                loading("Loading")
                continue 

            with open(akun_file, 'r') as f:
                reader = csv.reader(f)
                for data in reader:
                    if username == data[0].strip() and password == data[1].strip():
                        print(f"\nLogin Berhasil! Selamat datang, {data[2]}!")
                        loading("Loading")
                        menu_user(username)
                        return
            print("\nUsername atau Password anda salah!")  

    except KeyboardInterrupt:
            print("\nProgram diberhentikan karena kamu menekan CTRL+C :)")
            print("\nKeluar dari program")
    except EOFError:
            print("\nProgram diberhentikan karena kamu menekan CTRL+Z :)")
            print("\nKeluar dari program")
            loading()

                
# === Order ===

def order(username):

    daftar_pesanan = []
    
    while True:
        clear()
        print("=====================================================================")
        print("|                                                                   |")
        print("|                               ORDER                               |")
        print("|                                                                   |")
        print("=====================================================================")
        
        lihat_menu()
        
        nama = input("\nMasukkan nama menu yang ingin dipesan: ").strip()
        
        with open(menu_file, 'r') as f:
            reader = csv.reader(f)
            menu_ketemu = None
            for menu in reader:
                if menu[0].strip() == nama:
                    menu_ketemu = menu
                    break
        
        if menu_ketemu == None:
            print("\nMenu tidak ditemukan!")
            input("Tekan Enter untuk coba lagi...")
            continue
        
        harga = int(menu_ketemu[1])
        
        while True:
            try:
                jumlah = int(input("Masukkan jumlah: ").strip())
                if jumlah <= 0:
                    print("Jumlah harus lebih dari 0!")
                elif jumlah > 75:
                    print("Maksimal pesanan hanya 75!")
                    continue
                break
            except ValueError:
                print("Input harus berupa angka!")
        
        daftar_pesanan.append({'nama': nama, 'jumlah': jumlah, 'harga': harga})
        
        pesan_lagi = input("\nApakah anda ingin memesan menu lain? (Y/N): ").strip().upper()
        
        if pesan_lagi == "N":
            break
    loading("Loading")
    clear()
    print("=====================================================================")
    print("|                        KONFIRMASI PESANAN                         |")
    print("=====================================================================")
    
    try:
        total_bayar = 0
        print("\nRingkasan Pesanan:")
        for item in daftar_pesanan:
            subtotal = item['harga'] * item['jumlah']
            total_bayar += subtotal
            print(f"- {item['nama']} x{item['jumlah']} = Rp {subtotal:,}")
        
        print(f"\nTotal Pembayaran: Rp {total_bayar:,}")
        
        with open(akun_file, 'r') as f:
            data_akun = list(csv.reader(f))
        loading("Loading")
        saldo_user = 0
        for akun in data_akun:
            if akun[0].strip() == username:
                saldo_user = int(akun[4])
                break
        
        print(f"Saldo Anda: Rp {saldo_user:,}")
        
        if total_bayar > saldo_user:
            print("\nSaldo tidak cukup! Silakan top up terlebih dahulu.")
            input("Tekan Enter untuk kembali...")
            return
        
        konfirmasi = input("\nKonfirmasi Pembayaran? (Y/N): ").strip().upper()
        
        if konfirmasi == "Y":
            saldo_baru = saldo_user - total_bayar
            
            for akun in data_akun:
                if akun[0].strip() == username:
                    akun[4] = str(saldo_baru)
                    break
            
            with open(akun_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data_akun)
            loading("Loading")
            waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            with open(pesanan_file, 'a', newline='') as f:
                writer = csv.writer(f)
                for item in daftar_pesanan:
                    subtotal = item['harga'] * item['jumlah']
                    writer.writerow([username, item['nama'], item['jumlah'], item['harga'], subtotal, waktu])
            print("\nPembayaran berhasil!")
            print(f"Saldo terpotong: Rp {total_bayar:,}")
            print(f"Sisa saldo: Rp {saldo_baru:,}")
            
        elif konfirmasi == "N":
            print("\nPembayaran dibatalkan.")
        
        input("\nTekan Enter untuk kembali...")

    except KeyboardInterrupt:
            print("\nProgram diberhentikan karena kamu menekan CTRL+C :)")
            print("\nKeluar dari program")
    except EOFError:
            print("\nProgram diberhentikan karena kamu menekan CTRL+Z :)")
            print("\nKeluar dari program")
            loading()

# === Top Up Saldo ===

def topup_saldo(username):
    clear()
    print("=====================================================================")
    print("|                                                                   |")
    print("|                          TOP UP SALDO                             |")
    print("|                                                                   |")
    print("=====================================================================")
        
    try:
        while True:
            try:
                jumlah = int(input("Masukkan jumlah top up: Rp ").strip())
                if jumlah <= 49999:
                    print("Jumlah harus lebih dari Rp50.000! Coba lagi.\n")
                elif jumlah > 5000000:
                    print("Limit Top Up maksimal Rp5.000.000")
                    continue
                break
                
            except ValueError:
                    print("Input harus berupa angka! Coba lagi.\n")
            
        with open(akun_file, 'r') as f:
            data_akun = list(csv.reader(f))

        saldo_lama = 0
            
        for akun in data_akun:
            if akun[0].strip() == username:
                saldo_lama = int(akun[4])
                saldo_baru = saldo_lama + jumlah
                akun[4] = str(saldo_baru)
                break
            
        with open(akun_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data_akun)
        loading("Loading")
        print(f"\n✓ Top up berhasil untuk {username}!")
        print(f"Saldo lama : Rp {saldo_lama:,}")
        print(f"Top up     : Rp {jumlah:,}")
        print(f"Saldo baru : Rp {saldo_baru:,}")
        
    except KeyboardInterrupt:
            print("\nProgram diberhentikan karena kamu menekan CTRL+C :)")
            print("\nKeluar dari program")
    except EOFError:
            print("\nProgram diberhentikan karena kamu menekan CTRL+Z :)")
            print("\nKeluar dari program")
            loading()

# === Cek Saldo ===
    
def cek_saldo(username):
    clear()
    print("=====================================================================")
    print("|                                                                   |")
    print("|                            CEK SALDO                              |")
    print("|                                                                   |")
    print("=====================================================================")

    with open(akun_file, 'r') as f:
        reader = csv.reader(f)
        for data in reader:
            if data[0].strip() == username:
                saldo = int(data[4])
                print(f"\nUsername : {data[0]}")
                print(f"Nama     : {data[2]}")
                print(f"Saldo    : Rp {saldo:,}")
                break


# === Riwayat Order ===

def riwayat_order(username):
    clear()
    print("========================================================================")
    print("|                                                                      |")
    print("|                           RIWAYAT ORDER                              |")
    print("|                                                                      |")
    print("========================================================================")

    from prettytable import PrettyTable
    tabel = PrettyTable(["No", "Nama Menu", "Jumlah", "Harga", "Total", "Tanggal"])
    ada_riwayat = False

    with open(pesanan_file, 'r', newline='') as f:
        reader = csv.reader(f)
        no = 1
        for riwayat in reader:
            if not riwayat:
                continue

            if riwayat[0].strip() == username:
                nama_menu = riwayat[1]
                jumlah = riwayat[2]
                harga = int(riwayat[3])
                total = int(riwayat[4])
                tanggal = riwayat[5]

                tabel.add_row([no, nama_menu, jumlah, f"Rp {harga:,}", f"Rp {total:,}", tanggal])
                no += 1
                ada_riwayat = True
                continue

    if ada_riwayat:
        print(f"\nRiwayat pesanan untuk pengguna: {username}\n")
        print(tabel)
    else:
        print(f"\nBelum ada riwayat pesanan untuk pengguna '{username}'.\n")
        

# === Menu User ===

def menu_user(username):
    clear()
    while True:
        try:
            clear()
            print("====================================================================")
            print("|                                                                  |")
            print("|                            MENU USER                             |")
            print("|                                                                  |")
            print("====================================================================")
            print("|1. Lihat Menu                                                     |")
            print("|2. Order                                                          |")
            print("|3. Top Up Saldo                                                   |")
            print("|4. Cek Saldo                                                      |")
            print("|5. Riwayat Order                                                  |")
            print("|6. Keluar                                                         |")
            print("====================================================================")
            pilihan = input("Silahkan pilih menu 1-6: ").strip()
            if pilihan == "1":
                clear()
                loading("Loading")
                lihat_menu()
                input("\nTekan Enter untuk kembali...")
            elif pilihan == "2":
                loading("Loading")
                order(username)
            elif pilihan == "3":
                loading("Loading")
                topup_saldo(username)
                input("\nTekan Enter untuk kembali...")
            elif pilihan == "4":
                loading("Loading")
                cek_saldo(username)
                input("\nTekan Enter untuk kembali...")
            elif pilihan == "5":
                loading("Loading")
                riwayat_order(username)
                input("\nTekan Enter untuk kembali...")
            elif pilihan == "6":
                print("\nLogout berhasil! Kembali ke menu utama...\n")
                break
            else:
                print("Pilihan tidak tersedia!")
                input("\nTekan Enter untuk kembali...")
                loading("Loading")

        except KeyboardInterrupt:
            print("\nProgram diberhentikan karena kamu menekan CTRL+C :)")
            print("\nKeluar dari program")
            loading("Loading")
            break

        except EOFError:
            print("\nProgram diberhentikan karena kamu menekan CTRL+Z :)")
            print("\nKeluar dari program")
            loading("Loading")
            break


# === Menu Admin ===

def menu_admin():
    clear()
    while True:
        try:
            clear()
            print("=====================================================================")
            print("|                                                                   |")
            print("|                            MENU ADMIN                             |")
            print("|                                                                   |")
            print("=====================================================================")
            print("|1. Lihat Menu                                                      |")
            print("|2. Tambah Menu                                                     |")
            print("|3. Hapus Menu                                                      |")
            print("|4. Update Menu                                                     |")
            print("|5. Keluar                                                          |")
            print("=====================================================================")
            pilihan = input("Pilih 1-5 : ").strip()
            if pilihan == "1":
                clear()
                loading("Loading")
                lihat_menu()
                input("\nTekan Enter untuk kembali...")
            elif pilihan == "2":
                loading("Loading")
                tambah_menu()
                input("\nTekan Enter untuk kembali...")
            elif pilihan == "3":
                loading("Loading")
                hapus_menu()
                input("\nTekan Enter untuk kembali...")
            elif pilihan == "4":
                loading("Loading")
                update_menu()
                input("\nTekan Enter untuk kembali...")
            elif pilihan == "5":
                print("\nLogout berhasil! Kembali ke menu utama...\n")
                break
            else:
                print("Pilihan tidak tersedia!")
                input("\nTekan Enter untuk kembali...")
                loading("Loading")

        except KeyboardInterrupt:
            print("\nProgram diberhentikan karena kamu menekan CTRL+C :)")
            print("\nKeluar dari program")
            loading("Loading")
            break

        except EOFError:
            print("\nProgram diberhentikan karena kamu menekan CTRL+Z :)")
            print("\nKeluar dari program")
            loading("Loading")
            break


# === MENU UTAMA ===
def menu_utama():
    clear()
    while True:
        try:
            clear()
            print("======================================================================")
            print("|                                                                    |")
            print("|                            MENU UTAMA                              |")
            print("|                                                                    |")
            print("======================================================================")
            print("|1. Buat Akun                                                        |")
            print("|2. Login                                                            |")
            print("|3. Keluar                                                           |")
            print("======================================================================")

            pilihan = input("Pilih menu 1-3 :").strip()
            if pilihan == "1":
                buat_akun()
                input("\nTekan Enter untuk kembali...")
            elif pilihan == "2":
                login()
            elif pilihan == "3":
                print("\nKeluar Program! Terima kasih.\n")
                break
            else:
                print("Pilihan tidak tersedia!")  
                input("\nTekan Enter untuk kembali...")

        except KeyboardInterrupt:
            print("\nProgram diberhentikan karena kamu menekan CTRL+C :)")
            print("\nKeluar dari program")
            loading("Loading")
            break

        except EOFError:
            print("\nProgram diberhentikan karena kamu menekan CTRL+Z :)")
            print("\nKeluar dari program")
            loading("Loading")
            break


menu_utama()