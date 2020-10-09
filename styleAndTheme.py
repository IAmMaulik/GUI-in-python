from tkinter import *
from tkinter import ttk

root = Tk()
button1 = ttk.Button(root, text="Button1").pack()
button2 = ttk.Button(root, text="Button2").pack()
button3 = ttk.Button(root, text="Button3").pack()

style = ttk.Style()
# print(style.theme_names())
# print(style.theme_use())
style.theme_use('clam')


# but what if we already have a css file with the style
style.configure('TButton', foreground="green", background="cyan", font="Arial")


# but if we want it for specific button only
# style.configure('Info.TButton', foreground="red"
# button3.configure(style='Info.TButton')

style.map('button3', background=[('pressed', 'green'), ('disabled', 'grey')])
root.mainloop()
