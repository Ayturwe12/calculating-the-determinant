from tkinter import *
from tkinter import messagebox
import numpy as np

root = Tk()
root.geometry("500x550")
root.configure(bg="#f0f8ff")
root.title("Matrix App")
root.resizable(False, False)

matrix_labels = []
b_back = None
l_cap = None
entries = []
matris = []
row_number = ""
col_number = ""


def delete_all():
    global matrix_labels
    for widget in root.winfo_children():
        if widget != b_back and widget != l_cap:
            widget.destroy()

    for label in matrix_labels:
        label.destroy()
    matrix_labels.clear()


def back(x):
    delete_all()
    root.geometry("500x550")
    if x == "return_start":
        start()
    elif x == "matrix_add":
        matrix_app_label()
    elif x == "options":
        option_menu()


def matris_writer():
    l = Label(root, text="Matrix:", font=("Arial", 15, "bold"), bg="#f0f8ff")
    l.place(x=40, y=100)

    y_baslangic = int(row_number) * 30 + 20
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            label = Label(root, text=str(matris[i][j]), width=5, font=("Arial", 10), bg="white", relief="solid")
            label.place(x=150 + 50 * j, y=y_baslangic + 31 * i)


def bilinmeyen_bul2():
    delete_all()
    l = Label(root, text="Bilinmeyen Bulma:", font=("Arial", 15, "bold"), bg="#f0f8ff")
    l.place(x=40, y=100)
    letters = ["X", "Y", "Z", "A", "B"]
    try:
        y_baslangic = 100 + int(row_number) * 30 + 20
        for i in range(len(matris_solved)):
            for j in range(len(matris_solved[i])):
                harf = letters[i] if i < len(letters) else f"Harf{i}"
                metin = f"{harf} = {matris_solved[i][j]}"
                label = Label(root, text=metin, font=("Arial", 11), bg="#f0f8ff")
                label.place(x=150 + 50 * j, y=y_baslangic + 31 * i)
    except:
        root.geometry("500x550")
        label = Label(root, text="Çözüm Yapılamaz çünkü determinant 0.", font=("Arial", 15), bg="#f0f8ff", fg="red")
        label.place(x=50, y=250)


def bilinmeyen_bul1():
    global entriesx
    delete_all()
    b_back.config(command=lambda: back("options"))

    entriesx = []
    for i in range(int(row_number)):
        e = Entry(root, width=5)
        e.place(x=30, y=200 + 30 * i)
        entriesx.append(e)

    b_add = Button(root, text="Ekle", font=("Arial", 10), bg="#d9d9d9", command=matrisx_al)
    b_add.place(x=345, y=350)

    l = Label(root, text="Matrix 2:", font=("Arial", 15, "bold"), bg="#f0f8ff")
    l.place(x=40, y=100)


def matrisx_al():
    global matris_solved

    matrisx = []
    uyari_gosterildi = False
    for entry in entriesx:
        try:
            matrisx.append([float(entry.get())])
        except ValueError:
            if not uyari_gosterildi:
                messagebox.showwarning("Uyarı", "Sayı atanmayan her değer için 0 atanır.")
                uyari_gosterildi = True
            matrisx.append([0])
    print(matrisx)

    b_forward = Button(root, text="Devam", font=("Arial", 10), bg="#d9d9d9", command=bilinmeyen_bul2)
    b_forward.place(x=345, y=370)

    try:
        matris_solved = np.linalg.solve(matris, matrisx)
        print("Çözüm:", matris_solved)
    except np.linalg.LinAlgError:
        print("Bu matrisle çözüm yapılamaz. Determinantı sıfır.")


def minor(matrix, i, j):
    return np.delete(np.delete(matrix, i, axis=0), j, axis=1)


def ek_matris(matrix):
    n = matrix.shape[0]
    minors = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            submatrix = minor(matrix, i, j)
            minors[i][j] = np.linalg.det(submatrix)
    return minors


def ek_matris_label():
    delete_all()
    b_back.config(command=lambda: back("options"))
    ek = ek_matris(np.array(matris))
    matris_writer()

    l = Label(root, text="Ek matris:", font=("Arial", 15, "bold"), bg="#f0f8ff")
    l.place(x=40, y=300)

    y_start = 330

    for i in range(len(ek)):
        for j in range(len(ek[i])):
            label = Label(root, text=str(round(ek[i][j], 2)), width=5, bg="white", relief="solid")
            label.place(x=150 + 50 * j, y=y_start + 31 * i)
            matrix_labels.append(label)
    root.geometry("500x600")


