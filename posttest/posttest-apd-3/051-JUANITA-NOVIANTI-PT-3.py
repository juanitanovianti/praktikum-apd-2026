print(f"Selamat Datang di ANGKASA, silahkan masukkan NAMA dan NIM anda untuk login.")

nama = input("Masukkan nama anda: ")
nim = input("Masukkan NIM anda: ")

if nama == "juan" and nim == "51":
    print(f"Selamat Datang, anda berhasil login ke ANGKASA")
    print("-----------------PILIHAN PAKET-----------------")
    print("1. Paket Orbit - Start Your Journey")
    print("2. Paket Nebula - Find Your Vibe")
    print("3. Paket Galaxy - Music Without Limits")
    print("4. Paket Supernova - The Ultimate Experience")
    print("-----------------------------------------------")

    pilihan_paket = int(input("Masukkan Pilihan Paket Anda: "))

    biaya_langganan = 1500000
    
    if pilihan_paket == 1:
        admin = 0.01
        print("-----Keuntungan Paket Orbit-----")
        print("Fitur = Akses lagu lagu dasar populer untuk menemani setiap perjalanan anda")
        print("Biaya Administrasi = 0.01")
    elif pilihan_paket == 2:
        admin = 0.03
        print("-----Keuntungan Paket Nebula-----")
        print("fitur = Temukan lagu premium dan susun playlist sesuai mood anda")
        print("Biaya Administrasi = 0.03")
    elif pilihan_paket == 3:
        admin = 0.05
        print("-----Keuntungan Paket Galaxy-----")
        print("fitur = Nikmati musik premium, playlist pribadi dan mode offline")
        print("Biaya Administrasi = 0.05")
    elif pilihan_paket == 4:
        admin = 0.07
        print("-----Keuntungan Paket Supernova-----")
        print("fitur = Rasakan pengalaman terbaik dengan mengakses semua fitur, kustom playlist, mode offline dan konten ekslusif artis")
        print("Biaya Administrasi = 0.07")
    else:
        exit()

    total_bayar = biaya_langganan + (biaya_langganan * admin)

    print("------PEMBAYARAN------")
    print("Total biaya langganan anda:", total_bayar)
    print("----------------------")

    print("Terima kasih telah terbang bersama ANGKASA, let the music take you beyond the stars!")

elif nama != "juan" and nim != "51":
    print("Login tidak berhasil, nama dan NIM anda salah.")
elif nama != "juan":
    print("Login tidak berhasil, nama yang anda masukkan salah.")
elif nim != "51":
    print("Login tidak berhasil, NIM yang anda masukkan salah")
