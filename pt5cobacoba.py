import os

akun = [
    ["juan", "6051", "admin"],
    ["user", "2626", "user"]
]

data_umkm = [
    ["Kopi Memori", "Zhao Yufan", "Kopi dan Minuman Kekinian", 2],
    ["Sweet Bakery", "Juhoon", "Roti, Kue dan Pastry", 1],
    ["Dochicken", "Martin Edwards", "Ayam Goreng Potong", 2],
    ["Dimsum Delight", "Seonghyeon", "Dimsum dan Siomay", 1],
    ["Burger Station", "Ahn Keonho", "Burger", 2],
    ["Kebablasan", "Ohyul Kwon", "Kebab", 1],
    ["Batik Kita", "Kim Ryul", "Baju Batik dan Kain", 2],
    ["Parfume Pit Stop", "Jung Woojin", "Parfum dan Wewangian Tubuh", 1],
    ["Mochindut", "Louis Elliot", "Mochi", 2],
    ["Es Teh 5 Daun", "Anton", "Es Teh dan Minuman Segar", 1],
    ["Juicely", "Wonbin", "Jus Buah dan Smoothies", 2],
    ["Donut Chuu", "Sohee", "Donat dan Roti", 1]
]

while True:
    if os.name == "nt":         
        os.system("cls")         
    else:         
        os.system("clear") 
    print("=" * 34)
    print("SISTEM PENDATAAN UMKM PAKUWON MALL")
    print("=" * 34)
    print("1. Login")
    print("2. Register")
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
        print("==========REGISTER AKUN==========")
        username = input("Username Baru: ").strip()
        password = input("Password Baru: ").strip()

        username_dipakai = False 
        for u in akun:
            if u[0].lower() == username.lower():
                username_dipakai = True
        if username == "" or password == "":
            print("Username dan Password Tidak Boleh Kosong!")
        elif username_dipakai:
            print("Maaf, Username Sudah Digunakan.")
        else:
            akun.append([username, password, "user"])
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

        login_berhasil = False
        role = ""

        for pengguna in akun:
            if pengguna[0] == username and pengguna[1] == password:
                login_berhasil = True
                role = pengguna[2]
                break
            
        if login_berhasil:
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
                        else:
                            jumlah_petak = input("Jumlah Petak Lahan Dipakai: ").strip()

                            if jumlah_petak.isdigit() and int(jumlah_petak) > 0:
                                data_umkm.append([
                                    nama, nama_owner, produk, int(jumlah_petak)
                                ])
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
                            for i in range(len(data_umkm)):
                                print(f"\n-----UMKM ke-{i+1}-----")
                                print("Nama UMKM    :", data_umkm[i][0])
                                print("Nama Owner   :", data_umkm[i][1])
                                print("Produk       :", data_umkm[i][2])
                                print("Jumlah Petak :", data_umkm[i][3])

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
                            for i in range(len(data_umkm)):
                                print(f"{i+1}. {data_umkm[i][0]} (Owner: {data_umkm[i][1]})")

                            ubah_pilihan = input("\nPilih Nomor UMKM Yang Ingin Diubah: ").strip()
                            if ubah_pilihan.isdigit():
                                idx = int(ubah_pilihan) - 1
                                if 0 <= idx < len(data_umkm):
                                    print(f"\nMengubah Data untuk: {data_umkm[idx][0]}")
                                    print("(Tekan Enter Langsung Jika Tidak Ingin Mengubah Data Tertentu)")

                                    nama_baru = input(f"Nama UMKM Baru [{data_umkm[idx][0]}]: ").strip()
                                    owner_baru = input(f"Nama Owner Baru [{data_umkm[idx][1]}]: ").strip()
                                    produk_baru = input(f"Produk Baru [{data_umkm[idx][2]}]: ").strip()
                                    petak_baru = input(f"Jumlah Petak Baru [{data_umkm[idx][3]}]: ").strip()

                                    if nama_baru != "":
                                        data_umkm[idx][0] = nama_baru
                                    if owner_baru != "":
                                        data_umkm[idx][1] = owner_baru
                                    if produk_baru != "":
                                        data_umkm[idx][2] = produk_baru
                                    if petak_baru != "":
                                        if petak_baru.isdigit() and int(petak_baru) > 0:
                                            data_umkm[idx][3] = int(petak_baru)
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
                            for i in range(len(data_umkm)):
                                print(f"{i+1}. {data_umkm[i][0]} (Owner: {data_umkm[i][1]})")
                            
                            hapus_pilihan = input("\nPilih Nomor UMKM Yang Ingin Dihapus: ").strip()
                            if hapus_pilihan.isdigit():
                                idx = int(hapus_pilihan) - 1
                                if 0 <= idx < len(data_umkm):
                                    umkm_terhapus = data_umkm.pop(idx)
                                    print(f"\nData UMKM '{umkm_terhapus[0]}' Berhasil Dihapus!")
                                else:
                                    print("\nNomor UMKM Tidak Valid.")
                            else:
                                print("\nMasukkan Angka Yang Valid.")

                        input("\nTekan Enter Untuk Kembali. . . ")

                    elif menu == "5": 
                        print("\nBerhasil Logout Dari Akun Admin.")
                        break

                    else:
                        print("\nPilihan Tidak Valid. Silakan Pilih Menu 1-5.")
                        input("Tekan Enter Untuk Melanjutkan. . . ")

            if role.lower() == "user":
                while True:
                    if os.name == "nt":         
                        os.system("cls")         
                    else:         
                        os.system("clear")
                    print("==========MENU USER==========")
                    print("1. Lihat Data UMKM")
                    print("2. Logout")
                    print("-" * 29)

                    menu = input("Pilih Menu: ")

                    if menu == "1":
                        if os.name == "nt":         
                            os.system("cls")         
                        else:         
                            os.system("clear")
                        print("==========DAFTAR UMKM PAKUWON MALL==========")
                    
                        if len(data_umkm) == 0:
                            print("Data UMKM Belum Ada.")
                        else:
                            for i in range(len(data_umkm)):
                                print(f"\n-----UMKM ke-{i+1}-----")
                                print("Nama UMKM    :", data_umkm[i][0])
                                print("Nama Owner   :", data_umkm[i][1])
                                print("Produk       :", data_umkm[i][2])
                                print("Jumlah Petak :", data_umkm[i][3])
                    
                        input("\nTekan Enter Untuk Kembali. . . ")

                    elif menu == "2":
                        print("\nBerhasil Logout Dari Akun User.")
                        input("Tekan Enter Untuk Kembali ke Menu Utama. . . ")
                        break

                    else:
                        print("\nPilihan Tidak Valid. Silakan Pilih Menu 1-2.")
                        input("Tekan Enter Untuk Melanjutkan. . . ")

            else:
                input("Tekan Enter Untuk Kembali ke Menu Utama. . . ")
                
        else:
            print("\nLogin Gagal! Username atau Password salah.")
            input("\nTekan Enter Untuk Kembali. . . ")