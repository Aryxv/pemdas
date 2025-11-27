import numpy as np

nilai = np.array([[80, 75, 90, 88], [70, 60, 85, 78], [95, 88, 92, 96]])
rataarata = nilai.mean(axis=1)
tertinggi = nilai.max()_
tiga = nilai [:,2]
ratatinggi = ratarata.max()

print(f"nilai :\n{nilai}\nRata-rata nilai setiap siswa: {rataarata}\nNilai tertinggi: {tertinggi}\nNilai ketiga setiap siswa: {tiga}\nRata-rata tertinggi: {ratatinggi}")