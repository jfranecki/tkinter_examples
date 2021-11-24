from tkinter import *
# from PIL import ImageTk,Image

root = Tk()
root.title('The Frame GUI')
# root.iconbitmap('/home/pi/projects/tkinter_examples/icons/Double-J-Design-Origami-Colored-Pencil-Blue-home.ico')

# Frame text not necessary 
frame = LabelFrame(root, text="This is my frame...", padx=5, pady=5)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Do Not Click Here!")
b.grid(row=0, column=0)

b2 = Button(frame, text="...or here!")
b2.grid(row=2, column=2)

root.mainloop()
