from tkinter import *
from tkinter import LabelFrame
from PIL import Image, ImageTk
root= Tk()
root.title("learn the codding")
root.iconbitmap("C:/Users/aytur/Downloads/icon.ico")

def tikla():
    label1 = Label(root, text=var.get()).pack()
var=IntVar()
c = Checkbutton(root, text="check the box please!", variable=var).pack()

button1=Button(root,text="click me",command=tikla)
button1.pack()





root.mainloop()