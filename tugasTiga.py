nama = input("Masukkan Nama Anda : ")
usia = int(input("Masukkan Usia Anda : "))
gender = input("Masukkan Jenis Kelamin Anda (L/P): ")

if usia < 3:
	if gender == "L":
		print("Masih Diberi Asi")
	elif gender == "P":
		print("Masih Di Beri Asi")
	else :
		print("Usia Tidak Valid")
	exit()

aktivitas = input("Masukkan Tingkat Aktivitas Anda (sedentaria/ringan/sedang/berat/atlet): ")
kondisi = input("Masukkan Kondisi Kesehatan Anda(tidak ada/hamil/penyakit ginjal/penyakit jantung): ")

if usia > 3 or usia <= 18:
	if gender == "L":
		air = 1.6
	if gender == "P":
		air = 1.4
	else :
		print("Usia Tidak Valid")
elif usia >18 or usia <= 64:
	if gender == "L":
		air = 2.5
	if gender == "P":
		air = 2.0
	else :
		print("Usia Tidak Valid")
elif usia >= 65:
	if gender == "L":
		air = 2.0
	if gender == "P":
		air = 1.8
	else :
		print("Usia Tidak Valid")
else :
	print("Usia Tidak Valid")

if aktivitas == "sedentaria":
	ta = 0
elif aktivitas == "ringan":
	ta = 0.3
elif aktivitas == "sedang":
	ta = 0.5
elif aktivitas == "berat":
	ta = 0.8
elif aktivitas == "atlet":
	ta = 1.0
else :
	print("Aktivitas Tidak Valid")

if kondisi == "tidak ada":
	tak = 0
elif kondisi == "hamil" or "menyusui":
	tak = 0.5
elif kondisi == "demam" or "infeksi":
	tak = 0.7
elif kondisi == "penyakit ginjal":
	tak = -0.3
elif kondisi == "penyakit jantung":
	tak = -0.2
else :
	print("Kondisi Tidak Valid")

total = air + ta + tak

print(f"Nama : {nama}")
print(f"Kebutuhan air : {air} liter")
print(f"Kebutuhan Tambahan Air Menurut Aktivitas : {aktivitas} liter")
print(f"Kebutuhan Tambahan Air Menurut Kondisi : {kondisi} liter")
print(f"Total Kebutuhan Air : {total:.1f} liter")