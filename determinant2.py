def baslat():
    global secim

    liste_olusturma()

def liste_olusturma():
    global liste,liste_p,dete
    liste = []
    liste_p=[]

    try:
        while True:
            global secim
            global a,b
            print("1: determinant alma\n 2:ek matris alma\n 3:Cramer ile bilinmeyen bulma")
            secim = int(input("lütfen yapmak istediğiniz işlemi seçin:"))
            a, b = map(int, input("Satır ve Sütun sayılarını sırasıyla boşluk bırakarak girin:").strip().split())

            if a == 1 and b == 1:
                deger = int(input("a1x1: "))
                if secim==1:
                    determinant_islem_1()

            elif a == 2 and b == 2:
                for i in range(1, 3):
                    for j in range(1, 3):
                        deger = int(input("a{}{}: ".format(i, j)))
                        liste.append(deger)
                if secim==1:
                    determinant_islem_2()
            elif a == 3 and b == 3:
                for i in range(1, 4):
                    for j in range(1, 4):
                        deger = int(input("a{}{}: ".format(i, j)))
                        liste.append(deger)
                if secim==1:
                    determinant_islem_3()
                elif secim==2:
                    ek_matris_olusturma()
                elif secim==3:
                    liste_p_olusturma()
                    determinant_islem_3()
                    dete = determinant
                    determinant_cramer()

            elif a == 4 and b == 4:
                for i in range(1, 5):
                    for j in range(1, 5):
                        deger = int(input("a{}{}: ".format(i, j)))
                        liste.append(deger)
                if secim==1:
                    determinant_islem_4()
                elif secim==2:
                    ek_matris_olusturma()
                elif secim==3:
                    liste_p_olusturma()
                    determinant_islem_4()
                    dete = determinant
                    determinant_cramer()
            else:
                print("maalesef 5x5 ve üzeri matrisleri uygulama desteklememektedir.")
            liste.clear()

            ex = str(input("Çıkmak için q basın,(devam etmek için 'enter' tuşlayın)): "))
            if ex == "q":
                exit()
            else:
                continue
    except ValueError:
        print("Lütfen istenen değerleri girin.Tekrar deneyin...")
        baslat()

def liste_p_olusturma():
    print("--------------P'yi giriniz-------------------")
    for i in range(1,a+1):
        for j in range(1,2):
            deger = int(input("a{}{}: ".format(i, j)))
            liste_p.append(deger)
def determinant_cramer():
    global dete1,dete2,dete3,dete4,liste
    liste_s = []

    liste_s = liste.copy()
    if a==3 and b==3:
        liste[0] = liste_p[0]
        liste[3] = liste_p[1]
        liste[6] = liste_p[2]
        determinant_islem_3()
        dete1=determinant

        liste = liste_s.copy()
        liste[1] = liste_p[0]
        liste[4] = liste_p[1]
        liste[7] = liste_p[2]
        determinant_islem_3()
        dete2 = determinant

        liste = liste_s.copy()
        liste[2] = liste_p[0]
        liste[5] = liste_p[1]
        liste[8] = liste_p[2]
        determinant_islem_3()
        dete3 = determinant

    elif a == 4 and b == 4:
        liste[0] = liste_p[0]
        liste[4] = liste_p[1]
        liste[8] = liste_p[2]
        liste[12] = liste_p[3]
        determinant_islem_4()
        dete1 = determinant

        liste = liste_s.copy()
        liste[1] = liste_p[0]
        liste[5] = liste_p[1]
        liste[9] = liste_p[2]
        liste[13] = liste_p[3]
        determinant_islem_4()
        dete2 = determinant

        liste = liste_s.copy()
        liste[2] = liste_p[0]
        liste[6] = liste_p[1]
        liste[10] = liste_p[2]
        liste[14] = liste_p[3]
        determinant_islem_4()
        dete3 = determinant

        liste = liste_s.copy()
        liste[3] = liste_p[0]
        liste[7] = liste_p[1]
        liste[11] = liste_p[2]
        liste[15] = liste_p[3]
        determinant_islem_4()
        dete4= determinant
    cramer_sonuc()

def cramer_sonuc():
    if a==3 and b==3:
        print("x1=" , "{}/{}".format(dete1,dete),"=", dete1/dete)
        print("x2=", "{}/{}".format(dete2,dete),"=", dete2/dete)
        print("x3=", "{}/{}".format(dete3,dete),"=", dete3/dete)
    elif a==4 and b==4:
        print("x1=" , "{}/{}".format(dete1,dete),"=", dete1/dete)
        print("x2=", "{}/{}".format(dete2,dete),"=", dete2/dete)
        print("x3=", "{}/{}".format(dete3,dete),"=", dete3/dete)
        print("x4=", "{}/{}".format(dete4, dete), "=", dete4 / dete)



