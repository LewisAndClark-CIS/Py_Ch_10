# Chapter10, exercise3
# Author: Alton Stillwell
# Date: 3/10/15
###############
# Pizza Menu
# Three choices:
# cheese(5), pepperoni(6), supreme(8)
# have user enter amounts for each
# calculate total
#############
from tkinter import *
#############
class Application(Frame):

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.pizza_size = None
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,text = "Welcome to Alton's Pizzaria!").grid(row = 0, column = 0, columnspan = 2, sticky = W)

        Label(self,text = "Pizzas").grid(row = 2, column = 0, sticky = W)
        Label(self,text = "Amount").grid(row = 2, column = 1, sticky = W)
        
        self.cheese_pizza = BooleanVar()
        Checkbutton(self,text = "Cheese - $5.00", variable = self.cheese_pizza).grid(row = 3, column = 0, sticky = W)
        self.cheese_amount_ent = Entry(self)
        self.cheese_amount_ent.grid(row = 3, column = 1, sticky = W)
        
        self.pepperoni_pizza = BooleanVar()
        Checkbutton(self,text = "Pepperoni - $6.00", variable = self.pepperoni_pizza).grid(row = 4, column = 0, sticky = W)
        self.pepperoni_amount_ent = Entry(self)
        self.pepperoni_amount_ent.grid(row = 4, column = 1, sticky = W)

        self.supreme_pizza = BooleanVar()
        Checkbutton(self,text = "Supreme - $8.00", variable = self.supreme_pizza).grid(row = 5, column = 0, sticky = W)
        self.supreme_amount_ent = Entry(self)
        self.supreme_amount_ent.grid(row = 5, column = 1, sticky = W)

        Button(self,text = "Calculate Price", command = self.calculate_price).grid(row = 6, column = 0, columnspan = 4, sticky = W)

        Label(self,text = "Your total: ").grid(row = 7, column = 0, sticky = W)
        self.total_txt = Text(self, width = 20, height = 1, wrap = WORD)
        self.total_txt.grid(row = 7, column = 1)

    def calculate_price(self):
        totalPrice = 0
        if self.cheese_pizza.get():
            cheesePrice = 5 * int(self.cheese_amount_ent.get())
            totalPrice += cheesePrice

        if self.pepperoni_pizza.get():
            pepperoniPrice = 6 * int(self.pepperoni_amount_ent.get())
            totalPrice += pepperoniPrice

        if self.supreme_pizza.get():
            supremePrice = 8 * int(self.supreme_amount_ent.get())
            totalPrice += supremePrice
            
        totalPrice = str(totalPrice)
        totalPrice = "$"+totalPrice
        self.total_txt.delete(0.0, END)
        self.total_txt.insert(0.0, totalPrice)
#############
# Main
root = Tk()
root.title("Order Up!")
app = Application(root)
root.mainloop()
