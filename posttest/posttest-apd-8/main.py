import pwinput  
from prettytable import PrettyTable
from data import akun
from pembersihlayar import bersihkan_layar
from fitur_umkm import tampilkan_semua_umkm, tambah_umkm, ubah_umkm, hapus_umkm

def menu_registrasi():
    bersihkan_layar()
    print("========== REGISTRASI AKUN ==========")
    username = input("Username Baru: ").strip()
    password = pwinput.pwinput(prompt="Password Baru: ", mask="*").strip()

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

def menu_login():
    bersihkan_layar()
    print("========== LOGIN ==========")
    username = input("Username Anda: ").strip()
    password = pwinput.pwinput(prompt="Password Anda: ", mask="*").strip()

    if username in akun and akun[username]["password"] == password:
        role = akun[username]["role"]
        print("-" * 25)
        print("\nYay! Login Berhasil!")
        print("Selamat Datang,", username)
        input("Tekan Enter Untuk Melanjutkan. . . ")

        if role.lower() == "admin":
            jalankan_menu_admin()
        elif role.lower() == "user":
            jalankan_menu_user()
    else:
        print("-" * 25)
        print("Username atau Password Salah!")
        input("\nTekan Enter Untuk Kembali. . . ")

def jalankan_menu_admin():
    while True:
        bersihkan_layar()
        
        table = PrettyTable()
        table.field_names = ["NO", "MENU ADMIN"]
        table.align["MENU ADMIN"] = "left"
        table.add_row(["1", "Tambah Data UMKM"])
        table.add_row(["2", "Lihat Data UMKM"])
        table.add_row(["3", "Ubah Data UMKM"])
        table.add_row(["4", "Hapus Data UMKM"])
        table.add_row(["5", "Logout"])

        print("========== DASHBOARD ADMIN ==========")
        print(table)

        menu = input("Pilih Menu (1-5): ").strip()

        if menu == "1":
            tambah_umkm()
        elif menu == "2":
            tampilkan_semua_umkm()
        elif menu == "3":
            ubah_umkm()
        elif menu == "4":
            hapus_umkm()
        elif menu == "5":
            print("\nBerhasil Logout dari Akun Admin.")
            input("Tekan Enter Untuk Kembali. . . ")
            break
        else:
            print("Pilihan Menu Tidak Valid.")
            input("\nTekan Enter Untuk Kembali. . . ")

def jalankan_menu_user():
    while True:
        bersihkan_layar()

        table = PrettyTable()
        table.field_names = ["NO", "MENU USER"]
        table.align["MENU USER"] = "left"
        table.add_row(["1", "Lihat Data UMKM"])
        table.add_row(["2", "Logout"])

        print("========== DASHBOARD USER ==========")
        print(table)

        menu_user = input("Pilih Menu (1-2): ").strip()

        if menu_user == "1":
            tampilkan_semua_umkm()
        elif menu_user == "2":
            print("\nBerhasil Logout dari Akun User.")
            input("Tekan Enter Untuk Kembali. . . ")
            break
        else:
            print("Pilihan Menu Tidak Valid.")
            input("\nTekan Enter Untuk Kembali. . . ")

def main():
    program_berjalan = True
    while program_berjalan:
        bersihkan_layar()

        table = PrettyTable()
        table.field_names = ["NO", "MENU UTAMA"]
        table.align["MENU UTAMA"] = "left"
        table.add_row(["1", "Login"])
        table.add_row(["2", "Registrasi"])
        table.add_row(["3", "Keluar"])

        print("SISTEM PENDATAAN UMKM PAKUWON MALL")
        print(table)

        pilihan_utama = input("Pilih Menu (1-3): ").strip()

        if pilihan_utama == "3":
            print("\nTerima Kasih Telah Menggunakan Program Ini! See You When I See You >_____<")
            program_berjalan = False
        elif pilihan_utama == "2":
            menu_registrasi()
        elif pilihan_utama == "1":
            menu_login()
        else:
            print("Pilihan Menu Tidak Valid.")
            input("\nTekan Enter Untuk Kembali. . . ")

if __name__ == "__main__":
    main()