import tkinter
import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

#LIST
answers = [
    "pride",
    "fair",
    "button",
    "success",
    "august",
    "excited",
    "adorable",
    "petty",
    "correct",
    "quiz",

]

words = [
    "ridpe",
    "arif",
    "notbut",
    "cuscses",
    "gustua",
    "tedicex",
    "abledora",
    "typet",
    "retcorc",
    "izuq",

]

#creating variable to select random word
num = random.randrange(0,9,1)


#FUNCTIONS
#defining a function to the global variable and also override
def default():
    global words,answers,num
    lbl.config(text= words[num])

#create function to check answer
def checkanswer():
    global words, answers, num
    var = ent.get()
    if var == answers[num]:
        messagebox.showinfo("Correct!","Dude, you are smart")
        res()
    else:
        messagebox.showinfo("Incorrect!","You need to practice more vocabs")
        ent.delete(0, END)

#create reset function
def res():
    global words, answers, num
    num = random.randrange(0, 9, 1)
    lbl.config(text=words[num])
    ent.delete(0, END)

#WIDGET
#creating the main window
root =tkinter.Tk()
root.geometry("350x400+400+300")   
root.title('Guess the Word!')
root.configure(background="#000")

#label to display text
lbl = Label(
    root,
    text="Your text goes here",
    font=("verdana", 18),
    bg='#000',
    fg="#fff"
)
lbl.pack(pady=30,ipady=10,ipadx=10)


#create answer variable
ans1 = StringVar()
#creating the input box
ent = Entry(
    root,
    font=("verdana", 18),
    textvariable = ans1,
)
#setting the inner padding for the entry text
ent.pack(ipady=5,ipadx=5)

#creating the check button
btncheck = Button(
    root,
    text = "Check",
    font = ("cosmic sans ms", 16, "bold"),
    width = 16,
    bg="#64dd17",
    fg="#000000",
    relief = GROOVE,
    command = checkanswer,
)
btncheck.pack(pady=40)

btnreset = Button(
    root,
    text="Reset",
    font=("cosmic sans ms", 16, "bold"),
    width=16,
    bg="#ff3d00",
    fg="#000000",
    relief=GROOVE,
    command = res,
)
btnreset.pack()


default()

root.mainloop()
