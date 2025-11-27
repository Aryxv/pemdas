# ==============================
# Program Sederhana: Rekomendasi Minum Air Harian
# ==============================

print("=== PROGRAM REKOMENDASI AIR HARIAN ===\n")
print("Keterangan:")
print("Aktivitas Fisik: S=Sedentari, R=Ringan, SD=Sedang, B=Berat, A=Atlet")
print("Kondisi Kesehatan: TA=Tidak Ada, H=Hamil/Menyusui, D=Demam/Infeksi, PG=Penyakit Ginjal, PJ=Penyakit Jantung\n")

# Input data dari pengguna
nama = input("Masukkan nama anda: ")
umur = int(input("Masukkan umur anda: "))
jk = input("Masukkan jenis kelamin (Pria/Wanita): ")
aktivitas = input("Masukkan tingkat aktivitas fisik (S/R/SD/B/A): ")
kesehatan = input("Masukkan kondisi kesehatan (TA/H/D/PG/PJ): ")

# Nilai awal rekomendasi air
air = 0

# ==============================
# Bagian 1: Tentukan kebutuhan dasar berdasarkan umur dan jenis kelamin
# ==============================
if umur < 3:
    print("\nKarena usia di bawah 3 tahun, masih dianjurkan konsumsi ASI, jadi belum ada rekomendasi air minum.")
else:
    if umur >= 3 and umur < 18:
        if jk == "Pria":
            air = 1.6
        elif jk == "Wanita":
            air = 1.4
    elif umur >= 18 and umur <= 64:
        if jk == "Pria":
            air = 2.5
        elif jk == "Wanita":
            air = 2.0
    elif umur >= 65:
        if jk == "Pria":
            air = 2.0
        elif jk == "Wanita":
            air = 1.8

    # ==============================
    # Bagian 2: Tambahkan berdasarkan aktivitas fisik
    # ==============================
    if aktivitas == "S":
        tambahan_aktiv = 0
    elif aktivitas == "R":
        tambahan_aktiv = 0.3
    elif aktivitas == "SD":
        tambahan_aktiv = 0.5
    elif aktivitas == "B":
        tambahan_aktiv = 0.8
    elif aktivitas == "A":
        tambahan_aktiv = 1.0
    else:
        tambahan_aktiv = 0
        print("Aktivitas tidak dikenali, tidak ada tambahan air.")

    air += tambahan_aktiv

    # ==============================
    # Bagian 3: Tambahkan/dikurangi sesuai kondisi kesehatan
    # ==============================
    if kesehatan == "TA":
        tambahan_kesehatan = 0
    elif kesehatan == "H":
        tambahan_kesehatan = 0.5
    elif kesehatan == "D":
        tambahan_kesehatan = 0.7
    elif kesehatan == "PG":
        tambahan_kesehatan = -0.3
    elif kesehatan == "PJ":
        tambahan_kesehatan = -0.2
    else:
        tambahan_kesehatan = 0
        print("Kondisi kesehatan tidak dikenali, tidak ada tambahan.")

    air += tambahan_kesehatan

    # ==============================
    # Bagian 4: Tampilkan hasil
    # ==============================
    print("\n=== HASIL PERHITUNGAN ===")
    print(f"Nama\t\t: {nama}")
    print(f"Umur\t\t: {umur} tahun")
    print(f"Jenis Kelamin\t: {jk}")
    print(f"Aktivitas Fisik\t: {aktivitas}")
    print(f"Kondisi Khusus\t: {kesehatan}")
    print(f"\nRekomendasi Air: {air:.1f} Liter per hari")
