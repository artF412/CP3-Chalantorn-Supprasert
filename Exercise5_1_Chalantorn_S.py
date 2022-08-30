'''\
การรับ input ตัวแปร 2 ตัวเพื่อมาทำการคำนวณ บวก ลบ คูณ หาร
'''
num1 = int(input("Number 1 : "))
num2 = int(input("Number 2 : "))
sum = num1+num2
minus = num1-num2
multiplied = num1*num2
divide = num1/num2
print(num1 ,"+",num2,"=",sum)
print(num1 ,"-",num2,"=",minus)
print(num1 ,"*",num2,"=",multiplied)
print(num1 ,"/",num2,"=",divide)