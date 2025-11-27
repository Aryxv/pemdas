berat = 79
tinggi = 180

try :
	bmi=berat/(tinggi**2)
	print(f"Indeks masa tubuh (BMI) : {bmi:.2f}")
except ZeroDivisionError :
	print("Kesalahan : Tinggi tidak boleh nol")
except Exception as e :
	print("Terjadi kesalahan :",e)