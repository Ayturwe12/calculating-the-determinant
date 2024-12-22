from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
root= Tk()
root.title("learn the codding")
root.iconbitmap("C:/Users/aytur/Downloads/icon.ico")



def showimage():
    global myimage
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/Aytur/Desktop/images", title="sellect a file",
                                               filetypes=(("jpg", "*.jpg"), ("all files", "*.*")))

    myimage = ImageTk.PhotoImage(Image.open(root.filename))
    my2label = Label(root, image=myimage).pack()

mybutton=Button(root, text="click here to see the image", command=showimage).pack()
root.mainloop()