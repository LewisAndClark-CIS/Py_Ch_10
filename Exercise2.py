# Exercise2, chapter10
# Author: Alton Stillwell
# Date: 3/6/15
#############
# Guess My Number Game
#############
from tkinter import *
import random
#############
class Application(Frame):

    def __init__(self, master):
        super(Application,self).__init__(master)
        self.grid()
        self.the_number = random.randint(1,100)
        self.guesses = 0
        self.create_widgets()

    def create_widgets(self):
        Label(self,text = "Welcome to 'Guess My Number'!").grid(row = 0, column = 0, columnspan = 2, sticky = W)

        Label(self,text = "I'm thinking of a number between").grid(row = 2, column = 0, columnspan = 2, sticky = W)
        Label(self,text = "1 and 100. Try to guess it in as few").grid(row = 3, column = 0, columnspan = 2, sticky = W)
        Label(self,text = "attempts as possible.").grid(row = 4, column = 0, columnspan = 2, sticky = W)

        Label(self,text = "Take a guess: ").grid(row = 6, column = 0, sticky = W)
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row = 6, column = 1, sticky = W)

        Button(self,text = "Confirm Guess", command = self.make_guess).grid(row = 7, column = 0, sticky = W)
        Button(self,text = "Reset Game", command = self.reset_game).grid(row = 7, column = 1, sticky = W)

        self.textBox = Text(self, width = 50, height = 5, wrap = WORD)
        self.textBox.grid(row = 8, column = 0, columnspan = 2)

    def make_guess(self):
        self.textBox.delete(0.0, END)
        guess = self.guess_ent.get()
        guess = int(guess)
        if guess > self.the_number:
            self.textBox.insert(0.0,"Go lower")
            self.guesses += 1
        elif guess < self.the_number:
            self.textBox.insert(0.0,"Go higher")
            self.guesses += 1
        else:
            self.guesses += 1
            self.textBox.insert(0.0,"You guessed it! And it only took you ")
            self.textBox.insert(END, self.guesses)
            self.textBox.insert(END, " tries!")

    def reset_game(self):
        self.guesses = 0
        self.textBox.delete(0.0, END)
        self.the_number = random.randint(1,100)
#############
# Main
root = Tk()
root.title("Guess My Number")
app = Application(root)
root.mainloop()
