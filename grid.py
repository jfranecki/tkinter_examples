from tkinter import *

root = Tk()

# Creating a Label Widget
myLabel = Label(root, text="Hello World!") 
myLabel2 = Label(root, text="Just another label") 

myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

# The grid components are relative
# So if myLabel(r=0,c=0) and myLabel2(r=7,c=9), myLabel2 would default to (r=1,c=1)

root.mainloop()
