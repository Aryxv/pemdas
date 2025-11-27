jk = input("Apa jenis kelamin anda (L/P): ")
umur = int(input("Masukkan umur Anda: "))

if jk == "L" and umur < 18:
    print("Rekomendasi Asupan Air Anda: 1.6 liter")

elif jk == "P" and umur < 18:
    print("Rekomendasi Asupan Air Anda: 1.4 liter")          

elif jk == "L" and 18 <= umur <= 64:
    print("Rekomendasi Asupan Air Anda: 2.5 liter")

elif jk == "P" and 18 <= umur <= 64:
    print("Rekomendasi Asupan Air Anda: 2.0 liter")

elif jk == "L" and umur >= 65:
    print("Rekomendasi Asupan Air Anda: 2.0 liter")

else:
    print("Rekomendasi Asupan Air Anda: 1.8 liter")
