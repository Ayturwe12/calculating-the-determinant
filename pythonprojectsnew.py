import numpy as np
matris=[]

satir=int(input("lütfen satır sayısını girin:"))

for i in range(satir):
    row=input(f"{i+1}. satırdaki değerleri boşluk bırakarak gir:")

    matris.append([int(x) for x in row.split()])

for j in matris:
    print(j)

det=np.linalg.det(matris)
print(det)

