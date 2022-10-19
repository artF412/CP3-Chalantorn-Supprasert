class Vehicle:
    lecenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Pickup(Vehicle):
    def colorPickup(self):
        color = ""
        print("PickUpCars",self.color,"Color")

class Car(Vehicle):
    def sayHelloMG(self):
        nameDrive = ""
        print("Hello",self.nameDrive,"sir Safe Fight")

class Van(Vehicle):
    def numberPeople(self):
        howPeopleInVan = 0
        print("How many people in van cars :",self.howPeopleInVan)

pickup1 = Pickup()
pickup1.turnOnAirConditioner()
pickup1.color = "Neon Green"
pickup1.colorPickup()

car1 = Car()
car1.turnOnAirConditioner()
car1.nameDrive ="Chalantorn"
car1.sayHelloMG()

van1 = Van()
van1.turnOnAirConditioner()
van1.howPeopleInVan = 8
van1.numberPeople()
