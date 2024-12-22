from tkinter import *
import numpy as np

root=Tk()
root.title("Determinant finder")
root.geometry("500x300")

def  raw_column_num():
    global a,b
    a, b = map(int,entry1.get().strip().split())
    if a==b:
        create_matrix(a,b)

def create_matrix(x,y):
    global i,j,matrix1
    matrix1=np.zeros((x,y))
    buton1=Button(root,text="Enter",state=DISABLED).grid(row=0,column=2)
    entry1=Entry(root,width=10,state=DISABLED).grid(row=0,column=1)
def send_data(data,i,j):
    global matrix1
    add_data(data)
    label2.grid_forget()
    matrix1[i,j]=int(data)



    for i in range(1,x+1):
        for j in range(1,y+1):
            deger = ("a{}{}: ".format(i, j))
            label2=Label(root,text=deger)
            entry2 = Entry(root, width=10)
            buton2 = Button(root, text="Enter", command=lambda e = entry2,i=i,j=j: send_data(e.get(),i,j))
            buton2.grid(row=3, column=2, padx=10, pady=10)
            label2.grid(row=3,column=0,padx=10, pady=10)
            entry2.grid(row=3, column=1, padx=10, pady=10)

            entry2.config(state=NORMAL)  # Entry'i aktif hale getir
            buton2.config(state=NORMAL)  # Button'ı aktif hale getir








label1=Label(root,text="Matrisin satır ve sütun sayısını boşluk bırakarak giriniz:")
button1 = Button(root,text="enter", command=raw_column_num)
entry1=Entry(root,width=10)

buton2=Button(root,text="Enter",state=DISABLED)
entry2=Entry(root,width=10,state=DISABLED)
label2=Label(root,text="???")


buton2.grid(row=3,column=2,padx=10,pady=10)
entry2.grid(row=3,column=1,padx=10,pady=10)
label2.grid(row=3,column=0,padx=10,pady=10)

label1.grid(column=0,row=0)
button1.grid(column=2,row=0)
entry1.grid(column=1,row=0)



root.mainloop()
