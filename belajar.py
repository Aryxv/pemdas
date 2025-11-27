# (LIST) List kosong untuk menampung belanjaan
daftar_belanja = []
barang = "" # Variabel sementara untuk menampung input

print("Masukkan daftar belanja (ketik 'cukup' untuk berhenti):")

# (LOOP) Loop akan terus berjalan selama input 'barang'
#       bukan "cukup"
while barang.lower() != 'cukup':
    barang = input("Nama barang: ")
    
    # (IF) Kita perlu 'if' di sini agar kata "cukup"
    #      tidak ikut masuk ke dalam list belanjaan
    if barang.lower() != 'cukup':
        daftar_belanja.append(barang)

print("\n--- Daftar Belanja Anda ---")
# Loop 'for' untuk mencetak hasil akhir
for item in daftar_belanja:
    print(f"- {item}")