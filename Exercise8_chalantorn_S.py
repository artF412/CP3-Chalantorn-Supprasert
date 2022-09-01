userInput = input("Username : ")
passInput = input("Password : ")
if userInput == "admin" and passInput == "1234":
    print("Welcome To Cafe")
    print("-----Menu-----")
    print("1 : Americano 60 THB")
    print("2 : Latte 70 THB")
    print("3 : Mocha 75 THB")
    print("4 : Matcha Latte 80")
    print("5 : Blue Soda 60")
    choseProduct = int(input("Chose Product : "))
    if choseProduct == 1:
        print(" Americano : 60 THB")
        americano = 60
        pcs = int(input("Amount : "))
        result = americano * pcs
        print("Total :",result,"THB")
    elif choseProduct == 2:
        print(" Latte : 70 THB")
        latte = 70
        pcs = int(input("Amount : "))
        result = latte * pcs
        print("Total :",result,"THB")
    elif choseProduct == 3:
        print(" Mocha : 75 THB")
        mocha = 75
        pcs = int(input("Amount : "))
        result = mocha * pcs
        print("Total :",result,"THB")
    elif choseProduct == 4:
        print(" Matcha Latte : 80 THB")
        matchaLatte = 80
        pcs = int(input("Amount : "))
        result = matchaLatte * pcs
        print("Total :",result,"THB")
    elif choseProduct == 5:
        print(" Blue Soda : 60 THB")
        blueSoda = 60
        pcs = int(input("Amount : "))
        result = blueSoda * pcs
        print("Total :",result,"THB")
    else:
        print("No Item Order")

else:
    print("Wrong Username or Password!!")