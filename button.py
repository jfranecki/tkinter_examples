from tkinter import *

root = Tk()

myButton = Button(root, text="You cant click me!", state=DISABLED)
myButton.pack()

myButton2 = Button(root, text="Wide Button!", padx=50)
myButton2.pack()

myButton3 = Button(root, text="Tall Button!", pady=50)
myButton3.pack()

myButton4 = Button(root, text="Big Button!", padx=50, pady=50)
myButton4.pack()

def myClick():
    myLabel = Label(root, text="I did a thing!")
    myLabel.pack()

# If command=myClick --> command=myClick()
#   then myClick would be executed immediatly without clicking
myButton5 = Button(root, text="This button actually does something :)",  command=myClick)
myButton5.pack()

myButton6 = Button(root, text="Simple Colored Button!", fg="white", bg="black")
myButton6.pack()

myButton6 = Button(root, text="Hex Colored Button!", fg="#000000", bg="#ff9500")
myButton6.pack()

root.mainloop()
