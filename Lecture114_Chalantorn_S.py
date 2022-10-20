from tkinter import *
from forex_python.converter import CurrencyRates

c = CurrencyRates()
c.get_rates('USD')
print(c.get_rates('USD'))


"""#GUI program
main = Tk()



main.mainloop()
"""