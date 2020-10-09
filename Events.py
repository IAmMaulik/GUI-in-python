from tkinter import *
from tkinter import ttk

root = Tk()


def keyPress(event):
    print("This is the copy shortcut")


def buttonPress(event):
    print("Button is pressed")


bu = ttk.Button(root, text="Click ME!")
bu.pack()
bu.bind("<ButtonPress>", buttonPress)
root.bind("<Control-c>", keyPress)
# now because of this, the program always listens to what I type
# cool

root.mainloop()