def determinant_islem_1():
    print(deger)
def determinant_islem_2():
    determinant = liste[0] * liste[3] - liste[1] * liste[2]
    print("|a2x2|:", determinant)
def determinant_islem_3():
    global determinant
    determinant = liste[0] * (liste[4] * liste[8] - liste[7] * liste[5]) - liste[1] * (
                liste[3] * liste[8] - liste[6] * liste[5]) + liste[2] * (liste[3] * liste[7] - liste[6] * liste[4])
    if secim==1:
        print("|a3x3|:", determinant)

def determinant_islem_4():
    global determinant
    determinant1 = liste[0] * (liste[5] * (liste[10] * liste[15] - liste[11] * liste[14]) - liste[6] * (
                liste[9] * liste[15] - liste[11] * liste[13]) + liste[7] * (
                                           liste[9] * liste[14] - liste[10] * liste[13]))
    determinant2 = liste[1] * -1 * (liste[4] * (liste[10] * liste[15] - liste[11] * liste[14]) - liste[6] * (
                liste[8] * liste[15] - liste[11] * liste[12]) + liste[7] * (
                                                liste[8] * liste[14] - liste[10] * liste[12]))
    determinant3 = liste[2] * (liste[4] * (liste[9] * liste[15] - liste[13] * liste[11]) - liste[5] * (
                liste[8] * liste[15] - liste[12] * liste[11]) + liste[7] * (
                                           liste[8] * liste[13] - liste[9] * liste[12]))
    determinant4 = liste[3] * -1 * (liste[4] * (liste[9] * liste[14] - liste[13] * liste[10]) - liste[5] * (
                liste[8] * liste[14] - liste[12] * liste[10]) + liste[6] * (
                                                liste[8] * liste[13] - liste[12] * liste[9]))
    determinant=determinant1 + determinant2 + determinant3 + determinant4
    if secim == 1:

        print("|a4x4|:", determinant)
    determinant1 = determinant2 = determinant3 = determinant4 = determinant5 = 0


