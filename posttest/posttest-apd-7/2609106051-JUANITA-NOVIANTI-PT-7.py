import os

akun = {
    "juan": {"password": "6051", "role": "admin"},
    "user": {"password": "2626", "role": "user"}
}

data_umkm = {
    "Kopi Memori": {"owner": "Zhao Yufan", "produk": "Kopi dan Minuman Kekinian", "petak": 2},
    "Sweet Bakery": {"owner": "Juhoon", "produk": "Roti, Kue dan Pastry", "petak": 1},
    "Dochicken": {"owner": "Martin Edwards", "produk": "Ayam Goreng Potong", "petak": 2},
    "Dimsum Delight": {"owner": "Seonghyeon", "produk": "Dimsum dan Siomay", "petak": 1},
    "Burger Station": {"owner": "Ahn Keonho", "produk": "Burger", "petak": 2},
    "Kebablasan": {"owner": "Ohyul Kwon", "produk": "Kebab", "petak": 1},
    "Batik Kita": {"owner": "Kim Ryul", "produk": "Baju Batik dan Kain", "petak": 2},
    "Parfume Pit Stop": {"owner": "Jung Woojin", "produk": "Parfum dan Wewangian Tubuh", "petak": 1},
    "Mochindut": {"owner": "Louis Elliot", "produk": "Mochi", "petak": 2},
    "Es Teh 5 Daun": {"owner": "Anton", "produk": "Es Teh dan Minuman Segar", "petak": 1},
    "Juicely": {"owner": "Wonbin", "produk": "Jus Buah dan Smoothies", "petak": 2},
    "Donut Chuu": {"owner": "Sohee", "donat": "Donat dan Roti", "petak": 1} 
}

program_berjalan = True

def bersihkan_layar():
    if os.name == "nt":         
        os.system("cls")         
    else:         
        os.system("clear")

def tampilkan_semua_umkm():
    bersihkan_layar()
    print("==========DAFTAR UMKM PAKUWON MALL==========")

    if len(data_umkm) == 0:
        print("Data UMKM Belum Ada.")
    else:
        no = 1
        for nama, detail in data_umkm.items():
            print(f"\n-----UMKM ke-{no}-----")
            print("Nama UMKM    :", nama)
            print("Nama Owner   :", detail["owner"])
            print("Produk       :", detail.get("produk", detail.get("donat", "-")))
            print("Jumlah Petak :", detail["petak"])
            no += 1
            
    input("\nTekan Enter Untuk Kembali. . . ")

def hapus_umkm_oleh_admin(daftar_nama):

    hapus_pilihan = input("\nPilih Nomor UMKM Yang Ingin Dihapus: ").strip()
    
    try:
        idx = int(hapus_pilihan) - 1
        if 0 <= idx < len(daftar_nama):
            nama_terpilih = daftar_nama[idx]
            konfirmasi = input(f"Apakah Kamu Yakin Ingin Menghapus '{nama_terpilih}'? (y/n): ").strip().lower()
            if konfirmasi == "y":
                del data_umkm[nama_terpilih]
                print(f"\n Yay! UMKM '{nama_terpilih}' Berhasil Dihapus!")
            else:
                print("\nPenghapusan Dibatalkan.")
        else:
            print("\nError: Nomor UMKM Yang Anda Masukkan Di Luar Jangkauan Daftar.")
    except ValueError:
        print("\nError: Input Harus Berupa Angka Bulat Yang Valid!")

def ubah_umkm_oleh_admin(daftar_nama):

    ubah_pilihan = input("\nPilih Nomor UMKM Yang Ingin Diubah: ").strip()
    
    try:
        idx = int(ubah_pilihan) - 1
        if 0 <= idx < len(daftar_nama):
            nama_lama = daftar_nama[idx]
            detail = data_umkm[nama_lama]
            print(f"\nMengubah Data untuk: {nama_lama}")
            print("(Tekan Enter Langsung Jika Tidak Ingin Mengubah Data Tertentu)")

            nama_baru = input(f"Nama UMKM Baru [{nama_lama}]: ").strip()
            owner_baru = input(f"Nama Owner Baru [{detail['owner']}]: ").strip()
            produk_lama = detail.get("produk", detail.get("donat", "-"))
            produk_baru = input(f"Produk Baru [{produk_lama}]: ").strip()
            petak_baru = input(f"Jumlah Petak Baru [{detail['petak']}]: ").strip()

            if nama_baru != "" and nama_baru != nama_lama:
                data_umkm[nama_baru] = data_umkm.pop(nama_lama)
                key_target = nama_baru
            else:
                key_target = nama_lama

            if owner_baru != "":
                data_umkm[key_target]["owner"] = owner_baru
            if produk_baru != "":
                data_umkm[key_target]["produk"] = produk_baru
            
            if petak_baru != "":
                try:
                    petak_baru_int = int(petak_baru)
                    if petak_baru_int > 0:
                        data_umkm[key_target]["petak"] = petak_baru_int
                    else:
                        print("\nJumlah Petak Harus Lebih Dari 0. Petak Tidak Diubah.")
                except ValueError:
                    print("\nError: Jumlah Petak Harus Berupa Angka. Petak Tidak Diubah.")

            print("\n Yay! Data UMKM Berhasil Diperbarui!")
        else:
            print("\nError: Nomor UMKM Tidak Terdaftar Dalam List.")
    except ValueError:
        print("\nError: Mohon Masukkan Input Dalam Bentuk Angka.")

