from tkinter import *
from tkinter import ttk

root = Tk()
style = ttk.Style()
style.theme_use('classic')

ttk.Label(root, text="Green", background="Green").grid(row=0, column=0, padx=1, pady=1, sticky='snew')

ttk.Label(root, text="Yellow", background="Yellow").grid(row=0, column=1, ipadx=1, ipady=1, sticky='snew')

ttk.Label(root, text="Red", background="Red").grid(row=0, column=2, rowspan=2, sticky='snew')

ttk.Label(root, text="Orange", background="Orange").grid(row=1, column=0, columnspan=2, sticky='snew')
# here sn and we stand for sticking to south,north and west,east

root.rowconfigure(0, weight=2)
root.rowconfigure(1, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=2)

root.mainloop()