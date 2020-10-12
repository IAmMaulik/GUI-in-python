from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def BuClick():
    print("UserName: {}, Password: {}".format(etUserName.get(), etPassword.get()))
    if etUserName.get() == "admin" and etPassword.get() == "1234":
        messagebox.showinfo(title="Login Info", message="Welcome to the app")
    else:
        messagebox.showinfo(title="Wrong UserName or Password", message="Access Denied")

def ShowHide():
    etPassword.config(show="")


root = Tk()
root.title("Login Page")

l1 = ttk.Label(root, text="UserName: ")
l1.grid(row=0, column=0)
etUserName = ttk.Entry(root, width=20)
etUserName.grid(row=0, column=1)

l2 = ttk.Label(root, text="Password: ")
l2.grid(row=1, column=0)
etPassword = ttk.Entry(root, width=20)
etPassword.grid(row=1, column=1)
etPassword.config(show="*")

BuLogin = ttk.Button(root, text="Login")
BuLogin.grid(row=2, column=1)

Image = PhotoImage("image.gif")
BuShowHide = ttk.Button(root)
BuShowHide.grid(row=1, column=2)
BuShowHide.config(image=Image, command=ShowHide)

BuLogin.config(command=BuClick)
root.mainloop()