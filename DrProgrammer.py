#py \\S49FS\StudentHome$\1488808\Documents\CSpy\DrProgrammer.py

dir = input().split(" ")
x = input().split(" ")
y = input().split(" ")

def qA(z, l1, r1):
	global x
	global y
	
	pos = []
	out = 0
	
	for i in x:
		if int(i) >= l1 and int(i) <= r1:
			pos.append(int(i))
			
	for i in pos:
		for j in y:
			if int(i) + int(j) <= z:
				out += 1
	
	print(out)

def qB(z, l2, r2):
	global x
	global y
	
	pos = []
	out = 0
	
	for i in y:
		if int(i) >= l2 and int(i) <= r2:
			pos.append(int(i))
			
	for i in pos:
		for j in x:
			if int(i) + int(j) <= z:
				out += 1
	
	print(out)

def qC(z, l1, r1, l2, r2):
	global x
	global y
	
	posX = []
	posY = []
	out = 0
	
	for i in x:
		if int(i) >= l1 and int(i) <= r1:
			posX.append(int(i))
			
	for i in y:
		if int(i) >= l2 and int(i) <= r2:
			posY.append(int(i))
			
	for i in posX:
		for j in posY:
			if int(i) + int(j) <= z:
				out += 1
	
	print(out)

for i in range(int(dir[2])):
	input = input().split(" ")
	z = input[0]
	
	if input[1] == "A":
		qA(int(input[0]), int(input[2]), int(input[3]))
	elif input[1] == "B":
		qB(int(input[0]), int(input[2]), int(input[3]))
	elif input[1] == "C":
		qC(int(input[0]), int(input[2]), int(input[3]), int(input[4]), int(input[5]))