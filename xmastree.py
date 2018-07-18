def pattern():
	a= int(input("Enter number of rows:  "))
	b = a-3
	for k in range(b,0,-1):
		for f in range(0,5):
			print(" ",end="")
		for j in range(0,k):
			print("*",end="")
		for h in range(0, 2*(b-k)+1):
			print(" ",end="")
		print("\r")
	c=a-2
	for k in range(c,0,-1):
		for f in range(0,2):
			print(" ",end="")
		for j in range(0,k):
			print("*",end="")
		for h in range(0, 2*(c-k)+2):
			print(" ",end="")
		print("\r")
	d = a-1
	for k in range(d,0,-1):
		for f in range(0,1):
			print(" ",end="")
		for j in range(0,k):
			print("*",end="")
		for h in range(0, 2*(d-k)+3):
			print(" ",end="")
		print("\r")
	e = a-0
	for k in range(e,0,-1):
		for j in range(0,k):
			print(" ",end="")
		for h in range(0, 2*(e-k)+1):
			print("*",end="")
		print("\r")

pattern()