x = input()

for i in range(int(x)):
	y = input()
	z =  input()
	out = ""
	
	for j in z:
		if j == "A":
			out += "T"
		elif j == "T":
			out += "A"
		elif j == "G":
			out += "C"
		elif j == "C":
			out += "G"
		else:
			out = "Error RNA nucleobases found!"
			break
	
	print(out)