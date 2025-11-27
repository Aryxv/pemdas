
siswa = [
    ["Alice", [85, 90, 88]],
    ["Bob", [78, 82, 85]],
    ["Charlie", [92, 88, 90]]
]

alice_rata = sum(siswa[0][1]) / len(siswa[0][1])
bob_rata = sum(siswa[1][1]) / len(siswa[1][1])
charlie_rata = sum(siswa[2][1]) / len(siswa[2][1])

print("Rata-rata nilai setiap siswa:")
print("Alice :", round(alice_rata, 2))
print("Bob :", round(bob_rata, 2))
print("Charlie :", round(charlie_rata, 2))     