def determinant():
    delete_all()
    det = np.linalg.det(matris)
    b_back.config(command=lambda: back("options"))

    l_det = Label(root, text="Determinant:", font=("Arial", 15, "bold"), bg="#f0f8ff")
    l_det.place(x=40, y=350)

    l_det1 = Label(root, text=round(det, 2), font=("Arial", 15), bg="#f0f8ff")
    l_det1.place(x=200, y=350)

    matris_writer()


def option_menu():
    delete_all()
    b_back.config(command=lambda: back("matrix_add"))

    l1 = Label(root, text="Yapmak istediğiniz işlemi seçin:", font=("Arial", 15, "bold"), bg="#f0f8ff")
    l1.place(x=40, y=100)

    b_det = Button(root, text="Determinant\nBul", font=("Arial", 12), bg="#d9d9d9", height=5, width=10, command=determinant)
    b_det.place(x=20, y=170)

    b_ek = Button(root, text="Ek matris\nBul", font=("Arial", 12), bg="#d9d9d9", height=5, width=10, command=ek_matris_label)
    b_ek.place(x=140, y=170)

    b_carmer = Button(root, text="Bilinmeyen\nBul", font=("Arial", 12), bg="#d9d9d9", height=5, width=10, command=bilinmeyen_bul1)
    b_carmer.place(x=260, y=170)


def matrisi_al():
    global b_forward, matris
    uyari_gosterildi = False
    matris = []
    for i in range(int(row_number)):
        satir = []
        for j in range(int(row_number)):
            deger = entries[i][j].get()
            try:
                satir.append(float(deger))
            except ValueError:
                if not uyari_gosterildi:
                    messagebox.showwarning("Uyarı", "Sayı atanmayan her değer için 0 atanır.")
                    uyari_gosterildi = True
                satir.append(0)
        matris.append(satir)
        b_forward.configure(state=NORMAL)
    print(matris)


def olustur(row_number):
    global entries, b_forward
    b_add.configure(state=NORMAL)
    entries = []
    for i in range(int(row_number)):
        row = []
        for j in range(int(row_number)):
            e = Entry(root, width=5)
            e.place(x=30 + 50 * j, y=200 + 30 * i)
            row.append(e)
        entries.append(row)

    b_forward = Button(root, text="Devam", font=("Arial", 10), state=DISABLED, bg="#d9d9d9", command=option_menu)
    b_forward.place(x=345, y=370)


def get_row_number():
    global row_number
    selected_value = row.get()

    if selected_value != "Seç":
        row_number, col_number = selected_value.split('-')
        olustur(row_number)
        b_enter.config(state=DISABLED)


def matrix_app_label():
    global l, row, b_enter, b_add, b_back, l_cap
    l_cap = Label(root, text="Matrix App", font=("Arial", 20, "bold"), bg="#f0f8ff")
    l_cap.place(x=5, y=5)

    l1 = Label(root, text="Satır-Sütun sayısını seçin:", font=("Arial", 15), bg="#f0f8ff")
    l1.place(x=40, y=100)

    row = StringVar()
    row.set("Seç")
    secenekler = ["1-1", "2-2", "3-3", "4-4", "5-5"]
    dropdown_row = OptionMenu(root, row, *secenekler)
    dropdown_row.place(x=280, y=100)

    b_enter = Button(root, text="Yarat", font=("Arial", 10), bg="#d9d9d9", command=get_row_number)
    b_enter.place(x=345, y=100)

    b_add = Button(root, text="Ekle", font=("Arial", 10), state=DISABLED, bg="#d9d9d9", command=matrisi_al)
    b_add.place(x=345, y=350)

    b_back = Button(root, text="<-", font=("Arial", 10), bg="#d9d9d9", command=lambda: back("return_start"))
    b_back.place(x=450, y=5)


def main_screen():
    delete_all()
    matrix_app_label()


def start():
    global l, b_back
    try:
        b_back.config(state=DISABLED)
        l_cap.config(text="")
    except:
        pass
    l = Label(root, text="Matrix App", font=("Arial", 30, "bold"), bg="#f0f8ff")
    l.place(x=120, y=100)

    l1 = Label(root, text="Ahmet Güler tarafından yapıldı.", font=("Arial", 10), bg="#f0f8ff")
    l1.place(x=230, y=500)

    b = Button(root, text="Başla", font=("Arial", 20), bg="#d9d9d9", command=main_screen)
    b.place(x=180, y=200)


start()
root.mainloop()
