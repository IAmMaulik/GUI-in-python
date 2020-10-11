from tkinter import *
from tkinter import ttk

root = Tk()

l1 = ttk.Label(root, text="UserName: ")
l1.grid(row=0, column=0)
etUserName = ttk.Entry(root, width=30)
etUserName.grid(row=0, column=1)

l2 = ttk.Label(root, text="Password: ")
l2.grid(row=1, column=0)
etPassword = ttk.Entry(root, width=30)
etPassword.grid(row=1, column=1)

BuLogin = ttk.Button(root, text="Login")
BuLogin.grid(row=2, column=1)

root.mainloop()