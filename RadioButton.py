from tkinter import *
from tkinter import ttk

root = Tk()
rbVar = StringVar()
rb1 = ttk.Radiobutton(root, text="male", variable=rbVar, value="is male")
rb1.pack()
print(rbVar.get())

rb2 = ttk.Radiobutton(root, text="female", variable=rbVar, value="is female")
rb2.pack()
print(rbVar.get())

root.mainloop()