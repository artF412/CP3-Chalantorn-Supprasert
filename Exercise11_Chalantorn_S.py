number = int(input("Please Enter Number : "))
spaceBar = " "
for i in range(number):
    for x in range(number):
        number = number - 1
        i = i+1
        print(spaceBar*number,"*"*(i+x))