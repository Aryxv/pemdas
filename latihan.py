# Input suhu tubuh dalam derajat Celsius
suhu_tubuh = 39.5

# Input detak jantung per menit
detak_jantung = 110

# Mengecek apakah suhu tubuh di atas normal
if suhu_tubuh > 37.5:
    print("Suhu tubuh di atas normal.")

    # Mengecek apakah suhu tubuh sangat tinggi
    if suhu_tubuh > 39:
        print("Suhu tubuh sangat tinggi, butuh perhatian medis segera.")
    else:
        # Mengecek detak jantung jika suhu tubuh tidak terlalu tinggi
        if detak_jantung > 100:
            print("Detak jantung terlalu tinggi, butuh pemeriksaan lebih lanjut.")
        else:
            print("Detak jantung normal, perbanyak istirahat dan minum cairan.")
else:
    print("Suhu tubuh normal, tidak ada tindakan khusus yang diperlukan.")
