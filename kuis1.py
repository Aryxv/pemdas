roti = 30
total = 0
for i in range (1, 7) :
	print (f"pendapatan roti hari ke {i}")
	print (f"berapa banyak roti terjual {roti}")
	pendapatan = roti*8000
	print (f"jumlah pendapatan roti hari ke {i} = {pendapatan}")
	roti += 4
	total = total + pendapatan 

print (f"jadi total pendapatan sealana 6 hari adalah {total}")

	
	