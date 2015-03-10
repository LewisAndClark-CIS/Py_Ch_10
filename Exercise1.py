# Exercise1, chapter10
# Author: Alton Stillwell
# Date: 3/6/15
###############
# Mad Lib Program
###############
from tkinter import *
#############
class Application(Frame):
    
    def __init__(self,master):
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        Label(self, text = "Enter information for a new story").grid(row = 0, column = 0, columnspan = 2, sticky = W)

        Label(self, text = "Hero: ").grid(row = 1, column = 0, sticky = W)
        self.hero_ent = Entry(self)
        self.hero_ent.grid(row = 1, column = 1, sticky = W)

        Label(self, text = "Villian: ").grid(row = 2, column = 0, sticky = W)
        self.villian_ent = Entry(self)
        self.villian_ent.grid(row = 2, column = 1, sticky = W)

        Label(self, text = "Weapon: ").grid(row = 3, column = 0, sticky = W)
        self.weapon_ent = Entry(self)
        self.weapon_ent.grid(row = 3, column = 1, sticky = W)

        Label(self, text = "Plural Noun: ").grid(row = 4, column = 0, sticky = W)
        self.pluralNoun_ent = Entry(self)
        self.pluralNoun_ent.grid(row = 4, column = 1, sticky = W)

        Label(self, text = "Verb: ").grid(row = 5, column = 0, sticky = W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row =5, column = 1, sticky = W)

        Label(self, text = "Adjective(s): ").grid(row = 6, column = 0, sticky = W)
        self.is_ugly = BooleanVar()
        Checkbutton(self, text = "ugly", variable = self.is_ugly).grid(row = 7, column = 0, sticky = W)
        self.is_depressed = BooleanVar()
        Checkbutton(self, text = "depressed",variable = self.is_depressed).grid(row = 8, column = 0, sticky = W)
        self.is_smelly = BooleanVar()
        Checkbutton(self, text = "smelly",variable = self.is_smelly).grid(row = 9, column = 0, sticky = W)

        Label(self, text = "Body Part: ").grid(row = 6, column = 1, sticky = W)
        self.body_part = StringVar()
        self.body_part.set(None)
        body_parts = ["eye ball","spleen","face"]
        row = 7
        for part in body_parts:
            Radiobutton(self, text = part, variable = self.body_part, value = part).grid(row = row, column = 1, sticky = W)
            row += 1

        Button(self,text = "Click for story", command = self.tell_story).grid(row = 10, column = 0, sticky = W)

        self.story_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_txt.grid(row = 11, column = 0, columnspan = 4)

    def tell_story(self):
        # set variables
        hero = self.hero_ent.get()
        villian = self.villian_ent.get()
        weapon = self.weapon_ent.get()
        noun = self.pluralNoun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_ugly.get():
            adjectives += "ugly, "
        if self.is_depressed.get():
            adjectives += "depressed, "
        if self.is_smelly.get():
            adjectives += "smelly, "
        body_part = self.body_part.get()
        # create story
        story = "There was once a mighty hero named '"
        story += hero
        story += "', who protected his proud country of "
        story += adjectives
        story += " peoples with his bestie "
        story += villian
        story += ". Then one day, everything changed. "
        story += hero
        story += " purchased some new "
        story += noun
        story += ". This would have been fine, if he had bought some for his bestie "
        story += villian
        story += ". Needless to say, "
        story += villian
        story += " now felt unwanted, and turned to a life of crime to try and get "
        story += hero
        story += " to finally notice him again. "
        story += villian
        story += " started pirating movies! This injustice would not stand, "
        story += hero
        story += " decided. Grabing his trusty "
        story += weapon
        story += ", he set out to "
        story += verb
        story += " "
        story += villian
        story += "'s "
        story += body_part
        story += ". "
        story += villian
        story += " was defeated easily by "
        story += hero
        story += "'s "
        story += weapon
        story += ". Thus, saving the day! "
        story += villian
        story += " would go on to be the developer of FNAF."

        # display story
        self.story_txt.delete(0.0,END)
        self.story_txt.insert(0.0, story)
############################################
# main
root = Tk()
root.title("Mad Lib")
app = Application(root)
root.mainloop()
