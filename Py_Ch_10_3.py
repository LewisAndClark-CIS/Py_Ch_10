# Py_Ch_10_3.py
# Auhtors: Sam Coon and Tyler Kapusniak
# Date: 3/5/15

from tkinter import *

class Application(Frame):
    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create widgets to get customer information"""
        # Create instructions
        Label(self,
              text = "Check the boxes of the items you want."\
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # Create Label for foods
        Label(self,
              text = "Foods:"
              ).grid(row = 1, column = 0, sticky = W)

        # Create the check box items
        self.Hamburger = BooleanVar()
        Checkbutton(self,
                    text = "Hamburger",
                    variable = self.Hamburger
                    ).grid(row = 2, column = 0, sticky = W)

        self.Fries = BooleanVar()
        Checkbutton(self,
                    text = "Fries",
                    variable = self.Fries
                    ).grid(row = 3, column = 0, sticky = W)

        self.HotDog = BooleanVar()
        Checkbutton(self,
                    text = "Hot Dog",
                    variable = self.HotDog
                    ).grid(row = 4, column = 0, sticky = W)

        self.ChickenStrips = BooleanVar()
        Checkbutton(self,
                    text = "Chicken Strips",
                    variable = self.ChickenStrips
                    ).grid(row = 5, column = 0, sticky = W)

        self.Salad = BooleanVar()
        Checkbutton(self,
                    text = "Salad",
                    variable = self.Salad
                    ).grid(row = 6, column = 0, sticky = W)
        # Create the price Labels
        Label(self,
              text = "Price:"
              ).grid(row = 1, column = 1, sticky = W)

        Label(self,
              text = "$3.00"
              ).grid(row = 2, column = 1, sticky = W)

        Label(self,
              text = "$1.00"
              ).grid(row = 3, column = 1, sticky = W)

        Label(self,
              text = "$2.00"
              ).grid(row = 4, column = 1, sticky = W)

        Label(self,
              text = "$3.00"
              ).grid(row = 5, column = 1, sticky = W)

        Label(self,
              text = "$2.00"
              ).grid(row = 6, column = 1, sticky = W)

        # Create an order button
        Button(self,
               text = "Order",
               command = self.Order
               ).grid(row = 7, column = 0, sticky = W)

        self.order_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.order_txt.grid(row = 8, column = 0, columnspan = 2)
    def Order(self):
        total = 0
        Ordered = ""
        if self.Hamburger.get():
            Ordered += "Hamburger, "
            total += 3
        if self.Fries.get():
            Ordered += "Fries, "
            total += 1
        if self.HotDog.get():
            Ordered += "Hot Dog, "
            total += 2
        if self.ChickenStrips.get():
            Ordered += "Chicken Strips, "
            total += 3
        if self.Salad.get():
            Ordered += "Salad, "
            total += 2

       # Display receipt
        receipt = "You ordered "
        receipt += Ordered
        receipt += "\nYour total is: $"
        receipt += str(total)

       # Display the receipt
        self.order_txt.delete(0.0, END)
        self.order_txt.insert(0.0, receipt)
       
#main
root = Tk()
root.title("Order Up!")
app = Application(root)
root.mainloop()
