food1 = "tahu walik"
hargaf1 = 8000
food2 = "kentang saus keju"
hargaf2 = 15000
food3 = "cireng keju"
hargaf3 = 12000

drink1 = "es teh tarik"
hargad1 = 8000
drink2 = "es kelapa susu"
hargad2 = 12.000

pajak = 0.05 

print("===daftar menu makanan===")
print(f"1. {food1} Rp {hargaf1}")
print(f"2. {food2} Rp {hargaf2}")
print(f"3. {food3} Rp {hargaf3}")

print("\n===daftar menu minuman===")
print(f"1. {drink1} Rp {hargad1}")
print(f"2. {drink2} Rp {hargad2}")

jumlah_food1 = int(input(f"berapa porsi {food1}?"))
jumlah_food2 = int(input(f"berapa porsi {food2}?"))
jumlah_food3 = int(input(f"berapa porsi {food3}?"))
jumlah_drink1 = int(input(f"berapa banyak {drink1}?"))
jumlah_drink2 = int(input(f"berapa banyak {drink2}?"))

total_makanan = (hargaf1 * jumlah_food1) + (hargaf2 * jumlah_food2) + (hargaf3 * jumlah_food3) 
total_minuman = (hargad1 * jumlah_drink1) + (hargad2 * jumlah_drink2)

subtotal = total_makanan + total_minuman
total_pajak = subtotal * pajak
total_akhir = subtotal + total_pajak

print("\n====ringkasan pesanan====")
print(f"total_makanan : Rp{subtotal,:}")
print(f"pajak (5%) : Rp{int(total_pajak):,}")
print(f"total bayar : Rp{int(total_akhir):,}")
 





