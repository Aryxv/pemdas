akun_list = [
    ("Arya", "111"),
    ("Keisya", "222"),
    ("Maya", "333")
]

kesempatan = 3
login_sukses = False

while kesempatan > 0:
    print("\n=== LOGIN SISTEM ===")
    username = input("Username : ")
    password = input("Password : ")

    if (username, password) in akun_list:
        print("\nLogin berhasil! Selamat datang,", username)
        login_sukses = True
        break
    else:
        kesempatan -= 1
        print(f"Username atau password salah. Sisa percobaan: {kesempatan}")

if not login_sukses:
    print("\nAkun diblokir karena 3 kali gagal login.")
    exit()

produksi = {
    "anak-anak": 0.3,
    "remaja": 0.5,
    "dewasa": 0.8,
    "lansia": 0.6
}

komposisi = {
    "organik": 0.50,
    "anorganik": 0.30,
    "b3": 0.05,
    "lainnya": 0.15
}

pengurang = {
    "tidak ada": 0.00,
    "rendah": 0.10,
    "sedang": 0.20,
    "tinggi": 0.35
}

# input jumlah rumah tangga
while True:
    try:
        n = int(input("\nMasukkan jumlah rumah tangga yang akan diproses: "))
        if n > 0:
            break
        else:
            print("Jumlah harus lebih dari 0!")
    except ValueError:
        print("Masukkan angka yang valid")

total_gabungan = 0
i = 1

# loop utama: setiap iterasi memproses satu rumah tangga
while i <= n:
    print(f"\n=== Rumah Tangga ke-{i} ===")
    nama = input("Nama Kepala Rumah Tangga: ")

    while True:
        try:
            anggota = int(input("Jumlah anggota rumah tangga: "))
            if anggota > 0:
                break
            else:
                print("Jumlah harus lebih dari 0!")
        except ValueError:
            print("Masukkan angka yang valid!")

    while True:
        usia = input("Usia dominan (anak-anak/remaja/dewasa/lansia): ")
        if usia in produksi:
            break
        else:
            print("Masukkan salah satu kategori yang valid!")

    while True:
        jenis = input("Jenis sampah dominan (organik/anorganik/b3/lainnya/campuran): ")
        if jenis in ["organik", "anorganik", "b3", "lainnya", "campuran"]:
            break
        else:
            print("Masukkan jenis yang valid!")

    while True:
        kebiasaan = input("Kebiasaan daur ulang (tidak ada/rendah/sedang/tinggi): ")
        if kebiasaan in pengurang:
            break
        else:
            print("Masukkan kategori kebiasaan yang valid!")

    total_awal = anggota * produksi[usia]
    total_sesudah = total_awal * (1 - pengurang[kebiasaan])

    organik = total_sesudah * komposisi["organik"]
    anorganik = total_sesudah * komposisi["anorganik"]
    b3 = total_sesudah * komposisi["b3"]
    lainnya = total_sesudah * komposisi["lainnya"]

    total_gabungan += total_sesudah

    print(f"\nHasil Rumah Tangga: {nama}")
    print(f"Total sebelum pengurangan: {total_awal:.2f} kg")
    print(f"Total sesudah pengurangan: {total_sesudah:.2f} kg")
    print("Rincian komposisi:")
    print(f"  - Organik   : {organik:.2f} kg")
    print(f"  - Anorganik : {anorganik:.2f} kg")
    print(f"  - B3        : {b3:.2f} kg")
    print(f"  - Lainnya   : {lainnya:.2f} kg")

    if jenis == "organik":
        print("Saran: Prioritaskan pengomposan sampah organik.")
    elif jenis == "anorganik":
        print("Saran: Pisahkan plastik & logam untuk didaur ulang.")
    elif jenis == "b3":
        print("Saran: Buang ke tempat khusus limbah berbahaya.")
    elif jenis == "lainnya":
        print("Saran: Upayakan pemilahan lebih lanjut.")
    else:
        print("Saran: Campuran - lakukan pemilahan untuk efisiensi pengelolaan.")

    i += 1  # penting: naikkan counter agar berpindah ke rumah tangga berikutnya

print(f"\nTotal gabungan seluruh rumah tangga: {total_gabungan:.2f} kg/hari")