from tkinter import *
from tkinter import ttk

root = Tk()

Cb = ttk.Checkbutton(root, text="Are you Maulik Shah")
Cb.pack()

state = StringVar()
state.set('Yes')

Cb.config(variable=state, onvalue="Yes he is Maulik Shah", offvalue="No he is not Maulik Shah")
print(state.get())


root.mainloop()