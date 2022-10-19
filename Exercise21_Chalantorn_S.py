from tkinter import *

def calculateBMI(event):
    highCal = float(txtHight.get())
    WeightCal = float(txtWeight.get())

    highCal /= 100
    bmi = WeightCal/(highCal*highCal)

    if bmi < 18.5:
        labelResult.configure(text="ผอมเกินไป")
    elif bmi >= 18.6 and bmi <= 22.9:
        labelResult.configure(text="น้ำหนักปกติ เหมาะสม")
    elif bmi >= 23.0 and bmi <= 24.9:
        labelResult.configure(text="น้ำหนักเกิน")
    elif bmi >= 25.0 and bmi <= 29.9:
        labelResult.configure(text="อ้วน")
    else:
        labelResult.configure(text="อ้วนมาก")
    
    labelCalculate.configure(text=round(bmi,2))

main = Tk()
labelHight = Label(main,text="ส่วนสูง (CM)")
labelHight.grid(column=0,row=0)
txtHight = Entry(main)
txtHight.grid(column=1,row=0)

labelWeight = Label(main,text="น้ำหนัก (KG)")
labelWeight.grid(column=0,row=1)
txtWeight = Entry(main)
txtWeight.grid(column=1,row=1)

calculateButton = Button(main,text=("คำนวณ !!"))
calculateButton.bind('<Button-1>',calculateBMI)
calculateButton.grid(column=0,row=2)

labelResult = Label(main,text="ผลลัพธ์")
labelResult.grid(column=1,row=2)

labelCalculate = Label(main,text="ค่า BMI")
labelCalculate.grid(column=1,row=3)

main.mainloop()