class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added to Customer Name : "+self.name,self.lastname,"s Cart",self.age,"years old")

cus1 = Customer()
cus1.name = "Chalantorn"
cus1.lastname = "Supprasert"
cus1.age = 28

cus2 = Customer()
cus2.name = "Kawinwat"
cus2.lastname = "Mawairong"
cus2.age = 26

cus3 = Customer()
cus3.name = "Gump"
cus3.lastname = "An"
cus3.age = 39

cus4 = Customer()
cus4.name = "Shoji"
cus4.lastname = "Yanakisawa"
cus4.age = 25

cus1.addCart()
cus2.addCart()
cus3.addCart()
cus4.addCart()
