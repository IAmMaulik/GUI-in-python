from tkinter import *
from tkinter import ttk


def BuClick(ID):
    print("ID: {}".format(ID))


root = Tk()
ttk.Button(root, text="Click ME!", command=lambda: BuClick(10)).pack()
# using lambda is necessary here

root.mainloop()
