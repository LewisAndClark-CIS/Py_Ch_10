# Py_Ch_10_2.py
# Auhtors: Sam Coon and Tyler Kapusniak
# Date: 3/5/15

from tkinter import *
import random

class Application(Frame):
    """ GUI application that creates a story based on user input. """
    def __init__(self, master):
        """ Initialize Frame. """
        super(Application, self).__init__(master)  
        self.grid()
        self.create_widgets()
        self.number = random.randint(1,100)

    def create_widgets(self):
        """ Create widgets to get guess and display lower or higher"""
        # create instruction label
        Label(self,
              text = "Try to guess the number im thinking of between 1 and 100."
              ).grid(row = 0, column = 0, columnspan = 3, sticky = W)

        # create label and text entry for guess
        Label(self,
              text = "Guess: "
              ).grid(row = 1, column = 0, sticky = W)
        self.guess = Entry(self)
        self.guess.grid(row = 1, column = 1, sticky = W)

        # Create sumbit button
        Button(self,
               text = "Submit",
               command = self.guess_game
               ).grid(row = 2, column = 0, sticky = W)

        # Create new number button
        Button(self,
               text = "New Number",
               command = self.random_number
               ).grid(row = 3, column = 0, sticky = W)
        self.guess_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.guess_txt.grid(row = 4, column = 0, columnspan = 3)
        
    def random_number(self):
        self.number = random.randint(1,100)
        new = "A new number has been selected. Start guessing!"
        self.guess_txt.delete(0.0,END)
        self.guess_txt.insert(0.0, new )

    def guess_game(self):
        number = self.number
        guess = int(self.guess.get())
        if guess > number:
            outputLow = ("Guess Lower...")
            self.guess_txt.delete(0.0, END)
            self.guess_txt.insert(0.0, outputLow)

        elif guess < number:
            outputHigh = ("Guess Higher...")
            self.guess_txt.delete(0.0, END)
            self.guess_txt.insert(0.0, outputHigh)
        

        elif guess > 101 or guess < 1:
            outoutError =("That is an error, please guess between 1 and 100.")
            self.guess_txt.delete(0.0, END)
            self.guess_txt.insert(0.0, outputError)

        else:
            outputCorrect = ("You guess it! The number was " + str(number) + ".")
            self.guess_txt.delete(0.0, END)
            self.guess_txt.insert(0.0, outputCorrect)
        


            

#main
root = Tk()
root.title("Guess My Number!")
app = Application(root)
root.mainloop()
