from tkinter import *
from tkinter import ttk

root = Tk()

style = ttk.Style()
style.configure('TButton', foreground='#0B6CA3', font=('Arial', 18))

entry = ttk.Entry(root, width=30)
entry.pack()

button = ttk.Button(root, text="Submit")
button.pack()
logo = PhotoImage(file="C:\\Users\\yashs\\Desktop\\Maulik\\Python\\Udmey Course Hussein\\GUI\\login.gif")
button.config(image=logo, compound=LEFT)
# the image is too big so we will resize it
Resize_Logo = logo.subsample(10, 10)
button.config(image=Resize_Logo)

def BuClick():
    print(entry.get())
    entry.delete(0, END)
#   entry.insert(0, "Button Clicked")

button.config(command=BuClick)

root.mainloop()
