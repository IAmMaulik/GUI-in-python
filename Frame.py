from tkinter import *
from tkinter import ttk

root = Tk()
frame = ttk.Frame(root)
frame.pack()
frame.config(height=200, width=200)
# we can add many different features to our frame like padding, etc.
frame.config(relief=RIDGE, padding=(10, 10))

ttk.Button(frame, text="Click Me!").grid(row=0, column=0)
ttk.Button(frame, text="Click Me!").grid(row=0, column=3)

frame2 = ttk.Frame(root)
frame2.pack()
frame2.config(height=200, width=200)
ttk.Button(frame2, text="Click Me frame 2").pack()
ttk.Button(frame2, text="Click Me 2 frame 2").pack()
frame2.config(relief=RIDGE, padding=(10, 10))
# frames help us make our GUI look professional

ttk.LabelFrame(height=100, width=100, text="Third Frame").pack()


root.mainloop()