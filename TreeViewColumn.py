from tkinter import *
from tkinter import ttk
root = Tk()

tv = ttk.Treeview()
tv.pack()
tv.insert('', '0', 'item1', text="Maulik")
# the forst one is parent, second is index, and third is item id, 4th is text
tv.insert('', '1', 'item2', text="Mom")
tv.insert('', '2', 'item3', text="Dada")
tv.insert('', '3', 'item4', text="Papa")

tv.configure(column=('age'))
tv.column('age', width=80, anchor=CENTER)
# now we can see two columns up tere


# To add text to the header
tv.heading('#0', text='Name')
tv.heading('#1', text='Age')

tv.set('item1', 'age', '14')
tv.set('item2', 'age', '42')
tv.set('item3', 'age', '17')
tv.set('item4', 'age', '50')

def TreeviewSelect():
    print(tv.selection)

tv.bind('<<TreeiewSelect>>', TreeviewSelect)

root.mainloop()