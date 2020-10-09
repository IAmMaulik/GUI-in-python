from tkinter import *
from tkinter import ttk

root = Tk()
button = ttk.Button(root, text="Click Me!")
button.pack()


def ButtonClick():
    print("I'm Just Another button")


button.config(command=ButtonClick())
