from tkinter import *

root = Tk()

myLabel = Label(root, text="Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text="Just another label").grid(row=1, column=1)

# With Object Oriented Programming we can do without these lines
# myLabel.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)

root.mainloop()
