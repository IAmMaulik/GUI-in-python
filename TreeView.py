from tkinter import *
from tkinter import ttk
root = Tk()

tv = ttk.Treeview()
tv.pack()
tv.insert('', '0', 'item1', text="Maulik")
# the forst one is parent, second is index, and third is item id, 4th is text
tv.insert('item1', '1', 'item2', text="Shah")
tv.insert('item1', '2', 'item3', text="is")
tv.insert('item1', '3', 'item4', text="Great")

# tv.move('item2', 'item', '0') This is used to move the stuff
tv.item('item1', open=True)

# if i want to remove, we can use tv.detach('item3)
# but this does not delete but only hides it

# to permanently delete, we use tv.delete('item4')

root.mainloop()