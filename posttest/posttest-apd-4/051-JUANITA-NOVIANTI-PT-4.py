print("Silahkan Login Terlebih Dahulu: ")
username_benar = "juan"
password_benar = "051"
login = False

while login == False:
    username = input("Username: ").lower().strip()
    password = input("Password: ").lower().strip()

    if username == username_benar and password == password_benar:
        print("Login berhasil! Selamat datang, juan!")
        print("==========================================================")
        print("= PROGRAM REKAPITULASI TITIK API KEBAKARAN HUTAN & LAHAN =")
        print("=               BPBD & Tim Manggala Agni                 =")
        print("==========================================================")
        login = True
    elif username != username_benar and password == password_benar:
        print("Username salah, coba lagi!")
    elif username == username_benar and password != password_benar:
        print("Password salah, coba lagi!")
    elif username == "" or password == "":
        print("Username dan Password tidak boleh kosong!")
    else:
        print("Username dan Password salah, coba lagi!")

kal_gambut = 0
kal_mineral = 0
sum_gambut = 0
sum_mineral = 0
jumlah_data = 0
nama_pulau = "KALIMANTAN" or "SUMATERA"
lahan = "GAMBUT" or "MINERAL"

lagi = "Y"
while lagi == "Y":
    jumlah_data += 1
    print()
    print(f"INPUT DATA KE-{jumlah_data}")

    pulau = ""
    while pulau == "":
        pulau = input("  Pulau (KALIMANTAN/SUMATERA)  : ").strip().upper()
        if pulau == "":
            print("  [!] Pulau tidak boleh kosong!")
        elif pulau != "KALIMANTAN" and pulau != "SUMATERA":
            print("  [!] Pilih KALIMANTAN atau SUMATERA saja!")
            pulau = ""

    hotspot = -1
    while hotspot < 0:
        teks = input("  Jumlah Titik Api (Hotspot)   : ").strip()
        if teks == "":
            print("  [!] Jumlah titik api tidak boleh kosong!")
        elif teks.isdigit() == False:
            print("  [!] Isi dengan angka bulat (tanpa minus/huruf)!")
        else:
            hotspot = int(teks)

    luas = hotspot * 5

    if pulau == "KALIMANTAN":
        lahan = ""
        while lahan == "":
            lahan = input("  Jenis Lahan (GAMBUT/MINERAL) : ").strip().upper()
            if lahan == "":
                print("  [!] Jenis lahan tidak boleh kosong!")
            elif lahan != "GAMBUT" and lahan != "MINERAL":
                print("  [!] Pilih GAMBUT atau MINERAL saja!")
                lahan = ""

        if lahan == "GAMBUT":
            kal_gambut += luas
            hasil = "Kalimantan-Gambut"
        else:
            kal_mineral += luas
            hasil = "Kalimantan-Mineral"

    else:  
        lahan = ""
        while lahan == "":
            lahan = input("  Jenis Lahan (GAMBUT/MINERAL) : ").strip().upper()
            if lahan == "":
                print("  [!] Jenis lahan tidak boleh kosong!")
            elif lahan != "GAMBUT" and lahan != "MINERAL":
                print("  [!] Pilih GAMBUT atau MINERAL saja!")
                lahan = ""

        if lahan == "GAMBUT":
            sum_gambut += luas
            hasil = "Sumatera-Gambut"
        else:
            sum_mineral += luas
            hasil = "Sumatera-Mineral"

    
    print(f"  Kategori    : {hasil}")
    print(f"  Titik api   : {hotspot} titik")
    print(f"  Lahan rusak : {luas} Hektare")
    

    jawab = ""
    while jawab == "":
        jawab = input("\n  Apakah anda masih mau input data titik api lagi? (Y/T) : ").strip().upper()
        if jawab == "":
            print("  [!] Jawaban tidak boleh kosong!")
        elif jawab != "Y" and jawab != "T":
            print("  [!] Jawab Y atau T saja!")
            jawab = ""

    lagi = jawab

total = (kal_gambut + kal_mineral + sum_gambut + sum_mineral)

print()
print("RINGKASAN LUAS LAHAN TERBAKAR")
print(f"  Jumlah data diinput : {jumlah_data}")
print("==========================================================")
print(f"  Kalimantan-Gambut   : {kal_gambut:>8} Hektare")
print(f"  Kalimantan-Mineral  : {kal_mineral:>8} Hektare")
print(f"  Sumatera-Gambut     : {sum_gambut:>8} Hektare")
print(f"  Sumatera-Mineral    : {sum_mineral:>8} Hektare")
print("==========================================================")
print(f"  TOTAL               : {total:>8} Hektare")
print("==========================================================")
print("  Data siap dipakai untuk alokasi water bombing.")
print("==========================================================")