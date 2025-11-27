burger = 10
total = 0
for i in range (1, 6):
	print(f"pendapatan burger H ke {i}")
	print(f"banyak yang terjual {burger}")
	pendapatan = burger * 25000
	print(f"pendapatan hari ke {i} = {pendapatan} ")
	burger += 2
	total = total + pendapatan

print (f"pendapatan selama 5 hari adalah {total}")