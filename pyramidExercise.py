x = int(input(""))
for i in range(0,x):
    for j in range(0,x-i-1):
	    print(end=" ")
    for j in range(0,2*i+1):
	    print("*",end="")
    print()