def ek_matris_olusturma():
    global liste2
    global liste3

    liste2 = []  # ilk listedeki elemanların kofaktörü
    liste3 = []  # 2. listedeki elemanların transpozesi

    while True:

        if a==3 and b==3:

            def kofaktor_bul():
                liste2.append((liste[4] * liste[8] - liste[5] * liste[7]))
                liste2.append((-(liste[3] * liste[8] - liste[5] * liste[6])))
                liste2.append((liste[3] * liste[7] - liste[4] * liste[6]))
                liste2.append(-(liste[1] * liste[8] - liste[2] * liste[7]))
                liste2.append((liste[0] * liste[8] - liste[2] * liste[6]))
                liste2.append(-(liste[0] * liste[7] - liste[1] * liste[6]))
                liste2.append((liste[1] * liste[5] - liste[4] * liste[2]))
                liste2.append(-(liste[0] * liste[5] - liste[2] * liste[3]))
                liste2.append((liste[0] * liste[4] - liste[1] * liste[3]))
                transpoze_bul()

            def transpoze_bul():
                liste3.append(liste2[0])
                liste3.append(liste2[3])
                liste3.append(liste2[6])
                liste3.append(liste2[1])
                liste3.append(liste2[4])
                liste3.append(liste2[7])
                liste3.append(liste2[2])
                liste3.append(liste2[5])
                liste3.append(liste2[8])
                ekmatris_yazdir()

            def ekmatris_yazdir():
                for i in range(0, len(liste3), 3):
                    print(liste3[i:i + 3])

            kofaktor_bul()
        elif a == 4 and b == 4:
            def kofaktor_bul():
                liste2.append(
                    liste[5] * (liste[10] * liste[15] - liste[14] * liste[11])
                    - liste[6] * (liste[9] * liste[15] - liste[13] * liste[11])
                    + liste[7] * (liste[9] * liste[14] - liste[13] * liste[10])
                )

                liste2.append(
                    -1 * (
                            liste[4] * (liste[10] * liste[15] - liste[14] * liste[11])
                            - liste[6] * (liste[8] * liste[15] - liste[12] * liste[11])
                            + liste[7] * (liste[8] * liste[14] - liste[12] * liste[10])
                    )
                )

                liste2.append(
                    liste[4] * (liste[9] * liste[15] - liste[13] * liste[11])
                    - liste[5] * (liste[8] * liste[15] - liste[12] * liste[11])
                    + liste[7] * (liste[8] * liste[13] - liste[12] * liste[9])
                )

                liste2.append(
                    -1 * (
                            liste[4] * (liste[9] * liste[14] - liste[13] * liste[10])
                            - liste[5] * (liste[8] * liste[14] - liste[12] * liste[10])
                            + liste[6] * (liste[8] * liste[13] - liste[12] * liste[9])
                    )
                )

                liste2.append(
                    liste[1] * (liste[10] * liste[15] - liste[14] * liste[11])
                    - liste[2] * (liste[9] * liste[15] - liste[13] * liste[11])
                    + liste[3] * (liste[9] * liste[14] - liste[13] * liste[10])
                )

                liste2.append(
                    liste[0] * (liste[10] * liste[15] - liste[14] * liste[11])
                    - liste[2] * (liste[8] * liste[15] - liste[12] * liste[11])
                    + liste[3] * (liste[8] * liste[14] - liste[12] * liste[10])
                )

                liste2.append(
                    -1 * (
                            liste[0] * (liste[9] * liste[15] - liste[13] * liste[11])
                            - liste[1] * (liste[8] * liste[15] - liste[12] * liste[11])
                            + liste[3] * (liste[8] * liste[13] - liste[12] * liste[9])
                    )
                )

                liste2.append(
                    liste[0] * (liste[9] * liste[14] - liste[13] * liste[10])
                    - liste[1] * (liste[8] * liste[14] - liste[12] * liste[10])
                    + liste[2] * (liste[8] * liste[13] - liste[12] * liste[9])
                )

                liste2.append(
                     (
                            liste[1] * (liste[6] * liste[15] - liste[7] * liste[14])
                            - liste[2] * (liste[5] * liste[15] - liste[13] * liste[7])
                            + liste[3] * (liste[5] * liste[14] - liste[13] * liste[6])
                    )
                )

                liste2.append(
                    -1* (
                            liste[0] * (liste[6] * liste[15] - liste[14] * liste[7])
                           - liste[2] * (liste[4] * liste[15] - liste[12] * liste[7])
                           + liste[3] * (liste[4] * liste[14] - liste[12] * liste[6])
                     )
                )

                liste2.append(

                            liste[0] * (liste[5] * liste[15] - liste[13] * liste[7])
                            - liste[1] * (liste[4] * liste[15] - liste[12] * liste[7])
                            + liste[3] * (liste[4] * liste[13] - liste[12] * liste[5])

                )

                liste2.append(
                    -1*(
                            liste[0] * (liste[5] * liste[14] - liste[6] * liste[13])
                            - liste[1] * (liste[4] * liste[14] - liste[12] * liste[6])
                            + liste[2] * (liste[4] * liste[13] - liste[12] * liste[5])
                    )
                )

                liste2.append(
                    -1 * (
                            liste[1] * (liste[6] * liste[11] - liste[10] * liste[7])
                            - liste[2] * (liste[5] * liste[11] - liste[9] * liste[7])
                            + liste[3] * (liste[5] * liste[10] - liste[9] * liste[6])
                    )
                )

                liste2.append(
                    liste[0] * (liste[6] * liste[11] - liste[10] * liste[7])
                    - liste[2] * (liste[4] * liste[11] - liste[8] * liste[7])
                    + liste[3] * (liste[4] * liste[10] - liste[8] * liste[6])
                )

                liste2.append(
                    -1 * (
                            liste[0] * (liste[5] * liste[11] - liste[9] * liste[7])
                            - liste[1] * (liste[4] * liste[11] - liste[8] * liste[7])
                            + liste[3] * (liste[4] * liste[9] - liste[8] * liste[5])
                    )
                )

                liste2.append(
                    liste[0] * (liste[5] * liste[10] - liste[9] * liste[6])
                    - liste[1] * (liste[4] * liste[10] - liste[8] * liste[6])
                    + liste[2] * (liste[4] * liste[9] - liste[8] * liste[5])
                )
                transpoze_bul()

            def transpoze_bul():
                liste3.append(liste2[0])
                liste3.append(liste2[4])
                liste3.append(liste2[8])
                liste3.append(liste2[12])
                liste3.append(liste2[1])
                liste3.append(liste2[5])
                liste3.append(liste2[9])
                liste3.append(liste2[13])
                liste3.append(liste2[2])
                liste3.append(liste2[6])
                liste3.append(liste2[10])
                liste3.append(liste2[14])
                liste3.append(liste2[3])
                liste3.append(liste2[7])
                liste3.append(liste2[11])
                liste3.append(liste2[15])
                ekmatris_yazdir()

            def ekmatris_yazdir():
                for i in range(0, len(liste3), 4):
                    print(liste3[i:i + 4])

            kofaktor_bul()

        break
    liste2.clear()
    liste3.clear()
    secim = 0
baslat()