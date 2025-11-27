def hitung_diskon(total):
    if total >= 500000:
        diskon = 0.10 * total  # Diskon 10%
    elif total >= 300000:
        diskon = 0.05 * total  # Diskon 5%
    else:
        diskon = 0
    
    # PERBAIKAN: Indentasi baris ini harus sejajar dengan 'if'
    return diskon
    
def hitung_total_bayar(total):
    besar_diskon = hitung_diskon(total)
    total_setelah_diskon = total - besar_diskon
    return total_setelah_diskon

print("===== PROGRAM KASIR TOKO =====")

try:
    total_belanja = float(input("Masukkan total belanja Anda: Rp "))
    total_bayar_akhir = hitung_total_bayar(total_belanja)
    
    print("----------------------------------")
    print(f"Total Belanja:    Rp {total_belanja:,.0f}")
    
    # Panggil fungsi hitung_diskon lagi untuk TAMPILAN
    diskon_didapat = hitung_diskon(total_belanja)
    print(f"Diskon yang Anda dapat: Rp {diskon_didapat:,.0f}")
 
    print(f"Total yang harus dibayar: Rp {total_bayar_akhir:,.0f}")

except ValueError:
    print("Input tidak valid. Harap masukkan angka saja.")