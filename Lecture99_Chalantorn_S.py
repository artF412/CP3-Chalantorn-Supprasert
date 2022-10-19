from tkinter import *

def calculateBMI(event):
    highCal = float(txtHight.get())
    WeightCal = float(txtWeight.get())
    highCal /= 100
    bmi = WeightCal/(highCal*highCal)
    if bmi < 18.5:
        labelResult.configure(text="น้ำหนักน้อย / ผอม")
    elif bmi >= 18.5 and bmi <= 22.99:
        labelResult.configure(text="ปกติ (สุขภาพดี)")
    elif bmi >= 23 and bmi <= 24.99:
        labelResult.configure(text="ท้วม / โรคอ้วนระดับ 1")
    elif bmi >= 25 and bmi <= 29.99:
        labelResult.configure(text="อ้วน / โรคอ้วนระดับ 2")
    else:
        labelResult.configure(text="อ้วนมาก / โรคอ้วนระดับ 3")

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
main.mainloop()