def calculate():
    liste=[]
    while True:
        try:

                a,b=map(int,input("Satır ve Sütun sayılarını sırasıyla boşluk bırakarak girin:").strip().split())
                if a==1 and b==1:
                    deger = int(input("a1x1: "))
                    print(deger)
                elif a==2 and b==2:
                    for i in range(1, 3):
                        for j in range(1, 3):
                            deger = int(input("a{}{}: ".format(i, j)))
                            liste.append(deger)
                    determinant=liste[0]*liste[3]-liste[1]*liste[2]
                    print("|a2x2|:",determinant)
                elif a==3 and b==3:
                    for i in range(1,4):
                        for j in range(1,4):
                            deger=int(input("a{}{}: ".format(i,j)))
                            liste.append(deger)
                    determinant= liste[0]*(liste[4]*liste[8]-liste[7]*liste[5])-liste[1]*(liste[3]*liste[8]-liste[6]*liste[5])+liste[2]*(liste[3]*liste[7]-liste[6]*liste[4])
                    print("|a3x3|:",determinant)
                elif a==4 and b==4:
                    for i in range(1,5):
                        for j in range(1,5):
                            deger=int(input("a{}{}: ".format(i,j)))
                            liste.append(deger)
                    determinant1= liste[0]*(liste[5]*(liste[10]*liste[15]-liste[11]*liste[14])-liste[6]*(liste[9]*liste[15]-liste[11]*liste[13])+liste[7]*(liste[9]*liste[14]-liste[10]*liste[13]))
                    determinant2= liste[1]*-1*(liste[4]*(liste[10]*liste[15]-liste[11]*liste[14])-liste[6]*(liste[8]*liste[15]-liste[11]*liste[12])+liste[7]*(liste[8]*liste[14]-liste[10]*liste[12]))
                    determinant3= liste[2]*(liste[4]*(liste[9]*liste[15]-liste[13]*liste[11])-liste[5]*(liste[8]*liste[15]-liste[12]*liste[11])+liste[7]*(liste[8]*liste[13]-liste[9]*liste[12]))
                    determinant4= liste[3]*-1*(liste[4]*(liste[9]*liste[14]-liste[13]*liste[10])-liste[5]*(liste[8]*liste[14]-liste[12]*liste[10])+liste[6]*(liste[8]*liste[13]-liste[12]*liste[9]))
                    print("|a4x4|:",determinant1+determinant2+determinant3+determinant4)
                    determinant1=determinant2=determinant3=determinant4=determinant5=0
                else:
                    print("maalesef 5x5 ve üzeri matrisleri uygulama desteklememektedir.")
                liste.clear()
                determinant = 0

        except ValueError:
            print("Lütfen istenen değerleri girin.Tekrar deneyin...")

        ex = str(input("cıkma ıste q bas: "))
        if ex == "q":
            exit()
calculate()