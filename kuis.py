ulang = 0

while ulang < 3:
	print(f"\nNama Pasien ke-{ulang+1}")
	nama = input("Masukkan Nama Pasien : ")
	sistolik = int(input("Masukkan Tekanan Darah Sistolik (mmHg): "))
	diastolik = int(input("Masukkan Tekanan Darah Diastolik (mmHg): "))
	nadi = int(input("Masukkan Denyut Nadi (bpm): "))

	print("\nKondisi Dan Rekomendasi untuk", nama, ":")

	if sistolik > 180 or diastolik > 120:
		print("Krisis hipertensi!! Segera cari bantuan medis")
	else:
		if sistolik > 140 or diastolik > 90:
			print("Konsultasi dengan dokter mengenai hipertensi")
		elif (120 <= sistolik <= 139) or (80 <= diastolik <= 89):
			print("Berada dalam kategori prehipertensi")
		elif sistolik < 120 and diastolik < 80:
			print("Tekanan darah normal")

	match nadi:
		case n if n > 100:
			print("Periksa kondisi kesehatan jantung")
		case n if n < 60:
			print("Periksa apakah ada gejala lain yang mengiringi bradikardia")
		case _:
			print("Denyut nadi normal")

	ulang += 1
