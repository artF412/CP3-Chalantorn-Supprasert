menuMyFood = {'ข้าวหมูแดง':40,'ข้าวหมูกรอบ':40,'ข้าวหมูแดงหมูกรอบ':50}
menuList = []
def showBill():
    txt = "My Restaurants"
    cen = txt.center(24, "-")
    total = 0
    print(cen)
    for num in range(len(menuList)):
        print(menuList[num][0],menuList[num][1])
        total += int(menuList[num][1])
    print('ราคารวม',total,'บาท')
while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName,menuMyFood[menuName]])
showBill()
