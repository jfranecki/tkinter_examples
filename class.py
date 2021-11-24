from tkinter import *

root = Tk()
root.title('My TK App')
root.geometry('400x400')

class myClass:
    def __init__(self, masterRoot):
        myFrame = Frame(masterRoot)
        myFrame.pack()

        # Anytime you do stuff inside a function make sure you use "self."
        self.myButton = Button(masterRoot, text="Click Me!", command=self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print("HEY! YOU CLICKED A BUTTON! good job :)")


c = myClass(root)

root.mainloop()
