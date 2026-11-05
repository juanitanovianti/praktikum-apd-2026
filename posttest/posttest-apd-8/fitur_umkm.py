from prettytable import PrettyTable
from data import data_umkm
from pembersihlayar import bersihkan_layar

def tampilkan_semua_umkm():
    bersihkan_layar()
    print("========== DAFTAR UMKM PAKUWON MALL ==========")

    if len(data_umkm) == 0:
        print("Data UMKM Belum Ada.")
    else:
        table = PrettyTable()
        table.field_names = ["No", "Nama UMKM", "Nama Owner", "Produk", "Jumlah Petak"]
        table.align["Nama UMKM"] = "left"
        table.align["Nama Owner"] = "left"
        table.align["Produk"] = "left"

        no = 1
        for nama, detail in data_umkm.items():
            produk = detail.get("produk", detail.get("donat", "-"))
            table.add_row([no, nama, detail["owner"], produk, detail["petak"]])
            no += 1

        print(table)
            
    input("\nTekan Enter Untuk Kembali. . . ")

def tambah_umkm():
    bersihkan_layar()
    print("========== TAMBAH DATA UMKM ==========")

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

def ubah_umkm():
    bersihkan_layar()
    print("========== UBAH DATA UMKM ==========")
    if len(data_umkm) == 0:
        print("Data UMKM Belum Ada.")
        input("\nTekan Enter Untuk Kembali. . . ")
        return

    list_nama_admin = list(data_umkm.keys())
    
    table = PrettyTable()
    table.field_names = ["No", "Nama UMKM", "Owner"]
    table.align["Nama UMKM"] = "left"
    table.align["Owner"] = "left"
    
    for idx, nama in enumerate(list_nama_admin, start=1):
        table.add_row([idx, nama, data_umkm[nama]['owner']])
    print(table)

    ubah_pilihan = input("\nPilih Nomor UMKM Yang Ingin Diubah: ").strip()
    
    try:
        idx = int(ubah_pilihan) - 1
        if 0 <= idx < len(list_nama_admin):
            nama_lama = list_nama_admin[idx]
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

    input("\nTekan Enter Untuk Kembali. . . ")

def hapus_umkm():
    bersihkan_layar()
    print("========== HAPUS DATA UMKM ==========")
    if len(data_umkm) == 0:
        print("Data UMKM Belum Ada.")
        input("\nTekan Enter Untuk Kembali. . . ")
        return

    list_nama_admin = list(data_umkm.keys())
    
    table = PrettyTable()
    table.field_names = ["No", "Nama UMKM", "Owner"]
    table.align["Nama UMKM"] = "left"
    table.align["Owner"] = "left"
    
    for idx, nama in enumerate(list_nama_admin, start=1):
        table.add_row([idx, nama, data_umkm[nama]['owner']])
    print(table)

    hapus_pilihan = input("\nPilih Nomor UMKM Yang Ingin Dihapus: ").strip()
    
    try:
        idx = int(hapus_pilihan) - 1
        if 0 <= idx < len(list_nama_admin):
            nama_terpilih = list_nama_admin[idx]
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

    input("\nTekan Enter Untuk Kembali. . . ")