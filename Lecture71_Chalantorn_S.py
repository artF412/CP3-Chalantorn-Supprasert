menuList = []
priceList = []

def showBill():
    txt = "My Restaurants"
    cen = txt.center(24, "-")
    print(cen)
    for num in range(len(menuList)):
        print(menuList[num],priceList[num])
    print("ราคาอาหารทั้งหมด",sum(priceList),"บาท")    

while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()