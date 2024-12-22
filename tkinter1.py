from tkinter import *
root= Tk()
root.title("simple calculator")

e = Entry(root,width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10,pady=10)


def button_click(number):
    current= e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(number))

def button_clear_all():
    e.delete(0, END)
def button_clear():
    e.delete(e.index("end") - 1)

def button_equal():
    second_number=float(e.get())

    e.delete(0, END)
    if math=="addition":
        return e.insert(0,f_num +float(second_number))
    elif math=="subtraction":
        return e.insert(0,f_num -float(second_number))
    elif math=="multiplication":
        return e.insert(0,f_num *float(second_number))
    elif math=="division":
        return e.insert(0,f_num /float(second_number))
    elif math=="square_root":
        return e.insert(0,f_num**0.5)
    elif math=="square":
        return e.insert(0,f_num**2)
    elif math=="exponent":
        return e.insert(0,f_num**second_number)
    else:
        e.insert(0,"Try again..")
def button_all(process):
    first_number=e.get()
    global f_num
    global math
    math= "{}".format(process)
    f_num = float(first_number)
    e.delete(0, END)

button_1= Button(root,text="1", padx=40,pady=20,command= lambda: button_click(1))
button_2= Button(root,text="2", padx=40,pady=20,command= lambda:button_click(2))
button_3= Button(root,text="3", padx=40,pady=20,command= lambda:button_click(3))
button_4= Button(root,text="4", padx=40,pady=20,command=lambda: button_click(4))
button_5= Button(root,text="5", padx=40,pady=20,command=lambda: button_click(5))
button_6= Button(root,text="6", padx=40,pady=20,command= lambda:button_click(6))
button_7= Button(root,text="7", padx=40,pady=20,command= lambda:button_click(7))
button_8= Button(root,text="8", padx=40,pady=20,command= lambda:button_click(8))
button_9= Button(root,text="9", padx=40,pady=20,command= lambda:button_click(9))
button_0= Button(root,text="0", padx=40,pady=20,command= lambda:button_click(0))
button_add=Button(root,text="+", padx=39,pady=20,command= lambda:button_all("addition"))
button_equal= Button(root,text="=",padx=91,pady=20,command= button_equal)
button_clear_all= Button(root,text="clear all", padx=25,pady=20,command= button_clear_all)
button_clear= Button(root,text="clear ", padx=25,pady=20,command= button_clear)

button_subtrack=Button(root,text="-", padx=41,pady=20,command= lambda:button_all("subtraction"))
button_multiply=Button(root,text="x", padx=40,pady=20,command= lambda:button_all("multiplication"))
button_divide=Button(root,text="/", padx=44,pady=20,command= lambda:button_all("division"))

button_square_root=Button(root,text="²√", padx=37,pady=20,command= lambda:button_all("square_root"))
button_square=Button(root,text="x²", padx=38,pady=20,command= lambda:button_all("square"))
button_exponent=Button(root,text="^", padx=42,pady=20,command= lambda:button_all("exponent"))

button_1.grid(row= 3, column=0)
button_2.grid(row= 3, column=1)
button_3.grid(row= 3, column=2)

button_4.grid(row= 2, column=0)
button_5.grid(row= 2, column=1)
button_6.grid(row= 2, column=2)

button_7.grid(row= 1, column=0)
button_8.grid(row=1 , column=1)
button_9.grid(row= 1, column=2)

button_0.grid(row=4 , column=0)
button_clear_all.grid(row=4, column=1)
button_clear.grid(row=4, column=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1 , columnspan=2)

button_subtrack.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_square_root.grid(row=7, column=0)
button_square.grid(row=7, column=1)
button_exponent.grid(row=7, column=2)

root.mainloop()