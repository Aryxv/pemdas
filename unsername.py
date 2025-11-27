unsername = "Itenas"
Pwd = 123

i=0

while i < 10 :
	unsernama = input ("Unsername : ")
	pwd = int(input("Password : "))
	
	if unsername == unsername and pwd == Pwd :
		print (f"anda berhasil login")
		break

	else :
		print (f"anda gagal login coba lagi")
	i +=1	
	if i == 3 :
 		print (f"akun anda terblokir")
 		break