while program_berjalan:
    bersihkan_layar()
    print("=" * 34)
    print("SISTEM PENDATAAN UMKM PAKUWON MALL")
    print("=" * 34)
    print("1. Login")
    print("2. Registrasi")
    print("3. Keluar")
    print("-" * 34)

    pilihan_utama = input("Pilih Menu: ")

    if pilihan_utama == "3":
        print("\nTerima Kasih Telah Menggunakan Program Ini! See You When I See You >_____<")
        program_berjalan = False

    elif pilihan_utama == "2":
        bersihkan_layar()
        print("==========REGISTRASI AKUN==========")
        username = input("Username Baru: ").strip()
        password = input("Password Baru: ").strip()

        if username == "" or password == "":
            print("Username dan Password Tidak Boleh Kosong!")
        elif username.lower() in [key.lower() for key in akun.keys()]:
            print("Maaf, Username Sudah Digunakan.")
        else:
            akun[username] = {"password": password, "role": "user"}
            print("-" * 34)
            print("Yay! Registrasi Berhasil!")
            print("Silahkan Login Menggunakan Akun Baru.")

        input("\nTekan Enter Untuk Kembali. . . ")

    elif pilihan_utama == "1":
        bersihkan_layar()
        print("==========LOGIN==========")
        username = input("Username Anda: ").strip()
        password = input("Password Anda: ").strip()

        if username in akun and akun[username]["password"] == password:
            role = akun[username]["role"]
            print("-" * 25)
            print("\nYay! Login Berhasil!")
            print("Selamat Datang,", username)
            input("Tekan Enter Untuk Melanjutkan. . . ")

            if role.lower() == "admin":
                while True:
                    bersihkan_layar()
                    print("==========MENU ADMIN==========")
                    print("1. Tambah Data UMKM")
                    print("2. Lihat Data UMKM")
                    print("3. Ubah Data UMKM")      
                    print("4. Hapus Data UMKM")
                    print("5. Logout")
                    print("-" * 30)

                    menu = input("Pilih Menu: ")

                    if menu == "1":
                        bersihkan_layar()
                        print("==========TAMBAH DATA UMKM==========")

                        nama = input("Nama UMKM: ").strip()
                        nama_owner = input("Nama Owner: ").strip()
                        produk = input("Produk Yang Dijual: ").strip()

                        if nama == "" or nama_owner == "" or produk == "":
                            print("Harap Isi Semua Data Dengan Benar.")
                        elif nama in data_umkm:
                            print("Nama UMKM Sudah Terdaftar!")
                        else:
                            jumlah_petak = input("Jumlah Petak Lahan Dipakai: ").strip()

                            try:
                                petak_int = int(jumlah_petak)
                                if petak_int > 0:
                                    data_umkm[nama] = {
                                        "owner": nama_owner,
                                        "produk": produk,
                                        "petak": petak_int
                                    }
                                    print("\nYay! Data UMKM Berhasil Ditambahkan!")
                                else:
                                    print("Error: Jumlah Petak Harus Bernilai Lebih Dari 0.")
                            except ValueError:
                                print("Error: Input Jumlah Petak Wajib Berupa Angka Bulat.")

                        input("\nTekan Enter Untuk Kembali. . . ")

                    elif menu == "2":
                        tampilkan_semua_umkm()

                    elif menu == "3":
                        bersihkan_layar()
                        print("==========UBAH DATA UMKM==========")
                        if len(data_umkm) == 0:
                            print("Data UMKM Belum Ada.")
                        else:
                            list_nama_admin = list(data_umkm.keys())
                            no = 1
                        for nama in list_nama_admin:
                            print(f"{no}. {nama} (Owner: {data_umkm[nama]['owner']})")
                            no += 1

                        ubah_umkm_oleh_admin(list_nama_admin)
                        input("\nTekan Enter Untuk Kembali. . . ")
                    
                    elif menu == "4":
                        bersihkan_layar()
                        print("==========HAPUS DATA UMKM==========")
                        if len(data_umkm) == 0:
                            print("Data UMKM Belum Ada.")
                        else:
                            list_nama_admin = list(data_umkm.keys())
                            no = 1
                            for nama in list_nama_admin:
                                print(f"{no}. {nama} (Owner: {data_umkm[nama]['owner']})")
                                no += 1

                            hapus_umkm_oleh_admin(list_nama_admin)
                        input("\nTekan Enter Untuk Kembali. . . ")

                    elif menu == "5":
                        print("\nBerhasil Logout dari Akun Admin.")
                        input("Tekan Enter Untuk Kembali. . . ")
                        break
                    else:
                        print("Pilihan Menu Tidak Valid.")
                        input("\nTekan Enter Untuk Kembali. . . ")

            elif role.lower() == "user":
                while True:
                    bersihkan_layar()
                    print("==========MENU USER==========")
                    print("1. Lihat Data UMKM")
                    print("2. Logout")
                    print("-" * 27)

                    menu_user = input("Pilih Menu: ")

                    if menu_user == "1":
                        tampilkan_semua_umkm()

                    elif menu_user == "2":
                        print("\nBerhasil Logout dari Akun User.")
                        input("Tekan Enter Untuk Kembali. . . ")
                        break
                    else:
                        print("Pilihan Menu Tidak Valid.")
                        input("\nTekan Enter Untuk Kembali. . . ")
        else:
            print("-" * 25)
            print("Username atau Password Salah!")
            input("\nTekan Enter Untuk Kembali. . . ")