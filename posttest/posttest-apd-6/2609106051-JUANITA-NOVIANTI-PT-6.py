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
    "Donut Chuu": {"owner": "Sohee", "produk": "Donat dan Roti", "petak": 1}
}

while True:
    if os.name == "nt":         
        os.system("cls")         
    else:         
        os.system("clear") 
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
        break

    elif pilihan_utama == "2":
        if os.name == "nt":         
            os.system("cls")         
        else:         
            os.system("clear")
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
        if os.name == "nt":         
            os.system("cls")         
        else:         
            os.system("clear")
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
                    if os.name == "nt":         
                        os.system("cls")         
                    else:         
                        os.system("clear")
                    print("==========MENU ADMIN==========")
                    print("1. Tambah Data UMKM")
                    print("2. Lihat Data UMKM")
                    print("3. Ubah Data UMKM")      
                    print("4. Hapus Data UMKM")
                    print("5. Logout")
                    print("-" * 30)

                    menu = input("Pilih Menu: ")

                    if menu == "1":
                        if os.name == "nt":         
                            os.system("cls")         
                        else:         
                            os.system("clear")
                        print("==========TAMBAH DATA UMKM==========")

                        nama = input("Nama UMKM: ").strip()
                        nama_owner = input("Nama Owner: ").strip()
                        produk = input("Produk Yang Dijual: ").strip()

                        if nama == "" or nama_owner == "" or produk == "":
                            print("Harap Isi Semua Data Dengan Benar.")
                        elif nama in data_umkm:
                            print("Nama UMKM sudah terdaftar!")
                        else:
                            jumlah_petak = input("Jumlah Petak Lahan Dipakai: ").strip()

                            if jumlah_petak.isdigit() and int(jumlah_petak) > 0:
                                data_umkm[nama] = {
                                    "owner": nama_owner,
                                    "produk": produk,
                                    "petak": int(jumlah_petak)
                                }
                                print("\nYay! Data UMKM Berhasil Ditambahkan!")
                            else:
                                print("Jumlah Petak Hanya Berupa Angka dan Lebih dari 0.")

                        input("\nTekan Enter Untuk Kembali. . . ")

                    elif menu == "2":
                        if os.name == "nt":         
                            os.system("cls")         
                        else:         
                            os.system("clear")
                        print("==========DAFTAR UMKM PAKUWON MALL==========")

                        if len(data_umkm) == 0:
                            print("Data UMKM Belum Ada.")
                        else:
                            no = 1
                            for nama, detail in data_umkm.items():
                                print(f"\n-----UMKM ke-{no}-----")
                                print("Nama UMKM    :", nama)
                                print("Nama Owner   :", detail["owner"])
                                print("Produk       :", detail["produk"])
                                print("Jumlah Petak :", detail["petak"])
                                no += 1

                        input("\nTekan Enter Untuk Kembali. . . ")

                    elif menu == "3":
                        if os.name == "nt":         
                            os.system("cls")         
                        else:         
                            os.system("clear")
                        print("==========UBAH DATA UMKM==========")

                        if len(data_umkm) == 0:
                            print("Data UMKM Belum Ada.")
                        else:
                            daftar_nama = list(data_umkm.keys())
                            no = 1
                            for nama in daftar_nama:
                                print(f"{no}. {nama} (Owner: {data_umkm[nama]['owner']})")
                                no += 1

                            ubah_pilihan = input("\nPilih Nomor UMKM Yang Ingin Diubah: ").strip()
                            if ubah_pilihan.isdigit():
                                idx = int(ubah_pilihan) - 1
                                if 0 <= idx < len(daftar_nama):
                                    nama_lama = daftar_nama[idx]
                                    detail = data_umkm[nama_lama]
                                    
                                    print(f"\nMengubah Data untuk: {nama_lama}")
                                    print("(Tekan Enter Langsung Jika Tidak Ingin Mengubah Data Tertentu)")

                                    nama_baru = input(f"Nama UMKM Baru [{nama_lama}]: ").strip()
                                    owner_baru = input(f"Nama Owner Baru [{detail['owner']}]: ").strip()
                                    produk_baru = input(f"Produk Baru [{detail['produk']}]: ").strip()
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
                                        if petak_baru.isdigit() and int(petak_baru) > 0:
                                            data_umkm[key_target]["petak"] = int(petak_baru)
                                        else:
                                            print("\nJumlah petak tidak valid, petak tidak diubah.")

                                    print("\n Yay! Data UMKM Berhasil Diperbarui!")
                                else:
                                    print("\nNomor UMKM Tidak Valid.")
                            else:
                                print("\nHarap Masukkan Angka Yang Valid.")

                        input("\nTekan Enter Untuk Kembali. . . ")

                    elif menu == "4":
                        if os.name == "nt":         
                            os.system("cls")         
                        else:         
                            os.system("clear")
                        print("==========HAPUS DATA UMKM==========")

                        if len(data_umkm) == 0:
                            print("Data UMKM Belum Ada.")
                        else:
                            daftar_nama = list(data_umkm.keys())
                            no = 1
                            for nama in daftar_nama:
                                print(f"{no}. {nama} (Owner: {data_umkm[nama]['owner']})")
                                no += 1

                            hapus_pilihan = input("\nPilih Nomor UMKM Yang Ingin Dihapus: ").strip()
                            if hapus_pilihan.isdigit():
                                idx = int(hapus_pilihan) - 1
                                if 0 <= idx < len(daftar_nama):
                                    nama_terpilih = daftar_nama[idx]
                                    konfirmasi = input(f"Apakah kamu yakin ingin menghapus '{nama_terpilih}'? (y/n): ").strip().lower()
                                    if konfirmasi == "y":
                                        del data_umkm[nama_terpilih]
                                        print(f"\n Yay! UMKM '{nama_terpilih}' Berhasil Dihapus!")
                                    else:
                                        print("\nPenghapusan dibatalkan.")
                                else:
                                    print("\nNomor UMKM Tidak Valid.")
                            else:
                                print("\nHarap Masukkan Angka Yang Valid.")

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
                    if os.name == "nt":         
                        os.system("cls")         
                    else:         
                        os.system("clear")
                    print("==========MENU USER==========")
                    print("1. Lihat Data UMKM")
                    print("2. Logout")
                    print("-" * 27)

                    menu_user = input("Pilih Menu: ")

                    if menu_user == "1":
                        if os.name == "nt":         
                            os.system("cls")         
                        else:         
                            os.system("clear")
                        print("==========DAFTAR UMKM PAKUWON MALL==========")

                        if len(data_umkm) == 0:
                            print("Data UMKM Belum Ada.")
                        else:
                            no = 1
                            for nama, detail in data_umkm.items():
                                print(f"\n-----UMKM ke-{no}-----")
                                print("Nama UMKM    :", nama)
                                print("Nama Owner   :", detail["owner"])
                                print("Produk       :", detail["produk"])
                                print("Jumlah Petak :", detail["petak"])
                                no += 1

                        input("\nTekan Enter Untuk Kembali. . . ")

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